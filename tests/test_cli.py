"""Tests for Pygantry CLI commands."""
import pytest
import subprocess
import sys
import os
from pathlib import Path

def get_pyg_cmd():
    """Get the correct pyg command for the current environment."""
    return [sys.executable, "-m", "pygantry.cli"]

def test_version_command():
    """Test that version command works and returns correct format."""
    result = subprocess.run(
        get_pyg_cmd() + ["version"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    assert result.returncode == 0
    assert "Pygantry v" in result.stdout
    assert "Python" in result.stdout

def test_help_command():
    """Test that help command shows all expected commands."""
    result = subprocess.run(
        get_pyg_cmd() + ["--help"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    assert result.returncode == 0
    assert "init" in result.stdout
    assert "build" in result.stdout
    assert "run" in result.stdout
    assert "ship" in result.stdout

def test_init_creates_gantryfile(tmp_path):
    """Test that init command creates a Gantryfile."""
    os.chdir(tmp_path)
    result = subprocess.run(
        get_pyg_cmd() + ["init", "--name", "test_project"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    assert result.returncode == 0
    assert (tmp_path / "Gantryfile").exists()