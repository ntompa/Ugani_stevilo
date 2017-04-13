import random

def ugani_stevilo():
    print("Pozdravljen v igrici ugibanja števil!")
    print("--------------------------------------")

    izbira = random.randint(1, 101)

    ugibanje = int(input("Katero število med 1 in 100 imam v mislih? "))

    if izbira == ugibanje:
        print("Res je! Čestitam!")
    else:
        ponovno_ugibanje = ugibanje
        while izbira != ponovno_ugibanje:
            if izbira < ponovno_ugibanje:
                print()
                print("V mislih imam manjše število.")
            else:
                print()
                print("V mislih imam večje število")
                
            ponovno_ugibanje = int(input("Katero število med 1 in 100 imam v mislih? "))
            if izbira == ponovno_ugibanje:
                print()
                print("Res je! Čestitam!")
                print()
                print("END")
                
ugani_stevilo()
