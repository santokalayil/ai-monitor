"""
Tests for the core functionality of the AI monitor package.
"""
import pytest
from ai.core import monitor_status, get_version

def test_monitor_status():
    """Test that monitor_status returns the expected string."""
    result = monitor_status()
    assert isinstance(result, str)
    assert result == "AI systems are operational"

def test_get_version():
    """Test that get_version returns a valid version string."""
    version = get_version()
    assert isinstance(version, str)
    assert len(version.split(".")) == 3  # Should be semantic versioning
    # Check that each part is a number
    for part in version.split("."):
        assert part.isdigit() 