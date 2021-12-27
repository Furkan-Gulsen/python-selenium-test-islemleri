class Calculator(object):
    def __init__(self):
        self.result = 0.0

    @property
    def last_answer(self):
        return self.result

    def add(self, a, b):
        self.result = a + b
        return self.last_answer

    def subtract(self, a, b):
        self.result = a - b
        return self.last_answer

    def multiply(self, a, b):
        self.result = a * b
        return self.last_answer

    def divide(self, a, b):
        self.result = a * 1.0 / b
        return self.last_answer

    def maximum(self, a, b):
        self.result = a if a >= b else b
        return self.last_answer

    def minimum(self, a, b):
        self.result = a if a <= b else b
        return self.last_answer