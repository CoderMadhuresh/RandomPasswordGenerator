import random
n = int(input("How many passwords do you want - "))
l = int(input("Enter lenth/character of password - "))
if l<5:
    print('Password length must be greater than 5')
elif l>12:
    print('Password length must not be greater than 12')
else:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    symbol = "!@#$%&_-"
    all = lower + upper + num + symbol
    length = l
    password = "".join(random.sample(all,length))
    for i in range(n):
        password = "".join(random.sample(all,length))
        print("Password",i+1,'-',password)
    
    

    
