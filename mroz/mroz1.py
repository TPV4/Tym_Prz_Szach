import csv
import datetime
import msvcrt
import os
import funkcje1 as f

slownik=f.wczytaj_zadania()
while True:
  print("Co chcesz zrobić?")
  print("1. Wypisz zadania")
  print("2. Dodaj zadanie")
  print("3. Usuń zadanie")
  print("4. Inne operacje")
  print("5. Wyjdź")

  try:
    wybor = int(input("Wybierz [1-5]: "))
  except ValueError:
    print("Nieprawidłowy wybór!")
    continue

  if wybor == 1:
    if slownik=={}:
        print("Brak zadan")
        msvcrt.getch()
        os.system("cls")
    else:
        f.wypisz_zadania(slownik)
        msvcrt.getch()
        os.system("cls")
  elif wybor == 2:
    slownik=f.wczytaj_zadania()
    f.dodaj_zadanie(slownik)
    msvcrt.getch()
    os.system("cls")
  elif wybor == 3:
    f.wypisz_zadania(slownik)
    f.usun(slownik)
  elif wybor == 4:
    print()
  elif wybor == 5:
    print("Do zobaczenia!")
    break
  else:
    print("Nieprawidłowy wybór!")