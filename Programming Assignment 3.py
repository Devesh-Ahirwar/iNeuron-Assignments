#!/usr/bin/env python
# coding: utf-8

# # 1

# In[4]:


num = int(input("Enter the number"))

if num >= 0:
    if num == 0:
        print(f"{num} is Zero")
    else:
        print(f"{num} is positive")
else:
    print(f"{num} is negative")


# # 2

# In[9]:


num1 = int(input("Enter the number: "))

if num1 % 2 == 0 or num1 == 0:
    print(f"{num1} is a even number")
else:
    print(f"{num1} is a odd number")


# # 3

# In[10]:


year = int(input(" Enter the year: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    if year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


# # 4

# In[6]:


num = int(input("Enter the number: "))


if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# # 5 

# In[43]:


lrange = 1
urange = 10000

print("Prime numbers between", lrange, "and", urange, "are:")

for num in range(lrange, urange + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




