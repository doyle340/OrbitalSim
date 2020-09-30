# This program will solve the Two Body Problem in Lagrangian Methods

# TODO Implement Pytest

from AtlasEyes.MacroParticleManifest import MacroParticleManifest
from AtlasEyes.AtlasAPI import AtlasConstants
from AtlasEyes.AtlasAPI import AtlasParms as parms
from scipy.integrate import solve_ivp


class TwoBodyOrbit:
    """
    DoubleOrbit uses Lagrangians to solve the Two-Body Problem in cartesian coordinates.

    Parameters
    ----------
    atlas_object_1: dictionary
        First orbiting body's mass
    atlas_object_2: dictionary
        Second orbiting body's mass

    Methods
    -------
    dy_dt(t, y)
        Returns the right side of the differential equation in vector y,
        given time t and the corresponding value of y.
    """

    def __init__(self, atlas_object1=MacroParticleManifest().create_default_macroparticle(),
                 atlas_object2=MacroParticleManifest().create_default_macroparticle()):
        self.G = AtlasConstants.G
        self.mass1 = atlas_object1['mass']
        self.mass2 = atlas_object2['mass']
        
    def dy_dt(self, t, y):
        """
        This function returns the right-hand side of the differential equation:
        [dphi_1/dt dphi_1dot/dt dphi_2/dt dphi_2dot/dt]

        Parameters
        ----------
        t : float
            time 
        y : float
            8-component vector/list with

            y[0] = x1,     y[1] = x_1dot

            y[2] = x2,     y[3] = x_2dot

            y[4] = y1,     y[5] = y_1dot

            y[6] = y2,     y[7] = y_2dot

        """

        x_1DoubleDot = -(self.G * self.mass2 * (y[0] - y[2])) / (
                    ((y[0] - y[2]) ** 2 + (y[4] - y[6]) ** 2) ** (3.0 / 2.0))
        x_2DoubleDot = (self.G * self.mass1 * (y[0] - y[2])) / (
                    ((y[0] - y[2]) ** 2 + (y[4] - y[6]) ** 2) ** (3.0 / 2.0))
        y_1DoubleDot = -(self.G * self.mass2 * (y[4] - y[6])) / (
                    ((y[0] - y[2]) ** 2 + (y[4] - y[6]) ** 2) ** (3.0 / 2.0))
        y_2DoubleDot = (self.G * self.mass1 * (y[4] - y[6])) / (
                    ((y[0] - y[2]) ** 2 + (y[4] - y[6]) ** 2) ** (3.0 / 2.0))

        dy_dt = {
            'x_1dot': y[1],
            'x_1DoubleDot': x_1DoubleDot,
            'x_2dot': y[3],
            'x_2DoubleDot': x_2DoubleDot,
            'y_1dot': y[5],
            'y_1DoubleDot': y_1DoubleDot,
            'y_2dot': y[7],
            'y_2DoubleDot': y_2DoubleDot
        }

        return dy_dt

    def solve_ode(self, t_pts, x1_0, x_1dot0, x2_0, x_2dot0, y1_0, y_1dot0, y2_0, y_2dot0,
                  abserr=parms.absolute_error_resolution, relerr=parms.relative_error_resolution):
        """
        Solve the ODE given initial conditions.
        For now use odeint, but we have the option to switch.
        Specify smaller abserr and relerr to get more precision.
        """
        y = [x1_0, x_1dot0, x2_0, x_2dot0, y1_0, y_1dot0, y2_0, y_2dot0]

        solution = solve_ivp(self.dy_dt, (t_pts[0], t_pts[-1]), y, t_eval=t_pts, atol=abserr, rtol=relerr)

        x1, x_1dot, x2, x_2dot, y1, y_1dot, y2, y_2dot = solution.y

        solved_ode = {
            'x1': x1,
            'x_1dot': x_1dot,
            'x2': x2,
            'x_2dot': x_2dot,
            'y1': y1,
            'y_1dot': y_1dot,
            'y2': y2,
            'y_2dot': y_2dot
        }

        return solved_ode
