import time

def recherche_lineaire(tableau, search):
    start = time.time()
    count = 0
    for i in range(len(tableau)):
        count += 1
        if tableau[i] == search:
            end = time.time()
            timer = end - start
            return i, count, timer
    end = time.time()
    timer = end - start
    return False

def recherche_binaire(tableau, search, debut=0, fin=None, comparaisons=0, start_time=None):
    if start_time is None:
        start_time = time.time()
    if fin is None:
        fin = len(tableau) - 1
    if debut > fin:
        end_time = time.time()
        return (-1, comparaisons, end_time - start_time)
    
    mid = (debut + fin) // 2
    comparaisons += 1

    if tableau[mid] == search:
        end_time = time.time()
        return (mid, comparaisons, end_time - start_time)
    elif search > tableau[mid]:
        return recherche_binaire(tableau, search, mid + 1, fin, comparaisons, start_time)
    else:
        return recherche_binaire(tableau, search, debut, mid - 1, comparaisons, start_time)
    
def recherche_min_max(tableau):
    if len(tableau) < 1:
        return False
    start = time.time()

    if len(tableau) == 1:
        end = time.time()
        return (tableau[0], tableau[0],1,end-start)
    min_val = tableau[0]
    max_val = tableau[0]
    count = 0

    for i in range(len(tableau)):
        count += 1
        if tableau[i] > max_val:
            max_val = tableau[i]
        elif tableau[i] < min_val:
            min_val = tableau[i]
    end = time.time()
    return (min_val, max_val, count, end-start)

