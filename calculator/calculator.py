class Calculator():

    def add(self,a,b):
        return a+b

    def div(self,a,b):
        if b != 0:
            return a // b

    def cheng(self,a,b):
        return a*b

    def minus(self,a,b):
        if a >= b:
            return a-b
        else:
            return b-a


