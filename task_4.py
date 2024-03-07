# Lotka-Volterra Model
# Imports
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import argparse


# Function definitions
def parse_command_line_arguments_with_argpparse():

    parser = argparse.ArgumentParser(description='Input data')
    parser.add_argument('-i', '--initial', type=int, metavar='N', nargs='+', required=True, help='Sets the initial values for both species')
    parser.add_argument('-a', '--alpha', type=int, metavar='N', nargs='+', required=True, help='Alpha values (Max of 5)')
    parser.add_argument('-b', '--beta', type=int, metavar='', required=True, help='Beta value (Only 1)')
    parser.add_argument('-d', '--delta', type=int, metavar='', required=True, help='Delta value (Only 1)')
    parser.add_argument('-g', '--gamma', type=int, metavar='', required=True, help='Gamma value (Only 1)')
    parser.add_argument('-s', '--save_plot', type=str, metavar='', help='Saves plot with provided file name')

    args = parser.parse_args()

    initial_values = args.initial
    if len(initial_values) > 2:
        print("Error: Too many initial inputs (Max of 2)")
        exit()
    
    alpha_values = args.alpha
    if len(alpha_values) > 5:
        print("Error: Too many alpha inputs (Max of 5)")
        exit()
    
    beta_value = args.beta

    delta_value = args.delta

    gamma_value = args.gamma

    if args.save_plot:
        save_plot = True
        save_plot_name = args.save_plot
    else:
        save_plot = False
        save_plot_name = ''
    
    return (initial_values, alpha_values, beta_value, delta_value, gamma_value, save_plot, save_plot_name)

def diff_lotka_volterra(lotka, t, alpha, beta, delta, gamma):
    '''
    alpha = birth rate of the prey
    beta = preys growth rate
    delta = predators death rate
    gamma = predators growth rate
    '''

    dxdt = (alpha * lotka[0]) - (beta * lotka[0] * lotka[1])
    dydt = (delta * lotka[0] * lotka[1]) - (gamma* lotka[1])

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

    ax1.set_title(f'Lotka-Volterra equations, alpha={alpha}')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Prey population')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Predator population')




# Main function
def main():
    '''
    allow a user to set the value of alpha, beta, delta and gamma
    '''
    initial_values, alpha_values, beta_value, delta_value, gamma_value, save_plot, save_plot_name = parse_command_line_arguments_with_argpparse()

    for alpha in alpha_values:
        diff_lotka_volterra(initial_values, 10, alpha, beta_value, delta_value, gamma_value)
        data, t = solve_lotka_volterra(initial_values, 10, alpha, beta_value, delta_value, gamma_value)
        plot_lotka(t, data, alpha)
        if save_plot == True:
            plt.savefig(save_plot_name)
        else:
            plt.show()
    return

if __name__ == "__main__":
    main()