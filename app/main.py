import sys
import re

def main():
    # TODO: Uncomment the code below to pass the first stage
   
    while True:
        sys.stdout.write("$ ")
        command = input()
        out = re.search("^echo",command)
        type_check = re.search("^type",command)
        if command == "exit":
            exit()
        elif out:
            print(command[5:])
        elif type_check:
            ans = command[5:]
            if ans == "echo" or ans == "type" or ans=="exit":
                print(f"{ans} is a shell builtin")
            else:
                print(f"{ans}: not found")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
