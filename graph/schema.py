from graphene import ObjectType, Field, List, Schema, String
from graph.types import *
from db.mongo import find_one, find_all, find

class Query(ObjectType):
    numb_purchases_per_location = List(NumbPurchasesPerLocation, locations=List(String))
    comparingPurchasesOfPairs = List(ComparingPurchasesOfPairs, locations=List(String))

    # Test Data
    person = Field(PersonType, name=String(required=True))
    people = List(PersonType)

    def resolve_numb_purchases_per_location(self, info, locations=None):
        if locations:
            purchases_data = find("num_purchases_per_location", {"location": {"$in": locations}})
        else:
            purchases_data = find_all("num_purchases_per_location")
        return [
            NumbPurchasesPerLocation(
                location=purchase["location"],
                numb_purchases_cc=purchase["numb_purchases_cc"],
                numb_purchases_loyalty=purchase["numb_purchases_loyalty"]
            ) for purchase in purchases_data
        ]

    def resolve_comparing_purchases_of_pairs(self, info, locations=None):
        if locations:
            purchases_data = find("comparing_purchases_of_pairs",
                                  {"location": {"$in": locations}})
        else:
            purchases_data = find_all("comparing_purchases_of_pairs")

        # Debug print to check the fetched data
        print("Fetched purchases data:", purchases_data)

        if not purchases_data:
            return None

        return [
            ComparingPurchasesOfPairs(
                location=purchase["location"],
                absolut_card_pair=purchase["absolut_card_pair"],
                absolut_car_card_pair=purchase["absolut_car_card_pair"],
                absolut_no_car_card_pair=purchase["absolut_no_car_card_pair"],
                absolut_no_pair=purchase["absolut_no_pair"],
                percent_card_pair=purchase["percent_card_pair"],
                percent_car_card_pair=purchase["percent_car_card_pair"],
                percent_no_car_card_pair=purchase["percent_no_car_card_pair"],
                percent_no_pair=purchase["percent_no_pair"],
                avg_amount_card_pair=purchase["avg_amount_card_pair"],
                avg_amount_car_card_pair=purchase["avg_amount_car_card_pair"],
                avg_amount_no_car_card_pair=purchase["avg_amount_no_car_card_pair"],
                avg_amount_no_pair=purchase["avg_amount_no_pair"]
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
