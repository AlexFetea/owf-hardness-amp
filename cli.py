import time
from src.weak_owf import weak_one_way_function
from src.hardness_amp import direct_product_construction

def invert_weak_owf(target_hash, original_input):
    for seed in range(256):
        generated_hash = weak_one_way_function(original_input, seed=seed)
        if generated_hash == target_hash:
            return seed
    return None

# invert amplified version here
def invert_amplified_owf(amplified_hash, original_input, num_iterations):
    pass

original_input = "test"
num_iterations = 3


weak_hash = weak_one_way_function(original_input)
amplified_hash = direct_product_construction(weak_one_way_function, original_input, num_iterations)

# Test inversion of weak OWF
start_weak = time.time()
weak_seed = invert_weak_owf(weak_hash, original_input)
time_weak = time.time() - start_weak
print(f"Weak OWF inverted in {time_weak:.4f} seconds. Seed: {weak_seed}")

# Test inversion of amplified OWF
start_amplified = time.time()
amplified_seeds = invert_amplified_owf(amplified_hash, original_input, num_iterations)
time_amplified = time.time() - start_amplified
print(f"Amplified OWF inverted in {time_amplified:.4f} seconds. seeds: {amplified_seeds}")
