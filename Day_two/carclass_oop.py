class Car:
  #default values
  num_of_doors = 4
  num_of_wheels = 4
  type = 'saloon'
  name = 'General'
  model = 'GM'
  
  
  #default properties
  def __init__(self, model, name):
    self.model = 'model'
    self.name = 'name'



class honda(Car):
  name = 'Honda'
  
class toyota(Car): 
  name = 'Toyota'
  model = 'Corola'


class opel(Car):
  name = 'Opel'
  model = 'Omega 3'
  
class porshe(Car):
  name = 'Porshe'
  model = '911 Turbo'
  num_of_wheels = 2
  
  
class koenigsegg(Car):  
  name = 'Koenigsegg'
  model = 'Agera R'
  num_of_wheels = 2

print toyota.model

print honda.model
print koenigsegg.num_of_wheels