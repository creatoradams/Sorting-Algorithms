from matplotlib import pyplot as plt

from algorithms import bubbleSort
from algorithms import mergeSort
from algorithms import quickSort
from algorithms import randomNumbers
from algorithms import Timer
from algorithms import selectionSort   # kept for completeness; slot #4 remains the PDF placeholder
import numpy as np
import random
import matplotlib
import pandas as pd

SIZES = [100, 1000, 10000, 100000]

# the algorithms variables are declared in ALGOS and run_case


# graph the number of comparisons performed and time spent with data size

""" ------ Data generators for best/worst/average ------- """

def best(n: int):
    return list(range(n))

def worst(n: int):
    return list(range(n, -1, -1 -1))

def avg(n: int):
    return [random.randint(0, 10**6) for i in range(n)]


""" assign algorithms """
bs = bubbleSort.BubbleSort()
bubble = bs.bubble_sort

# mergeSort returns a new python list
ms = mergeSort.MergeSort()
merge = ms.sort

# quicksort: expects and returns numpy array
quick = lambda L: quickSort.QuickSort.sort(np.array(L)).tolist()

# selectionsort also expects and returns numpy arrays
select = lambda L: selectionSort.SelectionSort.sort(np.array(L)).tolist()

""" -------- Menu mappings --------- """

ALGOS = {
    1: ("Bubble Sort", bubble),
    2: ("Merge Sort", merge),
    3: ("Quick Sort", quick),
    4: ("Selection Sort", select),
}

CASES = \
{
    1: ("Best Case", best),   # case #1
    2: ("Average Case", avg), # case #2
    3: ("Worst Case", worst), # case #3
}

""" -------- Prompts for user --------- """

def prompt(msg: str) -> bool:
    while True:
        t = input(msg).strip().lower()
        if t in ("y", "yes"): return True
        if t in ("n", "no"): return False
        print("Please respond with 'y' or 'n'.")

def promptInt(msg: str, low: int, high: int) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if low <= v <= high:
                return v
        except ValueError:
            pass
        print(f"Enter a number between {low} and {high}.")


""" -------- Run the chosen algorithm --------- """

def run(algKey: int):
    alg_name, alg_func, = ALGOS[algKey]

    if alg_func is None:
        print("\n(This sorting algorithm isn't implemented yet")

    while True:
        print(f"\nCase Scenarios for {alg_name}:")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print(f"4. Back")
        c = promptInt("\nSelect the case (1-4): ", 1, 4)
        if c == 4:
            return

        caseName, gen = CASES[c]
        print(f"\nIn {caseName.lower()},")

        # build a case generator that returns a list. Timer copies it
        def case_gen(n: int):
            arr = gen(n)
            return list(arr)

        # time the algorithm on all cases
        times = Timer.Time.timeMany(alg_func, SIZES, case_gen)  # creating variable
        plotTimes(alg_name, caseName, SIZES, times)

        # Print a simple runtime table
        print("\n  N         Time (seconds)")
        print("  ------------------------")
        for n, t in zip(SIZES, times):
            if n == 100:
                print(f"For N = {n},   it takes {t:.6f} seconds")
            elif n == 1000:
                print(f"For N = {n},  it takes {t:.6f} seconds")
            else:
                print(f"For N = {n}, it takes {t:.6f} seconds")

        while prompt("\nTest another N for this case? (y/n): "):
            n2 = promptInt("Enter N: ", 1, 10_000_000)
            t2 = Timer.Time.timeMany(alg_func, [n2], case_gen, trials=3)[0]
            print(f"For N = {n2}, time = {t2:.6f} s")

        print(f"\nCase Scenarios for {alg_name}")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print(f"4. Exit {alg_name.lower()} test")

""" ---- DISPLAY GRAPH ---- """
def plotTimes(alg_name: str, case_name: str, sizes, times):
    """ Show a runtime chart for one algorithm/case. """
    x = np.array(sizes, dtype=float)
    y = np.array(times, dtype=float)

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n (log scale)')
    plt.ylabel('T(n) seconds (log scale)')
    plt.title(f'{alg_name} — {case_name}')
    plt.grid(True, which='both', linestyle=':')
    plt.tight_layout()
    plt.show()




""" -------- Main menu --------- """

def main():
    print("Welcome to the test suite of selected sorting algorithms!\n")
    while True:
        print("Select the sorting algorithm you want to test.")
        print("-------------------------")
        for k in sorted(ALGOS):
            print(f"{k}. {ALGOS[k][0]}")
        print(f"{max(ALGOS)+1}. Exit")

        sel = promptInt(f"Select a sorting algorithm (1-{max(ALGOS)+1}): ", 1, max(ALGOS)+1)
        if sel == max(ALGOS) + 1:
            print("\nBye!")
            break
        run(sel)



if __name__ == "__main__":
    np.random.seed(42)
    main()