
from algorithms import bubbleSort
from algorithms import mergeSort
from algorithms import quickSort
from algorithms import randomNumbers
from algorithms import Timer
from algorithms import selectionSort   # kept for completeness; slot #4 remains the PDF placeholder
import numpy


                # the algorithms variables are declared in ALGOS and run_case


# Selection Sort Algorithm

# Display runtime table for each size array

# graph the number of comparisons performed and time spent with data size




""" ------ Data generators for best/worst/avg ------- """


def gen_best(n, alg_name):
    return list(range(n))

def gen_worst(n, alg_name):
    return list(range(n, 0, -1))

def gen_avg(n, alg_name):
    return [random.randint(0, 10**6) for _ in range(n)]




""" -------- Menu mappings --------- """

ALGOS = {
    1: ("Bubble Sort", bubbleSort.bubbleSort().bubble_sort),
    2: ("Merge Sort", mergeSort.mergeSort().sort),
    3: ("Quick Sort", (lambda data: quickSort.quickSort.sort(numpy.array(list(data))))),
    4: ("Selection Sort (replacing this line with the algorithm )", None),  # still needs to be done
}

CASES = \
{
    ("Best Case", gen_best),   # case #1
    ("Average Case", gen_avg), # case #2
    ("Worst Case", gen_worst), # case #3
}


""" -------- Prompts --------- """

def prompt_yes_no(smg: str) -> bool:
    while True:
        t = input(msg).strip().lower()
        if t in ("y", "yes"): return True
        if t in ("n", "no"): return False
        print("Please respond with 'y' or 'n'.")

def prompt_int(msg: str, lo: int, hi: int) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if lo <= v <= hi:
                return v
        except ValueError:
            pass
        print(f"Enter a number between {lo} and {hi}.")


""" -------- Run a chosen algorithm --------- """

def run_case(alg_key: int):
    alg_name, alg_func, = ALGOS[alg_key]

    print(f"\nCase Scenarios for {alg_name}:")
    print("---------------")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print(f"4. Exit {alg_name.lower()} test")

    if alg_func is None:
        print("\n(This sorting algorithm isn't implemented yet")

    while True:
        c = prompt_int("\nSelect the case (1-4): ", 1, 4)
        if c == 4:
            return
        case_name, gen = CASES[c]
        print(f"\nIn {case_name.lower()},")

        sizes = randomNUmbers.randomNumbers(SIZES)  # creating variable

        def case_gen(n):
            arr = gen(n)
            try:
                return list(arr)
            except TypeError:
                return arr.tolist()

        times = Timer.Time.timeMany(alg_func, sizes. case_gen)  # creating variable

        for n, t in zip(sizes, times):
            if n == 100:
                print(f"For N = {n},   it takes {t:.6f} seconds")
            elif n == 1000:
                print(f"For N = {n},  it takes {t:.6f} seconds")
            else:
                print(f"For N = {n}, it takes {t:.6f} seconds")

        while prompt_yes_no("\nDo you want to input another N (Y/N)?"):
            n2 = int(input("What is the N? ").strip())
            t2 = Timer.Time.timeMany(alg_func, [n2], case_gen)[0]  # creating variable, dont know if could put these all up at the top together with ALGOS or not
            print(f"\nFor N = {n2}, it takes {t2:.6f} seconds")

        print(f"\nCase Scenarios for {alg_name}")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print(f"4. Exit {alg_name.lower()} test")

""" -------- Main menu --------- """

def main():
    print("Welcome to the test suite of selected sorting algorithms!\n")
    while True:
        print("Select the sorting algorithm you want to test.")
        print("-------------------------")
        for k in sorted(ALGOS):
            print(f"{k}. {ALGOS[k][0]}")
        print(f"{max(ALGOS)+1}. Exit")

        sel = prompt_int(f"Select a sorting algorithm (1-{max(ALGOS)+1}): ", 1, max(ALGOS)+1)
        if swl == max(ALGOS) + 1:
            print("\nBye!")
            break
        run_case(sel)

if __name__ == "__main__":
    numpy.random.seed(42)
    main()