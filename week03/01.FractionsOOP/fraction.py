from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        assert denominator >= 1, 'Zero or negative denominator.'

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        return f'Fraction {self}'

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __add__(self, other):
        numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator).simplify()

    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def simplify(self):
        divider = gcd(self.numerator, self.denominator)

        return Fraction(self.numerator // divider, self.denominator // divider)
