"""
Unit test este un nivel de testare care presupune testarea celor mai mici bucati
functionale din cod.

Exista mai multe niveluri de testare dupa cum urmeaza:

a) unit testing = primul nivel de testare care evalueaza functionarea corecta a celor mai mici bucati
									functionale din cod. De regula se testeaza clase sau functii.
									In general testarea unitara se face prin definirea unor functii care
									testeaza alte functii.
									In general testarea unitara este facuta de catre echipa de dezvoltare
b) component testing = al doilea nivel de testare care evalueaza functionarea corecta a unor module finalizate din cod
c) integration testing = al treilea nivel de testare care asigura comunicarea corecta intre componente sau sisteme
													Exista doua tipuri de testare de integrare:
													- component integration testing -> evalueaza comunicarea corecta intre doua componente
																	Exemplu: atunci cand cream o comanda noua vrem sa vedem ca aceeasi comanda pe care
																				 o vedem in cosul de cumparaturi o putem vedea si in istoricul comenzilor
													- system integration testing -> evalueaza comunicarea corecta intre doua sisteme
																	Exemplu: vrem ca utilizatorul sa poata sa plateasca produsele din cosul de cumparaturi
																					cu paypall. Caz in care vorbim de o integrare intre platforma de e-commerce
																					si sistemul paypall
d) system testing = al patrulea nivel de testare care evalueaza corectitudinea scenariilor complete (end to end  - e2e)
										Exemplu:
										Vrem sa evaluam posibilitatea de a cumpara produse incercand sa reproducem pasii utilizatorului
												in modul urmator:
												1. Intram in aplicatie
												2. Ne logam
												3. Cautam produsul care ne intereseaza
												4. Adaugam produsul in cosul de cumparaturi
												5. Completam toate datele pentru comanda
												6. Plasam comanda
e) acceptance testing = ultimul nivel de testare si care presupune o ultima validare din perspectiva utilizatorului / clientului
										Exista doua tipuri de acceptance testing:
										- alpha testing = testare facuta la sediul dezvoltatorului de catre echipa de testare
										- beta testing = testare facuta pe un mediu real sau pe un mediu similar cu cel real de catre client / utilizatorul final

Exemplu de unit testing: verifica faptul ca se calculeaza corect
													aplicarea voucherului in cosul de cumparaturi
Exemplu de component testing: verifica faptul ca toate functionalitatile din cosul
													de cumparaturi functioneaza corect

In contextul testarii automate, libraria unit test, desi este / poate fi cea folosita de catre eechipa de dezvoltare
		pentru scrierea testelor unitare, putem sa o folosim si noi pentru dezvoltarea testelor automate

Pentru a putea folosi aceasta librarie, va trebui sa cream clase de test care sa o mosteneasca

Atunci cand ne folosim de aceasta metoda, va trebui sa avem de asemenea si urmatoarele componente in clasa noastra:

- setup -> contine instructiuni ce trebuie sa fie executate inainte de fiecare test (preconditii)
- teardown -> contine instructiuni ce trebuie sa fie executate dupa fiecare test

Fiecare clasa de test va trebui sa aiba metode de test care OBLIGATORIU trebuie sa inceapa cu prefixul test_
				ca sa fie recunoscute de pachetul pytest

Pentru a putea rula testele din libraria unit test NU E NEVOIE de instantierea unui obiect

Orice metoda va trebui sa se termine cu instructiunea assert (obiectivul final al unui)

Assertul are urmatoarea structura:

assert valoare_pe_care_o_comparam valoare_cu_care_comparam, "mesaj de eroare in caz de fail"

"""