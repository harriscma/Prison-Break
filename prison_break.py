#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[2]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'


# In[4]:


data = data_from_url(url)


# Let's print the first three rows

# In[10]:


for row in data[0:3]:
    print(data)


# ## Modify the Data

# Let's remove the last element of each row

# In[11]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1
print(data[0:3])


# Now let's extract the year.

# In[12]:


for row in data:
    row[0] = fetch_year(row[0])

print(data[0:3])


# ## Create a list of lists

# In[24]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]

years = []
for y in range(min_year, max_year + 1):
    years.append(y)
    
attempts_per_year = []
for x in years:
    attempts_per_year.append([x, 0])


# In[25]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1

print(attempts_per_year)


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# The most attempts was 3 occurring in the years 1986, 2001, 2007, and 2009.

# ## Attempts by country

# In[28]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:
