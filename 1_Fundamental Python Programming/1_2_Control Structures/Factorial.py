print("Factorial in Python");

inp = int(input("Enter number to get its factorial: "));
p = 1;
fact = inp;

while(inp>0):
    p = p * inp;
    inp = inp-1;

print("Factorial of",fact,"is:",p);
