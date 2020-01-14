


# Duck Behaviors

# The interface that all flying behavior classes implement
class FlyBehavior:
    def fly(self):
        raise NotImplementedError


class QuackBehavior:
    def quack(self):
        raise NotImplementedError

# Implementing the Duck Behaviors

# Fly Behaviors

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

# Quack Behaviors
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

class Duck:
    def __init__(self):
        
        # Declare two reference variables for the behavior interface types.
        # All duck subclasses inherit these.
        self.quackBehavior = None
        self.flyBehavior = None

    def display(self):
        raise NotImplementedError

    # Delegate to the behavior class
    def performQuack(self):
        self.quackBehavior.quack()
    
    def performFly(self):
        self.flyBehavior.fly()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()
    
    def display(self):
        print("I'm a real Mallard duck")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()