""" Bank Class """
class Bank:
    def __init__(self, name, acc):
        self.name = name
        self.acc = acc

""" Account Class """
class Account:
    def __init__(self, name):
        self.name = name

""" Customer Class """
class Customer:
    def __init__(self, name):
        self.name = name

a = Account('MyAccount')
b = Bank('DB', a.__dict__)

print(b.__dict__)