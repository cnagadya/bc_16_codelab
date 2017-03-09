""" Car class to instatiate various vehicles"""
class Car(object):
  
  #car properties
  def __init__(self, name = 'General' , model = 'GM' , car_type = 'saloon'):
    self.name = name
    self.model = model
    self.car_type = car_type
    #self.speed = 0 #speed initially 0, ie when parked
    self.speed = 0
    

    #setting the doors no.
    if self.name == 'Porshe' or  self.name == 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
  

    #setting the wheel no.
    if self.car_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
      
  #for the saloon cars    
  def is_saloon(self):
    if self.car_type != 'trailer':
      return True
  
  
  #speed when pedal is hit using 
  def drive(self, drive_gear):
  
    if self.car_type == 'trailer':
      self.speed = 11*drive_gear
      
    else:
      self.speed = 10**drive_gear
      
    return self
      
  
honda = Car(name ='Honda')

toyota = Car(name ='Toyota', model = 'Corolla')

opel = Car(name ='Opel',  model = 'Omega 3')

porshe = Car(name ='Porshe',  model = '911 Turbo')

koenigsegg = Car(name ='Koenigsegg', model = 'Agera R')


  


print toyota.model

print honda.model
print honda.num_of_doors
print porshe.num_of_doors
