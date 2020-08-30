# Project API
from math import pi as pi
from astropy.constants.astropyconst40 import M_earth

# TODO: Add function annotations
# TODO: Implement Pytest

class Wolfram:
    """
    Contains information relevant to querying Wolfram Alpha
    """
    app_id = '368TAL-UW4J8AUH8E'
    question_predicate = 'What is '
    possessive = 'of'
    unit_assertion = 'in'


class Units:
    """
    Contains referenceable SI units
    """
    kg = 'Kilograms'
    m = 'Meters'
    cubic_m = 'Cubic Meters'

    acceptable_units = [kg, m, cubic_m]


class Queryables(Wolfram, Units):
    """
    Contains queryable terms to feed Wolfram Alpha questions
    """

    queryable_objects = {
        'earth': "Earth",
        'earths_moon': "the moon",
        'earths_sun': "the sun"
    }

    properties_and_units = {
        'mass': Units.kg,
        'radius': Units.m,
        'density': Units.kg + ' per ' + Units.cubic_m,
        'distance': Units.m
    }


class QueryConstructionError:
    """
    Exception raised in Wolfram Alpha Query

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class AtlasGeometry:
    """
    I got a C in algebra 2. Let's do more physics and less math. Yee-haww!
    """

    def sphere_volume(self, radius):
        """
        V = 4/3*pi*r^3
        :param radius:
        :return:
        Returns the volume of a sphere when provided the sphere's radius
        """
        sphere_volume = (4.0/3.0)*pi*(radius**3)

        return sphere_volume


class AtlasConstants:
    # TODO: Find out what the heck Astropy is doing... give me my constants, yo
    G = 1.0
    earth_mass = M_earth


class AtlasParms:
    absolute_error_resolution = 1.0e-10
    relative_error_resolution = 1.0e-10
