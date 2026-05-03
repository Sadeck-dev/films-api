from models import FilmPublic, Realisateur, Genre
from pydantic import HttpUrl

films_db: dict[int, FilmPublic] = {
    1: FilmPublic(
        id=1,
        titre="Inception",
        annee=2010,
        note=8.8,
        genres=[Genre.action, Genre.sf],
        realisateur=Realisateur(nom="Christopher Nolan", nationalite="britannique"),
        image_url = HttpUrl("https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg"
    )),
    2: FilmPublic(
        id=2,
        titre="Parasite",
        annee=2019,
        note=8.5,
        genres=[Genre.drame],
        realisateur=Realisateur(nom="Bong Joon-ho", nationalite="sud-coréenne"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png")
    ),
    3: FilmPublic(
        id=3,
        titre="The Dark Knight",
        annee=2008,
        note=9.0,
        genres=[Genre.action],
        realisateur=Realisateur(nom="Christopher Nolan", nationalite="britannique"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/1/1c/The_Dark_Knight_%282008_film%29.jpg")
        ),
    4: FilmPublic(
        id=4,
        titre="Interstellar",
        annee=2014,
        note=8.6,
        genres=[Genre.sf, Genre.drame],
        realisateur=Realisateur(nom="Christopher Nolan", nationalite="britannique"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")
    ),
    5: FilmPublic(
        id=5,
        titre="Get Out",
        annee=2017,
        note=7.7,
        genres=[Genre.horreur],
        realisateur=Realisateur(nom="Jordan Peele", nationalite="américaine"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/a/a1/Get_Out_poster.png")
    ),
    6: FilmPublic(
        id=6,
        titre="Intouchables",
        annee=2011,
        note=8.5,
        genres=[Genre.comedie, Genre.drame],
        realisateur=Realisateur(nom="Olivier Nakache", nationalite="française"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/4/4f/Intouchables_2011_film_poster.jpg")
    ),
    7: FilmPublic(
        id=7,
        titre="Everything Everywhere All at Once",
        annee=2022,
        note=7.8,
        genres=[Genre.action, Genre.comedie, Genre.sf],
        realisateur=Realisateur(nom="Daniel Kwan", nationalite="américaine"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/b/b4/Everything_Everywhere_All_at_Once.jpg")
    ),
    8: FilmPublic(
        id=8,
        titre="Alien",
        annee=1979,
        note=8.5,
        genres=[Genre.horreur, Genre.sf],
        realisateur=Realisateur(nom="Ridley Scott", nationalite="britannique"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_film_poster.jpg")
        ),
    9: FilmPublic(
        id=9,
        titre="Superbad",
        annee=2007,
        note=7.6,
        genres=[Genre.comedie],
        realisateur=Realisateur(nom="Greg Mottola", nationalite="américaine"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/9/97/Superbad_poster.jpg")
    ),
    10: FilmPublic(
        id=10,
        titre="Oldboy",
        annee=2003,
        note=8.1,
        genres=[Genre.action, Genre.drame],
        realisateur=Realisateur(nom="Park Chan-wook", nationalite="sud-coréenne"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/6/6d/Oldboykoreanposter.jpg")
    ),
    11: FilmPublic(
        id=11,
        titre="Hereditary",
        annee=2018,
        note=7.3,
        genres=[Genre.horreur, Genre.drame],
        realisateur=Realisateur(nom="Ari Aster", nationalite="américaine"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/5/5a/Hereditary_%28film%29.png"
    )),
    12: FilmPublic(
        id=12,
        titre="2001 : L'Odyssée de l'espace",
        annee=1968,
        note=8.3,
        genres=[Genre.sf],
        realisateur=Realisateur(nom="Stanley Kubrick", nationalite="américaine"),
        image_url= HttpUrl("https://upload.wikimedia.org/wikipedia/en/1/11/2001_A_Space_Odyssey_%281968%29.png")
    ),
}

next_id = 13