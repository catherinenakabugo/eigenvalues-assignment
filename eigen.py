import numpy as np

# Define the matrix B
B = np.array([[3, 1],
              [0, 2]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(B)

# Display the results
print("Matrix B:")
print(B)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors (each column corresponds to an eigenvalue):")
print(eigenvectors)
