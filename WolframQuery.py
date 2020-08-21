# This program will query Wolfram Alpha for the mass of an orbital body and persist as a usable object

import wolframalpha
from AtlasEyes.AtlasEyesAPI import Wolfram, Units, QueryConstructionError, Queryables


class WolframQuery:
    def __init__(self, objects, properties):
        self.objects = objects
        self.properties = properties

    def construct_question(self, property_units=Queryables.properties_and_units.objects):

        # Validate number of objects to ensure properties are relative
        if len(self.objects) > 1 and 'distance' not in self.properties:
            # If we have more than one object we need to be asking for relative distance
            raise QueryConstructionError(message="More than one object was provided, but the properties weren't "
                                                 "relative.")

        # Validate that we understand the units
        if property_units not in Units.acceptable_units:
            raise QueryConstructionError(message="Units provided were not found in the API file. Try again.")

        # Validate that our units are acceptable to the property requested
        if property_units != Queryables.properties_and_units.property:
            raise QueryConstructionError(message="Unit/Property Pairing is nonsense. Try again.")

        # Only allow query for one property of the object(s) for now
        if len(self.properties) > 1:
            raise QueryConstructionError(message="More than one property provided. Please query one non-relative "
                                                 "property per object.")

        if 'distance' in self.properties:
            # of the form "What is the distance between {x} and {y} in {km}
            question = Wolfram.question_predicate + 'distance between' + self.objects[0] + 'and' + self.objects[1] \
                       + Wolfram.unit_assertion.property_units
        else:
            # of the form "Whats is the mass of the Earth"
            question = Wolfram.question_predicate + 'the' + self.properties[0] + Wolfram.possessive + self.objects[0] \
                       + Wolfram.unit_assertion + property_units

        return question

    # question okay, let's establish a connection
    # Establish a connection to Wolfram and make it global to the class instance
    client = wolframalpha.Client(Wolfram.app_id)

    def ask_wolfram(self, question):
        wolframs_response = self.client.query(question)
        answer = next(wolframs_response.results).text

        return answer






