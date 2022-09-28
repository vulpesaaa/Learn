#邮件客户端
class MailAdminClient:
    # 创建用户
    def create_user(self):
        return MailUser()
    # 删除用户
    def delete_user(self, user):
        # do some cleanup
        pass

# 邮件的用户类
class MailUser:
    def __init__(self):
        self.inbox = []
    # 发送邮件
    def send_email(self, email, other):
        other.inbox.append(email)
    # 清空邮箱
    def clear_mailbox(self):
        self.inbox.clear()

# 邮件类
class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body