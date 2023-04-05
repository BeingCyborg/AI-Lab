import random
import math


def calculate_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[j] < state[i]:
                cost += 1
    return cost


def neighbor_state(current_state):
    neighbor = current_state.copy()
    i, j = random.sample(range(len(current_state)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def simulated_annealing_sort(initial_state):
    T = 1.0
    alpha = 0.99
    stopping_T = 0.00001

    current_state = initial_state
    current_cost = calculate_cost(current_state)

    
    while T > stopping_T:
        print(current_state,current_cost)
        neighbor = neighbor_state(current_state)
        neighbor_cost = calculate_cost(neighbor)
        energy_difference = neighbor_cost - current_cost

        # Decide whether to accept the neighbor state
        if energy_difference < 0:
            current_state = neighbor
            current_cost = neighbor_cost
        else:
            probability = math.exp(-energy_difference / T)
            if random.uniform(0,1) < probability:
                current_state = neighbor
                current_cost = neighbor_cost

        # Decrease the temperature
        T = T * alpha

    return current_state


def main():
    initial_state = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    sorted_state = simulated_annealing_sort(initial_state)

    print(
        f"Final State : {sorted_state} Cost : {calculate_cost(sorted_state)}")


main()
