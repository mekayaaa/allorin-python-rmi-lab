# Python RMI Lab


This project is a Python version of a simple Java RMI example using Pyro5 (Python Remote Objects).


It demonstrates:
- registering remote objects on a server
- looking them up by name from a client
- calling methods on a remote object over the local network


## Project files


- `server.py` – creates and registers remote product objects
- `client.py` – looks up the `laptop` object and prints its details
- `product.py` – defines the remote product interface
- `requirements.txt` – Python dependencies


## Setup


Create and activate a virtual environment if you want an isolated setup:


```bash
python -m venv .venv
.venv\Scripts\activate
```


Install the dependency:


```bash
python -m pip install -r requirements.txt
```


## Run the project


Start the server first in one terminal:


```bash
python server.py
```


Then run the client in another terminal:


```bash
python client.py
```


Expected output:


```text
Name:Laptop
Description: Lenovo laptop
Price: 800000.0
```


## Notes


- The server listens on `127.0.0.1:9000` by default.
- The client connects to the object named `laptop`.
- You can override the host and port with environment variables:


```bash
set PYRO_HOST=127.0.0.1
set PYRO_PORT=9000
```


Then start the app normally.
