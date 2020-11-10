from functools import reduce

while True:

    def addition(*args):
        numList = []
        for i in inputList:
            x = int(i)
            numList.append(x)
        numSum = sum(numList)
        return numSum


    def subtraction(*args):
        numList = []
        for i in inputList:
            x = int(i)
            numList.append(x)
        numSub = numList[0] - sum(numList[1:])
        return numSub

    def multiplication(*args):
        numList = []
        for i in inputList:
            x = int(i)
            numList.append(x)
        numMul = reduce(lambda x, y: x*y, numList)
        return numMul

    def division(*args):
        numList = []
        for i in inputList:
            x = int(i)
            numList.append(x)
        numDiv = reduce(lambda x, y: x/y, numList)
        return numDiv

    print('Simple Calculator') 

    print("Please enter your choice\n" +
        "1 -> Addition\n" +
        "2 -> Subtraction\n" +
        "3 -> Multiplication\n" +
        "4 -> Division\n")

    choice = int(input("Please enter your choice: "))
    if 1 <= choice <= 4:
        print("Please enter your values(seperated by spaces): ")
        inputList = input().split()
        

        if choice == 1:
            ansList = addition(inputList)
            print("The sum of your inputs is: ", ansList)
        elif choice == 2:
            ansList = subtraction(inputList)
            print("The difference of you inputs is: ", ansList)
        elif choice == 3:
            ansList = multiplication(inputList)
            print("The product of your inputs is: ", ansList)
        elif choice == 4:
            ansList = division(inputList)
            print("The quotient of your inputs is: ", ansList)
    else:
        not_valid = f"{choice} is not a valid choice\n"
        print(not_valid)
        
    print('if you want to continue press y else n')
    cont_choice=input('Enter youe choice\n y/n:').lower()
    if cont_choice == 'y':
        continue
    elif cont_choice == 'n':
        break
    else:
        print('Invalid ipnut. Closing app...')
        break
    