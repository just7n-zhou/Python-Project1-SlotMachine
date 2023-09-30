symbol_values = {
    "S": 4, 
    "A": 3, 
    "B": 2,
    "C": 1
}

all_symbol = []

for i, j in symbol_values.items():
    for _ in range(j):
        all_symbol.append(i)

print(all_symbol)
