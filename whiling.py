# while <expression>:
#     do work
import time

count = 0
while True:
    # if count == 5:
    #     break

    print(count)
    count = count + 1
    if count == 2 or count == 4:
        continue
    # count += 1
    time.sleep(1)


print("All done!")



#
# msg = "You scored a: "
# score = 99
# if score >= 90:
#     msg += "A!"
#     # msg = msg + "A!"
