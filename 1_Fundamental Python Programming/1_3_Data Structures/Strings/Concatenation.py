print("String concatenation");
str1 = "Nishkarsh";
str2 = "Raj";
str3 = "Khare";

print("Way 1: Can be used directly in print or using a new variable");
str4 = str1 + " " + str2 + " " + str3;
print(str4);

print("Way 2: Can be used only by print");
#print(str1) + print(" ") + print(str2) + print(" ") + print(str3);
print(str1,end=" ");
print(str2,end=" ");
print(str3);
## Note: Way 2 does not work in Python v2
