#!python3
from lib.run import run
from lib.update import update
from rich import print

import argparse

parser = argparse.ArgumentParser(
        description="Bypass windows administrator password requirement popup"
    )

subparsers = parser.add_subparsers(
    title="Comandos",
    description="Comandos disponibles",
    dest="command",
    required=True
)

# Subcomando: hello
hello_parser = subparsers.add_parser("hello", help="link the executable file")

# Subcomando: run
run_parser = subparsers.add_parser("run", help="run a exploit")
run_parser.add_argument("EXPLOIT", type=str, help="Exploit")
run_parser.add_argument("MODE", type=str, help="mode")
run_parser.add_argument("INPUT1", type=str, help="input1", nargs="?")
run_parser.add_argument("INPUT2", type=str, help="input2", nargs="?")

# Subcomando: update
run_parser = subparsers.add_parser("update", help="update keys")

args = parser.parse_args()

print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠚⠉⠀⠀⠉⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀     ") 
print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀      ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀     ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣠⠔⠋⠉⣩⣍⠉⠙⠢⣄⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀    ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢧⡜⢏⠓⠒⠚⠁⠈⠑⠒⠚⣹⢳⡸⠀⠀⠀⠀⠀⠀⠀⠀    ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠸⡄⠀⠀⠀⠀⠀⠀⢠⠇⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀     ")
print("⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⢣⡙⢦⡀⠀⠀⢀⡰⢋⡜⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀   ")
print("⠀⠀⠀⠀⠀⡴⠁⢀⣀⣀⣀⣙⣦⣉⣉⣋⣉⣴⣋⣀⣀⣀⡀⠈⢧⠀⠀⠀⠀⠀  ")
print("⠀⠀⠀⠀⡸⠁⠀⢸⠀⠀⠀⠀⢀⣔⡛⠛⡲⡀⠀⠀⠀⠀⡇⠀⠈⢇⠀⠀⠀⠀   ")
print("⠀⠀⠀⢠⠇⠀⠀⠸⡀⠀⠀⠀⠸⣼⠽⠯⢧⠇⠀⠀⠀⠀⡇⠀⠀⠘⡆⠀⠀⠀    ")
print("⠀⠀⠀⣸⠀⠀⠀⠀⡇⠀⠀⠀⠳⢼⡦⢴⡯⠞⠀⠀⠀⢰⠀⠀⠀⠀⢧⠀⠀⠀    ")
print("⠀⠀⠀⢻⠀⠀⠀⠀⡇⠀⠀⠀⢀⡤⠚⠛⢦⣀⠀⠀⠀⢸⠀⠀⠀⠀⡼⠀⠀⠀    ")
print("⠀⠀⠀⠈⠳⠤⠤⣖⣓⣒⣒⣒⣓⣒⣒⣒⣒⣚⣒⣒⣒⣚⣲⠤⠤⠖⠁⠀⠀⠀  ")
print("⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀  ")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ")
print(" ")


# Ejecutar comandos
if args.command == "hello":
    print("[red]welcome back legend[/red]")
elif args.command == "run":
    run(args.EXPLOIT,args.MODE,args.INPUT1,args.INPUT2)
elif args.command == "update":
    update()