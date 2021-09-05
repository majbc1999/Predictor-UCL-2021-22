############################################################################################################################################################

#                                                        * * * PREDICTOR UCL 2021 / 2022 * * *                                                             #
#                                                                Maj Gaberšček,  Bovec                                                                     #
############################################################################################################################################################

from polepsaj_kvote import polepsaj_kvote

def vrni_napoved(datoteka_kvot, datoteka_popular_prediction=None):
    # Tabela kvot
    kvote_polepsane = polepsaj_kvote(datoteka_kvot)
    kvote = kvote_polepsane[2]

    # Popularni rezulati, ki ne prinašajo dodatnih dveh točk
    popularni_rezultati = [
        "2:1",
        "1:2",
        "",
        "" 
    ]

    # Prva in druga ekipa (pazi vrstni red glede na kvote)
    ekipe = [kvote_polepsane[0], kvote_polepsane[1]]


    ############################################################################################################################################################

    #                                                     * * * TUKAJ NAPREJ JE KODA, NE TIKAJ * * *                                                           #

    ############################################################################################################################################################


    ### NAJBOLJŠA NAPOVED ###

    def simulacija(verjetnosti, popularni, ekipe):
        #print("--------------------------------------------------------------------")
        #print("Slovar verjetnosti")
        #print(verjetnosti)
        print("--------------------------------------------------------------------")
        najboljsa_napoved = "0:0"
        upanje1 = 0
        upanje_trenutno = 0
        for i in range(6):
            for j in range(6):
                rezultat = str(i) + ":" + str(j)
                upanje_trenutno = upanje(rezultat, verjetnosti, popularni)
                if upanje_trenutno >= upanje1:
                    upanje1 = upanje_trenutno
                    najboljsa_napoved = rezultat

        print("Najboljša napoved je: " + ekipe[0] + " " + najboljsa_napoved + " " + ekipe[1] + ". Pričakovane točke = " + str(round(upanje1, 2)))
        print("--------------------------------------------------------------------")



    ### SLOVAR VERJETNOSTI REZULTATA ###

    def verjetnosti(kvote):
        vsota_kvot = 0
        slovar = {}
        for i in range(6):
            for j in range(6):
                niz = str(i) + ":" + str(j)
                if niz not in kvote.keys():
                    continue
                if kvote[niz] != 0:
                    vsota_kvot += (1 / kvote[niz])
        for i in range(6):
            for j in range(6):
                niz = str(i) + ":" + str(j)
                if (niz not in kvote.keys()): slovar[niz] = 0
                elif kvote[niz] == 0: slovar[niz] = 0
                else:
                    slovar[niz] = 1 / (kvote[niz] * vsota_kvot)
        return slovar



    ### UPANJE REZULTATA ###
    def upanje(rezultat, verjetnosti, popularni):
        upanje1 = 0
        for i in range(6):
            for j in range(6):
                napoved = str(i) + ":" + str(j)
                if verjetnosti[napoved] > 0:
                    upanje1 += verjetnosti[napoved] * tocke(rezultat, napoved, popularni)
        return upanje1



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


    return(simulacija(verjetnosti(kvote), popularni_rezultati, ekipe))