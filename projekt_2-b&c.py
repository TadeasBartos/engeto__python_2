"""
projekt_2-b&c.py: druhý projekt do Engeto Online Python Akademie

author: Tadeáš Bartoš
email: bartos.tadeas@live.com
github: TadeasBoomer
"""

# bulls & cows

import random

def has_duplicates(num):
    """
    Funkce kontroluje, zda číslo obsahuje unikátní číslice.

    Parametry:
    -----------------
    num - číslo, které se má zkontrolovat

    Vrací:
    -----------------
    True, pokud číslo obsahuje duplicitní číslice, False jinak
    """
    num_str = str(num)
    return len(num_str) != len(set(num_str))

def carky(delka):
    """
    Funkce tiskne čárky o zadané délce.

    Parametry:
    -----------------
    delka - délka čárek

    Vrací:
    -----------------
    Vypisuje čárky o zadané délce
    """
    print("-" * delka)

def num_check(num):
    """
    Funkce vyzývá uživatele k zadání čísla do té doby, 
        - dokud nezadá číslo o délce 4 číslic, 
        - nezačínající 0, 
        - volá funkci has_duplicates(num), která kontroluje zda číslo obsahuje duplicitní číslice.

    Parametry:
    -----------------
    num - číslo, které se má zkontrolovat

    Vrací:
    -----------------
    Vypisuje číslo
    """
    while len(num) != 4 or num.startswith("0") or has_duplicates(num):
        num = input("Please, enter a number made of 4 digits, no letters, no duplicites and not starting with 0: ")
    return num

def bulls(cislo_hrac, cislo_stroj):
    """
    Funkce počítá bulls.

    Parametry:
    -----------------
    cislo_hrac - číslo hráče
    cislo_stroj - číslo stroje

    Vrací:
    -----------------
    Vypisuje bulls
    """
    bulls_counter = 0
    for i in range(0, 4):
        if cislo_hrac[i] == cislo_stroj[i]:
            bulls_counter = bulls_counter + 1
    return bulls_counter

def cows(cislo_hrac, cislo_stroj):
    """
    Funkce počítá cows.

    Parametry:
    -----------------
    cislo_hrac - číslo hráče
    cislo_stroj - číslo stroje

    Vrací:
    -----------------
    Vypisuje cows
    """
    cows_counter = 0 
    for j in range(0,4):
        if cislo_hrac[j] in cislo_stroj:
            cows_counter = cows_counter + 1
    return cows_counter

def print_score(bulls_counter, cows_counter):
    """
    Funkce vypisuje bulls a cows.

    Parametry:
    -----------------
    bulls_counter - počet bulls z předchozí funkce bulls
    cows_counter - počet cows z předchozí funkce cows

    Vrací:
    -----------------
    Vypisuje bulls a cows
    """
    print(f"You have got {bulls_counter} bull{'s' if bulls_counter != 1 else ''}. (správné číslo i umístění)")
    print(f"You have got {cows_counter} cow{'s' if cows_counter != 1 else ''}. (správné číslo)")
        
def bulls_and_cows():
    """
    Hlavní těly hry

    Parametry:
    -----------------
    žádné

    Vrací:
    -----------------
    1. Vygeneruje náhodně číslo stroje 1000-9999
    2. Následně toto generování opakuje do doby než nesplní parametry funkce has_duplicates(num)
    3. Uvítání hráče, zkontroluje zda zadané číslo hráče splňuje podmínky num_check(num)
    4. Převede obě čísla z int -> str, vynuluje bulls/cows_counter a počítadlo počtu pokusů
    5. Podmínka chodu hry je postavena tak, že cyklus while běží do doby než se číslo hráče nerovná číslu stroje
        5.1 Proběhne funkce bulls_counter, následně cows_counter
        5.2 Hodnoty bulls/cows_counteru jsou sděleny hráči
        5.3 Uživatel je vyzván k zadání dalšího čísla, kontrola čísla přes funkci num_check(num)
        5.4 Na konci while cyklu je podmínka, že pokud cislo_hrac == cislo_stroj, je uživateli sděleno že vyhrál a počet pokusů
    """

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

if __name__ == "__main__":
     bulls_and_cows()