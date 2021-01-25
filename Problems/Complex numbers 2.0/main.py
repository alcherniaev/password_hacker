class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.im_part * other.im_part
        imaginary = self.real_part * other.im_part + other.real_part * self.im_part
        return ComplexNumber(real, imaginary)

    def __eq__(self, other):
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))

    def __str__(self):
        if self.im_part < 0:
            sign = "-"
        else:
            sign = "+"
        string = "{} {} {}i".format(self.real_part, sign, abs(self.im_part))
        return string

    def __sub__(self, other):
        real = self.real_part - other.real_part
        imaginary = self.im_part - other.im_part
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def reciprocal(self):
        real_reciprocal = (self.real_part / (self.real_part ** 2 + self.im_part ** 2))
        im_reciprocal = -(self.im_part / (self.real_part ** 2 + self.im_part ** 2))
        return ComplexNumber(real_reciprocal, im_reciprocal)