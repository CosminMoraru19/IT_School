Xpath-ul reprezinta o adresa care identifica locul exact al elementului in toata suita
        de elemente din HTML
Exista doua tipuri de XPATH:
- XPATH absolut = o adresa completa incepand de la inceputul paginii si desfasurat din parinte in copil
                   pana la momentul identificarii elementelor cautate
                   Atunci cand se face cautare dupa XPATH absolut primul caracter din XPATH va fi "/"
- XPATH relativ = o adresa partiala incepand cu primul element unic identificat pe pagina
                    si desfasurat fie din parinte in copil fie din copil in parinte
                    fie din frate in frate pana la momentul identificarii elementelor cautate
                    Atunci cand se face cautare dupa XPATH absolut primul caracter din XPATH va fi "//"

In general NU este recomandat sa folosim XPATH absolut pentru ca daca se schimba structura site-ului,
        spre exemplu se adauga un element nou, atunci testele noastre vor incepe sa crape
        pentru ca adresa nu va mai fi corecta

Exemplu Xpath relativ: //button[@value="Login"]
Exemplu Xpath absolut: /html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button


Modalitati prin care putem sa folosim XPATH-ul relativ:
# 1.Cautare dupa atribut = valoare pentru un tag specific
        Acest lucru se va face prin scrierea caracterelor // ca sa anuntam sistemul
                ca vrem sa facem cautare dupa xpath relativ
                si apoi sa scriem tag-ul care ne intereseaza.
Exemplu: //button -> sistemul va cauta toate elemente de pe site care au tag-ul button


# 2.Cautare dupa atribut = valoare
In Xpath, atunci cand facem cautare dupa atribut=valoare,
                atributul trebuie precedat INTOTDEAUNA de caracterul @
           De asemenea, se va respecta conditia de plasare a perechii atribut=valoare intre paranteze patrate
Exemplu: //button[@value="Login"] -> sistemul va cauta toate elemente de pe site care au tag-ul button
                        si perechea atribut=valoare in care atributul este "value" si valoarea este "Login"

Atunci cand nu stim sau nu ne intereseaza neaparat tag-ul, putem sa cautam toate elementele care au
                        o pereche specifica atribut=valoare prin intermediul caracterului "*"
Exemplu: //*[@value="Login"]
//*[@class="btn btn-primary btn-block"]

ATENTIE!!! La XPATH daca avem elemente care au identificator de tip clasa separat prin spatiu
                (adica sunt mai multe clase) TREBUIE SA LE PUNEM PE TOATE

# 3. Cautare dupa copil prin navigare in jos
Atunci cand facem cautare din parinte in copil, acestia trebuie separati prin  caracterul "/"
Exemplu: //form/input -> form este parintele, input este copilul

Atunci cand vrem sa navigam nu la copil direct ci la un urmas mai indepartat
        va trebui sa folosim caracterele "//"
Exemplu: //div[@class="row"]//input[@name="SearchTerm"]

# 4. Navigarea in sus catre parent
Atunci cand vrem sa navigam din copil in parinte va trebui sa scriem caracterul "/"
        urmat de cuvantul cheie "parent" urmat de caracterele "::"
        urmate de numele tag-ului parintelui la care vrem sa ajungem
Exemplu: //span/parent::button[@type="submit" and @name="search"]

# 5. Navigarea in sus catre fratele anterior
Atunci cand vrem sa navigam dintr-un element in fratele anterior va trebui sa scriem caracterul "/"
        urmat de cuvantul cheie "preceding-sibling" urmat de caracterele "::"
        urmate de numele tag-ului parintelui la care vrem sa ajungem
Exemplu: //button[@type="submit" and @name="search"]/preceding-sibling::a

5. Putem as navigam la fratele ulterior cu "/following-sibling::tag"
Atunci cand vrem sa navigam dintr-un element in fratele anterior va trebui sa scriem caracterul "/"
        urmat de cuvantul cheie "following-sibling" urmat de caracterele "::"
        urmate de numele tag-ului parintelui la care vrem sa ajungem
Exemplu: //a[@class="search-cancel"]/following-sibling::button

# 4. Cautare cu OR - Ambele conditii sunt adevarate
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first name'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")

# 5. Cautare cu OR - Doar a doua conditie este adevarata
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first names'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")

# 6. Cautare cu OR - Nicio conditie nu este adevarata
chrome.find_element(By.XPATH,"//input[@placeholder='Enter first names'] | //*[@placeholder='Enter last name']").send_keys("Cautare cu OR")

#7. Tratare dropdown
years_of_experience = Select(chrome.find_element(By.XPATH,"//*[@id='select-menu']"))
time.sleep(2)
years_of_experience.select_by_visible_text("5-9")
time.sleep(2)
years_of_experience.select_by_visible_text("10+")
time.sleep(2)