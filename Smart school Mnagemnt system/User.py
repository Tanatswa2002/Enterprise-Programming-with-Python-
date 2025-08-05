#Base abstract class for each user

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,age):
        self.__name =name       #encapsulation, in that this variable is private, but why is this relavent and why is it being applied here?
        self.__age = age 


    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    #abtraction, what is the value and point of this?
    @abstractmethod
    def get_role(self):
        pass

    def describe(self):
        pass