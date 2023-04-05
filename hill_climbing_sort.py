

def calculate_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[j] < state[i]:
                cost += 1
    return cost


def state_genaration(current_state):
    count=0
    while True:
        current_state_cost = calculate_cost(current_state)
        print(current_state,current_state_cost)
        min_next_cost = 99999999
        min_next_state = None
        for j in range(len(current_state)):
            for i in range(j+1, len(current_state)):
                states = current_state.copy()
                states[j], states[i] = states[i], states[j]
                state_cost = calculate_cost(states)
                # print(states)
                count += 1
                if state_cost < min_next_cost:
                    min_next_cost = state_cost
                    min_next_state = states


        if min_next_cost < current_state_cost:
            current_state = min_next_state

        else:
        #     print(f'total states {count}')
                
            print(
                f"Final State : {current_state} Cost : {calculate_cost(current_state)}")
            break


def main():
    initial_list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    state_genaration(initial_list)


main()
