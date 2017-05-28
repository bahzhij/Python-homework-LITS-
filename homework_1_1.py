
def flatten(l): return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
lst = [1, [2, 3], 4, [[6, 7]]]
print(flatten(lst))
