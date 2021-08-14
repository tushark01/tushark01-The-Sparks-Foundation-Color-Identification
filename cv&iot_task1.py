#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATION
# ## DATA SCIENCE AND BUSINESS ANALYTICS INTERNSHIP (GRIP AUGUST-21)
# 
# 
# 
# Domain: Computer vision & Internet of Things
# 
# ### Title: Color Identification in Images
# ### Task: Implement an image color detector which identifies all the colors in an image or video
# 
# * By: Tushar Khete

# # Importing required libraries ::

# In[4]:


import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd


# # Reading and Plotting the image ::

# In[5]:


img_path = r'balls.jpg'
img = cv2.imread(img_path)
plt.imshow(img)


# ##Declaration of Global Variables 

# In[6]:


clicked = False
r = g = b = x_pos = y_pos = 0


# # Reading the csv file

# In[7]:


index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# # Function to print the color name

# In[8]:


def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# # Function to calculate the x,y cordinates

# In[9]:


def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[10]:


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)


# In[ ]:


while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

