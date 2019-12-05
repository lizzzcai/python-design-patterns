


# Duck Behaviors

class FlyBehavior:
    def fly(self):
        raise NotImplementedError


class QuackBehavior:
    def quack(self):
        raise NotImplementedError

# Implementing the Duck Behaviors

# Fly Behaviors
class FlyWithWings(FlyBehavior):
    def fly(self):
        # implements duck flying
        pass

class FlyNoWay(FlyBehavior):
    def fly(self):
        # do nothing - can't fly!
        pass

# Quack Behaviors
class Quack(QuackBehavior):
    def quack(self):
        # implements duck quacking
        pass

class Squeak(QuackBehavior):
    def quack(self):
        # rubber duckie squeak
        pass

class Quack(QuackBehavior):
    def quack(self):
        # do nothing - can't quack!
        pass

# Integrating the Duck Behavior

class Duck:
    def __init__(self):
        self.quackBehavior = None
        self.flyBehavior = None

    def performQuack(self):
        self.quackBehavior.quack()
    
    def performFly(self):
        self.flyBehavior.fly()