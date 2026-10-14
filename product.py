from Pyro5.api import expose
 
@expose
class Product:
 
    def getName(self):
        raise NotImplementedError
 
    def getDescription(self):
        raise NotImplementedError
 
    def getPrice(self):
        raise NotImplementedError