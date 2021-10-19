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
    req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    pripravi_imenik(path + stevilka + '.html')
    with open(path + stevilka + '.html', 'wb') as f:
        f.write(webpage)
        f.close()
        print('Uspešno shranjeno...' + stevilka)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pot = 'html/3/'

link01 = 'https://www.oddschecker.com/football/champions-league/besiktas-v-sporting/winner'
link02 = 'https://www.oddschecker.com/football/champions-league/club-brugge-v-man-city/winner'
link03 = 'https://www.oddschecker.com/football/champions-league/inter-milan-v-sheriff-tiraspol/winner'
link04 = 'https://www.oddschecker.com/football/champions-league/shakhtar-donetsk-v-real-madrid/winner'
link05 = 'https://www.oddschecker.com/football/champions-league/ajax-v-borussia-dortmund/winner'
link06 = 'https://www.oddschecker.com/football/champions-league/fc-porto-v-ac-milan/winner'
link07 = 'https://www.oddschecker.com/football/champions-league/atletico-madrid-v-liverpool/winner'
link08 = 'https://www.oddschecker.com/football/champions-league/psg-v-rb-leipzig/winner'

link09 = 'https://www.oddschecker.com/football/champions-league/barcelona-v-dynamo-kiev/winner'
link10 = 'https://www.oddschecker.com/football/champions-league/fc-salzburg-v-wolfsburg/winner'
link11 = 'https://www.oddschecker.com/football/champions-league/chelsea-v-malmo-ff/winner'
link12 = 'https://www.oddschecker.com/football/champions-league/zenit-st-petersburg-v-juventus/winner'
link13 = 'https://www.oddschecker.com/football/champions-league/benfica-v-bayern-munich/winner'
link14 = 'https://www.oddschecker.com/football/champions-league/lille-v-sevilla/winner'
link15 = 'https://www.oddschecker.com/football/champions-league/young-boys-v-villarreal/winner'
link16 = 'https://www.oddschecker.com/football/champions-league/man-utd-v-atalanta/winner'

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