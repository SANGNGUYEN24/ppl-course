class Exp:
    def eval(self):
        pass

    def printPrefix(self):
        pass


class BinExp(Exp):
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

    def printPrefix(self):
        _left = self.left.printPrefix()
        _right = self.right.printPrefix()
        return self.operator + " " + _left + " " + _right


class UnExp(Exp):
    def __init__(self, operator: str, operand):
        self.operator = operator
        self.operand = operand.eval()

    def eval(self):
        if self.operator == '+':
            return +self.operand
        if self.operator == '-':
            return -self.operand

    def printPrefix(self):
        _operand = self.operand.printPrefix()
        return self.operator + ". " + _operand


class IntLit:
    def __init__(self, number):
        self.value = int(number)

    def eval(self):
        return self.value

    def printPrefix(self):
        return self.value


class FloatLit:
    def __init__(self, number):
        self.value = float(number)

    def eval(self):
        return self.value

    def printPrefix(self):
        return self.value
