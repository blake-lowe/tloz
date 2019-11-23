class Object:
    def __init__(self, ID, description, isMovable, isMoved):
        self.ID = ID
        self.description = description
        self.isMovable = isMovable
        self.isMoved = isMoved
    def description():
        print(description)


class Rock(Object):
    def __init__(self, ID):
        super().__init__(self,
                         ID,
                         "It's grey, round, and heavy.",
                         False,
                         False
                         )
