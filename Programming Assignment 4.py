#!/usr/bin/env python
# coding: utf-8

# # 1

# In[ ]:


num = int(input("Enter the number to find factorial: "))

fact = 1

for i in range(1,num+1):
    fact = fact * i
    
print( fact)


# # 2

# In[11]:


num1 = int(input("Enter number to display multiplication table for the number: "))

for i in range(1,11):
    print(f"{num1} X {i} = {num1*i}")


# # 3

# In[65]:


length = int(input("Enter length of fibonacci series: "))
x=0
y=1
count = 0
while count < length:
    print(x)
    z = x + y
    x = y
    y = z
    count = count + 1


# 

# # 5

# In[182]:


num4 = str(input("Enter the number to check for Armstrong number: "))
z = 0
for i in range(0,len(num4)):
    x = int(num4[i])
    y = x**len(num4)
    z = z + y
if int(num4) % z == 0:
    print(f"{num4} is an Armstrong number")
else:
    print(f"{num4} is not an Armstrong number")


# Write a Python Program to Find Armstrong Number in an Interval?

# In[184]:


lr = int(input("Enter the lower range of interval: "))
ur = int(input("Enter the upper range of interval: "))

for i in range(lr,ur+1):
    if i <=9:
        print(i)
    else:
        m=str(i)
        z=0
        for j in range(len(m)):
            f = int(m[j])**len(m)
            z=z+f    
        if z == i:
            print(z)            


# # 6

# In[190]:


num = -89

if num < 0:
    print("Enter a positive number")
elif num==0:
    print("Zero is not a natural number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)


# In[ ]:




