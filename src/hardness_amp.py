import networkx as nx

def direct_product_construction(weak_owf, input_value: str, num_iterations: int = 5) -> str:
    results = [weak_owf(input_value, seed=i) for i in range(num_iterations)]
    return "".join(results)

def create_expander_graph(n, d):
    while True:
        G = nx.random_regular_graph(d, n)
        if nx.is_connected(G):
            return G

def random_walk_expander(G, start, steps):
    current = start
    walk = [current]
    for _ in range(steps):
        current = random.choice(list(G.neighbors(current)))
        walk.append(current)
    return walk

def weak_one_way_permutation(x):
    return ''.join(sorted(x))

def expander_construction(f, G, start, steps):
    """Random Walk on Expander Graph Construction
    Args:
        f (function): Weak one-way permutation
        G (networkx.Graph): Expander graph
        start (int): Starting node for the random walk
        steps (int): Number of steps in the random walk
    Returns:
        tuple: Final node after the walk and the sequence of nodes
    """
    walk = random_walk_expander(G, start, steps)
    final_node = walk[-1]
    return (f(final_node), walk)
