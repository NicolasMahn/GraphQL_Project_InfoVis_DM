from graphene import ObjectType, String, Int, Float


class PersonType(ObjectType):
    name = String()
    age = Int()

class NumbPurchasesPerLocation(ObjectType):
    location = String()
    numb_purchases_cc = Int()
    numb_purchases_loyalty = Int()

class LocationComparisonCleanedVsSketchy(ObjectType):
    location = String()
    absolut_cleaned = Int()
    absolut_sketchy = Int()
    percent_cleaned = Float()
    percent_sketchy = Float()
    avg_amount_cleaned = Float()
    avg_amount_sketchy = Float()
