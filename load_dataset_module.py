#!/usr/bin/env python
# coding: utf-8

# In[4]:


def load_dataset_module():
    try:
        ratings={}           #Empty Dictionary 1
        booksd = {}         #Empty Dictionary 1
        user_preference = {}   #Empty Dictionary 1
        with open("Book-Ratings.csv") as f:     #open Book-Ratings.csv file
            lines = f.readlines()
            lst = [list(line.strip().split(';')) for line in lines]   #creating List of all data and using delimiter/split
            lst.pop(0)                                             #Removing header of csv table data
        ratings = dict((item[0], item[1:]) for item in lst)        #creating nested dictionary for book-ratings data
        with open("Books.csv") as books:          #open Books.csv file
            lines = books.readlines()
            lst1 = [list(line.strip().split(';')) for line in lines]      #creating List of all data and using delimiter/split
            lst1.pop(0)
        booksd = dict((item[0], item[1:5]) for item in lst1)       #creating nested dictionary for book data
        keys1 = list(ratings.keys())
        vals1 = list(ratings.values())
        vals2 = list(booksd.values())
        for idx in range(len(keys1)):
            user_preference[keys1[idx]] = vals1[idx]+vals2[idx]    #creating nested dictionary by merging book-ratings,book data
        return user_preference
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
    finally:
        print("Book Ratings Data Loaded!")
load_dataset_module()

