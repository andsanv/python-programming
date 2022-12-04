def to_float(num):
    try:
        num = float(num)
    except ValueError:
        print(msg[1])
        num = "convertion_error"

    return num

def is_one_digit(x):
    output = False

    if x > -10.0 and x < 10.0 and x.is_integer():
        output = True
    
    return output

def check(x, y, op):
    message = ""

    if is_one_digit(x) and is_one_digit(y):
        message = message + msg[6]
    if (x == 1 or y == 1) and op == '*':
        message = message + msg[7]
    if (not x or not y) and (op == '*' or op == '+' or op == '-'):
        message = message + msg[8]
    
    if message != "":
        message = msg[9] + message
        print(message)
    
    return

def convert(x, y):
    global memory

    if x != 'M':
        x = to_float(x)
    else:
        x = memory

    if y != 'M':
        y = to_float(y)
    else:
        y = memory

    return (x, y)

def calculate(x, y, op):
    x, y = convert(x, y)
    if "convertion_error" in (x, y):
        return "error"

    check(float(x), float(y), op)

    if op in "+-*/" and len(op) == 1:
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            try:
                return x / y
            except ZeroDivisionError:
                print(msg[3])
            return "error"
    else:
        print(msg[2])
        return "error"

def manage_memory(result):
    global memory
    print(msg[4])
    choice_1 = input()
    
    valid_outer = False
    valid_inner = False

    while not valid_outer:
        valid_outer = True
        if choice_1 == 'y':
            if is_one_digit(result):
                msg_index = 10

                while not valid_inner:
                    valid_inner = True
                    print(msg[msg_index])
                    choice_2 = input()

                    if choice_2 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            valid_inner = False
                        else:
                            memory = result
                    elif choice_2 == 'n':
                        break
                    else:
                        valid_inner = False
            else:
                memory = result
                break
        elif choice_1 == 'n':
            break
        else:
            valid_outer = False
    
    return

def stay_in():
    print(msg[5])
    choice = input()
    
    while True:
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
            

        
msg = ("Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)")

memory = 0



while True:
    print(msg[0])
    calc = input()
    ops = calc.split()

    result = calculate(ops[0], ops[2], ops[1])
    
    if result == "error":
        continue
    
    print(result)

    manage_memory(result)
    
    if not stay_in():
        break