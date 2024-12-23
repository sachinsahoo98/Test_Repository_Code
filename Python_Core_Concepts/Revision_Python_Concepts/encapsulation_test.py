class Car:
    __drive = False
    def __init__(self, speed):
        self.__speed = speed
        self.__drive = False

    def accelerate(self, value):
        self.__speed +=value
        self.__drive = True

    def brake(self, value):
        self.__speed -= value
        if self.__speed == 0:
            self.__drive = False

    def getCurrentSpeed(self):
        return self.__speed


class Mercedes(Car):
    def __init__(self, speed, model):
        super().__init__(speed)
        self.model = model



Lambo = Car(0)
Lambo.accelerate(100)
print("Current Speed after acceleration is:")
initSpeed = Lambo.getCurrentSpeed()
print(initSpeed)
print("Current Speed after brake is:")
Lambo.brake(30)
brakeSpeed = Lambo.getCurrentSpeed()
print(brakeSpeed)



mercedes = Mercedes(0, "M1")
print("Current Speed is:", mercedes.getCurrentSpeed())
