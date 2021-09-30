# Python Program to find the L.C.M. of two number

def lcm(num1,num2):
    if num1>num2:
       max_num=num1
    else:
       max_num=num2
    while(True):
        if((max_num%num1==0)and(max_num%num2==0)):
           Lcm=max_num
           break
        max_num+= 1
    return(Lcm)

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))

print("The L.C.M. is:",lcm(num1, num2))







# Python Program to find H.C.F of two number

def lcm(num1,num2):
    if num1>num2:
       max_num=num1
    else:
       max_num=num2
    while(True):
        if((max_num%num1==0)and(max_num%num2==0)):
           Lcm=max_num
           break
        max_num+= 1
    return(Lcm)
def hcf(num1,num2):
    l=lcm(num1,num2)
    Hcf=int((num1*num2)/l)
    return Hcf

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))

print("The H.C.F is:",hcf(num1, num2))







# Python Program to find palindrome

num=int(input("Enter the number:"))
a=num
temp=0
while(num!=0):
    rem=int(num%10)
    num=int(num/10)
    temp=int((temp*10)+rem)
if a==temp:
    print("It is a palindrome")
else:
    print("It is not a plaindrome")








# Python Program to find Reverse of a number or string

def rev_number(num):
    temp=0
    while(num!=0):
        rem=int(num%10)
        num=int(num/10)
        temp=int((temp*10)+rem)
    return temp

def rev_str(string):
    a=""
    for i in string:
        a=i+a
    return a

num=int(input("Enter the number:"))
string=input("Enter the string:")
print("Reversed number:",rev_number(num))
print("Reversed String:",rev_str(string))









# Python Program to find Fibonacci Series

num=int(input("Enter the number of terms:"))
t1=0
t2=1
print("Fibonacci Series:",end=" ")
for i in range(1,num+1):
    nextTerm=t1+t2
    t1=t2
    t2=nextTerm
    print(t1,end=" ")











# Python Program to find Prime Number

num=int(input("Enter a number:"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
    if flag:
        print(num,"is not a prime number")
    else:
        print(num,"is prime number")
        

