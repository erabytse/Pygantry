#!/usr/bin/env python
"""Pygantry alias 'pyg' - works without installation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pygantry.cli import app
app()