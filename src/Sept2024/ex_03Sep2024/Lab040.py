# Real life example
# Web automation, login page

class VWOLoginPage:
    def __init__(self, email_args, password_args):
        self.email = email_args
        self.password = password_args

    # Behaviour
    def confirm_login(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Login allowed")
        else:
            print("Login not allowed")

email = input("Enter the email: ")
password = input("Enter the password: ")
# Create obj
vwo_obj = VWOLoginPage(email, password)
vwo_obj.confirm_login()

vwo_obj1 = VWOLoginPage("pramod@gmail.com", "pass123")
vwo_obj1.confirm_login()


