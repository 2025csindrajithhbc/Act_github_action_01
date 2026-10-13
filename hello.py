# for i in range(1,11):
#     print("2 x ",i," = ",2*i) 

print("1.add 2.sub 3.mult 4.division 5.exit")
option = int(input("Enter your choice:"))
while option != 5: 
    print("1.add 2.sub 3.mult 4.division 5.exit")
    option = int(input("Enter your choice:"))
    a = float(input("Enter the 1st number :"))
    b = float(input("Enter the 2st number :"))
    
    if(option == 1):
        print(a + b," sum of two number")
    elif option == 2:
        print(a - b," substraction of two number")
    elif option == 3:
        print(a * b," Multplaction of two number")
    elif option == 2:
        print(a / b," Division of two number")
    else:
        break
    

