import sys
import re
import os

def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = {"echo","type","exit"}
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            user_input = input().strip()
        except EOFError: # Handles Ctrl+D gracefully
            break

        if not user_input:
            continue

        parts = user_input.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "exit":
            # CodeCrafters usually requires an exit code (0)
            sys.exit(0)

        elif cmd == "echo":
            # Join all arguments back with a single space
            print(" ".join(args))

        elif cmd == "type":
            target = args[0] if args else ""
            if target in builtins:
                print(f"{target} is a shell builtin")
            else:
                print(f"{target}: not found")

        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
