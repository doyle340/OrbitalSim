# Project API

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

    objects = {
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
        query_input -- input expression attempted for query
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
