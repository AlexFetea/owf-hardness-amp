# core/weak_owf.py
import hashlib
import random

import numpy as np

def weak_owf(x):
    return hashlib.sha256(x).digest().hex()

def random_permutation(n: int):
    return np.random.permutation(n)