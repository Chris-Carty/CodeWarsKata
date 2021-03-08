# Given two arrays a and b write a function that checks whether the two arrays have the "same" elements, with the same multiplicities. 

# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# E.G The two arrays below would return True.
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]


#MY SOLUTION:

def comp(array1, array2):
    if array1 == None or array2 == None or len(array1) != len(array2):
        return False 
    array1.sort(key=abs)
    array2.sort(key=abs)
    return all(a**2 == b for a, b in zip(array1, array2))
    
