number1=int(input("type first number:  "))
number2=int(input("type second number:  "))
calc=int(input("type 1 to add the nubers and type 2 to multiply the numbers: "))
while calc!=1 and calc!=2:
    print("choose 1 or 2 only pleas")
    calc=int(input("type 1 to add the nubers and type 2 to multiply the numbers: "))
if  calc == 1:
    result = number1 + number2
    number1 + number2
    print( " addetion " , number1 , "+" , number2 , "=" , result)
else:
    result = number1 * number2
    print( " multiplication " , number1 , "*" , number2 , "=" , result)