from transform.spot import Spot

class Board:

    '''
    Board's overloaded functions and functions for
    board manipulation live here
    '''

    def __init__(self):
        self.walls = set()
        self.goals = set()
        self.boxes = set()
        self.movables = set()
        self.fboxes = frozenset()  # since set() is not hashable
        self.player = None

    def add_wall(self, x, y):
        self.walls.add(Spot(x+1, y+1))

    def add_goal(self, x, y):
        self.goals.add(Spot(x+1, y+1))

    def add_box(self, x, y):
        self.boxes.add(Spot(x+1, y+1))

    def add_movable(self, x, y):
        self.movables.add((Spot(x+1, y+1)))

    def set_player(self, x, y):
        self.player = Spot(x+1, y+1)
