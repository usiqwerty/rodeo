import json

from network import NetworkInfo

storage_fn = "data.json"


def load() -> dict[int, NetworkInfo]:
    try:
        with open(storage_fn, encoding='utf-8') as f:
            data = {}
            for k, v in json.load(f).items():
                data[k] = NetworkInfo(**v)
            return data
    except FileNotFoundError:
        return {}


def save(data: dict[int, NetworkInfo]):
    with open(storage_fn, 'w', encoding='utf-8') as f:
        json.dump({k: v.json for k, v in data.items()}, f)
