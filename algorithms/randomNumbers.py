import random
import numpy as np
class RandomNumbers:
    SIZES = (100, 1000, 10000, 100000) # testing number sets

    """ Average case """
    def average(num: int, low: int = 0, high: int = None) -> np.ndarray:
        return np.random.randint(low, high, size=num)

    """ best case """
    def best(n: int) -> np.ndarray:
        return np.arange(n)

    """ worst case """
    def worst(n: int) -> np.ndarray:
        return np.arange(n)

    """ build a dictionary of array sizes """
    def generate(cls, case: str = "Avg", unique: bool = False) -> dict[int, np.ndarray]:
        out: dict[int, np.ndarray] = {}
        for num in cls.SIZES:
            if case == "best":
                arr = cls.best(num)
            elif case == "worst":
                arr = cls.worst(num)
            else:
                arr = cls.average(num)
            out[num] = arr
        return out
