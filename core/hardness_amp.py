from typing import List
import networkx as nx
import os
import numpy as np

def direct_product_construction(f, input_values: List[str]) -> str:
    return "".join(map(f, input_values))

def generate_random_inputs(n, q):
    return [os.urandom(n) for _ in range(q)]

def create_expander_graph(n, d):
    while True:
        G = nx.random_regular_graph(d, n)
        if nx.is_connected(G):
            return G

def random_walk_expander(G: nx.Graph, start: int, steps: List[int], pi: List[int]):
    current = start
    for step in steps:
        current = pi[current]
        current = list(G[current].keys())[step]
    return current

def expander_construction(G: nx.Graph, start: int, steps: List[int], pi: List[int]):
    """Random Walk on Expander Graph Construction
    Args:
        f (function): Weak one-way permutation
        G (networkx.Graph): Expander graph
        start (int): Starting node for the random walk
        steps (int): Number of steps in the random walk
    Returns:
        tuple: Final node after the walk and the sequence of nodes
    """
    g_x = random_walk_expander(G, start, steps, pi)
    output = format(g_x, 'x')
    for step in steps:
        output += format(step, 'x')
    return output
