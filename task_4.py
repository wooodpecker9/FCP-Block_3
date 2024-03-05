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
    
    '''

    t = np.linspace(0, t_max)
    lotka = odeint(diff_lotka_volterra, lotka0, t, (alpha, beta, delta, gamma))

    return lotka, t

def plot_lotka(t, data):
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax1.plot(t, data[:, 0], label='x(t)')
    ax2 = fig.add_subplot(312)
    ax2.plot(t, data[:, 1], label='y(t)')

    plt.show()


# Main function
def main():
    return

if __name__ == "__main__":
    main()