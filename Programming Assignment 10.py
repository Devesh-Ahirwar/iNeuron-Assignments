#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find sum of elements in list?
# 2. Write a Python program to Multiply all numbers in the list?
# 3. Write a Python program to find smallest number in a list?
# 4. Write a Python program to find largest number in a list?
# 5. Write a Python program to find second largest number in a list?
# 6. Write a Python program to find N largest elements from a list?
# 7. Write a Python program to print even numbers in a list?
# 8. Write a Python program to print odd numbers in a List?
# 9. Write a Python program to Remove empty List from List?
# 10. Write a Python program to Cloning or Copying a list?
# 11. Write a Python program to Count occurrences of an element in a list?

# In[1]:


l1=[1,12,32,34,56,67,8]
sum=0
for i in l1:
    sum+=i
print(f"Sum of elements in list: {sum}")


# In[2]:


l2=[1,3,8]
mult=1
for i in l2:
    mult*=i
print(f"Multiplication of elements in list: {mult}")


# In[14]:


l3=[8,12,32,-100,-1,67,2]
smallest=l3[0]
for i in (l3):
    if i < smallest:
        smallest=i
print(smallest)


# In[17]:


l3=[8,12,32,-100,-1,67,2]
largest=l3[0]
for i in (l3):
    if i > largest:
        largest=i
print(largest)


# In[18]:


l3=[8,12,32,-100,-1,67,2]
largest=l3[0]
for i in (l3):
    if i > largest:
        second_largest=largest
        largest=i
print(second_largest)


# In[24]:


l3=[8,12,32,-100,-1,67,2,6,64,6,2,465,4654]
l3.sort()
N = 5
print(l3[-N:])


# In[25]:


l4=[8,12,32,-100,-3,7,80,465]
for i in l4:
    if i % 2==0:
        print(i)


# In[27]:


l4=[8,12,32,-100,-3,7,80,465]
for i in l4:
    if i % 2!=0 or i==1:
        print(i)


# In[30]:


l5=[8,[],9,21,[],12,"devesh"]

for i in l5:
    if i == []:
        l5.remove(i)
l5


# In[33]:


l6=[8,12,32,-100,-3,7,80,465]
l7=list()
l7=l6
l7


# In[43]:


l8=[8,12,32,-100,-1,67,2,6,64,6,2,465,4654]
i=6
print(f"Count of {i} in list is {l8.count(i)}")


# In[ ]:




