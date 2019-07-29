print("Printing Output in Python using Format Specifiers");
print("Syntax: (message with format specifiers)%(tuple of variables)");

str = "Nishkarsh Raj Khare";
roll = 41;
cgpa = 9.56;

print(("My name is %s and my roll number is %d and my CGPA is %0.2f.")%(str,roll,cgpa));
print("f has by default 6 decimals of precision and can be only altered by using 0.(digit 0-9)f");
print("Sending less than required arguments lead to error exception and program exits");

#print(("My name is %s and my roll number is %d and my CGPA is %0.2f.")%()); # printing without specifying variables
print(("My name is %s and my roll number is %d and my CGPA is %f.")%(str,roll,cgpa)); # Default float value
print(("My name is %s and my roll number is %d and my CGPA is %9.2f.")%(str,roll,cgpa)); #9.2f
print(("My name is %s and my roll number is %d and my CGPA is %2f.")%(str,roll,cgpa)); # 2f
print(("My name is %s and my roll number is %d and my CGPA is 2%f.")%(str,roll,cgpa)); #2%f
print(("My name is %s and my roll number is %d and my CGPA is 2%0.2f.")%(str,roll,cgpa)); #2%0.2f
