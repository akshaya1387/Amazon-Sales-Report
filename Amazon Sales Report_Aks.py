#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install seaborn')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[12]:


df=pd.read_csv(r'C:\Users\aksha\OneDrive\Documents\Python_Amazon_Sales_Analysis-main\Amazon Sale Report.csv',encoding= 'unicode_escape')


# In[13]:


df.shape


# In[15]:


df.head(10)


# In[16]:


df.tail()


# In[21]:


df.info()


# In[20]:


#drop unrealted/blank column
df.drop(['New','PendingS'], axis=1, inplace=True)


# In[22]:


#checking null value
pd.isnull(df)


# In[23]:


#sum will give total of null values
pd.isnull(df).sum()


# In[24]:


#to know no. of rows and column
df.shape


# In[25]:


#drop null values
df.dropna(inplace=True)


# In[26]:


df.shape


# In[27]:


#to know the names of columns
df.columns


# In[28]:


#change the data type
df['ship-postal-code']=df['ship-postal-code'].astype(int)


# In[29]:


#checking whether data type change or not
df['ship-postal-code'].dtype


# In[42]:


df['Date']=pd.to_datetime(df['Date'])


# In[43]:


df.info()


# In[44]:


#rename columns
df.rename(columns={'Qty':'Quantity'})


# In[45]:


#describe()method return description of the data in the DataFrame(i.e. count,mean,std,min..etc)
df.describe()


# In[46]:


df.describe(include= 'object')


# In[48]:


#use describe() for specific columns
df[['Qty','Amount']].describe()


# In[49]:


#Exploratory Data Analysis
df.columns


# In[50]:


#size
ax=sns.countplot(x='Size' ,data=df)


# In[51]:


ax=sns.countplot(x='Size' ,data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[54]:


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y='Qty', data=S_Qty)


# # from above graph, most of people buy M-size

# In[56]:


#courier status
plt.figure(figsize=(10,5))
ax=sns.countplot(data=df,x='Courier Status', hue='Status')
plt.show()


# In[57]:


#histogram
df['Size'].hist()


# In[65]:


df['Category']=df['Category'].astype(str)
column_data=df['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data,bins=20,edgecolor='Orange')
plt.xticks(rotation=45)
plt.show()


# In[66]:


#checking B2B data using pie Chart
B2B_check=df['B2B'].value_counts()

#plot the pie chart
plt.pie(B2B_check,labels=B2B_check, autopct='%1.1f%%')

#plt.axis('equal')
plt.show()


# In[69]:


#checking B2B data using pie Chart
B2B_check=df['B2B'].value_counts()
#plot the pie chart
plt.pie(B2B_check,labels=B2B_check.index, autopct='%1.1f%%')

#plt.axis('equal')
plt.show()


# In[ ]:


#from above we can see that max i.e 99.2% of buyers are retailers and 0.8% are B2B buyers


# In[74]:


a1= df['Fulfilment'].value_counts()

#plot the pie chart
fig, ax = plt.subplots()
ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect="equal")

plt.show()


# In[ ]:


#from above pie chart, we can see all the orders are fulfilled by Merchant


# In[76]:


#Prepare Data for Scatter plot for Category
x_data = df['Category']
y_data = df['Size']

#plot Scatter plot
plt.scatter(x_data,y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.show()


# In[ ]:


#from above Scatter Plot, we can see Tshirt & shirts are available in all sizes except free size.


# In[77]:


#plot the count of cities by state
plt.figure(figsize=(12,6))
sns.countplot(data=df, x= 'ship-state')
plt.xlabel('ship-state')
plt.ylabel('Count')
plt.title('Distribution of States')
plt.xticks(rotation=90)
plt.show()


# In[80]:


#top 10 States
top_10_states=df['ship-state'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.countplot(data=df[df['ship-state'].isin(top_10_states.index)], x= 'ship-state')
plt.xlabel('ship-state')
plt.ylabel('Count')
plt.title('Distribution of States')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#from above Graph we can see that most of the buyers are from Maharashtra State

Conclusion:
    
    The Data Analysis reveals that business has significant buyers from Maharashtra state and mainly served by retailers.  
    All oders are fulfilled through merchant(amazon) for M-Size Tshirts as buyer has high demand for M-Size tshirts.

