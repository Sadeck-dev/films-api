from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from enum import Enum

class Genre(str, Enum):
    drame = "drame"
    crime = "crime"
    horreur = "Horreur"
    amour = "amour"
    comedie = "comedie"
    action = "action"
    sf = "sf"
    
class Realisateur(BaseModel):
    nom: str
    nationalite: str
    
    
class FilmBase(BaseModel):
    titre: str = Field(min_length = 1, max_length = 100)
    annee: int = Field(ge = 1888, le = 2030)
    note: float = Field(ge = 0, le = 10, description = "Note du film sur 10.")
    genres: list[Genre]
    realisateur: Realisateur
    image_url: HttpUrl | None = None 
    
class FilmPublic(FilmBase):
    id: int
    
class FilmCreate(FilmBase):
    pass
    
class FilmUpdate(BaseModel):
    titre: Optional[str] = Field(default = None, min_length = 1, max_length = 100)
    annee: Optional[int] = Field(default = None, ge = 1888, le = 2030)
    note: Optional[float] = Field(default = None, ge = 0.0, le = 10.0, description = "Note du film sur 10.")
    genres: Optional[list[Genre]]
    realisateur: Optional[Realisateur]
    image_url: Optional[HttpUrl]
    
