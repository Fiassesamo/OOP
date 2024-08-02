from string import digits
class Registration:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @staticmethod
    def is_include_digit(new_password):
        numbers_i_letter = [int(i) for i in new_password if i in digits]
        if numbers_i_letter:
            return True
        else:
            return False
    @staticmethod
    def is_include_all_register(new_password):
        lower_and_upper_letters = [[i for i in new_password if i.isupper()],
                                  [j for j in new_password if j.islower()]]
        if lower_and_upper_letters[0] and lower_and_upper_letters[1]:
            return True
        else:
            return False

    @staticmethod
    def is_include_only_latin(new_password):
        latin_Upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' 'V', 'X', 'Y', 'Z']
        latin_lower_letters = list(map(lambda x: x.lower(), latin_Upper_letters))
        letter_password = [i for i in new_password if i not in digits]
        latin_letter_password = [j for j in letter_password
                                 if j in latin_Upper_letters or j in latin_lower_letters]
        if len(latin_letter_password) == len(letter_password):
            return True
        else:
            return False

    @staticmethod
    def check_password_dictionary(new_password):
        file = 'easy_passwords.txt'
        with open(file, 'r', encoding='utf-8') as file:
            password = file.read().splitlines()
            if new_password in password:
                return False
            else:
                return True
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_email):
        if isinstance(new_email, str):
            len_email = [i for i in range(len(new_email)) if new_email[i] == "@"]
            if len_email:
                if len(len_email) == 1:
                    index_dog = len_email[0]
                    len_dot = [j for j in range(len(new_email)) if new_email[j] == '.']
                    if len_dot:
                        index_dot = len_dot[0]
                        if index_dot > index_dog:
                            self.__login = new_email
                    else:
                        raise ValueError('login must include at least one .')
            else:
                raise ValueError('login must include at least one @')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            if 4 < len(new_password) < 12:
                if self.is_include_digit(new_password):
                    if self.is_include_all_register(new_password):
                        if self.is_include_only_latin(new_password):
                            if self.check_password_dictionary(new_password):
                                self.__password = new_password
                            else:
                                raise ValueError('your password in list the most easiest')
                        else:
                            raise ValueError('password must have only latin alphabet ')
                    else:
                        raise ValueError('password must have 1 or more upper and lowers letters')
                else:
                    raise ValueError('password must have one or more number')
            else:
                raise ValueError('Password must be longest than 4 and less 12')
        else:
            raise TypeError('Password must be string')




obj = Registration("asddas", '1234')
print(obj.login)
obj.password = '1234567890'


