#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt
from math import *


# In[8]:


import math
def jaccard(upref, user1, user2):        #Implementing Jaccard similarity Function
    try:
        m1 = upref[user1]       #inserting user1 data as list in m1
        m2 = upref[user2]       #inserting user2 data as list in m2
        a1 = set(m1)            #coverting user1 list into a set
        a2 = set(m2)            #coverting user2 list into a set
    
        b1 = len(a1.intersection(a2))          #using set function intersection
        b2 = len(a1.union(a2))                 #using set function union
        return b1/b2
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass


# In[3]:


from math import sqrt
from math import *
def euclidean_distnce(upref,user1, user2):  #Implementing Euclidean similarity Function
    try:
        common_item = {}                   #creating empty dictionary
        #common books in user1 and user2
        for item in upref[user1]:           #checking common items in list of two users data
            if item in upref[user2]:
                common_item[item] = True

        #if no item is common
        if len(common_item) == 0: return 0

        #calculate Euclidean distance
        distance = sum([math.pow(upref[user1][itm] - upref[user2][itm], 2) for itm in common_item.keys()])
        distance = math.sqrt(distance)
        return 1/(distance + 1)
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass


# In[4]:


from math import sqrt
from math import *

def cosine_similarity(upref,user1, user2):   #Implementing Cosine similarity Function
    try:
        m1 = [eval(i) for i in upref[user1]]   #Evaluating items in users list
        m2 = [eval(i) for i in upref[user2]]   #Evaluating items in users list
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(m2)):
            x = m1[i]; y = m2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass


# In[5]:


def pearson_correlation(upref,user1, user2):  #Implementing Pearson similarity Function
    try:
        si = {}                              #creating empty dictionary
        for item in upref[user1]:             #checking common items in list of two users data
            if item in upref[user2]:
                si[item] = 1

        n = len(si)
        if n == 0:
            return 0
        sum1 = sum([upref[user1][it] for it in si])            #calculating sum
        sum2 = sum([upref[user2][it] for it in si])

        sumSq1 = sum([pow(upref[user1][it], 2) for it in si])   #calculating sum of squares
        sumSq2 = sum([pow(upref[user2][it], 2) for it in si])
        
        sumPr = sum([upref[user1][it] * upref[user2][it] for it in si])   #calculate sum of products

        num = sumPr - (sum1*sum2/n)
        den = math.sqrt((sumSq1-pow(sum1, 2)/n)*(sumSq2 - pow(sum2, 2)/n))   #calculate person score
        if(den == 0):
            return 0
        r = num/den
        return r
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass


# In[6]:


def manhattan_distance(upref, user1, user2): #Implementing Manhattan similarity Function
    try:
        m=0
        for x in upref[user1]:               #checking common items in list of two users data
            if x in upref[user2]:
                a = upref[user1][x][0]
                b = upref[user2][x][0]
                a = int(a.replace('"',''))
                b = int(a.replace('"',''))
                m = m+abs(a-b)
        return m
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass


# In[7]:


def jaccardbooks(upref, book1, book2):        #Implementing Jaccard similarity Function for books similarity
    try:
        m1 = upref[book1]                     #inserting user1 data as list in m1
        m2 = upref[book2]
        a1 = set(m1)                        #coverting user1 list into a set
        a2 = set(m2)
    
        b1 = len(a1.intersection(a2))       #using set function intersection
        b2 = len(a1.union(a2))              #using set function union
        return b1/b2
    except KeyError as ke:
        print('Key Not Found in Books Dictionary:', ke)
        pass
    except FileNotFoundError:
        print('File not found!')
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except TypeError as te:
        print("The argument should be a number:", te)
    except ValueError as ve:
        print("You entered which is not a correct value.", str(e))
    except IndexError:
        print("Sorry, the list index is out of range")
        pass

