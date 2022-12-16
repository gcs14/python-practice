## Aminal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## a dog is-an animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## a cat is-an animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## a person is-an object
class Person(object):
    
    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## this employee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## employee has-a name
        ## When the subclass calls the parent class, 
        # use super(subclass name, self). Method name (parameter)
        ## The child class Employee needs to call the name of the 
        # parent class Person, because there is no such thing as 
        # name
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is an oject
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## haibut is-a fish 
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Jesus is-a cat
jesus = Cat("Jesus")

## mary is-a person
mary = Person("Mary")

## mary has-a pet named Jesus
mary.pet = jesus

## frank is-a employee making 120,000 dollars a year
frank = Employee("Frank", 120000)

## frank has-a pet named "Rover"
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

## tom has-many pets
tom = Person("Tom")
tom.pet = ["Terry", "Jerry", "Barry", "Perry", "Phil"]

print(tom.pet)