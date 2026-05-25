mixed_list = [10, "Hello", 3.14, True, "Python"]

print("საწყისი სია:", mixed_list)

item = input("რომელი ელემენტის წაშლა გსურს?: ")

if item == "10":
    item = 10
elif item == "3.14":
    item = 3.14
elif item == "True":
    item = True

if item in mixed_list:
    mixed_list.remove(item)
    print("განახლებული სია:", mixed_list)
else:
    print("Invalid Choice")