# Lambda Function: Shorter way to write Fucntions.

The common observations are:

These functions don’t have a name

These functions don’t need indentation or { } to indicate function body for single line functions

These functions don’t need return statement for single line functions. The expression is automatically returned

Let us take a look at where these lambda functions are used extensively

Test = lambda x,y : y/x
print(Test(10,2) ---->5


num_list=[10,20,30,40,50]

print("Map example")
print(list(map(lambda x:x*2,num_list)))

print("Filter Example")
print(list(filter(lambda x:x>30,num_list)));

print("Chain Example")
print(list(filter(lambda x:x>30,map(lambda x:x*2,num_list))));



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) --->22




# Map Function: 
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax:
map(fun, iter)

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.



# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result))  ---> [2, 4, 6, 8]



numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result))  ------------> [2, 4, 6, 8]


numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result))  ------> [5, 7, 9]
