#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Pythono3 code to rename multiple  
#files in a directory or folder 
  
# importing os module 
import os 

#set the path to the respective directory 
path = os.chdir('C:\Program Files\Change_this_path')

i = 0 #counter
for file in os.listdir(path):
    new_file_name = "provide_initial_filename{}.jpeg".format(i) #change the format if required
    os.rename(file,new_file_name)
    i = i + 1

