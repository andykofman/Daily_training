import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def create_grid(nx, ny):
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    return np.meshgrid(x, y)

def set_boundary_conditions(A, b, nx, ny, potentials):
    for i in range(nx):
        for j in range(ny):
            idx = i * ny + j
            if not np.isnan(potentials[i, j]):
                A[idx, :] = 0
                A[idx, idx] = 1
                b[idx] = potentials[i, j]

def fdm_discretization(nx, ny, epsilon):
    A = lil_matrix((nx * ny, nx * ny))
    b = np.zeros(nx * ny)

    dx = 1 / (nx - 1)
    dy = 1 / (ny - 1)

    for i in range(1, nx-1):
        for j in range(1, ny-1):
            idx = i * ny + j
            A[idx, idx] = -2 * (1 / dx**2 + 1 / dy**2)
            A[idx, idx-ny] = 1 / dx**2
            A[idx, idx+ny] = 1 / dx**2
            A[idx, idx-1] = 1 / dy**2
            A[idx, idx+1] = 1 / dy**2

    return A, b

def solve_system(A, b):
    return spsolve(A.tocsr(), b)

def compute_capacitance(potentials, epsilon):
    return np.sum(potentials) / (epsilon * len(potentials))

def visualize_grid(potentials):
    plt.imshow(potentials, cmap='viridis', origin='lower')
    plt.colorbar(label='Potential (V)')
    plt.title('2D Potential Distribution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    # Get user input for grid size
    nx = int(input("Enter the number of grid points in the x-direction (nx): "))
    ny = int(input("Enter the number of grid points in the y-direction (ny): "))
    
    grid = create_grid(nx, ny)
    
    # Get user input for epsilon
    epsilon = np.ones((nx, ny))
    custom_epsilon = input("Do you want to enter custom epsilon values? (yes/no): ").strip().lower()
    if custom_epsilon == 'yes':
        for i in range(nx):
            for j in range(ny):
                epsilon[i, j] = float(input(f"Enter epsilon value at ({i}, {j}): "))

    # Initialize potentials with NaN
    potentials = np.full((nx, ny), np.nan)
    
    # Get user input for conductors
    num_conductors = int(input("Enter the number of conductors: "))
    for _ in range(num_conductors):
        conductor_potential = float(input("Enter the potential for the conductor: "))
        x_start = int(input("Enter the x-start index for the conductor: "))
        x_end = int(input("Enter the x-end index for the conductor: "))
        y_start = int(input("Enter the y-start index for the conductor: "))
        y_end = int(input("Enter the y-end index for the conductor: "))
        potentials[x_start:x_end, y_start:y_end] = conductor_potential

    # Set boundary conditions (example: Dirichlet boundary conditions)
    potentials[0, :] = 0
    potentials[-1, :] = 0
    potentials[:, 0] = 0
    potentials[:, -1] = 0

    A, b = fdm_discretization(nx, ny, epsilon)
    set_boundary_conditions(A, b, nx, ny, potentials)
    
    solved_potentials = solve_system(A, b).reshape((nx, ny))
    
    capacitance = compute_capacitance(solved_potentials, epsilon[0, 0])
    print("Capacitance per unit length:", capacitance)
    
    # Visualize the grid
    visualize_grid(solved_potentials)

if __name__ == "__main__":
    main()
