t = (1, "a", 5, 10.5, 8)

nums = [x for x in t if isinstance(x, (int, float))]
print("Numbers:", nums)

try:
    t[0] = 100
except TypeError:
    print("Tuples are immutable")

t2 = (9, 10)
print("Concatenated:", t + t2)