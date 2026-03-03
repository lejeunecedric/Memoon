#!/usr/bin/env python
"""Create sample content for "les Toutous" French anime series."""

import os
import sys
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cartoon_manager.settings")
sys.path.insert(0, "/home/c/Dev/Memoon")
django.setup()

from series.models import (
    Series,
    Season,
    Episode,
    Sequence,
    Shot,
    Character,
    WardrobeItem,
)


def create_sample_data():
    print("Creating 'les Toutous' series...")

    # Create Series
    series, _ = Series.objects.get_or_create(
        title="Les Toutous",
        defaults={
            "description": "Une bande de chiens rigolos vivent des aventures délirantes dans le quartier de Belleville."
        },
    )
    print(f"Series: {series}")

    # Create Characters (fun dogs)
    characters_data = [
        {
            "name": "Pépin",
            "description": "Un petit chihuahua nerveux mais courageux. Leader malgré lui du groupe.",
            "wardrobe": ["Casquette rouge", "Bandana cool", "Lunettes de soleil"],
        },
        {
            "name": "Gros Bill",
            "description": "Un golden retriever géant et gentil. Toujours affamé et un peu simplet.",
            "wardrobe": ["Bavoir géant", "T-shirt trop petit", "Casque de chantier"],
        },
        {
            "name": "Mademoiselle Froufrou",
            "description": "Un caniche élégant et snob. Expert en mode et en manipulation.",
            "wardrobe": ["Robe rose", "Collier de perles", "Chapeau à plumes"],
        },
        {
            "name": "Capitaine Moustache",
            "description": "Un vieux teckel grincheux avec une moustache impressionnante. Raconte des histoires de guerre.",
            "wardrobe": ["Béret militaire", "Médailles en chocolat", "Foulard rouge"],
        },
        {
            "name": "Zoom",
            "description": "Un border collie hyperactif qui parle trop vite. Génie de la technologie.",
            "wardrobe": [
                "Lunettes futuristes",
                "Sac à dos high-tech",
                "Chaussures lumineuses",
            ],
        },
    ]

    created_characters = {}
    for char_data in characters_data:
        character, _ = Character.objects.get_or_create(
            name=char_data["name"], defaults={"description": char_data["description"]}
        )
        character.series.add(series)

        # Create wardrobe items
        for item_name in char_data["wardrobe"]:
            WardrobeItem.objects.get_or_create(
                character=character,
                name=item_name,
                defaults={"description": f"Item signature de {character.name}"},
            )

        created_characters[char_data["name"]] = character
        print(f"Character created: {character}")

    # Create Season
    season, _ = Season.objects.get_or_create(
        series=series,
        number=1,
        defaults={
            "title": "Saison 1: Les Débuts",
            "description": "Les toutous découvrent leur quartier et leurs premières aventures.",
        },
    )
    print(f"Season: {season}")

    # Create Episodes
    episodes_data = [
        {
            "number": 1,
            "title": "La Grande Course de Saucisses",
            "description": "Les toutous organisent une course pour gagner le dîner du siècle.",
            "script": """ÉPISODE 1: LA GRANDE COURSE DE SAUCISSES

INTRO:
Pépin (VOIX OFF): "Belleville, notre quartier. Un endroit parfait... sauf quand Gros Bill a faim."

SCÈNE 1 - LE PARC
Gros Bill: "J'ai faim... J'ai TRÈS faim..."
Pépin: "Bill, tu viens de manger ton troisième sandwich!"
Gros Bill: "Oui, mais j'ai encore faim pour le dessert!"

Mademoiselle Froufrou arrive avec un magazine.

Mademoiselle Froufrou: "Mes chéris, regardez! Le Bistro du Coin organise une course de saucisses! Le gagnant mange GRATUITEMENT pendant un mois!"

Gros Bill: *yeux qui brillent* "Un... mois?"

SCÈNE 2 - L'ENTRAÎNEMENT
Montage d'entraînement comique avec Capitaine Moustache qui crie des ordres.

Capitaine Moustache: "Plus vite! Vous êtes des chiens ou des escargots?!"
Zoom: "Théoriquement, un chien peut courir à 70km/h mais avec une saucisse en bouche, la dynamique change complètement selon mes calculs-"
Pépin: "ZOOM! Concentre-toi!"

À SUIVRE...""",
            "script_author": "Marie Dupont",
            "script_status": "final",
        },
        {
            "number": 2,
            "title": "Le Mystère du Jardinier Fantôme",
            "description": "Des fleurs disparaissent mystérieusement du jardin public.",
            "script": """ÉPISODE 2: LE MYSTÈRE DU JARDINIER FANTÔME

SCÈNE 1 - LE JARDIN PUBLIC
Mademoiselle Froufrou: "C'est SCANDALEUX! Mes roses préférées ont disparu!"

Pépin: "Calme-toi Froufrou, on va résoudre ce mystère."

Zoom avec ses gadgets: "J'ai analysé les traces. Empreintes de pas... de taille 45... et des poils de... chat?!"

Tous: "UN CHAT?!"

SCÈNE 2 - L'INVESTIGATION
Les toutous espionnent le jardin la nuit.

Gros Bill: "Je vois rien, il fait trop noir."
Capitaine Moustache: "Quand j'étais jeune, on marchait 50km dans la neige sans se plaindre!"
Gros Bill: "Mais il fait pas de neige..."

Le mystère s'épaissit quand ils découvrent que le "voleur" est en fait un chat qui redonne les fleurs à des personnes âgées tristes.

FIN: Les toutous aident le chat à créer un vrai jardin communautaire.""",
            "script_author": "Jean Martin",
            "script_status": "approved",
        },
        {
            "number": 3,
            "title": "Zoom Découvre Internet",
            "description": "Zoom devient célèbre sur les réseaux sociaux, mais à quel prix?",
            "script": """ÉPISODE 3: ZOOM DÉCOUVRE INTERNET

SCÈNE 1 - LA GROTTE DE ZOOM
Zoom a installé 12 écrans.

Zoom: "Les humains ont créé quelque chose d'incroyable! On peut partager nos talents avec le MONDE ENTIER!"

Pépin: "Tu fais quoi exactement?"

Zoom montre sa chaîne: 3 millions d'abonnés.

Gros Bill: "Ça veut dire quoi 'influenceur'?"
Zoom: "Ça veut dire que quand je dis que quelque chose est cool, tout le monde veut l'acheter!"

SCÈNE 2 - LA FOLIE
Zoom devient obsédé par les likes. Il fait des vidéos ridicules.

Mademoiselle Froufrou: "Tu danses avec une pastèque sur la tête... C'est de la haute couture?"
Zoom: "J'ai 50 000 likes!"
Capitaine Moustache: "À mon époque, on avait du respect pour soi-même!"

SCÈNE 3 - LE RÉVEIL
Zoom se rend compte qu'il a négligé ses vrais amis.

Zoom: "Je suis désolé... j'ai oublié ce qui compte vraiment."
Pépin: "On est toujours là, mon pote."

FIN: Zoom continue ses vidéos mais en privé, juste pour s'amuser avec les amis.""",
            "script_author": "Sophie Bernard",
            "script_status": "review",
        },
    ]

    for ep_data in episodes_data:
        episode, created = Episode.objects.get_or_create(
            season=season,
            number=ep_data["number"],
            defaults={
                "title": ep_data["title"],
                "description": ep_data["description"],
                "script": ep_data["script"],
                "script_author": ep_data["script_author"],
                "script_status": ep_data["script_status"],
            },
        )
        print(f"Episode {'created' if created else 'exists'}: {episode}")

        # Create sample sequences and shots for first episode
        if ep_data["number"] == 1 and created:
            # Sequence 1
            seq1 = Sequence.objects.create(
                episode=episode,
                number=1,
                title="Introduction des personnages",
                description="On découvre les toutous dans le parc",
            )

            # Shots for sequence 1
            Shot.objects.create(
                sequence=seq1,
                number=1,
                script="Gros Bill regarde tristement son ventre vide",
                background="Parc de Belleville, été, après-midi ensoleillé",
                camera_angle="Plan américain sur Bill",
                camera_movement="Légère roulade vers la droite",
            )

            Shot.objects.create(
                sequence=seq1,
                number=2,
                script="Pépin arrive en courant, paniqué",
                background="Même parc, allée principale",
                camera_angle="Contre-plongée sur Pépin",
                camera_movement="Zoom rapide",
            )

            # Sequence 2
            seq2 = Sequence.objects.create(
                episode=episode,
                number=2,
                title="L'annonce de la course",
                description="Froufrou arrive avec le magazine",
            )

            Shot.objects.create(
                sequence=seq2,
                number=1,
                script="Froufrou entre en scène avec son magazine chic",
                background="Banc du parc",
                camera_angle="Plan poitrine Froufrou",
                camera_movement="Stabilisé, suivi de Froufrou",
            )

    print("\n✅ Sample data created successfully!")
    print(f"   - Series: {series.title}")
    print(f"   - {len(created_characters)} characters")
    print(f"   - Season {season.number}: {season.title}")
    print(f"   - {len(episodes_data)} episodes with scripts")
    print("\nRun ./start.sh to view in the admin interface!")


if __name__ == "__main__":
    create_sample_data()
