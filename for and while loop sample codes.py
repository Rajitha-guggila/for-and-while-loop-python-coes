#!/usr/bin/env python
# coding: utf-8

# In[11]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[3]:


i = 1
while i < 6:
  print(i)
  if i==5: 
    break
  i += 1


# In[6]:


i = 0
while i < 6:
  i += 1
  if i == 2:
    continue
  print(i)


# In[10]:


i = 1
while i < 8:
  print(i)
  i += 1
else:
  print("i is no longer less than 8")


# In[12]:


fruits=["apple","banana","cherry","grapes"]
for x in fruits:
    print(x)


# In[24]:


fruits=["apple","banana","cherry","grapes"]
for x in fruits:
 print(x)
 if x=="banana":
    break
    
   


# In[22]:


for x in "banana":
  print(x)


# In[26]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# In[32]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
else:
  print("finished")


# In[45]:


for x in range(5,10,2):
   print(x)
else:
    print("finished")
 


# In[46]:


for x in [0, 1, 2]:
 pass


# In[48]:


# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 10]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)


# In[50]:


for i in range(10):
    print(i)


# In[51]:


print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))


# In[ ]:




