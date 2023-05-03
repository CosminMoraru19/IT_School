"""
BDD = Behaviour Driven Development

BDD este o abordare de software development care presupune scrierea de teste pornind de la scenariile de business

BDD este o abordare derivata din conceptul de TDD (Test Driven Development)

Logica activitatilor in TDD
- Se scriu testele automate
- Se ruleaza testele automate (la momentul asta asteptarea e ca acestea sa fie failed)
- Se scrie codul pe baza testelor automate care au fost scrise anterior
- Se refactorizeaza si reruleaza testele automate (la momentul asta asteptarea e ca acestea sa fie passed)
- In cazul in care exista teste care sunt failed la momentul asta, se va refactoriza codul astfel incat sa reparam probleme care au fost identificate
- Se vor rerula testele pana cand toate vor avea statusul passed

Logica activitatilor in BDD
- Se scriu scenariile de business care trebuie sa fie implementate
- Se scriu testele automate pornind de la scenariile de business care au fost definite
- Se ruleaza testele automate (la momentul asta asteptarea e ca acestea sa fie failed)
- Se scrie codul pe baza testelor automate care au fost scrise anterior
- Se reruleaza testele automate (la momentul asta asteptarea e ca acestea sa fie passed)
- In cazul in care exista teste care sunt failed la momentul asta, se va refactoriza codul astfel incat sa reparam probleme care au fost identificate
- Se vor rerula testele pana cand toate vor avea statusul passed

Avantajele TDD:
- O sa facem dezvoltarea pe baza testelor, si vom avea un nivel de acoperire si claritate mai mare a codului
- O sa primim rezultate mult mai devreme in procesul de dezvoltare
- O sa putem sa modificam codul mai usor prin faptul ca vom observa problemele pe masura ce acesta este scris

Avantajele BDD:
- Toate persoanele implicate vor putea intelege testele pe care le facem fara sa aiba neaparat cunostinte tehnice
- O sa facem dezvoltarea pe baza testelor, si vom avea un nivel de acoperire si claritate mai mare a codului
- O sa primim rezultate mult mai devreme in procesul de dezvoltare
- O sa putem sa modificam codul mai usor prin faptul ca vom observa problemele pe masura ce acesta este scris

In general abordarile TDD si BDD sunt implementate in metodologia Agile

Waterfall = metodologie de software development care este mai rigida si care nu permite modificari in timpul procesului de dezvoltare
Avantaje waterfall:
- stim de la inceput exact ce avem de implementat pe baza contractului semnat cu clientul
- stim exact ce buget avem
- stim cum va arata produsul
- exista sanse mici sa apara elemente neprevazute
- avem documentatie foarte bine definita pentru tot ceea ce tine de produs

Dezavantaje waterfall:
- daca apare necesitatea schimbarii anumitor cerinte de business acestea nu se pot face in momentul respectiv
        ci trebuie deschis proiect nou cu buget separat si resurse separate
- nu vom avea feedback de la client decat atunci cand produsul va fi complet dezvoltat
- rata de aparitie a bug-urilor poate sa fie mare din cauza complexitatii produsului creat in intregime
- rata de identificare a bug-urilor poate sa fie mai redusa din cauza complexitatii produsului

Agile = o metodologie de software development mai permisiva care poate sa sustina schimbari in timpul procesului de software development

Avantaje agile:
- dezvoltarea se face treptat in sprinturi in care sunt dezvoltate o serie de functionalitati care vor fi livrare la client
- vom primi feedback foarte devreme in procesul de dezvoltare din partea clientului
- putem sa facem schimbari oricand in procesul de dezvoltare
- se bazeaza pe o comunicare foarte buna din partea echipei

Dezvantaje agile:
- bugetul poate sa creasca avand in vedere ca nu stim de la bun inceput exact cum trebuie sa arate produsul
- este posibil sa nu ne atingem deadline-ul daca avem foarte multe schimbari in cod
- e necesara o colaborare foarte buna a echipei
- documentatia e destul de sumara si daca echipa nu comunica in mod corect pot aparea probleme

CI / CD = o modalitate prin care putem sa asiguram integrarea continua a noilor functionalitati in codul existent
https://www.redhat.com/en/topics/devops/what-is-ci-cd#:~:text=CI%2FCD%20is%20a%20method,continuous%20delivery%2C%20and%20continuous%20deployment.

Procesul de dezvoltare in metodologia AGILE:
- Se creeaza un backlog
- Se parcurge acel backlog si se efectueaza procesul de backlog refinement
- Se planifica sprint-urile
- se repeta planificarea sprinturilor pana cand tot produsul este complet dezvoltat

backlog = serie de functionalitati care trebuie sa fie dezvoltate pentru ca produsul sa fie complet
backlog refinement = proces in cadrul caruia se prioritizeaza functionalitatile care trebuie sa fie implementate
                            in functie de importanta pentru client
                      de asemenea, se poate decide renuntarea la anumite functionalitati care nu sunt atat de
                             importante pentru client si ar putea sa coste mai mult din punct de vedere timp si financiar
                             vs beneficiile pe care le-ar putea aduce
sprint = o perioada de timp (de regula cam de doua saptamani) in care se vor implementa un set de functionalitati
            Sprint-ul se desfasoara in felul urmator:
            - se trece printr-o sedinta de sprint planning in care se decide care functionalitati vor fi implementate in acel sprint
            - se fac zilnic sedinte de daily standup care sunt niste sedinte in care se discuta despre ce s-a facut in ziua anterioara
                        la ce se lucreaza in ziua curenta si daca exista ceva impedimente care ne impiedica sa mergem mai departe
            - la final de sprint se face ceea ce se numeste sprint review, in care evaluam ceea ce am implementat, daca este nevoie
                        vom muta task-urile care nu au putut fi implementate intr-un sprint viitor.
                        Tot in acest sprint review vom primi feedback de la client pentru lucrurile pe care deja le-am implementat
            - dupa sprint review exista ceea ce se numeste sprint retrospective in care se analizeaza activitatile pozitive
                         care ar trebui pastrate si in sprint-urile viitoare, dar si lucrurile mai putin bune care ar trebui
                         corectate in sprint-urile viitoare (lessons learned)

Syllabus ISTQB certificate: https://istqb-main-web-prod.s3.amazonaws.com/media/documents/ISTQB-CTFL_Syllabus_2018_v3.1.1.pdf
Syllabus certificare agile: https://istqb-main-web-prod.s3.amazonaws.com/media/documents/ISTQB-CTFL-AT_Syllabus_v1.0.pdf

"""