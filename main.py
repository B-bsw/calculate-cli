from typing import Literal, cast

import questionary

print("\033[H\033[J", end="")

OP = Literal["+", "-", "*", "/"]
isVerify = True

OPERATOR: OP | None = None
A: int | None = None
B: int | None = None
C: float

VALID_OPS: set[OP] = {"+", "-", "*", "/"}

# COLORS
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def calculate(oper, A, B):
    match oper:
        case "*":
            return A * B
        case "+":
            return A + B
        case "-":
            return A - B
        case "/":
            if B == 0:
                return 0
            return A / B
        case _:
            return 0


while isVerify:
    print(f"{CYAN}WELCOME TO CALCULATOR\n{RESET}")
    print(f"{GREEN}Example: 2+2\n{RESET}")

    try:
        expr = input("INPUT: ").replace(" ", "")

        found_op = None
        for op in VALID_OPS:
            if op in expr:
                found_op = op
                break

        if found_op is None:
            raise ValueError("Invalid operator")

        left, right = expr.split(found_op)

        A = int(left)
        B = int(right)
        raw = found_op

    except KeyboardInterrupt:
        break
    except:
        A = None
        B = None
        raw = None
        print(f"\n{RED}----- INPUT IS ERROR! -----{RESET}\n")
        print("\033[H\033[J", end="")
        continue

    if raw in VALID_OPS:
        OPERATOR = cast(OP, raw)
    else:
        OPERATOR = None

    C = calculate(OPERATOR, A, B)

    print(f"\nOUTPUT: {C}\n")

    choice = questionary.select("AGAIN?", choices=["Yes", "No"]).ask()

    if choice == "No":
        isVerify = False

    print("\033[H\033[J", end="")
