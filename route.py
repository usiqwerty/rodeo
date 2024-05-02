from pydantic import BaseModel


class Route(BaseModel):
    variants: list[list[str|None]]

    def add_variant(self, route: list[str | None]):
        self.variants.append(route)

    def merge(self, other):
        self.variants += other.variants

    def combined(self):
        res = [[] for i in range(len(self.variants[0]))]
        for variant in self.variants:
            for i in range(len(res)):
                if variant[i] not in res[i]:
                    res[i].append(variant[i])
        return res
