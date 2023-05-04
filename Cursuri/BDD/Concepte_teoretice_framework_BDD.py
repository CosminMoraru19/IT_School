"""
Atunci cand vrem sa implementam framework-ul BDD avem nevoie de urmatoarele elemente:

1. Feature files = fisiere descrise intr-un limbaj natural pentru a specifica scenariile pe care vrem sa le testam
    Ele sunt scrise in limbajul gherkin care este un limbaj scris in engleza simpla bazat pe urmatoarele
    cuvinte cheie: GIVEN, WHEN, THEN (https://www.tutorialspoint.com/behave/behave_quick_guide.htm)

2. Aceste features files trebuie sa aiba la randul lor o implementare tehnica
   Aceasta implementare tehnica se face in fisierel de tip steps
   Legatura intre ele se face in felul urmator:
   - La rulare se citeste mai intai pasul din features file
   - Pe baza textului din acel pas de features file se cauta corespondentul in fisierul de steps
   - Atunci cand este identificat este executata metoda care este apelata in acel step pe baza unui element context implementat in environment

3. Metodele care sunt apelate in fisierele de steps vor fi apelate in fisierele de tip pages
    Fisierele de tip pages sunt implementate pe baza unui design pattern numit POM (page object model) - https://springframework.guru/gang-of-four-design-patterns/
    What is a design pattern? https://refactoring.guru/design-patterns/what-is-pattern

    Page object model presupune crearea fisierelor de python pentru fiecare pagina web pe care o testam

4. Avand in vedere ca metodele de la punctul 3 sunt create in interiorul unei clase, ele trebuie sa fie apelate
   prin intermediul unui obiect instantiat in acea clasa
   Instantierea obiectelor se va face in fisierul environment, iar toate obiectele se vor salva intr-o variabila context

5. Tot in environment vom instantia si browserul, care va fi necesar sa fie instantiat inaintea executarii testelor

6. Atunci cand vrem sa implementam metode care sa fie folosite in mai multe clase ne putem folosi de fisierul base_page

7. Ca sa putem sa mapam plugin-ul pentru generarea raportului de HTML putem sa o facem intr-un fisier numit behave.ini
"""