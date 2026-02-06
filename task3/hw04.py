import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(path: Path, prefix: str = "") -> None:
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── " 
        next_prefix = prefix + ("    " if is_last else "│   ") # Adjust prefix for next level

        if entry.is_dir():
            print(prefix + connector + Fore.CYAN + entry.name + Style.RESET_ALL)
            print_tree(entry, next_prefix)
        else:
            print(prefix + connector + Fore.GREEN + entry.name + Style.RESET_ALL)


def main() -> None:
    init(autoreset=True) # Initialize colorama with autoreset

    if len(sys.argv) != 2:
        print("Usage: python hw04.py task3")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + "Error: path does not exist." + Style.RESET_ALL)
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + "Error: path is not a directory." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.CYAN + dir_path.name + Style.RESET_ALL)
    print_tree(dir_path)


if __name__ == "__main__":
    main()
