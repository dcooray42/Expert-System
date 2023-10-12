class Rule:
    def __init__(self, condition, conclusion):
        self.condition = condition
        self.conclusion = conclusion


class Fact:
    def __init__(self, fact, value=False, check=False):
        self.fact = fact
        self.value = value
        self.check = check
        self.rules = []

    def initial_fact(self):
        self.value = True
        self.check = True

    def check_already_present(self):
        if self.value == True and self.check == True:
            return True
        else:
            return False


class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.queries = []
    
    def populate_facts(self, rules):

        def parse_expression(expr, rule):
            for index, fact in enumerate(expr):
                if fact.isalpha():
                    if fact not in self.facts.keys():
                        self.facts[fact] = Fact(fact)
                    expr[index] = self.facts[fact]
                    self.facts[fact].rules.append(rule)

        for rule in rules:
            parse_expression(rule.condition, rule)
            parse_expression(rule.conclusion, rule)
