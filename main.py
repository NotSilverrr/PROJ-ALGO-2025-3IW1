from algorithmes_tri import tri_selection, tri_insertion, tri_fusion_result, tri_rapide_result
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
from utilitaires import lire_csv, ecrire_resultats, extraire_colonne
import time

TAILLES_DE_TEST = [100, 500, 1000]

resultats_des_tests = []


def effectuer_tests_de_tri(donnees_a_trier, taille_des_donnees):
    liste_des_prix = extraire_colonne(donnees_a_trier, "prix")
    resultats_des_tests.append(f"=== TRI PAR PRIX ({taille_des_donnees} éléments) ===")
    liste_des_prix_copie = liste_des_prix.copy()
    tableau_trie, nombre_de_comparaisons, nombre_d_echanges, temps_d_execution = tri_selection(liste_des_prix_copie.copy())
    resultats_des_tests.append(f"Tri SÉLECTION par PRIX : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_d_echanges} échanges")
    tableau_trie, nombre_de_comparaisons, nombre_de_decalages, temps_d_execution = tri_insertion(liste_des_prix.copy())
    resultats_des_tests.append(f"Tri INSERTION par PRIX : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_de_decalages} décalages")
    tableau_trie, nombre_de_comparaisons, temps_d_execution = tri_fusion_result(liste_des_prix.copy())
    resultats_des_tests.append(f"Tri FUSION par PRIX : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons")
    tableau_trie, nombre_de_comparaisons, nombre_d_echanges, temps_d_execution = tri_rapide_result(liste_des_prix.copy())
    resultats_des_tests.append(f"Tri RAPIDE par PRIX : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_d_echanges} échanges")

    liste_des_surfaces = extraire_colonne(donnees_a_trier, "surface")
    resultats_des_tests.append(f"=== TRI PAR SURFACE ({taille_des_donnees} éléments) ===")
    tableau_trie, nombre_de_comparaisons, nombre_d_echanges, temps_d_execution = tri_selection(liste_des_surfaces.copy())
    resultats_des_tests.append(f"Tri SÉLECTION par SURFACE : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_d_echanges} échanges")
    tableau_trie, nombre_de_comparaisons, nombre_de_decalages, temps_d_execution = tri_insertion(liste_des_surfaces.copy())
    resultats_des_tests.append(f"Tri INSERTION par SURFACE : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_de_decalages} décalages")
    tableau_trie, nombre_de_comparaisons, temps_d_execution = tri_fusion_result(liste_des_surfaces.copy())
    resultats_des_tests.append(f"Tri FUSION par SURFACE : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons")
    tableau_trie, nombre_de_comparaisons, nombre_d_echanges, temps_d_execution = tri_rapide_result(liste_des_surfaces.copy())
    resultats_des_tests.append(f"Tri RAPIDE par SURFACE : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | {nombre_d_echanges} échanges")

def effectuer_tests_de_recherche(donnees_a_rechercher, taille_des_donnees):
    if taille_des_donnees >= 500:
        maisons_a_paris = [d for d in donnees_a_rechercher if d["type_local"] == "Maison" and d["commune"].upper() == "PARIS"]
        compteur = 0
        nombre_de_comparaisons = 0
        debut = time.time()
        for d in donnees_a_rechercher:
            nombre_de_comparaisons += 1
            if d["type_local"] == "Maison" and d["commune"].upper() == "PARIS":
                compteur += 1
        fin = time.time()
        resultats_des_tests.append(f"Recherche linéaire MAISONS PARIS : {fin-debut:.4f}s | {nombre_de_comparaisons} comparaisons | Trouvées: {compteur}")

        prix = extraire_colonne(donnees_a_rechercher, "prix")
        prix_trie, _, _ = tri_fusion_result(prix.copy())
        position, nombre_de_comparaisons, temps_d_execution = recherche_binaire(prix_trie, 350000)
        resultats_des_tests.append(f"Recherche binaire PRIX 350000€ : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | Position: {position}")

        prix_m2 = extraire_colonne(donnees_a_rechercher, "prix_m2")
        min_valeur, max_valeur, nombre_de_comparaisons, temps_d_execution = recherche_min_max(prix_m2)
        resultats_des_tests.append(f"Min/Max PRIX_M2 : {temps_d_execution:.4f}s | {nombre_de_comparaisons} comparaisons | Min: {min_valeur}€/m² | Max: {max_valeur}€/m²")

        compteur = 0
        nombre_de_comparaisons = 0
        debut = time.time()
        for d in donnees_a_rechercher:
            nombre_de_comparaisons += 1
            try:
                if d["type_local"] == "Appartement" and int(d["nb_pieces"]) == 3:
                    compteur += 1
            except:
                continue
        fin = time.time()
        resultats_des_tests.append(f"Recherche APPART 3P : {fin-debut:.4f}s | {nombre_de_comparaisons} comparaisons | Trouvés: {compteur}")

def main():
    for taille in TAILLES_DE_TEST:
        donnees = lire_csv("Transactions immobilières.csv", taille)
        effectuer_tests_de_tri(donnees, taille)

    for taille in TAILLES_DE_TEST:
        donnees = lire_csv("Transactions immobilières.csv", taille)
        if taille in [500, 1000]:
            effectuer_tests_de_recherche(donnees, taille)
            
    ecrire_resultats("resultats.txt", resultats_des_tests)

if __name__ == "__main__":
    main()
