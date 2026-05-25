list = []
name = int(input ("შემოიტანე რიცხვი იმდენჯერ რამდენჯერ გინდა: "))
for i in range(1, name  +1):
    list.append(i)
for i in list:
    print(i)
name = len(list)
print(name)