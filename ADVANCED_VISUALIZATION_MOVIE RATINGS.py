#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


movie=pd.read_csv(r"D:\NIT\27_28NOV\MOVIE RATINGS _ ADVANCE VISUALIZATION _ EDA 1\Movie-Rating.csv")


# In[3]:


movie


# In[4]:


len(movie)


# In[5]:


movie.head()


# In[6]:


movie.tail()


# In[7]:


movie.columns


# In[8]:


type(movie)


# In[9]:


movie.columns=["Film","Genre","CriticRating","AudienceRating",'BudgetMillions','Year']


# In[10]:


movie


# In[11]:


movie.info()


# In[12]:


movie.dtypes


# In[13]:


movie.describe()


# In[14]:


movie['Film']


# In[15]:


movie.Film


# In[16]:


movie.Film=movie.Film.astype('category')


# In[17]:


movie.Genre=movie.Genre.astype('category')


# In[18]:


movie.Year=movie.Year.astype('category')


# In[19]:


movie.info()


# In[20]:


movie.Genre.cat.categories


# In[31]:


movie.Year.cat.categories


# In[32]:


movie.describe()


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[23]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating')


# #### kind : { "scatter" | "kde" | "hist" | "hex" | "reg" | "resid" }
# 

# In[24]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating',kind='kde')


# In[25]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating',kind='hist')


# In[26]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating',kind='hex')


# In[27]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating',kind='resid')


# In[28]:


j=sns.jointplot(data=movie,x='CriticRating',y='AudienceRating',kind='reg')


# In[29]:


d=sns.displot(movie.AudienceRating)


# In[30]:


d1=sns.distplot(movie.AudienceRating)


# In[31]:


sns.set_style('darkgrid')


# #### style : dict, or one of {darkgrid, whitegrid, dark, white, ticks}

# In[32]:


d1=sns.distplot(movie.AudienceRating)


# In[33]:


d=sns.displot(movie.AudienceRating)


# In[34]:


h=plt.hist(movie.AudienceRating)


# In[35]:


sns.set_style('white')


# In[36]:


h=plt.hist(movie.AudienceRating,bins=20)


# In[37]:


h1=plt.hist(movie.CriticRating,bins=20)


# In[38]:


h2=plt.hist(movie.BudgetMillions)


# In[39]:


h3=plt.hist(movie[movie.Genre == 'Drama'].BudgetMillions)


# In[40]:


h3=plt.hist(movie[movie.Genre == 'Action'].BudgetMillions)


# In[41]:


movie.Genre.cat.categories


# In[42]:


h3=plt.hist(movie[movie.Genre == 'Adventure'].BudgetMillions)


# In[43]:


movie.head(4)


# In[44]:


plt.hist(movie[movie.Genre == 'Action'].BudgetMillions, bins = 20)
plt.hist(movie[movie.Genre == 'Thriller'].BudgetMillions, bins = 20)
plt.hist(movie[movie.Genre == 'Drama'].BudgetMillions, bins = 20)

plt.show()


# In[45]:


for gen in movie.Genre.cat.categories:
    print(gen)


# In[46]:


l=sns.lmplot(data=movie,x='CriticRating',y='AudienceRating')


# In[47]:


l=sns.lmplot(data=movie,x='CriticRating',y='AudienceRating',fit_reg=False)


# In[48]:


l=sns.lmplot(data=movie,x='CriticRating',y='AudienceRating',fit_reg=False,hue='Genre')


# In[49]:


l=sns.lmplot(data=movie,x='CriticRating',y='AudienceRating',fit_reg=False,hue='Genre',aspect=1)


# In[50]:


f,sub=plt.subplots(1,2,figsize=(10,6))


# In[51]:


f ,sub1=plt.subplots(2,2)


# In[52]:


sub,q=plt.subplots(1,2,figsize=(10,6))
h=sns.scatterplot(data=movie,x="BudgetMillions",y="AudienceRating",ax=q[0])
h1=sns.kdeplot(data=movie,x="BudgetMillions",y="CriticRating",ax=q[1])
plt.show()



# In[53]:


b= sns.boxplot(data=movie, x='Genre', y = 'CriticRating')


# In[54]:


v = sns.violinplot(data=movie, x='Genre', y = 'CriticRating') 


# In[55]:


b1 = sns.boxplot(data=movie[movie.Genre == 'Drama'], x='Year', y = 'CriticRating')


# In[56]:


b2 = sns.boxplot(data=movie[movie.Year == 2009], x='Genre', y = 'CriticRating')


# In[57]:


b2 = sns.boxplot(data=movie[movie.Year == 2009], x='Genre', y = 'AudienceRating')


# In[63]:


f, axes = plt.subplots(1,2, figsize =(12,6))
k1 = sns.kdeplot(data=movie,x='BudgetMillions',y='AudienceRating',ax=axes[0])
k2 = sns.kdeplot(data=movie,x='BudgetMillions',y='CriticRating',ax = axes[1])


# In[66]:


g=sns.FacetGrid(movie,row='Genre',col='Year')


# In[68]:


plt.scatter(data=movie,x='CriticRating',y="AudienceRating")


# In[81]:


g=sns.FacetGrid(movie,row="Genre",col="Year",hue='Genre')
g=g.map(sns.scatterplot,'CriticRating','AudienceRating')


# In[82]:


g=sns.FacetGrid(movie,row="Genre",col="Year",hue='Genre')
g=g.map(plt.scatter,'CriticRating',"AudienceRating",)


# In[91]:


g=sns.FacetGrid(movie,row='Genre',col='Year',hue = 'Genre')
g=g.map(plt.hist,'BudgetMillions')


# In[89]:


g=sns.FacetGrid(movie,row='Genre',col='Year')
g=g.map(sns.histplot,'BudgetMillions')


# In[ ]:




