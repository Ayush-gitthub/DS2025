import numpy as np
import matplotlib.pyplot as plt



def gradient_descent(grad_f, w0, lr, max_iter=50000, tol=1e-8):
    w = np.array(w0, dtype=float)
    iterates   = [w.copy()]
    grad_norms = [np.linalg.norm(grad_f(w))]

    for k in range(max_iter):
        g = grad_f(w)
        norm_g = np.linalg.norm(g)
        if norm_g < tol:
            print(f"  Converged at iteration {k}  (||grad|| = {norm_g:.2e})")
            break
        w = w - lr * g
        iterates.append(w.copy())
        grad_norms.append(np.linalg.norm(grad_f(w)))

    return w, np.array(iterates), grad_norms


def f4(w):
    w1, w2 = w[0], w[1]
    return (3 - w1 - w2)**2 + (2 - w1)**2 + (1 - w2)**2

def grad_f4(w):
    w1, w2 = w[0], w[1]
    dw1 = -2*(3 - w1 - w2) - 2*(2 - w1)
    dw2 = -2*(3 - w1 - w2) - 2*(1 - w2)
    return np.array([dw1, dw2])

print("=" * 55)
print("Exercise 4")
print("=" * 55)

w0_ex4 = np.array([3/2, 1/2])
lr_ex4 = 0.1

w_star4, iterates4, grad_norms4 = gradient_descent(grad_f4, w0_ex4, lr_ex4)
f_vals4 = [f4(w) for w in iterates4]

print(f"  Starting point : w0 = {w0_ex4}")
print(f"  Step size      : alpha = {lr_ex4}")
print(f"  Minimizer      : w* = {w_star4}")
print(f"  Minimum value  : f(w*) = {f4(w_star4):.10f}")
print(f"  Iterations     : {len(iterates4) - 1}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Exercise 4 — Gradient Descent Convergence", fontsize=14)

axes[0].semilogy(f_vals4, color="steelblue")
axes[0].set_xlabel("Iteration $k$")
axes[0].set_ylabel("$f(w_k)$")
axes[0].set_title("Objective Function History")
axes[0].grid(True, which="both", alpha=0.3)

axes[1].semilogy(grad_norms4, color="darkorange")
axes[1].set_xlabel("Iteration $k$")
axes[1].set_ylabel(r"$\|\nabla f(w_k)\|$")
axes[1].set_title("Gradient Norm History")
axes[1].grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.savefig("ex4_convergence.png", dpi=150, bbox_inches="tight")
plt.show()
print("  Saved: ex4_convergence.png")

w1_grid = np.linspace(0.0, 3.5, 400)
w2_grid = np.linspace(-0.5, 2.5, 400)
W1, W2 = np.meshgrid(w1_grid, w2_grid)
F_grid = (3 - W1 - W2)**2 + (2 - W1)**2 + (1 - W2)**2

fig, ax = plt.subplots(figsize=(8, 7))
levels = np.geomspace(F_grid.min() + 1e-4, F_grid.max(), 30)
cp = ax.contourf(W1, W2, F_grid, levels=levels, cmap="Blues", alpha=0.85)
ax.contour(W1, W2, F_grid, levels=levels, colors="white", linewidths=0.4, alpha=0.5)
plt.colorbar(cp, ax=ax, label="$f(w_1, w_2)$")

ax.plot(iterates4[:, 0], iterates4[:, 1],
        "r.-", markersize=3, linewidth=1.2, label="GD iterates")
ax.plot(*iterates4[0], "go", markersize=10, label=r"$w_0$ (start)")
ax.plot(*w_star4, "r*", markersize=16, label=r"$w^*$ (minimum)")

ax.set_xlabel("$w_1$")
ax.set_ylabel("$w_2$")
ax.set_title("Exercise 4 — Gradient Descent Path on Contour Plot")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("ex4_iterates.png", dpi=150, bbox_inches="tight")
plt.show()
print("  Saved: ex4_iterates.png")

