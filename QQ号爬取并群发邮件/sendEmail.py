import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 配置发送方信息
from_addr = ''  # 发送邮箱
password = ''  # 授权码

# 发信服务器
host = 'smtp.qq.com'


def send_email(to_addr, content):

    # 构建邮件正文内容
    msg = MIMEText('hello %s' % content, 'plain', 'utf-8')

    # 构建邮件头部信息
    msg['From'] = Header('1924086038@qq.com')
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('群发邮件测试')

    # 连接邮件发送服务器
    server = smtplib.SMTP_SSL(host)
    server.connect(host, '465')
    # 登录邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


if __name__ == '__main__':
    send_email('', '逍遥子')
