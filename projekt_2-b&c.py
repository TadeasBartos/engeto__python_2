"""
projekt_2-b&c.py: druhý projekt do Engeto Online Python Akademie

author: Tadeáš Bartoš
email: bartos.tadeas@live.com
github: TadeasBoomer
"""

# bulls & cows

import random

def has_duplicates(num):
    """doplnit docstringy"""
    num_str = str(num)
    return len(num_str) != len(set(num_str))

def carky(delka):
    print("-" * delka)

def num_check(num):
    while len(num) != 4 or num.startswith("0") or has_duplicates(num):
        num = input("Please, enter a number made of 4 digits, no letters, no duplicites and not starting with 0: ")
    return num

def bulls(cislo_hrac, cislo_stroj):
    bulls_counter = 0
    for i in range(0, 4):
        if cislo_hrac[i] == cislo_stroj[i]:
            bulls_counter = bulls_counter + 1
    return bulls_counter

def cows(cislo_hrac, cislo_stroj):
    cows_counter = 0 
    for j in range(0,4):
        if cislo_hrac[j] in cislo_stroj:
            cows_counter = cows_counter + 1
    return cows_counter

def print_score(bulls_counter, cows_counter):
    print(f"You have got {bulls_counter} bull{'s' if bulls_counter != 1 else ''}. (správné číslo i umístění)")
    print(f"You have got {cows_counter} cow{'s' if cows_counter != 1 else ''}. (správné číslo)")
        
cislo_stroj = random.randint(1000,9999)

while has_duplicates(str(cislo_stroj)):
    cislo_stroj = random.randint(1000,9999)
    
print("Hi there!")
carky(50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
carky(50)
cislo_hrac = num_check(input("Enter a number:  "))
carky(50)
print("Game started!")
carky(50)

cislo_stroj = str(cislo_stroj)
cislo_hrac = str(cislo_hrac)

cows_counter = 0
bulls_counter = 0
run = 0

while cislo_hrac != cislo_stroj:
    bulls_counter = bulls(cislo_hrac=cislo_hrac, cislo_stroj=cislo_stroj)
    cows_counter = cows(cislo_hrac=cislo_hrac, cislo_stroj=cislo_stroj)

    run = run + 1
    print("This is your ", run, " run.")
    print_score(bulls_counter, cows_counter)

    carky(50)
    cislo_hrac = num_check(input("Enter a number: "))
    carky(50)

    if cislo_hrac == cislo_stroj:
        print("Congratulations! You did that in", run," runs!")