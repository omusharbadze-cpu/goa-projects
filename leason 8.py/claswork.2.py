name = int(input ("შემოიტანე რიცხვი: "))
name2 = int(input ("შემოიტანე რიცხვი: "))
list = []
for i in range(1, name  +1):
    i = i * name2
    list.append(i)
print(list)