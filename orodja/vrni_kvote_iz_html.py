import re
from orodja import vsebina_datoteke, convert_to_float

def vrni_kvote_iz_html(datoteka, matchday):
    tekma = vsebina_datoteke('html/' + matchday + '/' + datoteka + '.html')

    vzorec_za_rezulat = re.compile(
        r'<span class="float-wrap name-wrap"><span class="tcell"><div class="top-row"><a class="popup selTxt" target="_blank" title="View odds history for .*?" '
        r'href=".*?" data-name=".*?">'
        r'(?P<ekipa_rezultat>.*?)'
        r'</a></div></span></span></td>.*?<td class="bc bs o.*?(\n)?.*?" data-bk="B3" data-odig=".*?" data-o=".*?" data-hcap=".*?" data-fodds=".*?" data-best-ew=".*?" data-best-wo=".*?"><p>'
        r'(?P<kvote>.*?)'
        r'</p></td>',
        flags=re.DOTALL)

    vzorec_za_rezulat2 = re.compile(
        r'<p class="body-text-3 MarketExpanderBetName_m1m6ixsu">'
        r'(?P<goli1>\d*?)'
        r'-'
        r'(?P<goli2>\d*?)'
        r'</p>(.*?)<button type="button" class="button_b1oycxy6">'
        r'(?P<kvote>.*?)'
        r'</button>'
    )

    vzorec_za_rezulat3 = re.compile(
        r';">'
        r'(?P<goli1>\d+?)'
        r'-'
        r'(?P<goli2>\d+?)'
        r'</p>(.*?)<button type="button" class="button_b1oycxy6">'
        r'(?P<kvote>.*?)'
        r'</button>'
    )

    #vzorec_za_rezultat_vscode = <span class="float-wrap name-wrap"><span class="tcell"><div class="top-row"><a class="popup selTxt" target="_blank" title="View odds history for .*?" href=".*?" data-name=".*?".*?</a></div></span></span></td>.*?<td class="bc bs o.*?(\n)?.*?" data-bk="B3" data-odig=".*?" data-o=".*?" data-hcap=".*?" data-fodds=".*?" data-best-ew=".*?" data-best-wo=".*?"><p>.*?</p></td>"
    #vzorec2 = <p class="body-text-3 MarketExpanderBetName_m1m6ixsu">((\d*?)-(\d*?))</p>(.*?)<button type="button" class="button_b1oycxy6">(.*?)</button>
    #vzorec3 = ;">((\d+?)-(\d+?))</p>(.*?)<button type="button" class="button_b1oycxy6">


    vzorec_za_ekipe = re.compile(
        r'</style><title>'
        r'(?P<domaca_ekipa>[a-zA-Z\s]*?)'
        r' v '
        r'(?P<gostujoca_ekipa>[a-zA-Z\s]*?)'
        r' Correct Score',
        flags=re.DOTALL)

    vzorec_za_ekipe2 = re.compile(
        r'<title>'
        r'(?P<domaca_ekipa>[a-zA-Z\s]*?)'
        r' vs '
        r'(?P<gostujoca_ekipa>[a-zA-Z\s]*?)' 
        r'Betting Odds'
    )


    slovar = {}
    obrni = False

    #for razplet in re.finditer(vzorec_za_rezulat, tekma):
    #        rezultat = razplet['ekipa_rezultat']
    #        kvote = convert_to_float(razplet['kvote'])
    #        slovar[rezultat] = kvote

    i = 0

    for razplet in re.finditer(vzorec_za_rezulat3, tekma):
            if (razplet['goli1'] + ':' + razplet['goli2']) in slovar:
                obrni = True
            if obrni:
                rezultat = razplet['goli2'] + ':' + razplet['goli1']
            else:
                rezultat = razplet['goli1'] + ':' + razplet['goli2']
                
            kvote = convert_to_float(razplet['kvote'])

            slovar[rezultat] = kvote
            i = i+1

    #for ekipa in re.finditer(vzorec_za_ekipe, tekma):
    #    domaca_ekipa = ekipa['domaca_ekipa']
    #    gostujoca_ekipa = ekipa['gostujoca_ekipa']

    for ekipa in re.finditer(vzorec_za_ekipe2, tekma):
        domaca_ekipa = ekipa['domaca_ekipa']
        gostujoca_ekipa = ekipa['gostujoca_ekipa']

    return([domaca_ekipa, gostujoca_ekipa, slovar])

#print(vrni_kvote_iz_html('01', '8'))