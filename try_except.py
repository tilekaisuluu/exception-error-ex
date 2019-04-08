def exception(func):
    def wrapper_func(self, *args, **kwargs):
        if self.username == '':
            raise Exception('No username defined!')
        elif self.password == '':
            raise Exception('No password defined!')

    return wrapper_func


class User():
    def __init__(self):
        self.username = input("Enter name ")
        self.password = input("Enter password ")
    @exception
    def get_account_balance():
        return self.username

    @exception
    def change_password():
        return self.password



u = User()
u.get_account_balance()
u.change_password()
