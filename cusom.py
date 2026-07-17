class Range:
  def __init__(self,stop):
    self.stop = stop
    self.start = 0
  def __iter__(self):
    return self
  def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current += 1
        return value