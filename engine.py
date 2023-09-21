def evaluate_expression(es, expression) :
    stack = []

    for token in expression :
        if token.isalpha() :
            stack.append(token)
        else :
            operand = backward_chain(es, stack.pop())
            if token in "+|^" :
                operand_bis = backward_chain(es, stack.pop())
            if token == '+' :
                result = operand_bis and operand
            elif token == '|' :
                result = operand_bis or operand
            elif token == '!' :
                result = not operand
            elif token == '^' :
                result = operand_bis != operand  # XOR is not equal
            stack.append(result)

    # The result should be on the top of the stack
    return stack[0]


def backward_chain(es, query) :
    def val_to_check(es, conclusion, value) :
        for token in conclusion :
            if token.isalpha() :
                if es.facts[token].value != value and es.facts[token].check == True :
                    return False
        return True

    def update_facts(es, conclusion, value) :
        for token in conclusion :
            if token.isalpha() :
                es.facts[token].value = value
                es.facts[token].check = True

    if es.facts[query].check == True :
        return es.facts[query].value

    for rule in es.rules :
        if query in rule.conclusion and len(set(es.initial_facts).intersection(set(rule.conclusion))) == 0 :
            result = evaluate_expression(es, rule.condition)
            if val_to_check(es, rule.conlusion, result) :
                update_facts(es, rule.conclusion, result)
                return result

    return False