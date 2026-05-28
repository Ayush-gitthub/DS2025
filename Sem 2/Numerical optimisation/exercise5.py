import numpy as np
import matplotlib.pyplot as plt
import jax
import jax.numpy as jnp

x0_phys = jnp.array([0.0, 2.0])
g_phys = jnp.array([0.0, -9.81])
x_target5 = jnp.array([0.3, 0.0])

def impact_time(v):
    a = 0.5 * g_phys[1]
    b = v[1]
    c = x0_phys[1]
    disc = b**2 - 4.0 * a * c
    return (-b - jnp.sqrt(disc)) / (2.0 * a)

def x_impact(v):
    t = impact_time(v)
    return x0_phys + v * t + 0.5 * g_phys * t**2

def objective5(v):
    xi = x_impact(v)
    return (xi[0] - x_target5[0])**2 + (xi[1] - x_target5[1])**2

grad_obj5 = jax.grad(objective5)

v0 = jnp.array([jnp.cos(0.5), jnp.sin(0.5)])
lr = 0.05
tol = 1e-6

v = v0
v_hist = [v]
f_hist = [objective5(v)]

for k in range(100000):
    g = grad_obj5(v)
    if jnp.linalg.norm(g) < tol:
        break
    v = v - lr * g
    v_hist.append(v)
    f_hist.append(objective5(v))

v_star = v
t_star = impact_time(v_star)
x_star = x_impact(v_star)

print("v* =", np.array(v_star))
print("t* =", float(t_star))
print("impact =", np.array(x_star))
print("target =", np.array(x_target5))
print("F(v*) =", float(objective5(v_star)))

f_vals = np.array([float(f) for f in f_hist])

plt.figure(figsize=(8, 5))
plt.semilogy(f_vals)
plt.xlabel("Iteration k")
plt.ylabel("F(v_k)")
plt.title("Objective History")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.show()

t_vals = np.linspace(0.0, float(t_star), 500)
v_np = np.array(v_star)
x0_np = np.array(x0_phys)
g_np = np.array(g_phys)

traj = x0_np + np.outer(t_vals, v_np) + 0.5 * g_np * t_vals[:, None]**2

plt.figure(figsize=(9, 5))
plt.plot(traj[:, 0], traj[:, 1])
plt.scatter(x0_np[0], x0_np[1])
plt.scatter(x_star[0], x_star[1])
plt.scatter(float(x_target5[0]), float(x_target5[1]))
plt.axhline(0)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Optimal Trajectory")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()