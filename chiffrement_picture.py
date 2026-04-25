from PIL import Image
import os

def traiter_image(chemin, cle):
    if not os.path.exists(chemin):
        print("Erreur : Le fichier image est introuvable.")
        return

    img = Image.open(chemin)
    # On convertit en RGB pour s'assurer que le script fonctionne avec tous les formats
    img = img.convert("RGB")
    pixels = img.load()
    largeur, hauteur = img.size

    for x in range(largeur):
        for y in range(hauteur):
            r, v, b = pixels[x, y]
            # Manipulation par XOR (réversible avec la même clé)
            pixels[x, y] = (r ^ cle, v ^ cle, b ^ cle)

    nom_final = "resultat.png"
    img.save(nom_final)
    print(f"Opération terminée ! Image sauvegardée sous : {nom_final}")

# Interface simple
chemin_image = input("Glissez l'image ici ou tapez son nom : ").strip('"')
cle_utilisateur = int(input("Entrez une clé numérique (ex: 123) : "))

traiter_image(chemin_image, cle_utilisateur)
