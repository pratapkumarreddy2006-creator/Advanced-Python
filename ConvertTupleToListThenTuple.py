t = (5, 15, "hi", 3, 20)

lst = list(t)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]

t_new = tuple(lst)
print(t_new)