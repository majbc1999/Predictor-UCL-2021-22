from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '8'

# Tukaj napišemo popularne rezultate

sez01 = ["1:2", "1:1", "0:2", "2:1"]
sez02 = ["2:0", "3:0", "2:1", "3:1"]
sez03 = ["1:2", "1:1", "2:2", "2:1"]
sez04 = ["1:3", "1:2", "0:2", "0:3"]



# Tukaj izračuna vse

# Tekme 22.02
vrni_napoved(sez01, '01', matchday)
vrni_napoved(sez02, '02', matchday)
# Tekme 23.02
vrni_napoved(sez03, '03', matchday)
vrni_napoved(sez04, '04', matchday)


