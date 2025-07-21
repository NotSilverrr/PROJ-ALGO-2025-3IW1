from algorithmes_tri import tri_selection, tri_insertion, tri_fusion_result, tri_rapide_result
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
from utilitaires import lire_csv, ecrire_resultats, extraire_colonne
import time

LISTE_TAILLES = [100, 500, 1000]

journal_resultats = []

def main():
    for taille_actuelle in LISTE_TAILLES:
        donnees_chargees = lire_csv("Transactions immobilières.csv", taille_actuelle)
        realiser_tests_tri(donnees_chargees, taille_actuelle)

    for taille_actuelle in LISTE_TAILLES:
        donnees_chargees = lire_csv("Transactions immobilières.csv", taille_actuelle)
        if taille_actuelle in [500, 1000]:
            realiser_tests_recherche(donnees_chargees, taille_actuelle)
            
    ecrire_resultats("resultats.txt", journal_resultats)

def realiser_tests_tri(tab_donnees, nb_elements):
    colonne_prix = extraire_colonne(tab_donnees, "prix")
    journal_resultats.append(f"=== TRI PAR PRIX ({nb_elements} éléments) ===")
    copie_prix = colonne_prix.copy()
    resultat_tri, total_comparaisons, total_echanges, duree = tri_selection(copie_prix.copy())
    journal_resultats.append(f"Tri SÉLECTION par PRIX : {duree:.4f}s | {total_comparaisons} comparaisons | {total_echanges} échanges")
    resultat_tri, total_comparaisons, total_decalages, duree = tri_insertion(colonne_prix.copy())
    journal_resultats.append(f"Tri INSERTION par PRIX : {duree:.4f}s | {total_comparaisons} comparaisons | {total_decalages} décalages")
    resultat_tri, total_comparaisons, duree = tri_fusion_result(colonne_prix.copy())
    journal_resultats.append(f"Tri FUSION par PRIX : {duree:.4f}s | {total_comparaisons} comparaisons")
    resultat_tri, total_comparaisons, total_echanges, duree = tri_rapide_result(colonne_prix.copy())
    journal_resultats.append(f"Tri RAPIDE par PRIX : {duree:.4f}s | {total_comparaisons} comparaisons | {total_echanges} échanges")

    colonne_surface = extraire_colonne(tab_donnees, "surface")
    journal_resultats.append(f"=== TRI PAR SURFACE ({nb_elements} éléments) ===")
    resultat_tri, total_comparaisons, total_echanges, duree = tri_selection(colonne_surface.copy())
    journal_resultats.append(f"Tri SÉLECTION par SURFACE : {duree:.4f}s | {total_comparaisons} comparaisons | {total_echanges} échanges")
    resultat_tri, total_comparaisons, total_decalages, duree = tri_insertion(colonne_surface.copy())
    journal_resultats.append(f"Tri INSERTION par SURFACE : {duree:.4f}s | {total_comparaisons} comparaisons | {total_decalages} décalages")
    resultat_tri, total_comparaisons, duree = tri_fusion_result(colonne_surface.copy())
    journal_resultats.append(f"Tri FUSION par SURFACE : {duree:.4f}s | {total_comparaisons} comparaisons")
    resultat_tri, total_comparaisons, total_echanges, duree = tri_rapide_result(colonne_surface.copy())
    journal_resultats.append(f"Tri RAPIDE par SURFACE : {duree:.4f}s | {total_comparaisons} comparaisons | {total_echanges} échanges")

def realiser_tests_recherche(tab_recherche, taille_recherche):
    if taille_recherche >= 500:
        liste_maisons_paris = [elem for elem in tab_recherche if elem["type_local"] == "Maison" and elem["commune"].upper() == "PARIS"]
        compteur_maisons = 0
        nb_comparaisons_maisons = 0
        t_debut = time.time()
        for elem in tab_recherche:
            nb_comparaisons_maisons += 1
            if elem["type_local"] == "Maison" and elem["commune"].upper() == "PARIS":
                compteur_maisons += 1
        t_fin = time.time()
        journal_resultats.append(f"Recherche linéaire MAISONS PARIS : {t_fin-t_debut:.4f}s | {nb_comparaisons_maisons} comparaisons | Trouvées: {compteur_maisons}")

        colonne_prix_recherche = extraire_colonne(tab_recherche, "prix")
        prix_tries, _, _ = tri_fusion_result(colonne_prix_recherche.copy())
        position_prix, nb_comp_prix, t_exec_prix = recherche_binaire(prix_tries, 350000)
        journal_resultats.append(f"Recherche binaire PRIX 350000€ : {t_exec_prix:.4f}s | {nb_comp_prix} comparaisons | Position: {position_prix}")

        colonne_prix_m2 = extraire_colonne(tab_recherche, "prix_m2")
        min_m2, max_m2, nb_comp_m2, t_exec_m2 = recherche_min_max(colonne_prix_m2)
        journal_resultats.append(f"Min/Max PRIX_M2 : {t_exec_m2:.4f}s | {nb_comp_m2} comparaisons | Min: {min_m2}€/m² | Max: {max_m2}€/m²")

        compteur_appart = 0
        nb_comp_appart = 0
        t_debut = time.time()
        for elem in tab_recherche:
            nb_comp_appart += 1
            try:
                if elem["type_local"] == "Appartement" and int(elem["nb_pieces"]) == 3:
                    compteur_appart += 1
            except:
                continue
        t_fin = time.time()
        journal_resultats.append(f"Recherche APPART 3P : {t_fin-t_debut:.4f}s | {nb_comp_appart} comparaisons | Trouvés: {compteur_appart}")



main()