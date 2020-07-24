#!/usr/bin/env python
# coding: utf-8

# In[9]:


cc=[34,67,54,84,23,19]
cc.sort()
for i in range(len(cc)):
    print(cc[i])


# In[14]:


from statistics import mean    # this a one method to do so, 
cc=[34,67,54,84,23,19]
cc.sort()
trimmedvalue=int(0.1*len(cc))    #this was taking 10% of the actual crowd.
cc=cc[trimmedvalue:]             #upper 10% trimming.
cc=cc[:len(cc)-trimmedvalue]     #lower 10% trimming.
print(mean(cc))                  #printing the mean of the trimmed list of crowd.


# In[21]:


# this a second method to do so using SCIPY library
from scipy import stats
cc=[34,67,54,84,23,19]
cc.sort()
m=stats.trim_mean(cc,0.1)
print(m)


# In[2]:


import matplotlib.pyplot as plt
plt.plot([2,6,4,5])   # remember python automatically generates x values if we don't pass any.


# In[3]:


import matplotlib.pyplot as plt
plt.plot([2,3,4,5],[3,1,7,2])      #now this will be treated as (x,y) co-ordinates.
plt.ylabel("this is y coordinate") #this will label the y coordinate
plt.xlabel("this is x coordinate") 


# In[4]:


# plotting in form of dots
import matplotlib.pyplot as plt   
plt.plot([2,3,4,5],[3,1,7,2],'ro')


# In[5]:


#plotting in form of ----
import matplotlib.pyplot as plt
plt.plot([2,3,4,5],[3,1,7,2],'r--')


# In[6]:


#plotting in form of blue squares
import matplotlib.pyplot as plt
plt.plot([2,3,4,5],[3,1,7,2],'bs')


# In[7]:


#plotting in form of green traingles
import matplotlib.pyplot as plt
plt.plot([2,3,4,5],[3,1,7,2],'g^')


# In[8]:


#ploting the crowd data list.
import matplotlib.pyplot as plt
cc=[34,67,54,23,3,56,88]
plt.plot(cc)


# In[9]:


# now let us represent data on a constant y =5 with mean and median
import statistics
import matplotlib.pyplot as plt
cc=[34,67,54,23,3,56,88]
y=[]                                    # created an array
cc.sort()
trimmedvalue=int(0.1*(len(cc)))   # trimming 10% to get closer results.
cc=cc[trimmedvalue:]
cc=cc[:len(cc)-trimmedvalue]
for i in range(len(cc)):
    y.append(5)             # append any constant value. this will just get the data in x scale and represented as a line.
plt.plot(cc,y)
plt.plot([statistics.mean(cc)],[5],'ro')        # hence we import statistics(to get mean and median)library to do this.
plt.plot([statistics.median(cc)],[5],'bs')
plt.plot([49], [5], 'g^')

# what is shown here is that we had a list of data(collected from crowd of any entity) the actual answer was 49. but the people
# guessed it and we obtained a list of those data, now this is ploting of the same data i.e, the mean value is so close to 
# to the actual answer, this is crowd computing.


# In[ ]:




