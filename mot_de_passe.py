
def demander_mot_de_passe():
   mot_de_passe_int = 0
   while mot_de_passe_int == 0:
       mot_de_passe_str = input("Veuillez saisir votre mot de passe : ")
       try:
        mot_de_passe_int = int(mot_de_passe_str)
       except ValueError:
        print("ERREUR: Vous devez rentrer un nombre entier! Réessayez")
   return mot_de_passe_int
   
NB_ESSAIS = 4


mot_de_passe = 0
essais = NB_ESSAIS
while mot_de_passe != 1234 and essais > 0:
    print(f"Il vous reste {essais} essais")
    mot_de_passe = demander_mot_de_passe()
    if mot_de_passe == 1234:
        print("Mot de passe correct! Vous avez accès au compte")
    else:
        print("Mot de passe incorrect! Réssayez votre mot de passe")
        essais -= 1
if essais == 0:
    print("Votre compte est bloqué! Contactez un administrateur")
   