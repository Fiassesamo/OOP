class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Robot {self.name} created")
        Robot.population+=1

    def destroy(self):
        return f"Robot {self.name} was destroyed"
        del self

    def say_hello(self):
        return f"Robot {self.name} say hello"

    @staticmethod
    def how_many():
        return f"{Robot.population} Still alive"

r2 = Robot('R2-D2')
print(r2.say_hello())
r2_test2=Robot('R2-F1')
print(Robot.how_many())
print(r2.destroy())

