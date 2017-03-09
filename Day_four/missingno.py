"""find_missing function to compare two arrays and return the number in array 2 but not in array 1"""
def find_missing(array1, array2):
  
  #comparing empty lisys
	if array1 == [] or array2 == []:
		print 0
		
	#lists with same entries
	elif len(array1) == len(array2):
		print 0
	
  #number missing in one of the lists
	else:
		for num in array2:
			if num in array1:
				continue
			else:
				print num

find_missing([1, 2], [1, 2, 5])
find_missing([1, 2], [1, 2])
find_missing([],[])