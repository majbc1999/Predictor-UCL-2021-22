from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '13'

# Tukaj napišemo popularne rezultate

sez01 = ["2:1", "1:2", "1:1", ""]
sez02 = ["2:0", "2:1", "3:1", "3:0"]


# Rezultati prvih tekem (ne dopuščamo enajstmetrovk, ki niso najbolj verjetna stvar, zanemarimo, da v 120 min pade povprečno več zadetkov kakor po 90 min)
r01 = [12, 0]
r02 = [12, 0]


# Tukaj izračuna vse

# Tekme
vrni_napoved(sez01, '01', matchday, r01)
vrni_napoved(sez02, '02', matchday, r02)