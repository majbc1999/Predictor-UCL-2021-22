############################################################################################################################################################

#                                                        * * * PREDICTOR UCL 2021 / 2022 * * *                                                             #
#                                                                Maj Gaberšček,  Bovec                                                                     #
############################################################################################################################################################

from polepsaj_kvote import polepsaj_kvote
import time


    ### NAJBOLJŠA NAPOVED ###

def simulacija(verjetnosti, popularni, ekipe, prejsnji_rezultat):

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(ekipe[0].upper() + " : " + ekipe[1].upper())

        slovar_tock = {}
        najboljsa_napoved = "0:0"
        upanje1 = 0
        upanje_trenutno = 0
        for i in range(10):
            for j in range(10):
                rezultat = str(i) + ":" + str(j)

                # ne upoštevamo rezultatov, ki vodijo v podaljšek
                if (i + prejsnji_rezultat[0] != j + prejsnji_rezultat[1]):
                    upanje_trenutno = upanje(rezultat, verjetnosti, popularni)
                    if upanje_trenutno[0] >= upanje1:
                        upanje1 = upanje_trenutno[0]
                        najboljsa_napoved = rezultat
                        slovar_tock = upanje_trenutno[1]


        print(" ")
        print("Najboljša napoved je: " + ekipe[0] + " " + najboljsa_napoved + " " + ekipe[1])
        print("Pričakovane točke = " + format(upanje1,  '.2f'))
        print(" ")
        print("Verjetnosti točk:")
        for geslo in sorted(slovar_tock):
            print("     " + str(geslo) + " ...... " + str(round(100 * slovar_tock[geslo],1)) + "%")
        print(" ")


    ### SLOVAR VERJETNOSTI REZULTATA ###

def verjetnosti(kvote):
        vsota_kvot = 0
        slovar = {}
        for i in range(10):
            for j in range(10):
                niz = str(i) + ":" + str(j)
                if niz not in kvote.keys():
                    continue
                if kvote[niz] != 0:
                    vsota_kvot += (1 / kvote[niz])
        for i in range(10):
            for j in range(10):
                niz = str(i) + ":" + str(j)
                if (niz not in kvote.keys()): slovar[niz] = 0
                elif kvote[niz] == 0: slovar[niz] = 0
                else:
                    slovar[niz] = 1 / (kvote[niz] * vsota_kvot)
        return slovar


    ### UPANJE REZULTATA ###
def upanje(rezultat, verjetnosti, popularni):
        slovar_tock1 = {}
        upanje1 = 0
        for i in range(10):
            for j in range(10):
                napoved = str(i) + ":" + str(j)
                if verjetnosti[napoved] > 0:
                    tockice = tocke(rezultat, napoved, popularni)
                    upanje1 += verjetnosti[napoved] * tockice
                    if tockice in slovar_tock1:
                        slovar_tock1[tockice] += verjetnosti[napoved]
                    else: slovar_tock1[tockice] = verjetnosti[napoved]
        return [upanje1, slovar_tock1]


    ### TOČKE ZA NAPOVED ###
def tocke(rezultat, napoved, popularni):
        x = int(rezultat[0])
        y = int(rezultat[2])

        a = int(napoved[0])
        b = int(napoved[2])

        score = 0

        # Pravilna napoved rezultata
        if (x > y and a > b) or (x < y and a < b) or (x == y and a == b):
            score += 3

        # Stevilo golov
        if (x == a): score += 1
        if (y == b): score += 1
        if (x - y == a - b): score += 1

        # Underdog
        if (score == 6 and not (napoved in popularni)): score += 2 
        return score


    ### FUNKCIJA, KI VSE POVEZUJE ###
def vrni_napoved(seznam_popularnih_rezultatov, datoteka_kvot, matchday, prejsnji_rezultat):
        print(" ")
        start = time.perf_counter()

        # Tabela kvot
        kvote_polepsane = polepsaj_kvote(datoteka_kvot, matchday)
        kvote = kvote_polepsane[2]
    
        # Popularni rezulati, ki ne prinašajo dodatnih dveh točk
        popularni_rezultati = seznam_popularnih_rezultatov
    
        # Prva in druga ekipa (pazi vrstni red glede na kvote)
        ekipe = [kvote_polepsane[0], kvote_polepsane[1]]
    
        simulacija(verjetnosti(kvote), popularni_rezultati, ekipe, prejsnji_rezultat)

        end = time.perf_counter()
        cas = end - start

        print("Čas računanja: " + format(cas, '.3f') + " sekund")   
        print(" ")
        print("Končni rezultat:")
        print("Končne točke:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ")

