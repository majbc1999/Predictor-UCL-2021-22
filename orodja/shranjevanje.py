# Orodja za shranjevanje spletne strani
from urllib.request import Request, urlopen
import os

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def shrani_wp(link, stevilka, path):
    print('Shranjujem...' + stevilka)
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    pripravi_imenik(path + stevilka + '.html')
    with open(path + stevilka + '.html', 'wb') as f:
        f.write(webpage)
        f.close()
        print('Uspešno shranjeno...' + stevilka)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pot = 'html/2/'



link01 = 'https://www.oddschecker.com/football/champions-league/shakhtar-donetsk-v-inter-milan/correct-score'
link02 = 'https://www.oddschecker.com/football/champions-league/ajax-v-besiktas/correct-score'
link03 = 'https://www.oddschecker.com/football/champions-league/borussia-dortmund-v-sporting/correct-score'
link04 = 'https://www.oddschecker.com/football/champions-league/psg-v-man-city/correct-score'
link05 = 'https://www.oddschecker.com/football/champions-league/fc-porto-v-liverpool/correct-score'
link06 = 'https://www.oddschecker.com/football/champions-league/real-madrid-v-sheriff-tiraspol/correct-score'
link07 = 'https://www.oddschecker.com/football/champions-league/rb-leipzig-v-club-brugge/correct-score'
link08 = 'https://www.oddschecker.com/football/champions-league/ac-milan-v-atletico-madrid/correct-score'

link09 = 'https://www.oddschecker.com/football/champions-league/zenit-st-petersburg-v-malmo-ff/correct-score'
link10 = 'https://www.oddschecker.com/football/champions-league/atalanta-v-young-boys/correct-score'
link11 = 'https://www.oddschecker.com/football/champions-league/juventus-v-chelsea/correct-score'
link12 = 'https://www.oddschecker.com/football/champions-league/man-utd-v-villarreal/correct-score'
link13 = 'https://www.oddschecker.com/football/champions-league/bayern-munich-v-dynamo-kiev/correct-score'
link14 = 'https://www.oddschecker.com/football/champions-league/benfica-v-barcelona/correct-score'
link15 = 'https://www.oddschecker.com/football/champions-league/wolfsburg-v-sevilla/correct-score'
link16 = 'https://www.oddschecker.com/football/champions-league/fc-salzburg-v-lille/correct-score'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tukaj shrani strani

shrani_wp(link01, '01', pot)
shrani_wp(link02, '02', pot)
shrani_wp(link03, '03', pot)
shrani_wp(link04, '04', pot)
shrani_wp(link05, '05', pot)
shrani_wp(link06, '06', pot)
shrani_wp(link07, '07', pot)
shrani_wp(link08, '08', pot)

shrani_wp(link09, '09', pot)
shrani_wp(link10, '10', pot)
shrani_wp(link11, '11', pot)
shrani_wp(link12, '12', pot)
shrani_wp(link13, '13', pot)
shrani_wp(link14, '14', pot)
shrani_wp(link15, '15', pot)
shrani_wp(link16, '16', pot)
