from abc import ABC, abstractmethod

import sys
from parser import ServiceFactory

# """ Абстрактный класс для реализации адаптеров курортов. """
# class Table(ABC):
#     @abstractmethod
#     def __init__():
#         pass
    
#     @abstractmethod
#     def loadData(self):
#         pass


#     @abstractmethod
#     def getData(self):
#         pass


# class RosaAdapt(Table):
#     def __init__(self, data):
#         self.tp = data[0]
#         self.name = data[1]
#         self.distance = data[2]
#         self.people = data[3]
#         self.worktime = data[4]
#         self.status = data[5]
    
    
#     def loadData(self):
#         pass


#     def getData(self):
#         pass



# class LauraAdapt(Table):
#     def __init__(self, data):
#         self.tp = data[0]
#         self.name = data[1]
#         self.route = data[2]
#         self.worktime = data[3]
#         self.status = data[4]


#     def loadData(self):
#         pass


#     def getData(self):
#         pass


# class PolyanaAdapt(Table):
#     def __init__(self, data):
#         self.tp = data[0]
#         self.name = data[1]
#         self.status = data[2]


#     def loadData(self):
#         pass


#     def getData(self):
#         """select * from roads where courort = "Polyana"""
#         pass

# class ServiceFactory:
#     def __init__(self):
#         self.rosa = RosaChutor()
#         self.laura = Laura()
#         self.polyana = Polyana()

#     def getRosa(self):
#         return self.rosa.parseDoc()

#     def getLaura(self):
#         return self.laura.parseDoc()

#     def getPolyana(self):
#         return self.polyana.parseDoc()


obj = ServiceFactory()
a = obj.getPolyana()
print(a[0])