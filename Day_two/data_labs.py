""" Function data_type() checks for the data type of the item"""
def data_type(item):
  #item is a string
  if isinstance(item,str):
    return len(item)
  
  
  #item is None"""
  elif item is None:
    return "no value"
  
  
  #item is a bool
  elif isinstance(item,bool):
    return item
  
  
  #item is an int
  elif isinstance(item,int):
    if item < 100: #less than 100
      return 'less than 100'
    elif item ==100: #equal to 100
      return 'equal to 100'
    else: #greater than 100
      return 'more than 100'
  
  
  #item is an list  
  elif isinstance(item,list):
    if len(item) >= 3:
      return item[2]
    else:
      return None
      
  else:
    pass
  
  
  

data_type(None)
data_type([1, 2, 3])
data_type([1, 2])
data_type(True)
data_type(3)
data_type(200)
data_type('andela')