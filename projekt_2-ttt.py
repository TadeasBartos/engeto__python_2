"""
projekt_2-ttt.py: druhý projekt do Engeto Online Python Akademie

author: Tadeáš Bartoš
email: bartos.tadeas@live.com
github: TadeasBoomer
"""
import random

def mrizka(herni_pole):
    max_delka = max(len(s) for s in herni_pole)

    def horizontal_line(max):
        return f"+{'-' * (2 + max)}+{'-' * (2 + max)}+{'-' * (2 + max)}+"

    def format_row(start):
        return f"| {herni_pole[start]:^{max_delka}} | {herni_pole[start+1]:^{max_delka}} | {herni_pole[start+2]:^{max_delka}} |"

    print(horizontal_line(max_delka))
    print(format_row(0))
    print(horizontal_line(max_delka))
    print(format_row(3))
    print(horizontal_line(max_delka))
    print(format_row(6))
    print(horizontal_line(max_delka))

print("Vítejte ve hře piškvorky!")
print("Tvým úkolem je vytvořit řadu tří symbolů X na hrací ploše.")
print("Hrací ploše vypadá následovně: ")

herni_pole = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
mrizka(herni_pole)

print("Vždy dostaneš na výběr, na jaké pole chceš svůj kámen umístit.")
print("Pokud vybereš obsazené pole nebo něco jiného, budeš vyzván znovu, dokud nevybereš pole volné.")

volne_pole = herni_pole.copy()
vyherni_pole = [("a1", "a2", "a3"), ("b1", "b2", "b3"), ("c1", "c2", "c3"),
                ("a1", "b1", "c1"), ("a2", "b2", "c2"), ("a3", "b3", "c3"),
                ("a1", "b2", "c3"), ("a3", "b2", "c1")]

tahy_hrac = []
tahy_pocitac = []

for _ in range(5):
    tah_hrac = input("Zadej jaké chceš hrát volné pole: ")
    while tah_hrac not in volne_pole:
        tah_hrac = input("Pole je obsazené nebo neexistuje. Zadej jiné pole: ")
    
    tahy_hrac.append(tah_hrac)
    volne_pole.remove(tah_hrac)
    herni_pole[herni_pole.index(tah_hrac)] = "X"

    if any(set(pole).issubset(tahy_hrac) for pole in vyherni_pole):
        print("Vyhráváš ty!")
        mrizka(herni_pole)
        break

    if volne_pole:
        tah_pocitac = random.choice(volne_pole)
        tahy_pocitac.append(tah_pocitac)
        volne_pole.remove(tah_pocitac)
        herni_pole[herni_pole.index(tah_pocitac)] = "O"

        if any(set(pole).issubset(tahy_pocitac) for pole in vyherni_pole):
            print("Vyhrává počítač!")
            mrizka(herni_pole)
            break

    if not volne_pole:
        print("Je to remíza!")
        break

    mrizka(herni_pole)