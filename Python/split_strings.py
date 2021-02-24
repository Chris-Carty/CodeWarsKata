#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

#Examples:

#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']

#MY SOLUTION: 

def solution(s):
    n = 2
    split_lst = [s[i:i+n] for i in range(0, len(s), n)]
    for c, i in enumerate(split_lst):
        if len(i) < 2:
            split_lst[c] = i + "_"
    return split_lst
  
#IMPROVED SOLUTION: 

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
  
  
