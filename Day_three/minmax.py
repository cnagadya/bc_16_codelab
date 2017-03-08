""" find_max_min to find the maximun and minimum numbers in the list"""
def find_max_min(test_list):
  
  
  #for lists with same min and max
  if min(test_list) == max(test_list):
    return [len(test_list)]
    
  #lists with different min and max
  else:
    return [ min(test_list) , max(test_list)]
