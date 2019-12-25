# Convert Decibal number into Binary number:

"""
Given a decimal number as input, the task is to write a Python program 
to convert the given decimal number into equivalent binary number.


      2 | 17  1   ^
      2 | 8   0   |
      2 | 4   0   |
      2 | 2   0   |
        | 1   1   |
        
    17 =====>>>> 10001
    24 =====>>>> 11000
    7 =====>>>> 111
    

"""

def convertToBinary(num):
    if num > 1:
        convertToBinary(num//2)
    print num%2,


#Using inbuild Function
def decimalToBinary1(n):  
    return bin(n).replace("0b", "") 

dec_val = 24
convertToBinary(dec_val)
print "\n"
print decimalToBinary1(dec_val)
 
