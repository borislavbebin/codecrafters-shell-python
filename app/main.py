import sys
import shutil
import subprocess
import os


def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        else:
            args = command.split()
            if args[0] == "echo":
                print(" ".join(args[1:]))
            elif path := shutil.which(args[0]):
                subprocess.run(args)
            elif args[0] == "type":
                if args[1] in ["exit", "echo", "type", "pwd", "cd"]:
                    print(f"{args[1]} is a shell builtin")
                elif path := shutil.which(args[1]):
                    print(f"{command[5:]} is {path}")
                else:
                    print(f"{' '.join(args[1:])}: not found")
            elif args[0] == "pwd":
                print(os.getcwd())
            elif args[0] == "cd":
                try:
                    os.chdir(args[1])
                except FileNotFoundError:
                    print(f"cd: {args[1]}: No such file or directory")
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
