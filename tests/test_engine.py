"""Tests for Pygantry Engine."""
import pytest
import os
import sys
from pathlib import Path
from pygantry.engine import PyGantryEngine

def test_engine_initialization():
    """Test that engine initializes with default values."""
    engine = PyGantryEngine()
    assert engine.manifest_path == "Gantryfile"
    assert engine.env_dir == ".gantry"

def test_engine_custom_paths():
    """Test that engine accepts custom paths."""
    engine = PyGantryEngine(manifest_path="Custom.yml", env_dir=".custom")
    assert engine.manifest_path == "Custom.yml"
    assert engine.env_dir == ".custom"

def test_create_manifest(tmp_path):
    """Test that create_manifest creates a valid Gantryfile."""
    os.chdir(tmp_path)
    engine = PyGantryEngine()
    engine.create_manifest("test_app")
    
    assert (tmp_path / "Gantryfile").exists()
    
    # Verify content is valid YAML
    import yaml
    with open(tmp_path / "Gantryfile", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    assert config["project"] == "test_app"
    assert "python" in config
    assert "packages" in config