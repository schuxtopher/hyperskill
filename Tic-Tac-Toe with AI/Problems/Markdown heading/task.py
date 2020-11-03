def heading(string, level=1):
    if level < 1:
        return '#' + ' ' + string
    elif level > 6:
        return '#' * 6 + ' ' + string
    else:
        return '#' * level + ' ' + string
