'''class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    pass


seine = River("Siene", 777)

'''

class Plant:
    def __init__(self, spec):
        self.spec = spec


class Cactus(Plant):
    pass
basil = Plant("Ocimum basilicum")

opuntia = Cactus("Opuntia vulgaris")

print(isinstance(opuntia, object))
