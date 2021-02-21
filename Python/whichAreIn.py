#Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

#returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

#returns []

MY SOLUTION

def in_array(array1, array2):
    
    new_arr = []
    
    for word2 in array2:
        for word1 in array1:
            if word1 in word2:
                if word1 not in new_arr:
                    new_arr.append(word1)
    new_arr.sort()
    return new_arr
    
    IMPROVED SOLUTION
    
    def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
