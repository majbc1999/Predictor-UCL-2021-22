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

    polepsan_slovar = {}

    for kljuc in slovar:
        for kl in re.finditer(vzorec_za_polepsanje_slovarja, kljuc):
            if kl['ekipa'] == ekipa1:
                izid = str(kl['golivec']) + ':' + str(kl['golimanj'])
                polepsan_slovar[izid] = float(slovar[kljuc])
            elif kl['ekipa'] == 'Draw':
                izid = str(kl['golivec']) + ':' + str(kl['golimanj'])
                polepsan_slovar[izid] = float(slovar[kljuc])
            elif kl['ekipa'] == ekipa2:
                izid = str(kl['golimanj']) + ':' + str(kl['golivec'])
                polepsan_slovar[izid] = float(slovar[kljuc])
            else: print("Napaka pri branju imen ekip")
            
    return(ekipa1, ekipa2, polepsan_slovar)
