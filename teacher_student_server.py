"""使用前需安装 
tesseract-ocr (自行google)

强大的验证码识别。。
成功率在70 以上

等我有空了我再来完成这个烂尾项目
"""


from PIL import Image
from bs4 import BeautifulSoup
import requests
from io import BytesIO
import pytesseract
from config import *
import re


class Course(object):
    def __init__(self, time, weight, score, name):
        self.time = time
        self.weight = weight
        self.score = score
        self.name = name


class Login(object):
    def __init__(self):
        self.session = requests.session()
        self.captcha = ''
        self.get_captcha_img()
        self.login_action()
        # 示例程序 调来看看喽
        self.look_kb()

    def get_captcha_img(self):
        content = self.session.get(teacher_student_captcha_url)
        img = Image.open(BytesIO(content.content))
        img.show()
        img.seek(0)
        captcha = pytesseract.image_to_string(img)
        # 比较图片与自动识别的结果
        text = input("识别为： " + captcha + '若出现错误请更改[否则回车跳过]: ')
        if text:
            captcha = text
        self.set_captcha(captcha)
        return captcha

    def set_captcha(self, captcha):
        self.captcha = captcha

    def login_action(self):
        # username = input("请输入学号: ")
        # password = input("请输入密码: ")
        teacher_student_payload['j_username'] = '20146339'
        teacher_student_payload['j_password'] = 'woaickywa0'
        teacher_student_payload['validateCode'] = self.captcha
        request = self.session.post(check_student_url1,
                                    headers=teacher_student_header,
                                    data=teacher_student_payload)

    def look_cj(self):
        request = self.session.get(look_cj)
        soup = BeautifulSoup(request.content, "html5lib")
        a = soup.find_all('tr')
        courses = list()
        count = 1
        for i in a:
            try:
                if i['class'][0] == "t_con":
                    if count != int(i.td.string):
                        break
                    item = i.find_all('td')
                    tmp = Course(item[1].string, item[6].string,
                                 item[7].span.strong.string, item[3].string)
                    courses.append(tmp)
                    count += 1
            except:
                pass

        sum = 0
        xuefen = 0
        for i, course in enumerate(courses):
            if not int(course.score) < 60:
                sum += float(course.score) * float(course.weight)
                xuefen += float(course.weight)
        print(sum / (xuefen * 10))

    def look_kb(self):
        request = self.session.get(look_kb)
        context = request.text
        kb = re.findall(r"v>(.*)\n", context)
        for i in kb:
            if i.startswith("</di"):
                i = i[6:]
                print(i)


    def look_py(self):
        request = self.session.get(look_py)


new = Login()
