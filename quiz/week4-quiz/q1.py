# To express an arithmetic expression, there are 5 following classes:
# Exp: general arithmetic expression
# BinExp: an arithmetic expression that contains one binary operators (+,-,*,/) and two operands
# UnExp: an arithmetic expression that contains one unary operator (+,-) and one operand
# IntLit: an arithmetic expression that contains one integer number
# FloatLit: an arithmetic expression that contains one floating point number
# Define these classes in Python (their parents, attributes, methods) such that their objects can
# response to eval() message by returning the value of the expression. For example,
# let object x express the arithmetic expression 3 + 4 * 2.0, x.eval() must return 11.0

# class Literal:
#     def eval(self):
#         pass
#

class Exp:
    def eval(self):
        pass


class BinExp:
    def __init__(self, left, operator: str, right):
        self.operator = operator
        self.left = left.eval()
        self.right = right.eval()

    def eval(self):
        if self.operator == '+':
            return self.left + self.right
        if self.operator == '-':
            return self.left - self.right
        if self.operator == '*':
            return self.left * self.right
        if self.operator == '/':
            return self.left / self.right


class UnExp(Exp):
    def __init__(self, operator: str, operand):
        self.operator = operator
        self.operand = operand.eval()

    def eval(self):
        if self.operator == '+':
            return +self.operand
        if self.operator == '-':
            return -self.operand


class IntLit:
    def __init__(self, number):
        self.value = int(number)

    def eval(self):
        return self.value


class FloatLit:
    def __init__(self, number):
        self.value = float(number)

    def eval(self):
        return self.value


