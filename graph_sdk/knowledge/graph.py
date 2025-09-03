# graph_sdk/knowledge/graph.py
from typing import Any, Callable, Dict

class Graph:
    _providers: Dict[str, Callable[..., Any]] = {}

    @classmethod
    def register(cls, name: str):
        def _wrap(fn: Callable[..., Any]):
            if name in cls._providers:
                raise KeyError(f"Duplicate provider '{name}'")
            cls._providers[name] = fn
            return fn
        return _wrap

    @classmethod
    def fetch(cls, name: str, /, **ctx):
        try:
            fn = cls._providers[name]
        except KeyError as e:
            known = ", ".join(sorted(cls._providers))
            raise KeyError(f"Unknown provider '{name}'. Known: {known}") from e
        return fn(**ctx)

    @classmethod
    def all(cls):
        return sorted(cls._providers)