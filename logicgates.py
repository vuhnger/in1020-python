
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
            return not A ^ B

possible_combinations: list = [(True,True), (True, False), (False, True), (False, False)]

logic_gates: list = ['and', 'or', 'nand', 'nor', 'xor', 'xnor']

with open('truth_tables.txt', 'w', encoding='utf-8') as f:
    for gate in logic_gates:
        output: str = f'Truth table for {gate.upper()} gate\nA \tB \tResult'
        print(output)
        f.write(f"{output}\n")
        for combination in possible_combinations:
            A, B = combination
            output = f'{int(A)}\t{int(B)}\t{int(logic_operation(type=gate, A=A, B=B))}'
            print(output)
            f.write(f'{output}\n')