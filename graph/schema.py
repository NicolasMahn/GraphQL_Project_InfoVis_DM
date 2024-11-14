from graphene import ObjectType, Field, List, Schema, String
from graph.types import PersonType, NumbPurchasesPerLocation
from db.mongo import find_one, find_all

class Query(ObjectType):
    numb_purchases_per_location = List(NumbPurchasesPerLocation, location=String())

    # Test Data
    person = Field(PersonType, name=String(required=True))
    people = List(PersonType)

    def resolve_numb_purchases_per_location(self, info, location=None):
        if location:
            purchases_data = find_all("num_purchases_per_location", {"location": location})
        else:
            purchases_data = find_all("num_purchases_per_location")
        return [
            NumbPurchasesPerLocation(
                location=purchase["location"],
                numb_purchases_cc=purchase["numb_purchases_cc"],
                numb_purchases_loyalty=purchase["numb_purchases_loyalty"]
            ) for purchase in purchases_data
        ]

    # Test Data
    def resolve_person(self, info, name):
        person_data = find_one("test", {"name": name})
        if person_data:
            return PersonType(name=person_data["name"], age=person_data["age"])
        return None

    def resolve_people(self, info):
        people_data = find_all("test")
        return [PersonType(name=person["name"], age=person["age"]) for person in people_data]



schema = Schema(query=Query)
