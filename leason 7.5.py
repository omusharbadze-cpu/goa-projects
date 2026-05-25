products = ["apples", "bannanas", "orangers"]

while True:
    print("\n[პროდუქტების სია]")
    print("1. პროდუქტის დამატება")
    print("2. პროდუქტის წაშლა")
    print("3. პროდუქტების რაოდენობის გაგება")
    print("4. ყველა პროდუქტის ნახვა")
    print("5. გამოსვლა")

    choice = input("აირჩიე მოქმედება: ")


    if choice == "1":
        product = input("შემოიტანე პროდუქტის სახელი: ")
        products.append(product)
        print(product, "დაემატა სიაში.")

    
    elif choice == "2":
        product = input("შემოიტანე წასაშლელი პროდუქტი: ")

        if product in products:
            products.remove(product)
            print(product, "წაიშალა სიიდან.")
        else:
            print("პროდუქტი ვერ მოიძებნა.")
    
    elif choice == "3":
        print("პროდუქტების რაოდენობა არის:", len(products))

    
    elif choice == "4":
        print("\nპროდუქტები:")

        if len(products) == 0:
            print("სია ცარიელია.")
        else:
            for product in products:
                print("-", product)


    elif choice == "5":
        print("პროგრამა დასრულდა.")
        break

    
    else:
        print("არასწორი არჩევანი.")