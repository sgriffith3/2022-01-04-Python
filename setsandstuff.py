nums = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6]
more_nums = [1, 1, 2, 2, 3, 3, 9, 9, 9]
all_nums = [nums, more_nums]


uniq = set(nums)
print(uniq)

uniq2 = set(more_nums)
print(uniq2)

# Same
print(uniq.intersection(uniq2))

# Different
print(uniq.difference(uniq2))

print(uniq.union(uniq2))

# phrase = "My cat had a lollipop"
# print(set(phrase))

# {'M', 'd', 'y', ' ', 'h', 'p', 'c', 'l', 'o', 'i', 't', 'a'}
# {'c', 'h', 'o', 'p', 'd', 'i', 'a', 't', 'l', ' ', 'y', 'M'}
#
# if 5 in uniq:
#     print("Yep!")
# else:
#     print("Nope")
#
