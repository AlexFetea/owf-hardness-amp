def direct_product_construction(weak_owf, input_value: str, num_iterations: int = 5) -> str:
    results = [weak_owf(input_value, seed=i) for i in range(num_iterations)]
    return "".join(results)
