#!/usr/bin/env python3
import random

TABLE = random.randrange(1, 5)


def entree():
    r = input()
    while not r.isdigit():
        print("Il faut répondre avec un nombre")
        r = input()
    return int(r)


while True:
    TABLE = random.randrange(1, 5)

    if random.choice([True, False]):

        test_value = random.randrange(0, 11)
        print(f"{TABLE} X {test_value} = ", end="")
        # reponse = int(input())
        reponse = entree()
        first = True
        while first or reponse != test_value * TABLE:
            first = False
            if reponse == test_value * TABLE:
                print("Bravo")
            else:
                print("Essaie encore")
                reponse = entree()
                if TABLE * test_value == reponse:
                    print("Bravo")
    else:
        test_value = random.randrange(0, 11) * TABLE
        print(f"{test_value} : {TABLE} = ", end="")
        reponse = entree()
        first = True
        while first or TABLE * reponse != test_value:
            first = False
            if TABLE * reponse == test_value:
                print("Bravo")
            else:
                print("Essaie encore")
                reponse = entree()
                if TABLE * reponse == test_value:
                    print("Bravo")
