"""
Version management for the AI package.
"""
from typing import Final

# Version information
MAJOR_VERSION: Final[int] = 0    # Breaking changes
MINOR_VERSION: Final[int] = 2    # New features
PATCH_VERSION: Final[int] = 0    # Bug fixes

# Build version string
VERSION: Final[str] = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"

def get_version() -> str:
    """
    Get the current version of the package.
    
    Returns:
        str: The current version string
    """
    return VERSION

def get_version_tuple() -> tuple[int, int, int]:
    """
    Get the version as a tuple of integers.
    
    Returns:
        tuple[int, int, int]: Version as (major, minor, patch)
    """
    return (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION) 