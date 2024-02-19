from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Squelette du menu principal :
# Ce code peut être un bon point de départ.
# Il est possible de le modifier à votre guise ou de l'enlever complètement pour partir de zéro.




#USERNAME LOOP
while True: #infinite loop, while this is always true it will output the following
    
    nom_utilisateur = (input("Entrez votre nom d'utilisateur: "))
    if len(nom_utilisateur) >= 3  and nom_utilisateur.isalpha():
        print(f"Bienvenue, {nom_utilisateur}!\n\n\n"
        "Menu principal \n"
        "1. Commencer une partie \n"
        "2. Afficher l'historique \n"
        "3. Quitter \n")

            
        break
    else:
        print("Error, veuillez reentrez votre USERANME containing at least 3 letters and has to be words not numbers") 
        
# CHOIX LOOP
while True:        
        
    choix = input("Entrez votre choix: ")
    if choix.isdigit(): #si choix is a number then convert to int
        choix_menu_principal =int(choix)
        
        #CHOIX 3 : QUITTER 
        if choix_menu_principal == 3:
            clear_screen()
            print(f"Merci davoir joue {nom_utilisateur}!")
            
            break #break the USERNAME LOOP, exit the program, if i add a new while loop, itll break the choix loop and go back to USERNAME LOOP
        
        #CHOIX 1 : COMMENCER UNE PARTIE
        elif choix_menu_principal == 1:
            
            # GAME LOOP
            while True:
                clear_screen()

                # CHOIX = 1 : Demander à l'utilisateur de choisir une difficulté,
                print("Choisissez une difficulte: \n"
                                            "1. Facile \n"
                                            "2. Intermediaire \n"
                                            "3. Difficile \n")
                difficulte_selector = (input("Entrez votre choix: "))
                
                if difficulte_selector.isdigit():
                    difficulte_selector = int(difficulte_selector)
                    difficulte_mapping = {1: "facile", 2: "intermediaire", 3: "difficile"}
                    mots = lire_dictionnaires_mots()
                    
                # sélectionner un mot aléatoire
                    if difficulte_selector in difficulte_mapping:
                        difficulte = difficulte_mapping[difficulte_selector]
                        if difficulte in mots:
                            randomWord = random.choice(mots[difficulte])
                            print(f"mot selon difficulte: {randomWord}")  # temporary
                
                    
                ### COMMENCER LA PARTIE ###
                    #lives = hangman figure (1X HEAD, 2X ARMS, 1X TORSO , 2X LEGS)
                        lives = 6
                    #word count
                        mot_cache = ["_" for _ in randomWord]
                        lettre_trouvee = [] #need to b initialized outside while loop while "_" in mot_cache: or else everytime we write, it overwrites the appended letter we found previously to empty []
                        lettre_ratee = []
                    #Input lettre

                        while "_" in mot_cache and lives >0:
                            clear_screen()
                            print("Mot: " + " ".join(mot_cache))
                            print("Lettres trouvees: "+ " ".join(lettre_trouvee))    
                            print("Lettres ratees: "+ " ".join(lettre_ratee))
                            print("lives" + str(lives))
                            print(randomWord) # temporary
                            
                    
                            
                            lettre = input("Entrez une lettre: ").lower()
                        
                    #reveal le mot cache if guessed letter right (CORRECTE)
                            while not lettre.isalpha() or len(lettre) != 1: #tant que lettre nest pas une lettre or lettre nest pas len de 1, loop of vous devez entre 1 seul lettre continues.
                                print("Vous devez entrer une seule lettre.")
                                lettre = input("Entrez une lettre: ").lower()
                                continue
                            while lettre in lettre_trouvee or lettre in lettre_ratee: #while loop needed, cuz we want the loop to go on if the user inputs something thats not a letter everytime
                                print("Vous avez deja entree cette lettre")
                                lettre = input("Entrez une lettre: ").lower()
                            if lettre in randomWord:
                                lettre_trouvee.append(lettre)
                                for i, char in enumerate(randomWord):
                                    if char == lettre:
                                        mot_cache[i] = lettre
                                        
                        #si la lettre saisie est INCORRECTE         
                            elif lettre not in lettre_ratee and not lettre.isdigit(): # affect slm si c new lettre qui est ratee, sinn no drop hp
                                lives -= 1
                                lettre_ratee.append(lettre)
                                continue    
                                    
                                
                        #lost            
                        if lives <=0:
                            print(f"gg, le mot etait:  {randomWord}")
                            input("Appuyez sur Enter pour continuer...")
                            clear_screen()
                            print("Menu principal \n"
                                "1. Commencer une partie \n"
                                "2. Afficher l'historique \n"
                                "3. Quitter \n")
                            break 
                        
                        #won
                        elif "_" not in mot_cache and lives >0:
                            print("u won")    
                            input("Appuyez sur Enter pour continuer...")
                            clear_screen()
                            print("Menu principal \n"
                                "1. Commencer une partie \n"
                                "2. Afficher l'historique \n"
                                "3. Quitter \n")
                            
                            break # break this loop to go back to menu
                            
                else:   
                    print("Choix invalide, veuillez reessayer\n")
                continue
                
            
        elif choix_menu_principal == 2:
            # MENU Afficher l'historique de l'utilisateur.
            print("2")
        
        else:
            # MENU Afficher un message d'entrée invalide.  
            print("Choix invalide, veuillez reessayer\n")
            
    # MENU if not digit    
    else:
        print("Choix invalide, veuillez reessayer\n")
        