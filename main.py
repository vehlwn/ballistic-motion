import numpy
import scipy.integrate
import matplotlib.pyplot as plt

# mass of a projectile
m = 40.0e-3
# cross sectional area of a projectile
A = (5.7e-3 / 2.0) ** 2 * numpy.pi
# drag coefficient
CD = 0.1

# interval of integration
t_max = 0.5
# initial speed
v_0 = 700
initial_angle = numpy.deg2rad(0)
# initial height above sea level
y_0 = 0

# gravitational acceleration
g = 9.8
air_density = 1.2


def right_hand(_t, state):
    (_x, _y, v_x, v_y) = state
    k = -0.5 * CD * air_density * A
    return [v_x, v_y, k / m * v_x**2, -g + k / m * v_y**2]


initial_state = [
    0,
    y_0,
    v_0 * numpy.cos(initial_angle),
    v_0 * numpy.sin(initial_angle),
]
sol = scipy.integrate.solve_ivp(
    right_hand, t_span=(0, t_max), y0=initial_state, dense_output=True
)
print(sol)

t = numpy.linspace(0, t_max, 100)
state = sol.sol(t)

x = state[0, :]
y = state[1, :]
v_x = state[2, :]
v_y = state[3, :]
abs_v = numpy.hypot(v_x, v_y)

plt.clf()
plt.grid(True, linestyle=":")
plt.title("Trajectory")
plt.xlabel("x, m")
plt.ylabel("y, m")
plt.plot(x, y)
plt.savefig("trajectory.png", dpi=300)

plt.clf()
plt.grid(True, linestyle=":")
plt.title("Absolute speed")
plt.xlabel("time, s")
plt.ylabel("|v|, m/s")
plt.plot(t, abs_v)
plt.savefig("abs_v.png", dpi=300)
