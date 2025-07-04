import time

def tri_selection(tableau):
    tab = tableau
    n = len(tab)
    echanges = 0
    comps = 0
    start = time.time()
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j
            comps += 1
        if min_idx != i:
            temp = tab[i]
            tab[i] = tab[min_idx]
            tab[min_idx] = temp
            echanges += 1
    end = time.time()
    timer = end - start
    return tab, comps, echanges, timer

def tri_insertion(tableau):
    tab = tableau
    n = len(tab)
    echanges = 0
    comps = 0
    start = time.time()
    for i in range(1, n):
        print(tab)
        element_a_inserer = tab[i]
        j = i-1
        while j>=0 and tab[j] > element_a_inserer:
            comps += 1
            tab[j+1] = tab[j]
            echanges += 1
            j -= 1
        tab[j+1] = element_a_inserer
    end = time.time()
    timer = end - start
    return tab, comps, echanges, timer

def fusionner(gauche, droite):
    resultat = []
    i = 0
    j = 0
    comparaisons = 0
    while i < len(gauche) and j < len(droite):
        comparaisons += 1
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat, comparaisons

def tri_fusion(tableau):
    if len(tableau) <= 1:
        return list(tableau), 0
    milieu = len(tableau) // 2
    gauche = tableau[:milieu]
    droite = tableau[milieu:]
    gauche_trie, comps_gauche = tri_fusion(gauche)
    droite_trie, comps_droite = tri_fusion(droite)
    fusionne, comps_fusion = fusionner(gauche_trie, droite_trie)
    return fusionne, comps_gauche + comps_droite + comps_fusion

def tri_fusion_result(tableau):
    start = time.time()
    resultat, nb_comparaisons = tri_fusion(tableau)
    end = time.time()
    timer = end - start
    return resultat, nb_comparaisons, timer
    
def partitionner(tab, debut, fin):
    pivot = tab[fin]
    i = debut - 1
    comparaisons = 0
    for j in range(debut, fin):
        comparaisons += 1
        if tab[j] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[fin] = tab[fin], tab[i+1]
    return i + 1, comparaisons

def tri_rapide(tableau, debut=0, fin=None):
    if fin is None:
        fin = len(tableau) - 1
        tableau = list(tableau)
    comparaisons = 0
    if debut < fin:
        position_pivot, comps = partitionner(tableau, debut, fin)
        comparaisons += comps
        _, comps_left = tri_rapide(tableau, debut, position_pivot - 1)
        comparaisons += comps_left
        _, comps_right = tri_rapide(tableau, position_pivot + 1, fin)
        comparaisons += comps_right
    return tableau, comparaisons

def tri_rapide_result(tableau):
    start = time.time()
    resultat, nb_comparaisons = tri_rapide(tableau)
    end = time.time()
    timer = end - start
    return resultat, nb_comparaisons, timer

