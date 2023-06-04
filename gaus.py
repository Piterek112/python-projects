import numpy as np

def solve_linear_system(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A.astype(float), b.astype(float)))  # Konwersja na typ float
    
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            for j in range(i+1, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
        
        for j in range(i+1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] -= factor * augmented_matrix[i]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented_matrix[i][-1] - np.dot(augmented_matrix[i][i+1:-1], x[i+1:])) / augmented_matrix[i][i]
    
    return x

# Przykład użycia
A = np.array([[2, 1, -1],
              [3, 2, 1],
              [1, -1, 2]], dtype=float)  # Ustalenie typu float

b = np.array([1, 4, 5], dtype=float)  # Ustalenie typu float

solution = solve_linear_system(A, b)
print("Rozwiązanie:")
print(solution)
