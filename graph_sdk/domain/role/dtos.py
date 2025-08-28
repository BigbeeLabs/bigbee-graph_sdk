# graph_sdk/domain/role/dtos.py

from dataclasses import dataclass
from typing import Optional
from uuid import UUID

# Read-only DTOs (no create/update)

@dataclass
class RoleFindDto:
    id: UUID

@dataclass
class RolesFindByDto:
    system_name: Optional[str] = None
    display_name: Optional[str] = None

__all__ = [
    "RoleFindDto",
    "RolesFindByDto",
]