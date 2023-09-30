import random 

MAX_LINE = 5
MAX_BET = 100
MIN_BET = 1 

ROWS = 5 
COLS = 5

# Creating a dictionary containing symbol and it's rarity (the lower the higher rarity)
symbol_count = {
    "S": 2, 
    "A": 4, 
    "B": 6,
    "C": 8
}
# Creating a dictionary containing the price multiplier of each symbol tier
symbol_values = {
    "S": 16, 
    "A": 8, 
    "B": 4,
    "C": 2
}

def check_wining(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
         # "_" is an anonymous symbols in Python when we don't care about iteration number
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = "|")
            else:
                print(column[row], end = "")
        #skip to new line 
        print()

def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break 
            else:
                print("Amount must be great than 0.")
        else:
            print("Please enter a number.")

    return amount 

def get_number_of_line():
    while True:
        lines = input(f"How many lines do you want to bet on (1-{MAX_LINE})? ")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINE:
                break 
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                print(f"Amount must be between ${MAX_BET} - ${MIN_BET}")
        else:
            print("Please enter a number.")

    return amount 

def play_game(balance):
    lines = get_number_of_line()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to bet that amount.")
            print(f'Your current balance is ${balance}.')
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_wining(slots, lines, bet, symbol_values)
    print(f'YOu won ${winnings}.')
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("Press ENTER to play (q to quit).")
        if answer == "q":
            break 
        balance += play_game(balance)
    print(f"you left with ${balance}")

main()

