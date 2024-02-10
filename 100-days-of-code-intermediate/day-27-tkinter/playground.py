def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

num = add(1, 2, 3)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=4)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan")
print(my_car.model)