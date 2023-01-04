#Class is defined. Defines two variables speed and started.
class Car:
    speed = 0
    started = False

#Defines three methods that operate on the variables
#Python automatically fills in the first variable (self) and uses the name
#you can use self to reference other instance variable self.speed

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print('Halting')

#Creates instance of class Car with Car()
car = Car()
car.increase_speed(10)
car.start()
car.increase_speed(40)

