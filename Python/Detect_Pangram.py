#A pangram is a sentence that contains every single letter of the alphabet at least once. 

#For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# MY SOLUTION:

import string

def is_pangram(s):
    alphabet_lst = list(string.ascii_lowercase)
    letter_lst = list(s.lower())
    check =  all(item in letter_lst for item in alphabet_lst)
    return check


#TEST: 
  
pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)
