class Rule:
    def __init__(self, condition, conclusion):
        self.condition = condition
        self.conclusion = conclusion

class InitialFact:
    def __init__(self, facts):
        self.facts = facts

class Query:
    def __init__(self, symbols):
        self.symbols = symbols

class ExpertSystem:
    def __init__(self):
        self.rules = []  # List of Rule objects
        self.known_facts = {}  # Dictionary to store known facts

    def add_rule(self, expression, conclusion):
        rule = Rule(expression, conclusion)
        self.rules.append(rule)

    def add_fact(self, fact, value=True):
        self.known_facts[fact] = value

    def query(self, goal):
        return backward_chain(self, goal)