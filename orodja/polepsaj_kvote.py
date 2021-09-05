from vrni_kvote_iz_html import vrni_kvote_iz_html
import re

def polepsaj_kvote(datoteka):
    kvote = vrni_kvote_iz_html(datoteka)
    ekipa1 = kvote[0]
    ekipa2 = kvote[1]
    slovar = kvote[2]

    vzorec_za_polepsanje_slovarja = re.compile(
        r'(?P<ekipa>[a-zA-Z\s]*?)'
        r' '
        r'(?P<golivec>\d*?)'
        r'-'
        r'(?P<golimanj>\d*)',
        flags=re.DOTALL)

    print(slovar)
    polepsan_slovar = {}
    for kljuc in slovar:
        for kl in re.finditer(vzorec_za_polepsanje_slovarja, kljuc):
            if kl['ekipa'] == ekipa1:
                print(ekipa1)
                izid = str(kl['golivec']) + '-' + str(kl['golimanj'])
                print(izid)
                polepsan_slovar[izid] = slovar[kljuc]
            elif kl['ekipa'] == 'Draw':
                print('remi')
                izid = str(kl['golivec']) + '-' + str(kl['golimanj'])
                print(izid)
                polepsan_slovar[izid] = slovar[kljuc]
            elif kl['ekipa'] == ekipa2:
                print(ekipa2)
                izid = str(kl['golimanj']) + '-' + str(kl['golivec'])
                print(izid)
                polepsan_slovar[izid] = slovar[kljuc]
            else: print("Napaka pri branju imen ekip")
    return(polepsan_slovar)
