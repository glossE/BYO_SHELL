import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command = " "
    while command:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            exit()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
