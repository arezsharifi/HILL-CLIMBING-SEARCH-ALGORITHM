import random

class Node:
    """Represents a state in the search space."""
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def __repr__(self):
        return f"Node(State: {self.state}, Value: {self.value})"
    
def HILL_CLIMBING(problem):
    # problem: An object that must implement:
    # - problem.initial_state() -> returns a state
    # - problem.get_value(state) -> returns the heuristic value of a state
    # - problem.get_successors(state) -> returns a list of neighbor states

    current_state = problem.initial_state()
    current = Node(current_state, problem.get_value(current_state))
    while True:
        successor = problem.get_successor(current.state)

        if not successor:
            return current.state

        best_neighbor_state = max(successor, key=problem.get_value)
        best_neighbor_value = problem.get_value(best_neighbor_state)

        if best_neighbor_value <= current.value:
            return current.state
        current = current = Node(best_neighbor_state, best_neighbor_value)
        
