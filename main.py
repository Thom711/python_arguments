from data import surface_gravity_per_planet
import math

# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name: str, greet: str = 'Hello, <name>!'):
    greet = greet.replace('<name>', name)

    return greet 


def force(mass: float, body: str = "earth"):
    force = mass * surface_gravity_per_planet[body]

    return force


def pull(m1: float, m2: float, d: float):
    G = 6.674 * (10 ** -11)

    pull = G * ((m1 * m2) / (d ** 2))

    return pull


if __name__ == '__main__':
    print(greet(name="Thom"))
    print(force(mass=433, body="jupiter"))
    print(pull(0.1, 5.972 * (10 ** 24), 6.371 * (10 ** 6)))