str1 = "Nishkarsh Raj Khare";
print("Printing a String using Indexes");

print("Printin a string from start to end");
print("");
for i in range (0,len(str1)):
    print(str1[i]);

print("Printing a string from end to start");
print("");
for i in range (-1,-(len(str1)+1),-1):
    print(str1[i]);
