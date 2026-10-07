
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 5, 6, 7, 8]
merge = lis1 + lis2
uniq = list(dict.fromkeys(merge))
print("merged list:", merge)
print("unique list:", uniq)
