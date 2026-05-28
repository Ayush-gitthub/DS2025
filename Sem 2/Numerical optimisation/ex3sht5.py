
import numpy as np
import time

np.random.seed(42)


d = 1000
n = 100000
A = np.random.randn(n, d)


def F(x):
    return np.mean(np.sqrt(np.sum((x - A)**2, axis=1) + 1))

def grad(x):
    U = x - A
    S = np.sqrt(np.sum(U**2, axis=1) + 1)
    return np.mean(U / S[:, None], axis=0)

def grad_and_hessian(x):
    U = x - A
    S = np.sqrt(np.sum(U**2, axis=1) + 1)
    g = np.mean(U / S[:, None], axis=0)
    term1 = np.sum(1.0 / S) / n * np.eye(d)
    term2 = (U / S[:, None]**3).T @ U / n  
    return g, term1 - term2


# Newton
print("Newton's Method")
x = np.zeros(d)
hist_newton = [F(x)]
times_newton = []

for k in range(15):
    t = time.time()
    g, H = grad_and_hessian(x)
    delta = np.linalg.solve(H, -g)
    x = x + delta
    fval = F(x)
    hist_newton.append(fval)
    iter_t = time.time() - t
    times_newton.append(iter_t)
    print(f"Newton Iter {k+1:2d} | F(x) = {fval:.8f} | ||grad|| = {np.linalg.norm(g):.3e} | time = {iter_t:.2f}s")
    if np.linalg.norm(g) < 1e-10:
        print(f"converged at iter {k+1}")
        break

x_newton = x
t_newton = sum(times_newton)


# SGD
print("\nSGD")
x = np.zeros(d)
hist_sgd = [F(x)]
times_sgd = []

for epoch in range(20):
    t = time.time()
    idx = np.random.permutation(n)
    A_shuf = A[idx]
    for i in range(0, n, 256):
        batch = A_shuf[i:i+256]
        U = x - batch
        S = np.sqrt(np.sum(U**2, axis=1) + 1)
        x -= 0.1 * np.mean(U / S[:, None], axis=0)
    fval = F(x)
    hist_sgd.append(fval)
    epoch_t = time.time() - t
    times_sgd.append(epoch_t)
    print(f"SGD Epoch {epoch+1:2d} | F(x) = {fval:.8f} | ||grad|| = {np.linalg.norm(grad(x)):.3e} | time = {epoch_t:.2f}s")

x_sgd = x
t_sgd = sum(times_sgd)


# summary
print("\n" + "=" * 75)
print("FINAL COMPARISON")
print("=" * 75)
print(f"{'Method':<12}{'Final F(x)':<18}{'Iterations':<15}{'Total Time (s)':<18}{'Avg Iter Time (s)':<20}")
print("-" * 75)
print(f"{'Newton':<12}{hist_newton[-1]:<18.8f}{len(hist_newton)-1:<15}{t_newton:<18.2f}{np.mean(times_newton):<20.2f}")
print(f"{'SGD':<12}{hist_sgd[-1]:<18.8f}{len(hist_sgd)-1:<15}{t_sgd:<18.2f}{np.mean(times_sgd):<20.2f}")
print(f"\n||x_newton - x_sgd|| = {np.linalg.norm(x_newton - x_sgd):.6f}")