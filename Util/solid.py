class Customer():
    def get_discount(self, total_sale):
        return total_sale

    def print_num(self, num1, num2 = None):
        if not num2:
            print("Base num1: " + str(num1))
        else:
            print("Base num1 and num2: " + str(num1) + " : "+ str(num2))


class GoldCustomer(Customer):
    def get_discount(self, total_sale):
        return super(GoldCustomer,self).get_discount(total_sale) - 100

    def print_num(self, num1, num2 = None):
        if not num2:
            print("num1: " + str(num1))
        else:
            print("num1 and num2: " + str(num1) + " : "+ str(num2))

class SilverCustomer(Customer):
    def get_discount(self, total_sale):
        return super(SilverCustomer,self).get_discount(total_sale) - 50


customer = GoldCustomer()
customer.print_num(12)
customer.print_num(12, 13)
print(customer.get_discount(500))

customer = SilverCustomer()
print(customer.get_discount(500))

import interface
from interface import implements, Interface
class I(Interface):
    def method(self, a, b):
        pass

class C(implements(I)):
    def method(self):
        return "This shouldn't work"


