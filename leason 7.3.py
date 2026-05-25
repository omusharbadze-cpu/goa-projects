even_numbers = [2, 4, 6, 8, 10,]
odd_numbers = [3, 5 ,7 ,9, 11]

for i in range(10):
    num = int(input("შემოიტანე რიცხვი: "))

    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("ლუწი რიცხვები:", even_numbers)
print("კენტი რიცხვები:", odd_numbers)

