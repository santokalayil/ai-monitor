"""
Core functionality for AI monitoring.
"""
from typing import Final

def monitor_status() -> str:
    """
    Check the status of AI systems.
    
    Returns:
        str: Status message
    """
    return "AI systems are operational"

def get_version() -> str:
    """
    Get the current version of the AI monitor.
    
    Returns:
        str: Version string
    """
    from . import __version__
    return __version__

# Type constants
VERSION: Final[str] = "0.1.0"
STATUS_MESSAGE: Final[str] = "AI systems are operational" 