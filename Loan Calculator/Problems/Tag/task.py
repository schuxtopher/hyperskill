def tagged(func):
    def wrapper(arg):
        return f"<title>{func(arg)}</title>"

    return wrapper
