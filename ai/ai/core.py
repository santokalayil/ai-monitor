"""
Core functionality for AI monitoring.
"""

def monitor_status():
    """
    Check the status of AI systems.
    
    Returns:
        str: Status message
    """
    return "AI systems are operational"

def get_version():
    """
    Get the current version of the AI monitor.
    
    Returns:
        str: Version string
    """
    from . import __version__
    return __version__ 