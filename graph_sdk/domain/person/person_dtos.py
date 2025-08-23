# graph_sdk/domain/person/person_dtos.py

# use like:
#   from graph_sdk.domain.person.person_dtos import *

from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class PersonCreateDto:
    given_name: str
    family_name: str

@dataclass
class PersonFindDto:
    id: UUID

@dataclass
class PeopleFindByDto:
    id: Optional[UUID] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None

@dataclass
class PersonUpdateDto:
    given_name: Optional[str] = None
    family_name: Optional[str] = None

__all__ = [
    "PersonCreateDto",
    "PersonFindDto",
    "PersonUpdateDto",
    "PeopleFindByDto"
]