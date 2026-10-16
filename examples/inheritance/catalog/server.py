"""Catalog product entry point: catalog owns mutable metadata and revision state."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'shared'))
from runtime import serve
if __name__=='__main__':serve('catalog')
