#!/usr/bin/env python
# coding: utf-8

# In[2]:


import load_dataset_module as ld           #importing load_dataset_module.py file
import similarity_module as sm             #importing similarity_module.py file
import warnings
warnings.filterwarnings('ignore')
import sys as sys

def main():
    try:
        user_pref = ld.load_dataset_module()         #calling load_dataset_module function
        uorb= input("Enter userID as 'U' or Books ISBN as 'B' : ")   #Option menu for user to enter userID or books ISBN
        if uorb.lower() == "u":
            u1 = input("Enter first UserID : ")                #User ID 1 input by user
            u2 = input("Enter second UserID : ")               #User ID 2 input by user
        elif uorb.lower() == "b":
            b1 = input("Enter first Book ISBN : ")             #book ISBN 1 input by user
            b2 = input("Enter Second Book ISBN : ")            #book ISBN 2 input by user
        elif uorb == " " or "0":
            quit()                                             #quit function if user enters no value or number zero
        print("Functions : \n1)For Jaccard function type 1\n2)For Euclidean function type 2\n3)For Cosine function type 3\n4)For Pearson function type 4\n5)For Manhattan function type 5\n6)For Books similarity type 6\n Or Type 0 to Exit")
        simscore = input("Enter the function to determine Similarity score : ")   #User enters similarity from above menu
        while True:
            answer = input('Do you want to continue? (y/n):')   
            if answer.lower().startswith("y"):              #exit function if user enters "n" else continues if user enter "y"
                print("ok, continue then")
                if simscore.lower() == "1":             #executing Jaccard function if user enters number 1
                    x = sm.jaccard(user_pref,u1, u2)
                    print("Similarity score of the entered UserID's using Jaccards Function is" , x)
                elif simscore.lower() == "2":          #executing Euclidean function if user enters number 2
                    x = sm.euclidean_distnce(user_pref,u1, u2)
                    print("Similarity score of the entered UserID's using Euclideans Function is" , x)
                elif simscore.lower() == "3":          #executing Cosine function if user enters number 3
                    x = sm.cosine_similarity(user_pref,u1, u2)
                    print("Similarity score of the entered UserID's using Cosine Function is" , x)
                elif simscore.lower() == "4":          #executing Pearson function if user enters number 4
                    x = sm.pearson_correlation(user_pref,u1, u2)
                    print("Similarity score of the entered UserID's using Pearson Function is" , x)
                elif simscore.lower() == "5":          #executing Manhattan function if user enters number 5
                    x = sm.manhattan_distance(user_pref,u1, u2)
                    print("Similarity score of the entered UserID's using Manhattan Function is" , x)
                elif simscore.lower() == "6":          #executing Jaccard function if user enters number 6 for books similarity
                    x = sm.jaccardbooks(user_pref,b1, b2)
                    print("Similarity score of the entered UserID's using Manhattan Function is" , x)
                elif simscore.lower() == "0":         #exiting if statement if user enters number zero"0"
                    break
            elif answer.lower().startswith("n"):
                print("OK BYE, Thank You!!!!!")
                sys.exit("SYSTEM EXITED SUCCESSFULLY!! NO EXCEPTION OCCURED")    #sys.exit function to terminate program            
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
main()

