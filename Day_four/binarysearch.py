class BinarySearch(list): #inherits from the List class
  
  def __init__(self, a, b):
    self.length = a
    
    #using the super fn to create a list by accessing methods inside the list
    super(BinarySearch, self).__init__(self)
    
    #creating the list to search, take b as the step and intial value, a as length, max value of the list will be a*b, hence range upper limit is a*b + 1
    #self = self + range(b, (a*b) + 1, b)
    self += range(b, (a*b) + 1, b) #assignments to self can only be made using += and not = << raises error

    
    self.arr = self

  def print_list(self):
    #just to print out the array // self check note
    print self.arr

  def search(self, search_value):
    #method  only takes one argument which is the value to search 
    search_dict = {} #template for count and index pairs

if __name__ == '__main__': #read more about it
    bs = BinarySearch(20,2)
    bs.print_list() 