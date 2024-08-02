class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str):
            len_email = [i for i in range(len(new_email)) if new_email[i] == "@"]
            if len(len_email) == 1:
                index_dog = len_email[0]
                len_dot = [j for j in range(len(new_email)) if new_email[j] == '.']
                index_dot = len_dot[0]
                if index_dot > index_dog:
                    self.__email = new_email
                    return self.__email
                else:
                    return 'this email can be use dot before @, pls change email'
            else:
                return f'Errormail {new_email}'

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', "prince@wait.you")
print(k.set_email('prince@still@.wait'))


