import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2 

def monte_carlo_integration(f, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    area_estimate = (b - a) * np.mean(y_random)
    return area_estimate

result_analytical = (b**3)/3 - (a**3)/3

result_quad, error = spi.quad(f, a, b)

num_samples = 10000
result_monte_carlo = monte_carlo_integration(f, a, b, num_samples)

print(f"Аналітичний результат: {result_analytical}")
print(f"Результат SciPy quad: {result_quad} з помилкою {error}")
print(f"Результат Монте-Карло ({num_samples} вибірок): {result_monte_carlo}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()