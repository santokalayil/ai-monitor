from typing import NoReturn
from ai.core import monitor_status, get_version

def main() -> NoReturn:
    """
    Main entry point for the application.
    
    Returns:
        NoReturn: This function doesn't return anything
    """
    print("Hello, World!")
    print(f"AI Monitor Version: {get_version()}")
    print(f"Status: {monitor_status()}")

if __name__ == "__main__":
    main() 