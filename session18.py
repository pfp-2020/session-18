# -*- coding: utf-8 -*-

#%% Creating classes

#class ElectricCar:
    
class Car:
    pass

car1 = Car()
car2 = Car()
car3 = Car()

print(type(car1))

#%% constructing objects

class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    
ford_fiesta = Car("Ford", "Fiesta")
tesla_modelx = Car("Tesla", "Model X")

print(ford_fiesta.model)
    
print(tesla_modelx.brand)

print(dir(ford_fiesta))
    
#%% validation on construction
    
class Car:
    
    def __init__(self, brand, model):
        
        if brand != "Tesla":
            raise ValueError("Only Tesla accepted, we're green!")
        
        self.brand = brand
        self.model = model
    
car1 = Car("Tesla", "Model S")

car2 = Car("Ford", "Mondeo")
    
#%% 

class Clock:
    
    def __init__(self, hours, minutes):
        
        if type(hours) != int or type(minutes) != int:
            raise TypeError("hours and minutes need to be ints")
            
        if hours < 0 or hours > 23:
            raise ValueError("hours need to be in the 0-23 range")
        
        if minutes < 0 or minutes > 59:
            raise ValueError("minutes need to be in the 0-59 range")
        
        self.hours = hours
        self.minutes = minutes
    
    

clock1 = Clock(1, 55)
# clock_wrong = Clock("hello", "my friends")
#clock_wrong = Clock(3,-6)

#%%

class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.started = False
        
    def start_engine(self):
        self.started = True
        
    def honk(self):
        print("BEEEEEP")
        
        
car = Car("Audi", "A3")

print(car.started)

car.start_engine()

print(car.started)

car.honk()

#%%

class Member:
    
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        
    def play(self):
        print(self.name + " is playing the " + self.instrument)
        
john = Member("John", "voice")
paul = Member("Paul", "bass guitar")
george = Member("George", "guitar")
ringo = Member("Ringo", "drums")

    
class RockBand:

    def __init__(self):
        self.members = []
        
    def add_member(self, member):
        self.members.append(member)
    
    def rehearse(self):
        for member in self.members:
            member.play()
        
    
beatles = RockBand()

beatles.add_member(john)
beatles.add_member(paul)
beatles.add_member(george)
beatles.add_member(ringo)

beatles.rehearse()


















    
    
    
    