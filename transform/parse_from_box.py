from transform.sokoban_game import SokobanGame
from pddlgym.parser import PDDLProblemParser, PDDLDomainParser
from transform.parse_func import parse_objects, parse_initial_state, parse_goal
import os

TAR_DIR = "transform/puzzles/hard"

if __name__ == "__main__":
    cnt = 0
    for file in sorted(os.listdir(TAR_DIR)):
        sok = SokobanGame()
        boards = sok.new_board(os.path.join(TAR_DIR, file))
        for b in boards:
            domian_file = "/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/sokoban.pddl"
            problem_file = "/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/sokoban_test/task02.pddl"
            domain = PDDLDomainParser(domian_file)
            problem = PDDLProblemParser(
                problem_file, domain.domain_name, domain.types, domain.predicates, domain.actions, domain.constants
            )

            problem.objects = parse_objects(b, domain.types)
            problem.goal = parse_goal(b, domain.types, domain.predicates)
            problem.initial_state = parse_initial_state(b, domain.types, domain.predicates)

            with open('/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/sokoban/{}.pddl'.format(cnt), 'w') as f:
                PDDLProblemParser.create_pddl_file(
                    f, problem.objects, problem.initial_state, problem.problem_name,
                    problem.domain_name, problem.goal
                )

            cnt += 1
            if cnt == 5:
                exit(0)