def descending_order(num):
    # Bust a move right here
    list_int = [x for x in str(num)] 
    list_int.sort(reverse = True)
    join_lst = ''.join(list_int)
    return int(join_lst)