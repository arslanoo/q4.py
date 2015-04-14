
# coding: utf-8

# In[5]:

def partition(L,p):
    greaterp = []
    equalp = []
    lessp = []
    count = 0
    for i in L:
        if i < p:
            lessp.append(i)
        if i > p:
            greaterp.append(i)
        if i == p:
            equalp.append(i)
            count += 1
    return lessp, count, greaterp


# In[8]:

def quick(L):
    p = 0
    sort_list = []
    while p <= max(L):
        Endp = partition (L, p)
        greaterp = Endp[2]
        lessp = Endp[0]
        totalmults = Endp[1]
        while totalmults != 0:
            sort_list.append(p)
            totalmults -= 1
        p += 1
    return sort_list


# In[3]:

partition([14.38, 15.2, 11.18, 1.23, 17.91, 9.05, 1.44, 2.7, 9.28, 16.08, 3.4, 8.76],8.2)


# In[ ]:



