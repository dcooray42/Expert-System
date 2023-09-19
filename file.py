from data import Rule, Fact, Query

def read_file(es, file_path) :
    with open(file_path, "r") as file :
        rules = []
        queries = None
        lines = file.readlines()
        for line in lines:
            raw_line = line.strip()
            trimed_line = "".join(raw_line.split("#")[0:1]).lstrip().rstrip()
            final_line = "".join(trimed_line.split())
            if not len(final_line) :
                continue
            if final_line.startswith("="):
                init_fact = final_line[1:]
                for fact in init_fact :
                    if fact not in es.known_facts.keys() :
                        es.known_facts[fact] = Fact(fact, True, True)
                    else :
                        raise Exception(f"Intial fact called twice or more : {fact}")
            elif final_line.startswith("?"):
                queries = Query(trimed_line[1:])
            else:
                if final_line.find("=>") > 0 :
                    line_splited = final_line.split("=>")
                exp_1, exp_2 = is_well_formed(line_splited[0]), is_well_formed(line_splited[1])
                if exp_1 and exp_2 :
                    condition = convert_to_rpn(line_splited[0])
                    conclusion = convert_to_rpn(line_splited[1])
                    if not any(char in "|^" for char in conclusion) :
                        rules.append(Rule(condition, conclusion))
                    else :
                        raise Exception(f"One or multiple of these operations (OR / |) or (XOR / ^) is / are present in the conclusion.")
                else :
                    malformed_str = line_splited[0] if not exp_1 else line_splited[1]
                    raise Exception(f"This expression is malformed : {malformed_str}")
                    


    print("Rules:")
    for rule in rules:
        print(f"Condition: {rule.condition}, Conclusion: {rule.conclusion}")

    print("\nInitial Facts:")
    for fact in es.known_facts.keys() :
        info = es.known_facts[fact]
        print(f"Fact: {fact}, es.fact = {info.fact}, value = {info.value}, check = {info.check}")

    print("\nQueries:")
    print(f"Symbols: {queries.symbols}")

def is_well_formed(expression):
    stack = []

    for index, char in enumerate(expression) :
        if index :
            pre_char = expression[index - 1]
        if char == '(' :
            stack.append(char)
        elif char == ')' :
            if len(stack) == 0 :
                return False
            else :
                if index :
                    if pre_char in "+|!^(" :
                        return False
            stack.pop()
        elif char in "+|!^" :
            if index == 0 and char != "!" :
                return False
            elif index :
                if char != "!" and pre_char in "+|!^(" :
                    return False
                elif char == "!" and (pre_char.isalpha() or pre_char in "!)") :
                    return False
        elif char.isalpha() :
            if index :
                if pre_char not in "+|!^(" or pre_char.isalpha() :
                    print(pre_char not in "+|!^(", pre_char.isalpha())
                    return False
        else:
            return False

    return len(stack) == 0

def convert_to_rpn(infix_expression) :
    precedence = {"!": 1, "+": 2, "|": 3, "^": 4}
    output = []
    stack = []

    for token in infix_expression :
        if token.isalpha() :
            output.append(token)
        elif token in "!+|^" :
            while stack and stack[-1] in "+|^!" and precedence[token] >= precedence[stack[-1]] :
                output.append(stack.pop())
            stack.append(token)
        elif token == '(' :
            stack.append(token)
        elif token == ')' :
            while stack and stack[-1] != '(' :
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return "".join(output)