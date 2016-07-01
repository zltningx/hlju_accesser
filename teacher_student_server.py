from PIL import Image
from bs4 import BeautifulSoup
import requests
from io import BytesIO
import pytesseract
from config import *


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
        self.look_cj()

    def get_captcha_img(self):
        content = self.session.get(teacher_student_captcha_url)
        img = Image.open(BytesIO(content.content))
        img.show()
        captcha = pytesseract.image_to_string(img)
        text = input("识别为： " + captcha + '若出现错误请更改[否则回车跳过]: ')
        if text:
            captcha = text
        self.set_captcha(captcha)
        return captcha

    def set_captcha(self, captcha):
        self.captcha = captcha

    def login_action(self):
        username = input("请输入学号: ")
        password = input("请输入密码: ")
        teacher_student_payload['j_username'] = username
        teacher_student_payload['j_password'] = password
        teacher_student_payload['validateCode'] = self.captcha
        request = self.session.post(check_student_url1,
                                    headers=teacher_student_header,
                                    data=teacher_student_payload)
        print(request.headers['Content-Length'])
        request = self.session.get("http://ssfw1.hlju.edu.cn/ssfw/common/ajaxLoginResult.jsp?success=true")
        print(request.content)

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
        soup = BeautifulSoup(request.content, "html5lib")
        print(request.text)

    def look_py(self):
        request = self.session.get(look_py)


new = Login()
