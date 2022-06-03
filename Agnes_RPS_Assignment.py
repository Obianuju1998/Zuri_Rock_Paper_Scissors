# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:31:46 2022

@author: Dell XPS 15
"""
# This is a program for the rock, paper, and scissors game.
from random import choice

rps = ['R', 'P', 'S']


def CPU(select):
    return choice(select)

def getChoiceName(option):
    if(option == 'R'):
        return 'Rock'
    elif(option == 'P'):
        return 'Paper'
    elif(option == 'S'):
        return 'Scissors'
    else:
        print("You have entered the wrong option. Try again.")
        
selected = CPU(rps)        
        
user_input = input("Enter any option between R, P, and S:")

while (True):
    if (user_input not in rps):
        print("Error!!! You have entered the wrong option. Try again.")
        user_input = input("Enter any option between R, P, and S:")
    else:
        if (selected == user_input):
            selected = CPU(rps)
            print(f'CPU ({getChoiceName(selected)}) : Player ({getChoiceName(user_input)})')
            print("It's a Tie")
            user_input = input("Enter any option between R, P, and S:")
        
        else:
            print(f'CPU ({getChoiceName(selected)}) : Player ({getChoiceName(user_input)})')
            if((selected == 'R') and (user_input == 'S')):
                print("CPU Wins!!!")
        
            elif((selected == 'S') and (user_input == 'R')):
                print("Player Wins!!!")
            
            elif((selected == 'P') and (user_input == 'R')):
                print("CPU Wins!!!")
        
            elif((selected == 'R') and (user_input == 'P')):
                print("Player Wins!!!")
            
            elif((selected == 'S') and (user_input == 'P')):
                print("CPU Wins!!!")
            
            elif((selected == 'P') and (user_input == 'S')):
                print("Player Wins!!!")
            break
     
        
        
