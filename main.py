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

def calculate(oper,A,B):
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
    print("WELCOME TO CALCULATOR\n\n")

    if A is not None and B is not None and OPERATOR is not None:
        print(f"{A} {OPERATOR} {B} = {C}")
    else:
        print("A OPERATOR B")

    try:
        A = int(input("ENTER A : ")) | 0
        B = int(input("ENTER B : ")) | 0

        raw = input("ENTER OPERATOR(+, -, *, /): ") | None
    except:
        A = None
        B = None
        raw = None
        print("\n----- INPUT IS ERROR! -----\n")

    if raw in VALID_OPS:
        OPERATOR = cast(OP, raw)
    else:
        print("Invalid operator")
        OPERATOR = None

    C = calculate(OPERATOR,A,B)
    
    while True:
            choice = questionary.select(
                "AGAIN?",
                choices=[
                    "Yes",
                    "No"
                ]
            ).ask()

            if choice == "No":
                isVerify = False
                break
            else:
                break
            

    print("\033[H\033[J", end="")