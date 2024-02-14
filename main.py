from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Squelette du menu principal :
# Ce code peut être un bon point de départ.
# Il est possible de le modifier à votre guise ou de l'enlever complètement pour partir de zéro.
while True: #infinite loop, while this is always true it will output the following
    
    #USERNAME
    nom_utilisateur = (input("Entrez votre nom d'utilisateur: "))
    if len(nom_utilisateur) >= 3  and nom_utilisateur.isalpha():
        print(f"Bienvenue, {nom_utilisateur}!\n\n\n"
            "Menu principal \n"
            "1. Commencer une partie \n"
            "2. Afficher l'historique \n"
            "3. Quitter \n")
        
        #CHOIX
        choix = input("Entrez votre choix: ")
        if choix.isdigit(): #si choix is a number then convert to int
            choix_menu_principal =int(choix) 
            if choix_menu_principal == 1:
                clear_screen()
                
                # Demander à l'utilisateur de choisir une difficulté,
                print("Choisissez une difficulte: \n"
                                            "1. Facile \n"
                                            "2. Intermediaire \n"
                                            "3. Difficile \n")
                difficulte_selector = int(input("Entrez votre choix: "))
                mots = lire_dictionnaires_mots()
                difficulte_mapping = {1:"facile",2:"intermediaire",3:"difficile"}
                # sélectionner un mot aléatoire
                if difficulte_selector in difficulte_mapping:
                    difficulte = difficulte_mapping[difficulte_selector]
                    if difficulte in mots:
                        randomWord = random.choice(mots[difficulte])
                        print(f"mot selon difficulte: {randomWord}")  # temporary
                else:
                    print("Choix invalide, veuillez reessayer\n")
                # et commencer la partie.
                
                
            elif choix_menu_principal == 2:
                # Afficher l'historique de l'utilisateur.
                print("2")
            elif choix_menu_principal == 3:
                # Quitter le programme.
                print("3")

            else:
                # Afficher un message d'entrée invalide.
                print("Choix invalide, veuillez reessayer\n")
        else:
            print("Choix invalide, veuillez reessayer\n")
        break
    else:
        print("Error, veuillez reentrez votre USERANME containing at least 3 letters and has to be words not numbers")