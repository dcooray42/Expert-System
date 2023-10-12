from argparse import ArgumentParser
from data import ExpertSystem
from engine import backward_chain
from file import read_file

def main():
    es = ExpertSystem()
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="File to read")
    args = parser.parse_args()
#    try:
    args = vars(args)
    read_file(es, **args)
    for query in es.queries:
        print(f"asdfoiuhoidsfiouh query : {query.fact} {len(query.rules)}")
        backward_chain(query)
    print("Queries:")
    for query in es.queries:
        print(f"{query.fact} is {query.value}")
#    except Exception as e:
#        print(str(e))
#        parser.print_help()

if __name__ == "__main__":
    main()