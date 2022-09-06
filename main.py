from asyncore import loop
from lib2to3.pgen2.token import EQUAL
from operator import length_hint
from os import remove
from posixpath import split
from queue import Empty
import random as rd
from re import I, S
from secrets import choice
from turtle import done
import time

list_of_names = ["amanda","bruno",'vinicius','fernanda',"pedrao",'joao','juninho','carol',"luis","gabriela"]



def random_choice(list_of_names):
    for _ in range(1):
        selection = choice(list_of_names)
    return selection


def create_new_list(selection):
    word_splitter = [j for j in selection]
    return word_splitter

def show_num_of_letters():
    
    print("Here is where the game starts!!")
    print('''Each time that you get one letter wrong, one party of our buddy's body will apper, once you get 6 mistakes, you are out!''')



def getting_input(spllited_list: list) -> str: #this def gets an input and says if the name has or not the word typed        
    
    
    global lower_guess
    lower_guess = '!'
    letter = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','k','K','L','l','M','m','n','N','o','O','p','P','q','Q','r','R','s','S','T','t','u','U','V','v','w','W','x','X','Y','y','Z','z','ç','Ç']
     
    while lower_guess not in letter:
        qnt = len(spllited_list)
        
        if len(spllited_list) > 2:
            print(f'There is still {qnt} letters')
        else:
            print(f'There is still {qnt} letter')
        guess = input('Please type your guess!: ')
        
        lower_guess = guess.lower()
        if lower_guess not in letter:
            print('Please type an valid letter! ')
            lower_guess = guess.lower()
        elif lower_guess in letter:
            return lower_guess


def removing_from_list(spllited_list: list, q = 2):
    
    while len(spllited_list) >= 1:
        getting_input(spllited_list)
        if lower_guess in spllited_list:
            while lower_guess in spllited_list:
                spllited_list.remove(lower_guess)
        
        elif lower_guess not in spllited_list:
        
            
            
            

            if q ==2:

                
                print('''Oh no, you made a mistake, our buddy just got a head! You still have 5 chances! 
___
|   O
|  
|  
|
''')
            
                
                time.sleep(2)

                removing_from_list(spllited_list, q=3)
                

            
            
            
            
            elif q ==3:

                
                print('''Keep calm, our friend just got his cheast, but do not worry, we still have a long way to go! You still have 4 chances! 
___
|   O
|   |
|  
|



                ''')
                time.sleep(2)

                removing_from_list(spllited_list,q=4)
                










            
            
            
            
            elif q ==4:
                print('''The first arm is up, give your best!!!!!! You still have 3 chances! 

___
|   O
|   |-
|   
|
''')
                time.sleep(2)

                removing_from_list(spllited_list, q=5)
                









        
        
        
        
        
        
        
            elif q ==5:
                print('''Do not give up!!!!!! You still have 2 chances!             
___
|   O
|  -|-
|  
|
                ''')
                time.sleep(2)

                removing_from_list(spllited_list,q=6)
                


            elif q ==6:
                print('''He can not handle another mistake!!!!! You still have 1 chance!              
___
|   O
|  -|-
|  / 
|
''')
                time.sleep(2)
                removing_from_list(spllited_list,q=7)
                

                
            



            
            
            elif q == 7:
                print('''
___
|   O
|  -|-
|  / \\
|
''')


                print('I am sorry, you lost the game :(')
                
                time.sleep(3)
                pag()
               

                
            
                
                


        
                
                
                
            
            
            
            
    while len(spllited_list) == 0:
        print('Congratulations, you won the game!!!!!!!')
        break

def pag():
    playagain = input('Do you want to play again?(Y/N)\t')
    if playagain == 'y' or 'Y':
        show_num_of_letters()
    elif playagain == 'n' or 'N':
        exit
    else:
        pag()

def run(list_of_names):
    selection = random_choice(list_of_names) 
    spllited_list = create_new_list(selection) 
    show_num_of_letters()
    
    
    removing_from_list(spllited_list)
    
    
    
    


run(list_of_names)






