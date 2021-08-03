import abc from ABC,abstractmathod

class CoffeeMatchine(ABC):
    def __init__(self,co,tea,mil,wt,su):
        self.coffee=co
        self.tea=tea
        self.milk=mil
        self.water=wt
    
    def coffee(self):
        pass
    
    def milk(self):
        pass
   
    def tea(self):
        pass
    @abstractmathod
    def water(self):
        pass
    @abstractmathod
    def sugar(self):
        pass



class blackCoffee(CoffeeMatchine):
    def __init__(self):
        pass
    
    def coffee(self):
        pass
    def water(self):
        pass
    def sugar(self):
        pass
    def price(self):
        pass

    
class blackTea(CoffeeMatchine):
    def __init__(self):
        pass
    
    def tea(self):
        pass
    def water(self):
        pass
    def sugar(self):
        pass
    def price(self):
        pass


    
class Coffee(CoffeeMatchine):
    def __init__(self):
        pass
    
    def coffee(self):
        pass
    def milk(self):
        pass
    def water(self):
        pass
    def sugar(self):
        pass
    def price(self):
        pass


    
class Tea(CoffeeMatchine):
    def __init__(self):
        pass
    
    def tea(self):
        pass
    def milk(self):
        pass
    def water(self):
        pass
    def sugar(self):
        pass
    def price(self):
        pass

    
'''class calCulate(blackCoffee,blackTea,Coffee,Tea):
    def __init__(self):
        pass
    
    def totle(self):
        pass'''


bcoffee = blackCoffee()
bta = blackTea()
coffee = Coffee()
tea = Tea()
#cal = calCulate()
while True:
    
