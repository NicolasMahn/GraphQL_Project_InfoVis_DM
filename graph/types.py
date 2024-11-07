from graphene import ObjectType, String, Int

class PersonType(ObjectType):
    name = String()
    age = Int()
