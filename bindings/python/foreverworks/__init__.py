"""Dependency-free Python reference binding for Forever Works 0.1."""
from .model import Model, ModelError, load_model, normalize
__all__ = ["Model", "ModelError", "load_model", "normalize"]
