import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    r = np.random.random(data.shape[0])

    for _ in range(num_steps):
        r = (data @ r) / np.sqrt(np.sum((data @ r) ** 2))

    return float((r.T @ data @ r) / (r.T @ r)), r