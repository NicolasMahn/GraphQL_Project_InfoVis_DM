from graphene import ObjectType, String, Int, Float


class PersonType(ObjectType):
    name = String()
    age = Int()

class NumbPurchasesPerLocation(ObjectType):
    location = String()
    numb_purchases_cc = Int()
    numb_purchases_loyalty = Int()

class ComparingPurchasesOfPairs(ObjectType):
    location = String()
    absolut_card_pair = Int()
    absolut_car_card_pair = Int()
    absolut_no_car_card_pair = Int()
    absolut_no_pair = Int()
    percent_card_pair = Float()
    percent_car_card_pair = Float()
    percent_no_car_card_pair = Float()
    percent_no_pair = Float()
    avg_amount_card_pair = Float()
    avg_amount_car_card_pair = Float()
    avg_amount_no_car_card_pair = Float()
    avg_amount_no_pair = Float()

