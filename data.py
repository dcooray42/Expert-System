class Rule:
    def __init__(self, condition, conclusion, log_relationship):
        self.condition = condition
        self.conclusion = conclusion
        self.log_relationship = log_relationship

class InitialFact:
    def __init__(self, facts):
        self.facts = facts

class Query:
    def __init__(self, symbols):
        self.symbols = symbols
