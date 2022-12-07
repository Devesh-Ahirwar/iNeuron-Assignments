#!/usr/bin/env python
# coding: utf-8

# # 1.	Write a Python program to print "Hello Python"?
# 
# 

# In[1]:


print(f"Hello Python")


# # 2.	Write a Python program to do arithmetical operations addition and division.?
# 

# In[3]:


A=10
B=15

Addition = A + B

Division = A / B

print(f"""Addition of number {A} and {B} is: {Addition}
Division of number {A} and {B} is {Division}""")


# # 3.	Write a Python program to find the area of a triangle?
# 

# In[4]:


b=10
h=20

area_of_triangle= 0.5 * b * h

print(f"Area of triangle is {area_of_triangle}")


# # 4.	Write a Python program to swap two variables?
# 

# In[5]:


a=5
b=6
print(f"Number before swapping is a= {a} and b= {b}")
print("...............")
a,b = b,a
print(f"Number after swapping is a= {a} and b= {b}")


# # 5.	Write a Python program to generate a random number?

# In[25]:


from random import randint as rand
print(rand(0,1000))

