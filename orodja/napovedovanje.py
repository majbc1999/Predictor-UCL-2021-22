from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '11'

# Tukaj napišemo popularne rezultate

sez01 = ["0:2", "1:3", "1:2", "0:3"]
sez02 = ["2:1", "2:0", "3:1", ""]
sez03 = ["1:3", "0:3", "0:2", "1:2"]
sez04 = ["1:1", "1:2", "2:1", ""]


# Rezultati prvih tekem (ne dopuščamo enajstmetrovk, ki niso najbolj verjetna stvar, zanemarimo, da v 120 min pade povprečno več zadetkov kakor po 90 min)
r01 = [20, 0]
r02 = [20, 0]
r03 = [20, 0]
r04 = [20, 0]


# Tukaj izračuna vse

# Tekme 22.02
vrni_napoved(sez01, '01', matchday, r01)
vrni_napoved(sez02, '02', matchday, r02)

# Tekme 23.02
vrni_napoved(sez03, '03', matchday, r03)
vrni_napoved(sez04, '04', matchday, r04)


