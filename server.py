import os

try:
    from Pyro5.api import Daemon, expose
except ModuleNotFoundError as exc:
    raise SystemExit("Pyro5 is not installed. Run: python -m pip install Pyro5") from exc

from product import Product

HOST = os.getenv("PYRO_HOST", "127.0.0.1")
PORT = int(os.getenv("PYRO_PORT", "9000"))

@expose
class ProductImpl(Product):

    def __init__(self, new_name, new_description, new_price):
        self.name = new_name
        self.description = new_description
        self.price = new_price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

def main():
    try:
        print("Server is booting....")

        p1 = ProductImpl("Laptop", "Lenovo laptop", 800000.0)
        p2 = ProductImpl("Mobile", "MI 9 mobile", 24000.0)
        p3 = ProductImpl("Bag", "Branded bag", 800.0)
        p4 = ProductImpl("Charger", "MI Charger", 230.0)

        daemon = Daemon(host=HOST, port=PORT)
        daemon.register(p1, objectId="laptop")
        daemon.register(p2, objectId="ram")
        daemon.register(p3, objectId="bag")
        daemon.register(p4, objectId="charger")

        print(f"Server is ready on {HOST}:{PORT}")
        print("Registered objects: laptop, ram, bag, charger")
        print("Waiting for client requests... (Ctrl+C to stop)")
        daemon.requestLoop()

    except OSError as exc:
        print(f"Server error: {exc}")
    except Exception as exc:
        print(f"Server error: {exc}")

if __name__ == "__main__":
    main()