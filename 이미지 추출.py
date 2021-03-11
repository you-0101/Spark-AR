#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2


# In[13]:


vidcap = cv2.VideoCapture(r'C:\Users\you10\Downloads\archive\a.mp4')
success,image = vidcap.read()


# In[14]:



count = 1
success = True

while success:
    success,image = vidcap.read()
    cv2.imwrite(r"C:\Users\you10\Downloads\archive\test\%d.jpg" % count, image)
    print("saved image %d.jpg" % count)
    cv2.imshow('image', image)
    cv2.waitKey(10)
    if cv2.waitKey(10) == 27:                    
        break
    count += 1


# In[ ]:




