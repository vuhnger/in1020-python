
def logic_operation(type: str, A: bool, B: bool) -> bool:
    match type:
        case 'and':
            return A and B
        case 'or':
            return A or B
        case 'nand':
            return not (A and B)
        case 'nor':
            return not (A or B)
        case 'xor':
            return A ^ B
        case 'xnor':
            return not (A ^ B)

possible_combinations: list = [(True,True), (True, False), (False, True), (False, False)]

logic_gates: list = ['and', 'or', 'nand', 'nor', 'xor', 'xnor']

with open('truth_tables.txt', 'w', encoding='utf-8') as table:
    for gate in logic_gates:
        header: str = f'Truth table for {gate.upper()} gate\nA \tB \tResult'
        print(header)
        table.write(f"{header}\n")
        for combination in possible_combinations:
            A, B = combination
            table_row = f'{int(A)}\t{int(B)}\t{int(logic_operation(type=gate, A=A, B=B))}'
            print(table_row)
            table.write(f'{table_row}\n')