""" words function to determine the number of times a word occurs in a string"""
def words(input_string):
  
  #dictionary template to display words as keys and occurances as values
  words_dict = {}
  
  #splitting string into list to enable iteration
  words_list = input_string.split()

  #iterate through the list to check for the
  for word in words_list:
  	#print (words_list.count(word))
  	words_dict[word] = words_list.count(word)
  print words_dict

  	

words("one fish two fish red fish blue fish")
words('testing 1 2 testing')
