#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data =pd.read_csv('DOB - Sheet1.csv')


# In[2]:


data


# In[30]:


name_len = []

for i in range(len(data)):
    
    name_len.append(len(data['fname'][i] + data['lname'][i]))
    
print(name_len)


# In[31]:


dup_ind = {}
for a in s:
    d = []
    for i in range(len(name_len)):
        if name_len[i] == a:
            d.append(i)
        dup_ind[a] = d
print(dup_ind)


# In[32]:


dob = data['dob'].tolist()


# In[21]:


from datetime import datetime
dob.sort(key = lambda date: datetime.strptime(date, '%d-%b-%Y'))


# In[22]:


dob_pref = []
for i in data['dob'].tolist():
    dob_pref.append(dob.index(i))
print(dob_pref)


# In[27]:


for i in list(set(names_len)):
    if len(dup_ind[i]) > 1:
        h = []
        for j in dup_ind[i]:
            h.append(dob_pref[j])
        for i in sorted(h):
            print(data['fname'][dob_pref.index(i)] + " "+data['lname'][dob_pref.index(i)])
    else:
        print(data['fname'][name_len.index(i)]+" "+data['lname'][name_len.index(i)])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




