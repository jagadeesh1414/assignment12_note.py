l = [("x", 2), ("x", 4), ("x", 6), ("y", 6), ("y", 3), ("z", 12)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)