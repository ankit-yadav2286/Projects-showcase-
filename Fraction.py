class Fraction:

    def __init__(self,nr,dr):

        self.nr=nr
        self.dr=dr

    def __str__(self):
        return f"{self.nr}/{self.dr}"

    def __add__(self, other):
        temp_num=self.nr * other.dr + other.nr * self.dr
        temp_den=self.dr * other.dr
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self, other):
        temp_num=self.nr * other.dr - other.nr * self.dr
        temp_den=self.dr * other.dr
        return "{}/{}".format(temp_num,temp_den)

    def __mul__(self, other):
        temp_num=self.nr * other.nr
        temp_den=self.dr * other.dr
        return "{}/{}".format(temp_num,temp_den)

    def __truediv__(self,other):
        temp_num=self.nr * other.dr
        temp_den=self.dr*other.nr
        return "{}/{}".format(temp_num, temp_den)

num1=Fraction(7,8)
print(num1)
num2=Fraction(4,5)
print(num2)

print(num1+num2)
print(num1 - num2)
print(num1*num2)
print(num1/num2)