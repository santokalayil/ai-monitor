"""
Core functionality for AI monitoring.
"""
from typing import Final
from .version import get_version as get_package_version

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
    return get_package_version()

# Type constants
STATUS_MESSAGE: Final[str] = "AI systems are operational" 