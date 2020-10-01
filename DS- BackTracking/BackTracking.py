def pm(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in pm(1, s)
                 for x in pm(list - 1, s)
                 ]

print(pm(1, ["a","b","c"]))
print(pm(2, ["a","b","c"]))
