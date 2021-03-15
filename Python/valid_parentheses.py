#Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
#The function should return true if the string is valid, and false if it's invalid.

#e.g

# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# MY SOLUTION:

def valid_parentheses(myStr):
  
    #The lists below could be expanded to other types of parentheses i.e '[' or '{' 
    open_list = ["("] 
    close_list = [")"]
    
    stack = []
    
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False
  
  
