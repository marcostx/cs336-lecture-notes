import torch

def test_matrix_multiplication():
  """Simple matrix multiplication test using PyTorch"""
  # Create two random matrices
  a = torch.randn(3, 4)
  b = torch.randn(4, 5)
  
  # Perform matrix multiplication
  c = torch.matmul(a, b)
  
  print(f"Matrix A shape: {a.shape}")
  print(f"Matrix B shape: {b.shape}")
  print(f"Result C shape: {c.shape}")
  print(f"\nMatrix A:\n{a}")
  print(f"\nMatrix B:\n{b}")
  print(f"\nMatrix C (A @ B):\n{c}")

  d = torch.ones(16, 32)
  e = torch.ones(32, 2)

  f = d @ e

  assert f.size() == torch.Size([16, 2])



if __name__ == "__main__":
  print("\n" + "="*50)
  print("Testing PyTorch matrix multiplication:")
  print("="*50)
  test_matrix_multiplication()