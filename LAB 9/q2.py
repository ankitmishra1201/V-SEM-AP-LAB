def calculator():
    print("\n")

    try:
        num1=float(input("Enter the first number"))
        num2=float(input("Enter the second number"))

    except ValueError as err:
        print("Invalid Input\n")
        print(err)
        return
    

    
    opp=input("Enter the operator (+ or - or * or /) ")
    if(opp=="+"):
        ans=num1+num2
    elif(opp=="-"):
        ans=num1-num2
    elif(opp=="*"):
        ans=num1*num2
    elif(opp=="/"):
        try:
            ans=num1/num2
        except ZeroDivisionError as err:
            print("Invalid equation")
            print(err)
            return
    else:
        ans="Invalid Operation"

    print(ans)


calculator()