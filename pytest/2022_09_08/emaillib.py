# content of emaillib.py

class MailAdminClient:
    # 创建用户
    def create_user(self):
        return MailUser()

    def delete_user(self, user):
        # do some cleanup
        pass


class MailUser:
    def __init__(self):
        self.inbox = []
    # 发送邮件,[mail]
    def send_email(self, email, other):
        other.inbox.append(email)
    # 清除邮件
    def clear_mailbox(self):
        self.inbox.clear()

# 邮件类
class Email:
    # 初始化主题,邮件主体
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body