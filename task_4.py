# Lotka-Volterra Model
# Imports
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


# Function definitions
def diff_lotka_volterra(lotka, t, alpha, beta, delta, gamma):
    '''
    alpha = birth rate of the prey
    beta = preys growth rate
    delta = predators death rate
    gamma = predators growth rate
    '''

    dxdt = (alpha * lotka[0]) - (beta * lotka[0] * lotka[1])
    dydt = (delta * lotka[0] * lotka[1]) - (gamma * lotka[1])

    grad = [dxdt, dydt]

    return grad

def solve_lotka_volterra(lotka0, t_max, alpha, beta, delta, gamma):
    '''
    solve the Lotka-Volterra equations
    lotka0 = the initial conditions
    t_max = the maximum time
    '''

    t = np.linspace(0, t_max)
    lotka = odeint(diff_lotka_volterra, lotka0, t, (alpha, beta, delta, gamma))

    return lotka, t

def plot_lotka(t, data, alpha):
    '''
    plot the simulation results of the Lotka-Volterra equation and save it
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax1.plot(t, data[:, 0], label='x(t)')
    ax2 = fig.add_subplot(312)
    ax2.plot(t, data[:, 1], label='y(t)')

    ax1.set_title(f'Lotka-Volterra Simulation (Alpha={alpha})')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Prey Population Density')

    ax2.set_xlabel('Time')
    ax2.set_ylabel('Predator Population Density')

    save_filename = f'lotka_volterra_alpha={alpha}.png'
    plt.savefig(save_filename)
    print(f'Figure is saved as {save_filename}')


# Main function
def main():
    '''
    allow a user to set the value of alpha, beta, delta and gamma
    '''
    n = int(input('Enter how many values of alpha(up to 5): '))
    while n > 5:
        n = int(input('Please enter a value less than or equal to 5:'))
    all_alpha = []
    for i in range(0,n):
        alpha = int(input('Enter alpha: '))
        all_alpha.append(alpha)
    beta = int(input('Enter beta: '))
    delta = int(input('Enter delta: '))
    gamma = int(input('Enter gamma: '))
    for alpha in all_alpha:
        diff_lotka_volterra([1, 1], 10, alpha, beta, delta, gamma)
        data, t = solve_lotka_volterra([1, 1], 10, alpha, beta, delta, gamma)
        plot_lotka(t, data, alpha)

    return

if __name__ == "__main__":
    main()
