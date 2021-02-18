This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"


The parameter of accum is a string which includes only letters from a..z and A..Z.

MY SOLUTION: 

def accum(s):
    arr = list(s)
    new_arr = []
    for index, char in enumerate(arr):
        num_repeat = index + 1
        str = char * num_repeat
        new_arr.append(str.lower().capitalize())
    return '-'.join(new_arr)

BEST PRACTICE:

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
