
def read_file(file_path) :
    with open(file_path, "r") as file :
        lines = file.readlines()
        for line in lines:
            raw_line = line.strip()
            trimed_line = "".join(raw_line.split("#")[:-1]).lstrip().rstrip()
            if len(trimed_line) :
                print(f"trimed = {trimed_line}")
            final_line = "".join(trimed_line.split())
            if len(final_line) :
                print(f"final = {final_line}")