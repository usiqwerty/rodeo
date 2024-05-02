import json
import time
from dataclasses import asdict

from network import fingerprint_network
from route import Route
from storage import load, save


networks = load()
for k in networks:
    print(k)

save(networks)