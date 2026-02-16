import sys
import re

def main():
    # TODO: Uncomment the code below to pass the first stage
   
    while True:
        sys.stdout.write("$ ")
        command = input()
        out = re.search("^echo",command)
        if command == "exit":
            exit()
        if out:
            print(command[5:])
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()
