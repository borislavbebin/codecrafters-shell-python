import sys


def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        else:
            commands = command.split(" ")
            if commands[0] == "echo":
                print(" ".join(commands[1:]))
                continue
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
