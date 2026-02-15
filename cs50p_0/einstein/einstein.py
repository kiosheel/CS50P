def main():
    masse = int(input("Saisissez une masse: "))
    print(resultat(masse))

def resultat(energie):
    energie = energie*300000000 ** 2
    return energie
main()