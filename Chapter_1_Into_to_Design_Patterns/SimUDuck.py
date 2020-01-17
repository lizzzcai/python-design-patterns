from abc import ABC, abstractmethod
##################
# Duck Behaviors
##################
# The interface that all flying behavior classes implement
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

##################
# Implementing the Duck Behaviors
##################

### Fly Behaviors ###

# Flying behavior implementation for ducks that DO fly 
class FlyWithWings(FlyBehavior):
    def fly(self):
        # implements duck flying
        print("I'm flying !!")

# Flying behavior implementation for ducks that DO NOT fly(like rubber ducks and decoy ducks)
class FlyNoWay(FlyBehavior):
    def fly(self):
        # do nothing - can't fly!
        print("I can't fly")

# Rocket powered flying behavior
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


### Quack Behaviors ###
class Quack(QuackBehavior):
    def quack(self):
        # implements duck quacking
        print("Quack")

class Squeak(QuackBehavior):
    def quack(self):
        # rubber duckie squeak
        print("Squeak")

class MuteQuack(QuackBehavior):
    def quack(self):
        # do nothing - can't quack!
        print("<< Silence >>")

# Integrating the Duck Behavior // Page.15

# Duck Abstracted class
class Duck(ABC):
    def __init__(self):
        # Declare two reference variables for the behavior interface types.
        # All duck subclasses inherit these.
        self.quackBehavior = None
        self.flyBehavior = None

    # setting behavior dynamically on the fly
    def setFlyBehavior(self, fb):
        self.flyBehavior = fb
    
    def sefQuackBehavior(self, qb):
        self.quackBehavior = qb

    @abstractmethod
    def display(self):
        raise NotImplementedError

    # Delegate to the behavior class
    def performQuack(self):
        self.quackBehavior.quack()
    
    def performFly(self):
        self.flyBehavior.fly()

    def swim(self):
        print("All ducks float, even decoys!")

##################
# Extend the Duck
##################

class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()
    
    def display(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyNoWay()
    
    def display(self):
        print("I'm a model duck")



# Testing the MallardDuck code
def MiniDuckSimulator():
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()

    model = ModelDuck()
    model.display()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()



if __name__ == "__main__":
    MiniDuckSimulator()
