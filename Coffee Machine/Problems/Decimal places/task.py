def decimal_places():
    floating_point = float(input())
    decimal_count = int(input())

    print(f"%.{decimal_count}f" % floating_point)


decimal_places()
