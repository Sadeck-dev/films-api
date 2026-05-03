from fastapi import APIRouter, status, HTTPException, Query, Path
from typing import Annotated
from models import FilmPublic, FilmUpdate, FilmCreate, Genre, FilmBase
import data as db

film_router = APIRouter(prefix = '/films')

@film_router.get('/films', status_code = status.HTTP_200_OK, response_model = list[FilmPublic])
async def get_all_films(
    annee_min: Annotated[int | None, Query(description = "Filtrer par annee minimum")] = None,
    genre: Annotated[Genre | None, Query(description = "Filtrer par genre")] = None,
    annee_max: Annotated[int | None, Query(description = "Filtrer par maximum")] = None,
    note_min: Annotated[float | None, Query(description = "Filtrer par note minimal")] = 0.0,
    limit: Annotated[int, Query(ge = 1, le = 100)] = 20,
    offset: Annotated[int, Query(ge = 0)] = 0
):
    resultats = list(db.films_db.values())
    if genre:
        resultats = [film for film in resultats if genre in film.genres]
    if annee_min:
        resultats = [film for film in resultats if film.annee >= annee_min]
    if annee_max:
        resultats = [film for film in resultats if film.annee <= annee_max]
    if note_min:
        resultats = [film for film in resultats if film.note >= note_min]
        
    return resultats[offset: offset + limit]

@film_router.get('/films/{film_id}', response_model = FilmPublic, status_code = status.HTTP_200_OK)
async def get_a_film(film_id: int = Path(ge = 1)):
    if film_id not in db.films_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = f"Film {film_id} introuvable."
        )
    return db.films_db[film_id]

@film_router.post('/films', status_code = status.HTTP_201_CREATED, response_model = FilmPublic)
async def create_a_film(film: FilmCreate):
    new_film = FilmPublic(id = db.next_id, **film.model_dump())
    db.films_db[db.next_id] = new_film
    db.next_id += 1
    return new_film

@film_router.put('/films/{film_id}', status_code = status.HTTP_200_OK, response_model = FilmPublic)
async def put_a_film(film: FilmBase, film_id: int = Path(ge = 1)):
    update_film = FilmPublic(id = film_id, **film.model_dump())
    db.films_db[film_id] = update_film
    return update_film

@film_router.patch('/films/{film_id}', status_code = status.HTTP_200_OK, response_model = FilmPublic)
async def patch_a_film(film_id: int, film: FilmUpdate):
    if film_id not in db.films_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = f"Film {film_id} introuvable."
        )
        
    film_existant = db.films_db[film_id]
    champs_a_modifier = film.model_dump(exclude_unset = True)
    film_mis_a_jour = film_existant.model_copy(update = champs_a_modifier)
    db.films_db[film_id] = film_mis_a_jour
    
    return film_mis_a_jour

@film_router.delete('/films/{film_id}', status_code = status.HTTP_204_NO_CONTENT)
def suuprimer_film(film_id: int):
    if film_id not in db.films_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = f"Film {film_id} introuvable."
        )
    del db.films_db[film_id]
