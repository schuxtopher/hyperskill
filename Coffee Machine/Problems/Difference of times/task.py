t0_hours = int(input())
t0_minutes = int(input())
t0_seconds = int(input())
t1_hours = int(input())
t1_minutes = int(input())
t1_seconds = int(input())

t0_seconds = t0_hours * 60 ** 2 + t0_minutes * 60 + t0_seconds
t1_seconds = t1_hours * 60 ** 2 + t1_minutes * 60 + t1_seconds

delta_seconds = t1_seconds - t0_seconds

print(delta_seconds)
