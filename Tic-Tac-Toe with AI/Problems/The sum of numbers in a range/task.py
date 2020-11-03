def range_sum(numbers, start, end):
    if not numbers:
        return 0
    return sum(x for x in numbers if start <= x <= end)


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))
