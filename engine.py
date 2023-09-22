def evaluate_expression(es, expression) :
    stack = []

    for token in expression :
        if token.isalpha() :
            stack.append(token)
        else :
            operand = stack.pop()
            operand = backward_chain(es, operand) if isinstance(operand, str) else operand
            if token in "+|^" :
                operand_bis = stack.pop()
                operand_bis = backward_chain(es, operand_bis) if isinstance(operand_bis, str) else operand
            if token == '+' :
                result = operand_bis and operand
            elif token == '|' :
                result = operand_bis or operand
            elif token == '!' :
                result = not operand
            elif token == '^' :
                result = operand_bis != operand
            stack.append(result)
    return stack[0]


def backward_chain(es, query) :
    
    def val_to_check(es, conclusion, value) :
        stack = []
        for token in conclusion :
            if token.isalpha() :
                stack.append([token, True])
            elif token == "!" :
                top_stack = stack.pop()
                top_stack[1] = False
                stack.append(top_stack)
        for token_combination in stack :
            token = token_combination[0]
            token_state = token_combination[1]
            if ((es.facts[token].value != value and token_state == True)
                or (es.facts[token].value == value and token_state == False)) and es.facts[token].check == True :
                return False
        return True

    def update_facts(es, conclusion, value) :
        stack = []
        for token in conclusion :
            if token.isalpha() :
                stack.append([token, True])
            elif token == "!" :
                top_stack = stack.pop()
                top_stack[1] = False
                stack.append(top_stack)
        for token_combination in stack :
            token = token_combination[0]
            token_state = token_combination[1]
            es.facts[token].value = value if token_state else not value
            es.facts[token].check = True

    if es.facts[query].check == True :
        return es.facts[query].value

    for rule in es.rules :
        if query in rule.conclusion and len(set(es.initial_facts).intersection(set(rule.conclusion))) == 0 :
            result = evaluate_expression(es, rule.condition)
            if val_to_check(es, rule.conclusion, result) :
                update_facts(es, rule.conclusion, result)
                return result

    update_facts(es, [query], False)
    return False