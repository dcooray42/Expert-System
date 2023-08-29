from data import Rule, InitialFact, Query

def read_file(file_path) :
    with open(file_path, "r") as file :
        rules = []
        initial_facts = None
        queries = None
        lines = file.readlines()
        for line in lines:
            raw_line = line.strip()
            trimed_line = "".join(raw_line.split("#")[:-1]).lstrip().rstrip()
            final_line = "".join(trimed_line.split())
            if not len(final_line) :
                continue
            if final_line.startswith('='):
                initial_facts = InitialFact(final_line[1:])
            elif final_line.startswith('?'):
                queries = Query(trimed_line[1:])
            else:
                line_splited = final_line.split("=>")
                exp_1, exp_2 = is_well_formed(line_splited[0]), is_well_formed(line_splited[1])
                if exp_1 and exp_2 :
                    rules.append(Rule(line_splited[0], line_splited[1]))
                else :
                    malformed_str = line_splited[0] if not exp_1 else line_splited[1]
                    print(f"This expression is malformed : {malformed_str}")
                    


    print("Rules:")
    for rule in rules:
        print(f"Condition: {rule.condition}, Conclusion: {rule.conclusion}")

    print("\nInitial Facts:")
    print(f"Facts: {initial_facts.facts}")

    print("\nQueries:")
    print(f"Symbols: {queries.symbols}")

def is_well_formed(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                print(1)
                return False
            stack.pop()
        elif char in "+|!^":
            if not stack or stack[-1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ)!":
                print(2)
                print(stack, char)
                return False
        elif char.isalpha():
            if stack and stack[-1] in "+|!^":
                print(3)
                return False
        else:
            print(char)
            return False

    print(f"nique ta mere {stack}")
    return not stack