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
    absolut_cc = Int()
    absolut_loyalty = Int()
    absolut_cars_in_area = Int()
    absolut_card_pair = Int()
    absolut_car_card_pair = Int()
    absolut_no_car_card_pair = Int()
    absolut_no_pair = Int()
    percent_cc = Float()
    percent_loyalty = Float()
    percent_cars_in_area = Float()
    percent_card_pair = Float()
    percent_car_card_pair = Float()
    percent_no_car_card_pair = Float()
    percent_no_pair = Float()
    avg_amount_cc = Float()
    avg_amount_loyalty = Float()
    avg_amount_cars_in_area = Float()
    avg_amount_card_pair = Float()
    avg_amount_car_card_pair = Float()
    avg_amount_no_car_card_pair = Float()
    avg_amount_no_pair = Float()