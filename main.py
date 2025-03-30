from ai.core import monitor_status, get_version

def main():
    print("Hello, World!")
    print(f"AI Monitor Version: {get_version()}")
    print(f"Status: {monitor_status()}")

if __name__ == "__main__":
    main() 