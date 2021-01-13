class Car:
    serial = 1000
    def __init__(self, id, name, fsize, cfsize):
        self.__id = id
        self.__name = name
        self.__fszie = fsize
        self.__cfszie = cfsize
        self.__serial = Car.serial
        Car.serialCount()

    @classmethod
    def serialCount(cls):
        cls.serial += 1

    def print(self):
        return self.__id, self.__name, self.__fszie, self.__cfszie, self.__serial

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getFsize(self):
        return self.__fszie

    def getCfsize(self):
        return self.__cfszie

    def setCfsize(self, size):
        self.__cfszie += size

