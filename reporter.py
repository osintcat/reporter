import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit(f"python3 {sys.argv[0]} tabletype(1/2)")

tabletype = sys.argv[1]

def info_table(data, num, headers):
    if num == "1":
        return tabulate.tabulate(data, tablefmt="fancy_grid")
    elif num == "2":
        return tabulate.tabulate(data, headers, tablefmt="fancy_grid")

def table_input(num, headers = ""):
    contents = []
    print("Type data in\neg name: John Doe\npress CTRL-D to save\n")
    while True:
        try:
            line = input()
        except EOFError:
            break
        info = line.split(":", 1)
        first = info[0].lstrip()
        second = info[1].lstrip()
        contents.append([first, second])
    print(info_table(contents, num, headers))
    return info_table(contents, num, headers)

def save_to_file(info):
    filename = input("filename: ")
    file = open(filename, "a+")
    file.write(info + "\n")
    file.close()
    print(f"output saved to: {filename}")

if tabletype == "1":
    info = table_input("1")
    savetofile = input("would you like to save the output to a file?(y/n): ")
    if savetofile.lstrip().lower() == "y":
        save_to_file(info)
elif tabletype == "2":
    headers = input("format:header0,header1,header2\neg. Social Network,Usernames\nheaders:").split(",")
    info = table_input("2", headers)
    savetofile = input("would you like to save the output to a file?(y/n): ")
    if savetofile.lstrip().lower() == "y":
        save_to_file(info)
