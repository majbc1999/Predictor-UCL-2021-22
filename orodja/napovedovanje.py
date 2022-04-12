from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '12'

# Tukaj napišemo popularne rezultate

sez01 = ["2:1", "2:0", "1:1", ""]
sez02 = ["3:0", "2:0", "3:1", ""]
sez03 = ["1:2", "1:1", "0:2", "0:1"]
sez04 = ["2:0", "3:0", "2:1", "3:1"]


# Rezultati prvih tekem (ne dopuščamo enajstmetrovk, ki niso najbolj verjetna stvar, zanemarimo, da v 120 min pade povprečno več zadetkov kakor po 90 min)
r01 = [3, 1]
r02 = [0, 1]
r03 = [0, 1]
r04 = [3, 1]


# Tukaj izračuna vse

# Tekme 22.02
vrni_napoved(sez01, '01', matchday, r01)
vrni_napoved(sez02, '02', matchday, r02)

# Tekme 23.02
vrni_napoved(sez03, '03', matchday, r03)
vrni_napoved(sez04, '04', matchday, r04)


