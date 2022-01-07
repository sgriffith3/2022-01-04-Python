# def thing_printer(first, middle=None, last="Smith"):
#     print(f"You entered the thing: {first}")
#     if not middle:
#         print(f"And their middle name is: {middle}")
#     if middle is not None:
#         print(f"And their middle name is: {middle}".upper())
#     print(f"Their last name is: {last}")
#
#
# thing_printer("Steve", "Eustace", last="Jones")
# thing_printer("Becky", "")

# # def func(psa1, psa2, *args, kw=val, **kwargs):
# def mathy(multiplier, *nums, pwr=2, **operation):
#     print(f"multiplier = {multiplier}")
#     print(f"*nums = {nums}")
#     print(f"pwr = {pwr}")
#     print(f"**operation = {operation}")
#     mutated = []
#     for num in nums:
#         new_num = num**pwr
#         mutated.append(new_num)
#     print(mutated)
#     return sum(mutated) * multiplier
#
#
# print(mathy(10, 3, 5, 6, 7, 8, 22, 99, 395, pwr=5, plus="+", minus="-", exponent="**"))
# #            |  \                         /    /
# #            |    -----\    /-------------    /
# #            |           \ /       -----------
# #            |            |       |
# # def mathy(multiplier, *nums, pwr=2, **operation):

# type hinting
def reverse_sentence(phrase: str = "moo") -> list:
    print(phrase)
    return list(phrase[::-1])


rev = input("what phrase do you want reversed? ")
print(reverse_sentence(rev))
