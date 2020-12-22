from transform.board import Board, Spot

class SokobanGame:

    '''
    Sokoban game class
    '''

    def touchable_wall(self, b):
        touchable_walls = set()
        for s in b.movables:
            for i in [-1, 1]:
                for new_wall in [Spot(s.x+i, s.y), Spot(s.x, s.y+i)]:
                    if new_wall in b.walls:
                        touchable_walls.add(new_wall)
        return touchable_walls

    def new_board(self, filename):
        ''' Creates new board from file '''
        with open(filename, 'r') as f:  # automatically closes file

            read_data = f.read()
            lines = read_data.split('\n')

            b = None
            for line in lines:
                if ";" in line:
                    b = Board()
                    x = 0
                    y = 0
                    continue
                elif line == "":
                    assert hasattr(b, 'player')
                    # b.walls = self.touchable_wall(b)
                    yield b
                else:
                    for char in line:
                        # adds Spots to board's sets by reading in char
                        if char == '#':
                            b.add_wall(x, y)
                        elif char == '.':
                            b.add_goal(x, y)
                            b.add_movable(x, y)
                        elif char == '@':
                            b.set_player(x, y)
                            b.add_movable(x, y)
                        elif char == '+':
                            b.set_player(x, y)
                            b.add_goal(x, y)
                            b.add_movable(x, y)
                        elif char == '$':
                            b.add_box(x, y)
                            b.add_movable(x, y)
                        elif char == '*':
                            b.add_box(x, y)
                            b.add_goal(x, y)
                            b.add_movable(x, y)
                        elif char == ' ':
                            b.add_movable(x, y)
                        x += 1
                    y += 1
                    x = 0


