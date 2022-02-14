# Izračunamo verjetnost, da bo ena ekipa prva zadela in potem pričakovane točke

def izracunaj(kvote1, kvote2, nogoal):
    vsota = 1/float(kvote1) + 1/float(kvote2) + 1/float(nogoal)
    return( 1 / (min(float(kvote1), float(kvote2), float(nogoal)) * vsota))

print("")

kvote1 = input("Kvote 1. ekipe: ")
kvote2 = input("Kvote 2. ekipe: ")
nogoal = input("Kvote 0-0: ")

print("")
print("Pričakovane točke: " + str(izracunaj(kvote1, kvote2, nogoal)))

# Comission pri FPTS je: ~ 45%. Pričakovane točke na strelca je 2 / (kvota * 1.45)