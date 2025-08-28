from __future__ import annotations
import importlib
import pkgutil
from typing import Dict


class Entities:
    """
    Registry/barrel for entity classes and DTOs across the SDK.
    Usage:
        from graph_sdk.entities import Entities
        Person = Entities.fetch("Person")
    """

    _DOMAIN_ROOT = "graph_sdk.domain"
    _EXPORTS: Dict[str, str] = {}
    _RESOLVED: Dict[str, object] = {}

    @classmethod
    def _iter_exports(cls) -> Dict[str, str]:
        exports: Dict[str, str] = {}
        domain_pkg = importlib.import_module(cls._DOMAIN_ROOT)

        for modinfo in pkgutil.walk_packages(domain_pkg.__path__, domain_pkg.__name__ + "."):
            if not modinfo.name.endswith(".exports"):
                continue
            mod = importlib.import_module(modinfo.name)
            mod_exports = getattr(mod, "EXPORTS", None)
            if not isinstance(mod_exports, dict):
                continue

            for public_name, target in mod_exports.items():
                if public_name in exports and exports[public_name] != target:
                    raise RuntimeError(
                        f"Duplicate export name {public_name!r} "
                        f"from {modinfo.name}; already exported as {exports[public_name]!r}"
                    )
                exports[public_name] = target
        return exports

    @classmethod
    def _ensure_exports(cls):
        if not cls._EXPORTS:
            cls._EXPORTS = cls._iter_exports()

    @classmethod
    def fetch(cls, name: str):
        cls._ensure_exports()
        if name in cls._RESOLVED:
            return cls._RESOLVED[name]

        try:
            target = cls._EXPORTS[name]
        except KeyError as e:
            known = ", ".join(sorted(cls._EXPORTS.keys()))
            raise ValueError(f"Unknown entity/DTO {name!r}. Known: {known}") from e

        mod_path, attr = target.split(":")
        obj = getattr(importlib.import_module(mod_path), attr)
        cls._RESOLVED[name] = obj
        return obj

    @classmethod
    def all_exports(cls):
        """Return a sorted list of all registered export names."""
        cls._ensure_exports()
        return sorted(cls._EXPORTS.keys())