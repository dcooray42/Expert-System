class Rule:
    def __init__(self, condition, conclusion):
        self.condition = condition
        self.conclusion = conclusion
        self.facts = []

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
        self.facts = {}  # Dictionary to store known facts
        self.queries = []

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        fact = ""
        for fact_info in self.facts.keys():
            fact += self.facts[fact_info].__repr__()
        queries = f"Queries: {self.queries}"
        return fact + queries