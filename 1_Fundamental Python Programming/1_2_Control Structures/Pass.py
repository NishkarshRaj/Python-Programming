print("Pass statement in Python");

for i in range (1,11,1):
    if(i==3):
        i = i + 1;
        pass;
    else:
        print(i);
        i = i + 1;
