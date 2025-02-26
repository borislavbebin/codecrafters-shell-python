import sys
import shutil


def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        else:
            args = command.split(" ")
            if args[0] == "echo":
                print(" ".join(args[1:]))
                continue
            elif args[0] == "type":
                if args[1] in ["exit", "echo", "type"]:
                    print(f"{args[1]} is a shell builtin")
                    continue
                elif path := shutil.which(args[1]):
                    print(f"{args[1:]} is {path}")
                else:
                    print(f"{' '.join(args[1:])}: not found")
                    continue
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
