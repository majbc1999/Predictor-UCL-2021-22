# Orodja za shranjevanje spletne strani
from urllib.request import Request, urlopen

def shrani_wp(link, stevilka, path):
    print('Shranjujem...' + stevilka)
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    with open(path + stevilka + '.html', 'wb') as f:
        f.write(webpage)
        f.close()
        print('Uspešno shranjeno...' + stevilka)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pot = 'html/1/'





link01 = 'https://www.oddschecker.com/football/champions-league/sevilla-v-fc-salzburg/correct-score'
link02 = 'https://www.oddschecker.com/football/champions-league/young-boys-v-man-utd/correct-score'
link03 = 'https://www.oddschecker.com/football/champions-league/barcelona-v-bayern-munich/correct-score'
link04 = 'https://www.oddschecker.com/football/champions-league/chelsea-v-zenit-st-petersburg/correct-score'
link05 = 'https://www.oddschecker.com/football/champions-league/dynamo-kiev-v-benfica/correct-score'
link06 = 'https://www.oddschecker.com/football/champions-league/lille-v-wolfsburg/correct-score'
link07 = 'https://www.oddschecker.com/football/champions-league/malmo-ff-v-juventus/correct-score'
link08 = 'https://www.oddschecker.com/football/champions-league/villarreal-v-atalanta/correct-score'
link09 = 'https://www.oddschecker.com/football/champions-league/besiktas-v-borussia-dortmund/correct-score'
link10 = 'https://www.oddschecker.com/football/champions-league/sheriff-tiraspol-v-shakhtar-donetsk/correct-score'
link11 = 'https://www.oddschecker.com/football/champions-league/atletico-madrid-v-fc-porto/correct-score'
link12 = 'https://www.oddschecker.com/football/champions-league/club-brugge-v-psg/correct-score'
link13 = 'https://www.oddschecker.com/football/champions-league/inter-milan-v-real-madrid/correct-score'
link14 = 'https://www.oddschecker.com/football/champions-league/liverpool-v-ac-milan/correct-score'
link15 = 'https://www.oddschecker.com/football/champions-league/man-city-v-rb-leipzig/correct-score'
link16 = 'https://www.oddschecker.com/football/champions-league/sporting-v-ajax/correct-score'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tukaj shrani strani
#shrani_wp(link01, '01', pot)
#shrani_wp(link02, '02', pot)
shrani_wp(link03, '03', pot)
#shrani_wp(link04, '04', pot)
#shrani_wp(link05, '05', pot)
#shrani_wp(link06, '06', pot)
#shrani_wp(link07, '07', pot)
#shrani_wp(link08, '08', pot)
#shrani_wp(link09, '09', pot)
#shrani_wp(link10, '10', pot)
#shrani_wp(link11, '11', pot)
#shrani_wp(link12, '12', pot)
#shrani_wp(link13, '13', pot)
#shrani_wp(link14, '14', pot)
#shrani_wp(link15, '15', pot)
#shrani_wp(link16, '16', pot)
