import time

"""
Times one run on a copy of data and returns the elapsed time in seconds
"""
class Time:

  def timeOnce(alg_func, data, check=True):
      work = list(data) #mutable copy for swapping

      start = time.perf_counter()
      result = alg_func(work)
      elapsed = time.perf_counter() - start

      if check:
          expected = sorted(list(data))
          if result is None:
              out_seq = work
          else:
              try:
                  out_seq = list(result)
              except TypeError:
                  out_seq = result.tolist()
          if out_seq != expected:
              raise AssertionError('The result is not equal to the expected result')


  def timeMany(alg_func, size_list, case_gen, trials=1, check=True):
      """
      For each num in `size_list`, build input via `case_gen(n)` and time `alg_func`
      over `trials` runs. Returns a list of average times.
      """
      results = []
      for n in size_list: # loop over input sizes
          total = 0.0
          for _ in range(trials): # run multiple trials
              data = case_gen(n)
              total += Time.timeOnce(alg_func, data, check=check)
          results.append(total / trials) # avg runtime
      return results # list of runtimes