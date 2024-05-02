from pydantic import BaseModel
from route import Route
from traceroute import traceroute

urls = ["google.com", "yandex.ru", "youtube.com", "vk.com", "amazon.com"]


def fingerprint_network() -> dict[str, list[list[str|None]]]:
    """
    Traceroute different URLs
    :return:
    """
    info = {}

    for url in urls:
        info[url] = [[node] for node in traceroute(url)]

    return info
