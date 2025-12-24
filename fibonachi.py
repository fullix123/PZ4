import time
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
def fib_iter(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def fib_rec(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_rec(n - 1, memo) + fib_rec(n - 2, memo)
    return memo[n]



N = 50

start = time.perf_counter()
fib_iter_result = fib_iter(N)
end = time.perf_counter()
logging.info(f"Iterativnaya Fib({N}) = {fib_iter_result}")
logging.info(f"Iterativnaya time: {end - start:.6f} sec")

start = time.perf_counter()
fib_rec_result = fib_rec(N)
end = time.perf_counter()
logging.info(f"Recusrs Fib({N}) = {fib_rec_result}")
logging.info(f"Resurs time: {end - start:.6f} sec")
