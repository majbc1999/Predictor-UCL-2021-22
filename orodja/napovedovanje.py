from rezultat import vrni_napoved

# Tukaj nastavimo matchday
matchday = '7'

# Tukaj napišemo popularne rezultate

sez01 = ["2:1", "1:2", "1:1", ""]
sez02 = ["0:3", "1:3", "0:2", ""]
sez03 = ["1:2", "1:3", "0:2", ""]
sez04 = ["0:3", "0:4", "1:3", "1:4"]

#sez05 = ["0:3", "0:4", "1:3", "1:4"]
#sez06 = ["2:1", "2:0", "3:1", "3:0"]
#sez07 = ["1:2", "1:1", "0:2", "0:1"]
#sez08 = ["2:0", "1:1", "2:1", "1:0"]


# Tukaj izračuna vse
# Tekme 15.02
vrni_napoved(sez01, '01', matchday)
vrni_napoved(sez02, '02', matchday)
# Tekme 16.02
vrni_napoved(sez03, '03', matchday)
vrni_napoved(sez04, '04', matchday)



#vrni_napoved(sez05, '05', matchday)
#vrni_napoved(sez06, '06', matchday)
#vrni_napoved(sez07, '07', matchday)
#vrni_napoved(sez08, '08', matchday)
