import abc


# BettingStrategy will work as a superclass with default values
# The basic bet() method in the abc superclass will raise an exception.
# bet() method must be overriden in the subclasses, the rest can remain
# the same to provide default values
class BettingStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass
