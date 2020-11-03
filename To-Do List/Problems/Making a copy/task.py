import copy


def my_copy(obj, copy_mode):
    if copy_mode == "shallow copy":
        return copy.copy(obj)
    elif copy_mode == "deep copy":
        return copy.deepcopy(obj)
    else:
        return None
