"""fizz_buzz function to return Fizz, Buzz, FizzBuzz depending on whether a function is divisible by 3, 5, both or neither"""
def fizz_buzz(num):
  #number divisible by 3 and 5
  if num % 3 == 0 and num % 5 == 0:
    return 'FizzBuzz'
    
  #number divisible by 3 only
  elif num % 3 == 0:
    return 'Fizz'
    
  #number divisible by 5 only
  elif num % 5 == 0:
    return 'Buzz'
    
  
  #number divisible by neither 3 nor 5
  else:
    return num
  
    
fizz_buzz(3)
fizz_buzz(33)
fizz_buzz(5)
fizz_buzz(25)
fizz_buzz(15)
fizz_buzz(105)
fizz_buzz(101)
fizz_buzz(8)  