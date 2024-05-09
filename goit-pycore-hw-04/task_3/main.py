from pathlib import Path
from colorama import Fore

p = Path("task_3/pictures")

def parse_file(path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)
        else:
            print(Fore.GREEN + f"       {el}")

def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(Fore.BLUE +f"   {el}")
            parse_file(path)
        else:
            print(Fore.GREEN + f"   {el}")

 
parse_folder(p)