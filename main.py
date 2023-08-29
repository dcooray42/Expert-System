from argparse import ArgumentParser
from file import read_file

def main() :
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="File to read")
    args = parser.parse_args()
#    try :
    args = vars(args)
    read_file(**args)
#    except Exception as e :
#        print(str(e))
#        parser.print_help()

if __name__ == "__main__" :
    main()