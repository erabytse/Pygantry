"""Pytest configuration and fixtures."""
import pytest
import os
import shutil
from pathlib import Path

@pytest.fixture(autouse=True)
def clean_gantry_files(tmp_path):
    """Clean up Gantryfile and .gantry directory after each test."""
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    yield
    os.chdir(original_dir)