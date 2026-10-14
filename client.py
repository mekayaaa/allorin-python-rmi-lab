import os

try:
    from Pyro5.api import Proxy
except ModuleNotFoundError as exc:
    raise SystemExit("Pyro5 is not installed. Run: python -m pip install Pyro5") from exc

def main():
    host = os.getenv("PYRO_HOST", "127.0.0.1")
    port = os.getenv("PYRO_PORT", "9000")
    uri = f"PYRO:laptop@{host}:{port}"

    try:
        # Equivalent of LocateRegistry.getRegistry("127.0.0.1", 9000)
        # followed by registry.lookup("laptop")
        laptop = Proxy(uri)

        laptop_name = laptop.getName()
        laptop_description = laptop.getDescription()
        price = laptop.getPrice()

        print(f"Name:{laptop_name}")
        print(f"Description: {laptop_description}")
        print(f"Price: {price}")

    except Exception as exc:
        print(f"Exception in client side: {exc}")

if __name__ == "__main__":
    main()