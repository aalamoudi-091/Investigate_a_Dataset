#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Before submitting your project, it will be a good idea to go back through your report and remove these sections to make the presentation of your work as tidy as possible. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset (Replace this with something more specific!)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > **Tip**: In this section of the report, provide a brief introduction to the dataset you've selected for analysis. At the end of this section, describe the questions that you plan on exploring over the course of the report. Try to build your report around the analysis of at least one dependent variable and three independent variables. If you're not sure what questions to ask, then make sure you familiarize yourself with the dataset, its variables and the dataset context for ideas of what to explore.
# 
# > If you haven't yet selected and downloaded your data, make sure you do that first before coming back here. In order to work with the data in this workspace, you also need to upload it to the workspace. To do so, click on the jupyter icon in the upper left to be taken back to the workspace directory. There should be an 'Upload' button in the upper right that will let you add your data file(s) to the workspace. You can then click on the .ipynb file name to come back here.

# In[84]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
m=pd.read_csv('tmdb-movies.csv')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.
# 
# ### General Properties

# In[85]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
m.head()


# In[86]:


mo.shape


# 10866 Movies and 21 columns

# In[87]:


m.isnull().sum()


# We check to see if there's empty data in one of the columns.
# so we have some miss data

# In[88]:


m.duplicated().sum() 


# We check to see if there's empty data in one of the columns.
# so we have one duplicate

# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.
# 
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
# 
# ### Data Cleaning (Replace this with more specific notes!)

# In[89]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
m.dropna(inplace=True) # If there is any missing data, the row will be deleted and True mean save resulte 


# In[90]:


m.isnull().sum() #Make sure there is missing data


# In[91]:


m.duplicated().sum() # no duplicate


# In[92]:


m.drop(['imdb_id', 'homepage', 'keywords', 'keywords' ,'overview' ,'tagline' , 'release_date' ,'release_year','runtime' , 'vote_count','popularity'],axis=1, inplace=True)
m.head()


# Now let's delete the columns I don't need in my data analysis

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.
# 
# ### Research Question 1 (Replace this header name!)

# In[93]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.


# - What are the top 5 movies By vote average? ,                                                                                  - What are the top 5 movies By revenue ?,                                                                                       - What is the rating of the top 5 movies and what genres of movie By vote average ?,
# - What is the rating of the top 5 movies and what genres of movie By vote revenue ?
# - what the Top Five Directors's moves  By vote average?
# - How much is the highest profit in movies which is average and what is the lowest for 100 movies by revenue ?"
# - Compare  the budget of the top 5 movies By revenue and their revenues?
# 

# ## What are the top 5 movies By vote average?

# In[94]:


top_five_movies_by_vote=m.nlargest(5,['vote_average']) # best 5 by vote_average
top_five_movies_by_vote


# In[95]:


top_five_movies_by_vote.groupby('original_title')['vote_average'].value_counts().plot(kind='pie' , title=" top 5 moves by vote_average");


# We can note that the best film is "The Godfather	" and vote 8.3  in second place "Whiplash" and  vote 8.2also note that it's the top 5 very close movies in the ratings

# ## What are the top 5 movies By revenue ?

# In[96]:


top_five_movies_by_revenue=m.nlargest(5,['revenue']) # best 5 by Top 5 Movies revenue
top_five_movies_by_revenue


# In[97]:


top_five_movies_by_revenue.plot(kind='bar',x='original_title',y='revenue', title="Top 5  Movies Revenue")
plt.xlabel(' Names' , fontsize=18)
plt.ylabel('vote_average' , fontsize=18);


# "Avatar" comes in first place in terms of revenue and has reached 2781505847 , And comes in second place " Star Wars: The Force Awakens	" and has reached the revenues of 2068178225, the place "Titanic" and has reached the revenues of 1845034188, Fourth "لإhe Avengers" and has reached the revenues of 1519557910 and fifth "Jurassic World"  and has reached the revenues of 1513528810	 

# ### An important note we can see clearly that not a condition of the best 5 movies in terms of rating is the same as the highest profit returns, there are other things affecting profits such as movie commercials

# ## What is the rating of the top 5 movies and what genres of movie By vote average ?

# In[98]:


top_five_movies_by_vote().head(1)


# In[99]:


top_five_movies_by_vote.groupby('genres')['vote_average'].value_counts().plot(kind='pie' , title="Top 5 genres vote average ", autopct='%1.1f%%',  shadow=True, startangle=0);


# Dramatic movies come in first place with 80% (4 films from 5 movies) and also the highest rating at 8.3, and in second place crime movies with 40% (two films of 5 films) and also comes in second in terms of rating with 8.2

# ## What is the rating of the top 5 movies and what genres of movie By vote revenue ?
# 

# In[100]:


top_five_movies_by_revenue.groupby('genres')['vote_average'].value_counts().plot(kind='pie' , title="Top 5 genres vote average ", autopct='%1.1f%%',  shadow=True, startangle=0);


# Shares 3 genres in first place , action movies come in first place with 80% (4 movies from 5 movies)  also the highest rating at 7,5 and comes in first place frequently Science Fiction movies with 80% ((4 movies from 5 movies)  also the  same highest rating at 7,5, and comes in first place Adventure movies with 80% ((4 movies from 5 movies)  also the  same highest   and also the  same highest rating at 7,5 (( And here, through the proceeds of the profits, we can say that people prefer action movies, Science Fiction , Adventure))

# ### An important note. Here also our previous observation is not a condition of the best 5 types of movies in terms of rating is itself the highest movies in terms of revenue, 

# ## what the Top Five Directors's moves  By vote average?

# In[102]:


top_five_movies_by_vote.plot(kind='bar',x='director',y='vote_average' , title="Top 5 director By vote average ")
plt.xlabel('director' , fontsize=18)
plt.ylabel('revenue' , fontsize=18);


# The top 5 film directors in terms of ratings can note that "Francis Ford Coppola" takes first place and comes in second place "Damien Chazelle" and third "Richard Press"and fourth "David Fincher" and  fifth "Christopher Nolan" we can also note the difference between them very simple

# In[60]:


top_100_movies_by_revenue=m.nlargest(100,['revenue']) # best 100 by revenue
top_100_movies_by_revenue


# ## How much is the highest profit in movies which is average and what is the lowest for 100 movies by revenue ?"

# In[104]:


data = top_100_movies_by_revenue['revenue']
result = plt.hist(data, bins=20, color='c', edgecolor='k', alpha=0.65) 
plt.axvline(data.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(data.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(data.mean()))


# We can see here the highest movie revenue of more than 2.5 percent, with an average of 0.7, and the lowest return of about 0.6.

# In[ ]:





# ## Compare  the budget of the top 5 movies By revenue and their revenues?

# In[109]:


pos = list(range(len(top_five_movies_by_revenue['revenue']))) 
width = 0.25 
fig, ax = plt.subplots(figsize=(10,5))
plt.bar(pos, top_five_movies_by_vote['revenue'] ,
        width , 
        alpha=0.5, color='#EE3224', 
        label=top_five_movies_by_vote['original_title'])
plt.bar([p + width for p in pos],
        top_five_movies_by_vote['budget'],
        width, 
        alpha=0.5, 
        color='#F78F1E', 
        label=top_five_movies_by_vote['original_title']) 

ax.set_ylabel('revenue and budget')

ax.set_title('compare between revenue and budget')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(top_five_movies_by_revenue['original_title'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(top_five_movies_by_vote['revenue'] + top_five_movies_by_vote['budget'] )] )
plt.legend(['revenue', 'budget'], loc='upper left')
plt.grid()
plt.show()



        


# In[ ]:





# ## Conclusions

# ###   we can see clearly that not a condition of the best 5 movies in terms of rating is the same as the highest profit returns, there are other things affecting profits such as movie commercials
# 
# ### our previous observation is not a condition of the best 5 types of movies in terms of rating is itself the highest movies in terms of revenue, 
# 
# ### We can see here the highest movie revenue of more than 2.5 percent, with an average of 0.7, and the lowest return of about 0.6. and mean 871353659.84 

# ### my refrance

# https://chrisalbon.com/python/data_visualization/matplotlib_grouped_bar_plot/

# <a id='conclusions'></a>
# ## Conclusions
# 
# > **Tip**: Finally, summarize your findings and the results that have been performed. Make sure that you are clear with regards to the limitations of your exploration. If you haven't done any statistical tests, do not imply any statistical conclusions. And make sure you avoid implying causation from correlation!
# 
# > **Tip**: Once you are satisfied with your work here, check over your report to make sure that it is satisfies all the areas of the rubric (found on the project submission page at the end of the lesson). You should also probably remove all of the "Tips" like this one so that the presentation is as polished as possible.
# 
# ## Submitting your Project 
# 
# > Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[ ]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

