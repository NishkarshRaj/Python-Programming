print("Conditional Statements");
print("Dynamic age scale teller");
print("");
age = int(input("Enter your age: "));

#if-elif-else block
if((age>=0) and (age<=13)):
    print("Child");
elif((age>13) and(age<=19)):
    print("Teenager");
elif((age>19) and (age<=30)):
    print("Youngster");
elif((age>30) and (age<=60)):
    print("Grown up");
else:
    print("Senior Citizen");

    
