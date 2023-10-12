class Rule:
    def __init__(self, condition, conclusion):
        self.condition = condition
        self.conclusion = conclusion

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        condition = f"Condition: {self.condition}\n"
        conclusion = f"Conclusion: {self.conclusion}\n"
        return condition + conclusion


class Fact:
    def __init__(self, fact, value=False, check=False, initial_fact=False):
        self.fact = fact
        self.value = value
        self.check = check
        self.initial_fact = initial_fact
        self.rules = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        fact = f"Fact: {self.fact}\n"
        value = f"Value: {self.value}\n"
        check = f"Check: {self.check}\n"
        init_fact = f"Initial fact: {self.initial_fact}\n"
        rules = ""
        for rule in self.rules:
            rules += f"Rules: {rule}\n"
        return fact + value + check + init_fact + rules


class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.queries = []

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        fact = ""
        for fact_info in self.facts.keys():
            fact += self.facts[fact_info].__repr__()
        queries = f"Queries: {self.queries}"
        return fact + queries
    
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
