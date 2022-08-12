#!/usr/bin/env python3
import random

LIMIT = 7
TABLE = random.randrange(1, LIMIT)

N_tests = 0
N_fail = 0
prev_fail = False

def entree():
    r = input()
    while not r.isdigit():
        if r == 'q':
            print(f'Nombre de questions {N_tests}')
            print(f'Taux de succès {(N_tests-N_fail)/N_tests}')
            import sys
            sys.exit(0)
        print("Il faut répondre avec un nombre")
        r = input()
    return int(r)


while True:
    TABLE = random.randrange(1, LIMIT+1)
    if prev_fail:
        N_fail += 1
    prev_fail = False

    N_tests += 1
    if random.choice([True, True]):

        test_value = random.randrange(0, LIMIT+1)
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
                prev_fail = True
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
                prev_fail = True
                reponse = entree()
                if TABLE * reponse == test_value:
                    print("Bravo")
