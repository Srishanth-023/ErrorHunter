'''Comparing arrays'''

'''This problem helps one to understand the key concepts of an array(list) in Python. 
Two arrays are said to be the same if they contain the same elements and in the same order.
However, in this problem, we will compare two arrays to see if they are same, but with a slight twist.
Here, two arrays are the same if the elements of one array are squares of elements of other arrays and regardless of the order. 
Consider two arrays a and b.

'''
# function to compare the arrays 
def comp(array1, array2): 
 
    # Handle edge cases where one or both arrays could be None
    if array1 is None or array2 is None:
        return array1 == array2  # Return True only if both are None

    # Check if sorted squares of array1 are equal to sorted elements of array2
    return (sorted(array1) == sorted([i ** 2 for i in array2])) or (sorted(array2) == sorted([i ** 2 for i in array1]))
 
# Example usage:
print(comp([1, 2, 3, 4], [1, 4, 9, 16]))
 
 
   
    if array1 is None and array2 is not None:  
        return False
      
     
    if (sorted(array1) == sorted([i ** 2 for i in array2])) or (sorted(array2) == sorted([i ** 2 for i in array1])):  
        return True
      
    return False
  
lis1=eval(input("Enter list 1: "))
lis2=eval(input("Enter list 2: "))
print(comp(lis1,lis2))
 