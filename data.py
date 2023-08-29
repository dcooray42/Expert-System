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
