"""
Pytest configuration file.
"""
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Debug information
print(f"conftest.py - Python path: {sys.path}")
print(f"conftest.py - Current directory: {os.getcwd()}")
print(f"conftest.py - Project root: {project_root}")
print(f"conftest.py - Files in project root: {os.listdir(project_root)}")

# Verify the ai package exists
ai_package = project_root / 'ai'
if not ai_package.exists():
    raise RuntimeError(f"AI package not found at {ai_package}") 