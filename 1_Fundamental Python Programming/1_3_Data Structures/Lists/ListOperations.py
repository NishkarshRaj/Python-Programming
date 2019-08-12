print("List operations");
list1 = [1,2,3,4,5,6,7,8,9,10];
print(list1);
print("");
print("");

print("1) Replace kth element: ");
list1[3] = 41; # replacing 3rd element: 4 with 41
print(list1);
print("");
print("");

print("2) Insertion at any point");
list1.insert(3,4); #Insert at 3rd index and move previous 3rd index and rest 1 index right
print(list1);
print("");
print("");

print("3) Remove an element by its value rather than index");
print("listname.remove(value)");
list1.remove(41);
print(list1);
print("");
print("");

print("4) Append vales");
list1.append("Appended text");
print(list1);
#or list1.insert(len(list1)-1)
