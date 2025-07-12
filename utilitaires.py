def lire_csv(chemin, nombre_elements=None):
    donnees = []
    with open(chemin, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
    entetes = lignes[0].strip().split(',')
    for ligne in lignes[1:]:
        if nombre_elements is not None and len(donnees) >= nombre_elements:
            break
        champs = ligne.strip().split(',')
        if len(champs) != len(entetes):
            continue
        d = {entetes[i]: champs[i] for i in range(len(entetes))}
        donnees.append(d)
    return donnees

def ecrire_resultats(chemin, lignes):
    with open(chemin, 'w', encoding='utf-8') as fichier:
        for ligne in lignes:
            fichier.write(ligne + '\n')

def extraire_colonne(donnees, colonne):
    resultat = []
    for d in donnees:
        try:
            resultat.append(float(d[colonne]))
        except:
            resultat.append(0)
    return resultat