# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import cookielib
import urllib
import urllib2

ID_USERNAME = 'loginform-username'
ID_PASSWORD = 'loginform-password'
USERNAME = '419288922@qq.com'
PASSWORD = 'jwh6867285'
LOGIN_URL = 'http://home.51cto.com/index?reback=http://www.51cto.com/'
NORMAL_URL = 'http://home.51cto.com/'


def extract_cookie_info():
    """
    用cookie登录网站
    :return:
    """
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME: USERNAME,
                                   ID_PASSWORD: PASSWORD})
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')]
    resp = opener.open(LOGIN_URL, login_data)

    # 发送登录信息
    for cookie in cj:
        print "第一次cookie: %s ---> %s" %(cookie.name, cookie.value)
        print "头部信息: %s" %resp.headers

    # 访问没有登录信息
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print "+++++第二次cookie: %s -- > %s" %(cookie.name, cookie.value)
        print "头部信息: %s" %resp.headers

if __name__ == '__main__':
    extract_cookie_info()
