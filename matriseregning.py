import numpy as np
import time
from multiprocessing import Pool
import sys

# Sum up matrice value manually by row
def traverse_by_row(matrice: list, matrice_size: int) -> int:
    total: int = 0
    start_tid: int = time.time()
    for i in range(matrice_size):
        for j in range(matrice_size):
            total += matrice[i, j]
    slutt_tid: int = time.time()
    assert total == matrice_size * matrice_size
    return slutt_tid - start_tid

# Sum up matrice value manually by col instead of row
def traverse_by_col(matrice: list, matrice_size: int) -> int:
    total: int = 0
    start_tid: int = time.time()
    for j in range(matrice_size):
        for i in range(matrice_size):
            total += matrice[i, j]
    slutt_tid: int = time.time()
    assert total == matrice_size * matrice_size
    return slutt_tid - start_tid

def main():

    n: int = 5

    matrice_size = 100
    with open('resultat-matriseregning.txt', 'w', encoding='utf-8') as f:

        while matrice_size < 12_000:
        
            # Initialize a matrice of ones by variable size
            matrise: list = np.ones((matrice_size, matrice_size), dtype=int)


            # Compute sums with threading and store timestamps in separate arrays
            with Pool() as pool:
                print(f"Starting row traversals, matrice_size: {matrice_size}")
                row_times: list = pool.starmap(traverse_by_row, [(matrise, matrice_size) for _ in range(n)]) # Map functions to input
                print(f"Starting col traversals, matrice_size: {matrice_size}")
                col_times: list = pool.starmap(traverse_by_col, [(matrise, matrice_size) for _ in range(n)])

            avg_row: int = sum(row_times) / n
            avg_col: int = sum(col_times) / n

            res_row: str = f"Avg row time for {n} runs: {avg_row}s"
            res_col: str = f"Avg col time for {n} runs: {avg_col}s"
            diff: str = f"Difference: {abs(avg_col-avg_row)}s with matrice size {matrice_size}x{matrice_size}"
            print(f"{res_row}\n{res_col}\n{diff}")
        
            f.write(f"{res_row}\n{res_col}\n{diff}")
            matrice_size = matrice_size*2
        


if __name__ == "__main__":
    main()
