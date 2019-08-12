print("Accessing list elements and traversing the list");

list1 = ["Nishkarsh Raj Khare","CSE DevOps","UPES",41,20,500060720,9.56];
print(list1);

print("First element: ",list1[0]);
print("Last element:",list1[len(list1)-1]);

print("Traversal using for loop");
for el in list1:
    print(el);
