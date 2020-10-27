from transform.sokoban_game import SokobanGame
from pddlgym.parser import PDDLProblemParser, PDDLDomainParser
from transform.parse_func import parse_objects, parse_initial_state, parse_goal

SOKOBAN_LEVELs = ["easy{}".format(i) for i in range(1, 5)] + ["mod{}".format(i) for i in range(1, 8)]
SOKOBAN_LEVELs = ["easy1"]
if __name__ == "__main__":
    for l in SOKOBAN_LEVELs:
        sok = SokobanGame()
        b = sok.new_board("transform/puzzles/{}.txt".format(l))
        domian_file = "/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/transform.pddl"
        problem_file = "/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/sokoban_test/task02.pddl"
        domain = PDDLDomainParser(domian_file)
        problem = PDDLProblemParser(
            problem_file, domain.domain_name, domain.types, domain.predicates, domain.actions, domain.constants
        )

        problem.objects = parse_objects(b, domain.types)
        problem.goal = parse_goal(b, domain.types, domain.predicates)
        problem.initial_state = parse_initial_state(b, domain.types, domain.predicates)

        with open('/Users/yangchen/PycharmProjects/pddlgym/pddlgym/pddl/transform/{}.pddl'.format(l), 'w') as f:
            PDDLProblemParser.create_pddl_file(
                f, problem.objects, problem.initial_state, problem.problem_name,
                problem.domain_name, problem.goal
            )



