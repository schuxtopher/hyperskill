def morning(func):
    def wrapper(arg):
        func(arg)
        print(f"Good morning, {arg}")

    return wrapper
