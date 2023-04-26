import csv
import datetime
import msvcrt
import os
def usun(zadania):
    """Usuwa zadanie o podanej nazwie i dacie utworzenia."""
    nazwa = input("Podaj nazwę zadania do usunięcia: ")
    data_utworzenia = input("Podaj datę utworzenia zadania do usunięcia (w formacie rrrr-mm-dd): ")
    czas_utworzenia = input("Podaj czas utworzenia zadania do usunięcia (w formacie hh-mm): ")
    for zadanie_id, zadanie in zadania.items():
        if zadanie['nazwa'] == nazwa and zadanie['data_utworzenia']==data_utworzenia and zadanie['czas_utworzenia']==czas_utworzenia:
            del zadania[zadanie_id]
            print("Usunięto zadanie.")
            return
    print("Nie znaleziono zadania o podanej nazwie i dacie utworzenia.")
def wczytaj_zadania():
    """Ładuje zadania z pliku txt do słownika."""
    zadania = {}
    with open("d:\c++\python\zadania.txt", "r") as file:
        for linia in file:
            nazwa,data_realizacji,czas_realizacji, priorytet, status,kategoria,opis, data_utworzenia,czas_utworzenia,data_edytowania,czas_edytowania = linia.strip().split(',')
            zadanie_id = str(len(zadania) + 1)
            zadania[zadanie_id] = {
                'nazwa': nazwa,
                'data_realizacji':data_realizacji,
                'czas_realizacji':czas_realizacji,
                'priorytet': priorytet,
                'status': status,
                'kategoria':kategoria,
                'opis':opis,
                'data_utworzenia': data_utworzenia,
                'czas_utworzenia':czas_utworzenia,
                'data_edytowania': data_edytowania,
                'czas_edytowania': czas_edytowania
            }
    return zadania

def zapisz_zadania(zadania):
    """Zapisuje zadania ze słownika do pliku txt."""
    with open('zadania_odp.txt', 'w') as file:
        for zadanie_id, zadanie in zadania.items():
            linia = f"{zadanie['name']},{zadanie['priority']},{zadanie['status']},{zadanie['created']},{zadanie['updated']}\n"
            file.write(linia)

def wypisz_zadania(zadania):
    """Wyświetla zadania z słownika."""
    for zadania_id,zadanie in zadania.items():  
        print(f"Nazwa: {zadanie['nazwa']}")
        print(f"Realizacja(data): {zadanie['data_realizacji']}")
        print(f"Realizacja(czas): {zadanie['czas_realizacji']}")
        print(f" Priorytet: {zadanie['priorytet']}")
        print(f" Status: {zadanie['status']}")
        print(f" Kategoria: {zadanie['kategoria']}")
        print(f" Opis: {zadanie['opis']}")
        print(f" Utworzone(data): {zadanie['data_utworzenia']}")
        print(f" Utworzone(czas): {zadanie['czas_utworzenia']}")
        print(f" Aktualizowane(data): {zadanie['data_edytowania']}")
        print(f" Aktualizowane(czas): {zadanie['czas_edytowania']}")

def dodaj_zadanie(zadania):
    """Dodaje nowe zadanie do słownika."""
    nazwa = input("Podaj nazwę zadania: ")
    data_realizacji= input("Podaj date realizacji: ")
    czas_realizacji= input("Podaj czas realizacji: ")
    priorytet = input("Podaj priorytet zadania (niski, normalny, wysoki): ")
    status = input("Podaj status zadania (0;100): ")
    kategoria=input("Podaj kategorie: ")
    opis=input("Podaj opis: ")
    data_utworzenia = datetime.datetime.now().strftime("%Y-%m-%d")
    czas_utworzenia=datetime.datetime.now().strftime( "%H:%M")
    data_edytowania = data_utworzenia
    czas_edytowania = czas_utworzenia
    zadanie_id = str(len(zadania) + 1)
    zadania[zadanie_id] = {
                'nazwa': nazwa,
                'data_realizacji':data_realizacji,
                'czas_realizacji':czas_realizacji,
                'priorytet': priorytet,
                'status': status,
                'kategoria':kategoria,
                'opis':opis,
                'data_utworzenia': data_utworzenia,
                'czas_utworzenia':czas_utworzenia,
                'data_edytowania': data_edytowania,
                'czas_edytowania': czas_edytowania
            }
    print("Zadanie zostało dodane")