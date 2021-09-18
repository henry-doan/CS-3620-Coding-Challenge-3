# Part 1
def studentDiscount(amt): 
  discounted = 0.10 * amt
  return amt - discounted

def moreDiscount(amt):
  discounted = 0.05 * amt 
  return amt - discounted

# test case with $90
print(moreDiscount(studentDiscount(90.00)))

# Part 2
#x*(x+5)^2 where x = 5 with order of operations
result = (lambda x:(x*((x+5)**2)))(5)
print(result)

# Part 3
# initial prices
prices = [10.00, 20.00, 30.00, 40.00, 50.00]

def discountAll(price):
  discounted = 0.10 * price 
  return price - discounted

# map and discount the list
result = list(map(discountAll, prices))

print(result)

# Part 4
# computer parent class
class Computer:

  def __init__(self, cpu, ram, storage, graphicCard):
    self.cpu = cpu 
    self.ram = ram 
    self.storage = storage 
    self.graphicCard = graphicCard

  def getspecs(self, cpu, ram, storage, graphicCard):
    self.cpu = cpu 
    self.ram = ram 
    self.storage = storage 
    self.graphicCard = graphicCard

  def displayspecs(self):
    print(self.cpu)
    print(self.ram)
    print(self.storage)
    print(self.graphicCard)

# desktop child class inherit parent class
class Desktop(Computer):

  def __init__(self, powerWatts):
    self.powerWatts = powerWatts 

  def getDesktopSpecs(self, powerWatts):
    self.powerWatts = powerWatts 

  def displayDesktopSpecs(self):
    print(self.powerWatts)

# desktop child class inherit parent class
class Laptop(Computer):

  def __init__(self, batteryLife):
    self.batteryLife = batteryLife 

  def getLaptopSpecs(self, batteryLife):
    self.batteryLife = batteryLife 

  def displayLaptopSpecs(self):
    print(self.batteryLife)

com = Computer("", "", "", "")
# would get the user input on each field by autofill to show results
com.getspecs("Intel I7", "16GB", "100TB", "3090")
com.displayspecs()

desktop1 = Desktop("")
desktop1.getspecs("Intel I9", "32GB", "10TB", "30800")

desktop1.displayspecs()
desktop1.getDesktopSpecs("1000Watts")
desktop1.displayDesktopSpecs()

laptop1 = Laptop("")
laptop1.getspecs("Intel I7", "16GB", "100TB", "3090")

laptop1.displayspecs()
laptop1.getLaptopSpecs("700hrs")
laptop1.displayLaptopSpecs()

# Part 5
class OverloadingMult: 
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def __mul__(self, other):
    # product = num1 + num2
    num1 = self.num1 + other.num1
    num2 = self.num2 + other.num2
    return OverloadingMult(num1, num2)

  def __str__(self):
    return "({0}, {1})".format(self.num1, self.num2)

o = OverloadingMult(1, 2)
o1 = OverloadingMult(2, 2)
print(o * o1)