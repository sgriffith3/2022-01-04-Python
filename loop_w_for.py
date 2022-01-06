
# for <iterator> in <iterable>:
#    do something

nums = [60, 70, 80, 90, 100]
for num in nums:
    print(num)
    if num < 70:
        print("D")
        break
    if num == 80:
        print("Way to go!")
        continue
    print("not 80")

print("done")

# [0, 1, 2, 3]
print(type(range(4)))
for n in range(4):
    print(n)