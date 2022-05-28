from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '15'

# Tukaj napišemo popularne rezultate

sez01 = ["1:2", "2:1", "2:3", "1:3"]


# Rezultati prvih tekem (ne dopuščamo enajstmetrovk, ki niso najbolj verjetna stvar, zanemarimo, da v 120 min pade povprečno več zadetkov kakor po 90 min)
r01 = [0, 15]


# Tukaj izračuna vse

# Tekme
vrni_napoved(sez01, '01', matchday, r01)