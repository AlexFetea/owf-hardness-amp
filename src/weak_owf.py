# core/weak_owf.py
import hashlib
import random

def weak_one_way_function(input_value: str, seed: int = None) -> str:
    if seed is not None:
        random.seed(seed)
    salt = random.randint(0, 255)
    return hashlib.sha256(f"{input_value}{salt}".encode()).hexdigest()
