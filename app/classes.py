class Constellation:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Star:
    def __init__(self, id, name, x, y, description, constellation_id, size):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.description = description
        self.constellation_id = constellation_id
        self.size = size
