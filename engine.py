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
                operand_bis = backward_chain(operand_bis) if isinstance(operand_bis, Fact) else operand_bis
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

    def fact_sign(conclusion, fact):
        index = 1
        while index < len(conclusion):
            if conclusion[index - 1] == fact:
                if conclusion[index] == "!":
                    return False
            index += 1
        return True
    
    def return_value(rslt):
        false_false = False
        false_true = False
        true_false = False
        true_true = False
        for iter in rslt:
            if iter[0] == False and iter[1] == False:
                false_false = True
            elif iter[0] == False and iter[1] == True:
                false_true = True
            elif iter[0] == True and iter[1] == False:
                true_false = True
            else:
                true_true = True
        if (false_false and false_true) or (true_false and true_true):
            raise Exception("error: Enexpected behaviour during value assignation")
        if true_true or false_false:
            return True
        else:
            return False


    print(f"{query.fact} = {query.value}, {query.check}")
    store_rslt = []
    if query.check == True:
        return query.value

    for rule in query.rules:
        if query in rule.conclusion:
            print(f"query : {query.fact} | ", end="")
            for token in rule.condition:
                if isinstance(token, Fact):
                    print(token.fact, end="")
                else:
                    print(token, end="")
            print(" = ", end="")
            for token in rule.conclusion:
                if isinstance(token, Fact):
                    print(token.fact, end="")
                else:
                    print(token, end="")
            print("\n----------------------------")
            rule_rslt = []

            rule_rslt.append(evaluate_expression(rule.condition))
            rule_rslt.append(fact_sign(rule.conclusion, query))
            store_rslt.append(rule_rslt)
    query.value = return_value(store_rslt)
    query.check = True
    print(f"after {query.fact} = {query.value}, {query.check}")
    return query.value