print("Monetų aparatas - pasiruošęs")

def gautiGaza(P, N, nominalai=[1, 5, 10, 25, 50, 100]):
    graza = int((P - N) * 100)
    if graza < 0:
        return None
    monetos = []
    for moneta in reversed(nominalai):
        while graza >= moneta:
            graza -= moneta
            monetos.append(moneta)
    return [monetos.count(nominalas) for nominalas in nominalai]


while True:
    try:
        print("-" * 40)
        print("Nauja prekė:")
        print("")
        P = float(input("Įveskite sumą, kurią sumokate: "))
        N = float(input("Įveskite prekės kainą: "))
        ivesti_nominalai = input("Įveskite leidžiamų nominalų sąrašą (atskirtus tarpais, bei kableliais PVZ: 1, 2, 3 ir t.t) (nieko neivedus bus naudojamas standartinis nominalų sarašas): ").strip()
        if ivesti_nominalai:
            nominalai = [int(x) for x in ivesti_nominalai.split(',')]
        else:
            nominalai = [1, 5, 10, 25, 50, 100]
        graza = gautiGaza(P, N, nominalai)
        if graza is None:
            print("-" * 40)
            print("Mokėjimas suma mažesne už prekės kainą.")
            print("-" * 40)
        else:
            print("-" * 40)
            print("Gražą: ", graza)
            print("-" * 40)
    except ValueError:
        print("*" * 40)
        print("Netinkamas įvedimas, įveskite skaičių.")
        print("*" * 40)
    except Exception as z:
        print("Įvyko klaida: ", str(z))
    pasirinkimas = input("Ar norite testi? (taip/ne): ").strip().lower()
    if pasirinkimas != 'taip':
        print("-" * 40)
        print("Programa išjungta.")
        break
