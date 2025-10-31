from collections import defaultdict

class BPETokenParams:
  def __init__(self, indices: list[int], merges: dict[tuple[int, int], int]):
    self.indices = indices
    self.merges = merges

def merge(indices: list[int], pair: tuple[int, int], new_index: int) -> list[int]:
  return [new_index if i in pair else i for i in indices]

def bpe_algorithm(string: str, n_merges: int) -> BPETokenParams:
  """ Byte Pair Encoding algorithm """
  # list of bytes in the string
  indices =   list(map(int, string.encode("utf-8")))
  # merges to be done
  merges: dict[tuple[int, int], int] =  {}
  # vocabulary
  vocab: dict[int, bytes] = {i: bytes(i) for i in range(256)}

  for _ in range(n_merges):
    counts = defaultdict(int)
    for index1, index2 in zip(indices, indices[1:]):
      counts[(index1, index2)] += 1

    # find the most common pair
    pair = max(counts, key=counts.get)
    index1, index2 = pair

    # merge the pair
    new_index = 251 + _
    merges[pair] = new_index

    vocab[new_index] = vocab[index1] + vocab[index2]
    indices = merge(indices, pair, new_index)

  return BPETokenParams(indices, merges)

if __name__ == "__main__":
  string = "hello world"
  n_merges = 10
  params = bpe_algorithm(string, n_merges)
  print(f"Indices: {params.indices}")

