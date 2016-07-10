"""These are Some API of HLJU
"""

# 校园信息门户网站 my.hlju.edu.cn 登录
my_hlju_captcha_url = "http://my.hlju.edu.cn/captchaGenerate.portal"  # 获取验证码

# 抓包过程中发现进行了一次数据库查询验证验证码是否正确，可以跳过此过程
my_hlju_is_valid_url = "http://my.hlju.edu.cn/captchaValidate.portal?captcha={}&what=captcha&value={}"
# 登录行为： POST 方法 需要提供post数据。 使用 payload: my_hlju_payload 
my_hlju_login_url = "http://my.hlju.edu.cn/userPasswordValidate.portal"
# 登录成功访问的主页
my_hlju_index_url = "http://my.hlju.edu.cn/index.portal"

# 神奇的payload
my_hlju_payload = {
    'Login.Token1': '',  # 用户名
    'Login.Token2': '',  # 密码
    'captcha': '',       # 验证码
    'goto': 'http%3A%2F%2Fmy.hlju.edu.cn%2FloginSuccess.portal',
    'gotoOnFail': 'http%3A%2F%2Fmy.hlju.edu.cn%2FloginFailure.portal',
}

# 如需多次（暴力）访问请加上header 避免被KILL
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

check_student_url2 = "http://ssfw1.hlju.edu.cn/ssfw/common/ajaxLoginResult.jsp?success=true"



# 教务管理系统（师生服务）
teacher_student_captcha_url = "http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do"  # 获取验证码 
# 登录行为： POST 方法 需要提供post数据。使用 payload: teacher_student_payload  
check_student_url1 = "http://ssfw2.hlju.edu.cn/ssfw/j_spring_ids_security_check"
# index 主页
teacher_student_index = "http://ssfw1.hlju.edu.cn/ssfw/index.do"

# 查询成绩
look_cj = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/cjxx.do"

# 查询课表
look_kb = "http://ssfw1.hlju.edu.cn/ssfw/pkgl/kcbxx/xskcb.do"

# 查询培养方案
look_py = "http://ssfw1.hlju.edu.cn/ssfw/zhcx/pyfa/xsfaTree.do"

# 查询个人考试信息
look_kx = "http://ssfw1.hlju.edu.cn/ssfw/xsks/kcxx.do"

# 屌炸天的payload 
teacher_student_payload = {
    'j_username': '',  # 这几个应该都知道是什么
    'j_password': '',
    'validateCode': '',
}

# 如需多次（暴力）访问请加上header 避免被KILL
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


# 选课网站 xsxk.hlju.edu.cn/xsxk
xsxk_captcha = "http://xsxk.hlju.edu.cn/xsxk/servlet/ImageServlet"  # 获取验证码
# 验证登录抓包发现的验证过程。 应该可以跳过
xsxk_check_login = "http://xsxk.hlju.edu.cn/xsxk/loadData.xk?method=checkLogin&username={}&password={}&verifyCode={}"
# 登录行为： POST 方法 需要提供post数据。使用 payload: xsxk_payload
xsxk_login = "http://xsxk.hlju.edu.cn/xsxk/login.xk"

# 比较屌的payload
xsxk_payload = {
    "username": '',
    "password": '',
    "verifyCode": ''
}

# header
xsxk_header = {
    'Host': 'xsxk.hlju.edu.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.8.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://xsxk.hlju.edu.cn/xsxk/logout.xk',
}


# 黑龙江大学图书馆
lib_captcha = "http://210.46.107.77:8080/kaptcha"  # 获取验证码
# 登录行为： POST 方法 需要提供post 数据。
lib_login = "http://210.46.107.77:8080/pages/include/checklogin.jsp"

# payload
lib_payload = {
    "username": "",
    "password": "",
    "loginType": "barCode",
    "kaptcha": "",
}

# header
lib_header = {
    'Host': '210.46.107.77:8080',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://210.46.107.77:8080/opac/login'
}

# 黑龙江大学身份认证平台 比较简单无需验证码
ids_login_url = 'http://ids.hlju.edu.cn/amserver/UI/Login'

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
