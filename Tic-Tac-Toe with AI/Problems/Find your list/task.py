def find_my_list(_all_lists, my_list):
    for _index, lst in enumerate(_all_lists):
        # Change the next line
        if lst is my_list:
            return _index
    return None
