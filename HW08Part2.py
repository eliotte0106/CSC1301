"""
Georgia Institute of Technology - CS1301 - Summer 2021
HW08 Part 2 - Recursion
Collaboration Statement:
"""

#########################################

"""
Function Name: doubleChars()  
Parameters: sentence (str)   
Returns: number of times there are two of the same
         characters in a row (int)
"""

def doubleChars(sentence):
    if len(sentence) <= 1:
        return 0
    if sentence[0] == sentence[1]:
        return doubleChars(sentence[1:]) + 1
    return doubleChars(sentence[1:])
    
#print(doubleChars("the queen fell down a cliff"))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################
#print(doubleChars("the queen fell down a cliff"))
"""
Function Name: sumOfNums()  
Parameters: string of characters (str)
Returns: sum of the digits within the string (int)
"""

def sumOfNums(string):
    if len(string) == 0:
        return 0
    if string[0].isdigit():
        return sumOfNums(string[1:]) + int(string[0])
    return sumOfNums(string[1:])

print(sumOfNums("1xsrsr78ms3"))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################
