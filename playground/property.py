class Temperature:
    def __init__(self, value):
        self.degrees = float(value)

    @property
    def farenheit(self):
        return (self.degrees * 1.8) + 32

    @farenheit.setter
    def farenheit(self, value):
        self.degrees = (value - 32) / 1.8


t = Temperature(100)
print(t.degrees, t.farenheit)

t.farenheit = 100
print(t.degrees, t.farenheit)
