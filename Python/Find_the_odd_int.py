#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.


def find_it(seq):

    for int in seq:
        count = seq.count(int)
        if count % 2 == 1:
            return int
