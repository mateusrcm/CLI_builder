import datetime


class People:

    def __init__(self, __id__: int, name: str, cpf: str, email: str, account: object, birthday: object):
        self.__id__ = __id__
        self.name = name
        self.cpf = cpf
        self.email = email
        self.account = account
        self.birthday = birthday

    def __repr__(self):
        pass

    def get_age(self):
        return abs(self.birthday - datetime.datetime)
