from data import Fact

def evaluate_expression(expression):
    if len(expression) == 1:
        operand = expression[0]
        return backward_chain(operand)
    stack = []

    for token in expression:
        if isinstance(token, Fact):
            stack.append(token)
        else:
            operand = stack.pop()
            operand = backward_chain(operand) if isinstance(operand, Fact) else operand
            if token in "+|^":
                operand_bis = stack.pop()
                operand_bis = backward_chain(operand_bis) if isinstance(operand_bis, Fact) else operand
            if token == '+':
                result = operand_bis and operand
            elif token == '|':
                result = operand_bis or operand
            elif token == '!':
                result = not operand
            elif token == '^':
                result = operand_bis != operand
            stack.append(result)
    return stack[0]


def backward_chain(query):
    
    def val_to_check(conclusion, value):
        stack = []
        for token in conclusion:
            if isinstance(token, Fact):
                stack.append([token, True])
            elif token == "!":
                top_stack = stack.pop()
                top_stack[1] = False
                stack.append(top_stack)
        for token_combination in stack:
            token = token_combination[0]
            token_state = token_combination[1]
            if ((token.value != value and token_state == True)
                or (token.value == value and token_state == False)) and token.check == True:
                return False
        return True

    def update_facts(conclusion, value):
        stack = []
        for token in conclusion:
            if isinstance(token, Fact):
                stack.append([token, True])
            elif token == "!":
                top_stack = stack.pop()
                top_stack[1] = False
                stack.append(top_stack)
        for token_combination in stack:
            token = token_combination[0]
            token_state = token_combination[1]
            token.value = value if token_state else not value
            token.check = True

    def fact_sign(conclusion, fact):
        index = 1
        while index < len(conclusion):
            if conclusion[index - 1] == fact:
                if conclusion[index] == "!":
                    return False
            i += 1
        return True

#    print(f"{query.fact} = {query.value}, {query.check}")
    store_rslt = []
    if query.check == True:
        return query.value

    for rule in query.rules:
        if query in rule.conclusion:
            rule_rslt = []
#            for token in rule.condition:
#                if isinstance(token, Fact):
#                    print(token.fact, end="")
#                else:
#                    print(token, end="")
#            print(" = ", end="")
#            for token in rule.conclusion:
#                if isinstance(token, Fact):
#                    print(token.fact, end="")
#                else:
#                    print(token, end="")
#            print("\n----------------------------")
            rule_rslt.append(evaluate_expression(rule.condition))
            rule_rslt.append(fact_sign(rule.conclusion, query))
            if val_to_check(rule.conclusion, result):
                update_facts(rule.conclusion, result)
                return result

    update_facts([query], False)
    return False