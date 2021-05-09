# Encodes the maze into an mdp
# Actions [1, 2, 3, 4] correspond to [north, south, east, west]
import planner
import planner_class


def text_to_matrix(address):
    maze_matrix = []
    data = open(address, "r")
    while True:
        row_str = data.readline()
        if (row_str == ""):
            break
        row_str = list(row_str.split())
        row = map(int, row_str)
        row = list(map(int, row_str))
        maze_matrix.append(row)
    data.close()
    return maze_matrix


def give_index(grid):
    state_index_matrix = grid
    state_index_counter = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] != 1:
                state_index_matrix[y][x] = state_index_counter
                state_index_counter += 1
            else:
                state_index_matrix[y][x] = None
    return state_index_matrix


reward = -1
terminal_reward = 1
disc_fac = 1


def matrix_to_mdp(state_index_matrix, address):
    matrix = text_to_matrix(address)
    state_set = []
    start_state = None
    end_state = []
    action_set = [0, 1, 2, 3]
    counter = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if matrix[y][x] == 1:
                pass
            else:
                state = planner_class.State(state_index_matrix[y][x], 4)
                counter += 1
                if matrix[y][x] == 0 or matrix[y][x] == 2:
                    for action_ind in action_set:
                        if action_ind == 0:
                            if y - 1 >= 0:
                                if state_index_matrix[y - 1][x] is not None:
                                    state.actions[0].nxt_states.append(state_index_matrix[y - 1][x])
                                    state.actions[0].rewards.append(reward)
                                    state.actions[0].prob.append(1)
                                    state.actions[0].set_action_func()
                                else:
                                    state.actions[0].nxt_states.append(state_index_matrix[y][x])
                                    state.actions[0].rewards.append(reward)
                                    state.actions[0].prob.append(1)
                                    state.actions[0].set_action_func()
                            else:
                                state.actions[0].nxt_states.append(state_index_matrix[y][x])
                                state.actions[0].rewards.append(reward)
                                state.actions[0].prob.append(1)
                                state.actions[0].set_action_func()

                        elif action_ind == 1:
                            if y + 1 <= len(matrix) - 1:
                                if state_index_matrix[y + 1][x] is not None:
                                    state.actions[1].nxt_states.append(state_index_matrix[y + 1][x])
                                    state.actions[1].rewards.append(reward)
                                    state.actions[1].prob.append(1)
                                    state.actions[1].set_action_func()
                                else:
                                    state.actions[1].nxt_states.append(state_index_matrix[y][x])
                                    state.actions[1].rewards.append(reward)
                                    state.actions[1].prob.append(1)
                                    state.actions[1].set_action_func()
                            else:
                                state.actions[1].nxt_states.append(state_index_matrix[y][x])
                                state.actions[1].rewards.append(reward)
                                state.actions[1].prob.append(1)
                                state.actions[1].set_action_func()

                        elif action_ind == 2:
                            if x + 1 <= len(matrix) - 1:
                                if state_index_matrix[y][x + 1] is not None:
                                    state.actions[2].nxt_states.append(state_index_matrix[y][x + 1])
                                    state.actions[2].rewards.append(reward)
                                    state.actions[2].prob.append(1)
                                    state.actions[2].set_action_func()
                                else:
                                    state.actions[2].nxt_states.append(state_index_matrix[y][x])
                                    state.actions[2].rewards.append(reward)
                                    state.actions[2].prob.append(1)
                                    state.actions[2].set_action_func()
                            else:
                                state.actions[2].nxt_states.append(state_index_matrix[y][x])
                                state.actions[2].rewards.append(reward)
                                state.actions[2].prob.append(1)
                                state.actions[2].set_action_func()

                        elif action_ind == 3:
                            if x - 1 >= 0:
                                if state_index_matrix[y][x - 1] is not None:
                                    state.actions[3].nxt_states.append(state_index_matrix[y][x - 1])
                                    state.actions[3].rewards.append(reward)
                                    state.actions[3].prob.append(1)
                                    state.actions[3].set_action_func()
                                else:
                                    state.actions[3].nxt_states.append(state_index_matrix[y][x])
                                    state.actions[3].rewards.append(reward)
                                    state.actions[3].prob.append(1)
                                    state.actions[3].set_action_func()
                            else:
                                state.actions[3].nxt_states.append(state_index_matrix[y][x])
                                state.actions[3].rewards.append(reward)
                                state.actions[3].prob.append(1)
                                state.actions[3].set_action_func()

                    if matrix[y][x] == 2:
                        start_state = state.index
                elif matrix[y][x] == 3:
                    end_state.append(state.index)
                    for action_ind in action_set:
                        state.actions[action_ind].nxt_states.append(state_index_matrix[y][x])
                        state.actions[action_ind].rewards.append(terminal_reward)
                        state.actions[action_ind].prob.append(1)
                state_set.append(state)
    mdp = planner_class.MDP(counter, 4, state_set, start_state, end_state, False, disc_fac)
    return mdp


addr = "data/maze/grid100.txt"
file = r"{}".format(addr)
matrix_global = text_to_matrix(file)
state_index_matrix_global = give_index(matrix_global)
mdp = matrix_to_mdp(state_index_matrix_global, file)

mdp_new = planner.value_iteration(mdp)
for i in mdp_new.state_set:
    print(i.value, i.optimal_action.index)


