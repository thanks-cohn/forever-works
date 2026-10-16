"""Dependency-free Python reference binding for Forever Works 0.1."""
from .model import Model, ModelError, load_model, normalize
__all__ = ["Model", "ModelError", "load_model", "normalize", "load_model_lossless", "JsonNumber", "parse_lossless", "canonical_lossless"]

from .model import load_model_lossless
from .lossless import JsonNumber, parse_lossless, canonical_lossless
