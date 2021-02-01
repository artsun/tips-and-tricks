"""
https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
https://habr.com/ru/post/337314/

 sequence
  +
  |
  v
   def __getitem__(self, index: int):
  +    ...
  |    raise IndexError
  |
  |
  |              def __iter__(self):
  |             +     ...
  |             |     return <iterator>
  |             |
  |             |
  +--> or <-----+        def __next__(self):
       +        |       +    ...
       |        |       |    raise StopIteration
       v        |       |
    iterable    |       |
           +    |       |
           |    |       v
           |    +----> and +-------> iterator
           |                               ^
           v                               |
   iter(<iterable>) +----------------------+
                                           |
   def generator():                        |
  +    yield 1                             |
  |                 generator_expression +-+
  |                                        |
  +-> generator() +-> generator_iterator +-+
"""

def fib(lim: int):
    n, prev, cur = 0, 0, 1
    while n < lim:
        yield prev
        prev, cur = cur, prev + cur
        n += 1

class FibonacciGenerator:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return result

    def __iter__(self):
        return self




