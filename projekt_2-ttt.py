"""
projekt_2-ttt.py: druhý projekt do Engeto Online Python Akademie

author: Tadeáš Bartoš
email: bartos.tadeas@live.com
github: TadeasBoomer
"""
import random

def mrizka(herni_pole):
    """ 
    Funkce vykresluje herní pole.

    Parametry:
    -----------------
    herni_pole - list obsahující popis polí

    Vrací:
    -----------------
    Vypisuje herní pole
    """
    max_delka = max(len(s) for s in herni_pole)

    def horizontal_line(max):
        """
        Funkce vykresluje horizontální čáru

        Parametry:
        -----------------
        max - maximální délka pole

        Vrací:
        -----------------
        Vypisuje horizontální čáru
        """
        return f"+{'-' * (2 + max)}+{'-' * (2 + max)}+{'-' * (2 + max)}+"

    def format_row(start):
        """
        Funkce vykresluje řádek herního pole

        Parametry:
        -----------------
        start - index prvního pole

        Vrací:
        -----------------
        Vypisuje řádek herního pole
        """
        return f"| {herni_pole[start]:^{max_delka}} | {herni_pole[start+1]:^{max_delka}} | {herni_pole[start+2]:^{max_delka}} |"

    print(horizontal_line(max_delka))
    print(format_row(0))
    print(horizontal_line(max_delka))
    print(format_row(3))
    print(horizontal_line(max_delka))
    print(format_row(6))
    print(horizontal_line(max_delka))

def piskvorky():
    """
    Hlavní tělo hry

    Parametry:
    -----------------
    žádné 

    Vrací:
    -----------------
    1. Přivítání hráče, vysvětlení hry
    2. Vytvoření herního pole
    3. Vytvoření listu volne_pole, vyherni_pole a prázdných listů tahy_hrac, tahy_pocitac
    4. Cyklus hry
    5. Vytvoření proměnné tah_hrac, která je zkontrolována, zda se nachází ve volne_pole, aby hráč nevybral obsazené pole
    6. Přidání tah_hrac do listu tahy_hrac, odebrání z listu volne_pole a přiřazení symbolu X
    7. Zkontrolování, zda tah_hrac nebyl výherní
    8. Pokud je list volne_pole prázdný, je vyhlášena remíza
    9. Vytvoření proměnné tah_pocitac, která je náhodně vybrána z listu volne_pole, aby počítač nevybral obsazené pole
    10. Přidání tah_pocitac do listu tahy_pocitac, odebrání z listu volne_pole a přiřazení symbolu O
    11. Zkontrolování, zda tah_pocitac nebyl výherní
    12. Takto probíhá cyklus, dokud jedna strana nevyhraje nebo dojde k remíze
    """
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

if __name__ == "__main__":
    piskvorky()