from functools import wraps
from sisl._internal import set_module
from sisl.category import Category, NullCategory


__all__ = ["NullCategory", "AtomCategory"]


def _sanitize_loop(func):
    @wraps(func)
    def loop_func(self, geometry, atoms=None):
        if atoms is None:
            return [func(self, geometry, ia) for ia in geometry]
        # extract based on atoms selection
        atoms = geometry._sanitize_atom(atoms)
        if atoms.ndim == 0:
            return func(self, geometry, atoms)
        return [func(self, geometry, ia) for ia in atoms]
    return loop_func


@set_module("sisl.geom")
class AtomCategory(Category):
    __slots__ = tuple()
