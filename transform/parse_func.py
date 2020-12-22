from pddlgym.structs import TypedEntity, LiteralConjunction

PLAYER = "player-0"
DIR_DOWN = "dir-down"
DIR_LEFT = "dir-left"
DIR_RIGHT = "dir-right"
DIR_UP = "dir-up"

def parse_objects(board, types):
    to_ret = set()
    to_ret.add(TypedEntity(PLAYER, types['thing']))
    for o in [DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP]:
        to_ret.add(TypedEntity(o, types['direction']))
    for i, _ in enumerate(board.boxes):
        to_ret.add(TypedEntity("stone-{}".format(i), types['thing']))
    for p in board.movables:
        to_ret.add(TypedEntity("pos-{}-{}".format(p.x, p.y), types['location']))
    for p in board.walls:
        to_ret.add(TypedEntity("pos-{}-{}".format(p.x, p.y), types['location']))
    return sorted(to_ret)

def parse_goal(board, types, predicates):
    all_preds = [
        predicates["at-goal"](
            *[TypedEntity("stone-{}".format(i), types['thing'])]
        ) for i, _ in enumerate(board.boxes)
    ]
    return LiteralConjunction(all_preds)

def parse_initial_state(board, types, predicates):
    initial_lits = set()
    for dir in [DIR_RIGHT, DIR_LEFT, DIR_DOWN, DIR_UP]:
        initial_lits.add(
            predicates['move'](
                *[
                    TypedEntity(dir, types['direction']),
                ]
            )
        )

    initial_lits.add(
        predicates['at'](
            *[
                TypedEntity(PLAYER, types['thing']),
                TypedEntity("pos-{}-{}".format(board.player.x, board.player.y), types['location'])
            ]
        )
    )
    initial_lits.add(
        predicates['is-player'](
            *[
                TypedEntity(PLAYER, types['thing']),
            ]
        )
    )
    for i, box in enumerate(board.boxes):
        if box in board.goals:
            initial_lits.add(
                predicates['at-goal'](
                    *[
                        TypedEntity("stone-{}".format(i), types['thing'])
                    ]
                )
            )

        initial_lits.add(
            predicates['at'](
                *[
                    TypedEntity("stone-{}".format(i), types['thing']),
                    TypedEntity("pos-{}-{}".format(box.x, box.y), types['location'])
                ]
            )
        )
        initial_lits.add(
            predicates['is-stone'](
                *[
                    TypedEntity("stone-{}".format(i), types['thing']),
                ]
            )
        )
    for spot in board.walls:
        initial_lits.add(
            predicates['is-nongoal'](
                *[
                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                ]
            )
        )

    for spot in board.movables:
        if spot in board.goals:
            initial_lits.add(
                predicates['is-goal'](
                    *[
                        TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                    ]
                )
            )
        else:
            initial_lits.add(
                predicates['is-nongoal'](
                    *[
                        TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                    ]
                )
            )
        if spot not in board.boxes and spot != board.player:
            initial_lits.add(
                predicates['clear'](
                    *[
                        TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                    ]
                )
            )
        for another_spot in board.movables:
            if another_spot == spot:
                continue
            else:
                if another_spot.x == spot.x:
                    if another_spot.y == spot.y + 1:
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    DIR_DOWN
                                ]
                            )
                        )
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    DIR_UP
                                ]
                            )
                        )
                    elif another_spot.y == spot.y - 1:
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    DIR_UP
                                ]
                            )
                        )
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    DIR_DOWN
                                ]
                            )
                        )
                elif another_spot.y == spot.y:
                    if another_spot.x == spot.x + 1:
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    DIR_RIGHT
                                ]
                            )
                        )
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    DIR_LEFT
                                ]
                            )
                        )
                    elif another_spot.y == spot.y - 1:
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    DIR_LEFT
                                ]
                            )
                        )
                        initial_lits.add(
                            predicates['move-dir'](
                                *[
                                    TypedEntity("pos-{}-{}".format(another_spot.x, another_spot.y), types['location']),
                                    TypedEntity("pos-{}-{}".format(spot.x, spot.y), types['location']),
                                    DIR_RIGHT
                                ]
                            )
                        )
    return frozenset(initial_lits)