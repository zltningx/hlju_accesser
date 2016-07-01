

my_hlju_captcha_url = "http://my.hlju.edu.cn/captchaGenerate.portal"
my_hlju_is_valid_url = "http://my.hlju.edu.cn/captchaValidate.portal?captcha={}&what=captcha&value={}"
my_hlju_login_url = "http://my.hlju.edu.cn/userPasswordValidate.portal"
my_hlju_index_url = "http://my.hlju.edu.cn/index.portal"

check_student_url1 = "http://ssfw2.hlju.edu.cn/ssfw/j_spring_ids_security_check"
check_student_url2 = "http://ssfw1.hlju.edu.cn/ssfw/common/ajaxLoginResult.jsp?success=true"

teacher_student_url = "http://ssfw1.hlju.edu.cn/ssfw/index.do"
teacher_student_captcha_url = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"
teacher_student_index = "http://ssfw1.hlju.edu.cn/ssfw/index.do"

look_cj = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/cjxx.do"
look_py = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/pyfa/xsfaTree.do"
look_kb = "http://ssfw1.hlju.edu.cn/ssfw/pkgl/kcbxx/xskcb.do"


ids_login_url = 'http://ids.hlju.edu.cn/amserver/UI/Login'

my_hlju_header = {
    'Host': 'my.hlju.edu.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.8.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://my.hlju.edu.cn/',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded'
}

teacher_student_header = {
    'Host': 'ssfw1.hlju.edu.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.8.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://ssfw1.hlju.edu.cn/ssfw/login/ajaxlogin.do',
}

my_hlju_payload = {
    'Login.Token1': '',
    'Login.Token2': '',
    'captcha': '',
    'goto': 'http%3A%2F%2Fmy.hlju.edu.cn%2FloginSuccess.portal',
    'gotoOnFail': 'http%3A%2F%2Fmy.hlju.edu.cn%2FloginFailure.portal',
}


teacher_student_payload = {
    'j_username': '',
    'j_password': '',
    'validateCode': '',
}


ids_header = {
    'Host': 'ids.hlju.edu.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.8.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://ids.hlju.edu.cn/amserver/UI/Login',
}

ids_payload = {
    'IDToken0': '',
    'IDToken1': '',
    'IDToken2': '',
    'IDButton': 'Submit',
    'goto': '',
    'encoded': 'false',
    'gx_charset': 'UTF-8'
}