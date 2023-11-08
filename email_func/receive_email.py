import email
import poplib

# # 配置邮箱服务器和端口号
# pop_server = "imap.feishu.cn"
# pop_port = 993
#
# # 登录邮箱
# username = ""
# password = ""
# pop = poplib.POP3_SSL(pop_server, pop_port)
# pop.user(username)
# pop.pass_(password)
#
# # 获取邮件列表和内容
# message_list = pop.list()
# for num in message_list[1]:
#     # 获取邮件头部信息
#     header = pop.top(num, 0)[0]
#     # 获取邮件内容
#     content = pop.top(num, 1)[0].decode("utf-8")
#     print(f"Subject: {header.split()[0]}")
#     print(f"From: {header.split()[1]}")
#     print(f"To: {header.split()[2]}")
#     print(f"Date: {header.split()[3]}")
#     print(content)
#     print("=" * 50)
#
# # 关闭邮箱连接
# pop.quit()

import imaplib
import datetime

# 配置邮箱服务器和端口号
imap_server = "imap.feishu.cn"
imap_port = 993

# 登录邮箱
username = "coffee.qiao@shaoke.com"
password = "6GkV0CG4QEVBiYXW"
mail = imaplib.IMAP4_SSL(imap_server, imap_port)
mail.login(username, password)

# 选择一个文件夹
mail.select("inbox")
today = datetime.date.today()
# 搜索邮件
status, messages = mail.search(None,'ON 07-Nov-2023')
print(type(messages))
print(len(messages))
print(messages)
# 遍历并打印每条邮件的主题
for num in messages[0].split():
    print(num)
    status, message = mail.fetch(num, '(RFC822)')
    print(status)
    print(len(message))
    email_message = message[0][1]
    email_parser = email.message_from_bytes(email_message)
    # 构建一个新的邮件消息对象
    new_msg = email.message.Message()
    new_msg['From'] = email_parser['From']
    new_msg['To'] = email_parser['To']
    new_msg['Subject'] = email_parser['Subject']
    new_msg['Date'] = email_parser['Date']
    # new_msg.set_payload(email_parser.get_payload())
    for part in email_parser.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True)
            print('Body:',body.decode('utf-8'))
