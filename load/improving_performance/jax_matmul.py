import jax.numpy as jnp
from jax import random
import time

KEY = random.PRNGKey(0)
SIZE = 10000

x = random.normal(KEY, (SIZE, SIZE), dtype=jnp.float64)

start_time = time.perf_counter()

jnp.dot(x, x.T).block_until_ready()

duration = time.perf_counter() - start_time

print(f"JAX took {duration:.2f} second(s) to multiply the matrices")
