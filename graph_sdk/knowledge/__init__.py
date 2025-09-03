# graph_sdk/knowledge/__init__.py
import importlib, pkgutil, pathlib

_pkg = __name__
_pkg_path = pathlib.Path(__file__).parent

for m in pkgutil.walk_packages([str(_pkg_path)], prefix=_pkg + "."):
    # Only import leaf modules (skip packages’ __init__)
    if not m.ispkg:
        importlib.import_module(m.name)
