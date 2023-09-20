def evaluate_expression(expression, known_facts) :
    stack = []

    for token in expression:
        if isinstance(token, FactNode) :
            # If it's a FactNode, push its value onto the stack
            stack.append(token.value)
        elif token in "+|!^" :
            # If it's an operator, apply it to the operands on the stack
            if token == '+' :
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 and operand2
            elif token == '|' :
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 or operand2
            elif token == '!' :
                operand = stack.pop()
                result = not operand
            elif token == '^' :
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 != operand2  # XOR is not equal
            stack.append(result)

    # The result should be on the top of the stack
    return stack[0]


def backward_chain(es, query) :
    if es.known_facts[query].check == True :
        return es.known_fact[query].value

    for rule in es.rules :
        if query in rule.conclusion and len(set(es.initial_facts).intersection(set(rule.conclusion))) == 0 :
            # non termine a partir d'ici
            is_rule_valid = evaluate_expression(rule.expression, inference_engine.known_facts)
            if is_rule_valid :
                inference_engine.known_facts[goal] = True
                return True

    return False