# graph_sdk/domain/email_address/email_address_dtos.py

# use like:
#   from graph_sdk.domain.email_address.email_address_dtos import *

from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class EmailAddressCreateDto:
    address: str

@dataclass
class EmailAddressFindDto:
    id: UUID

@dataclass
class EmailAddressesFindByDto:
    id: Optional[UUID] = None
    address: Optional[str] = None

@dataclass
class EmailAddressUpdateDto:
    address: Optional[str] = None

__all__ = [
    "EmailAddressCreateDto",
    "EmailAddressFindDto",
    "EmailAddressUpdateDto",
    "EmailAddressFindByDto"
]