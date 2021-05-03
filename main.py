# SoC Assignment 1
# MDP Solver

import MDP_Reader
from math import inf


def value_func(state_ind, mdp):
    for i in mdp.state_set:
        if i.index == state_ind:
            return i.value


def bellman_equation(state, action_index, mdp):
    total = 0
    for action in state.actions:
        if action.index == action_index:
            for nxt_state, reward, prob in action.action_func:
                total += prob * (reward + mdp.dis_fac * value_func(nxt_state, mdp))
    return total


def value_iteration(mdp):
    ERR = 1000
    while not abs(ERR) <= 0.0000000000000001:
        for state in mdp.state_set:
            cur_max = -1*inf
            optimal_action = None
            value = state.value
            old_value = state.value
            for action in state.actions:
                value = bellman_equation(state, action.index, mdp)
                if value > cur_max:
                    cur_max = value
                    optimal_action = action
            state.optimal_action = optimal_action
            state.value = cur_max
            ERR = min(abs(old_value - state.value), ERR)
    return mdp


given_MDP = MDP_Reader.data_reader(r"mdp\continuing-mdp-50-20.txt")
given_MDP = value_iteration(given_MDP)

for i in given_MDP.state_set:
    print(i.value)
