def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently: "
        for index, name in enumerate(katz_deli, start=1):
            current_line += f"{index}. {name} "
        print(current_line.strip())

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = katz_deli.index(name) + 1
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        next_in_line = katz_deli.pop(0)
        print(f"Currently serving {next_in_line}.")
