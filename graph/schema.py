from graphene import ObjectType, Field, List, Schema, String
from graph.types import PersonType
from db.mongo import find_one, find_all

class Query(ObjectType):
    person = Field(PersonType, name=String(required=True))
    people = List(PersonType)

    def resolve_person(self, info, name):
        person_data = find_one("test", {"name": name})
        if person_data:
            return PersonType(name=person_data["name"], age=person_data["age"])
        return None

    def resolve_people(self, info):
        people_data = find_all("test")
        return [PersonType(name=person["name"], age=person["age"]) for person in people_data]

schema = Schema(query=Query)
