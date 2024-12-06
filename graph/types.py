from graphene import ObjectType, String, Int, Float, List


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

class PurchasesOverTime(ObjectType):
    starttime = Float()
    endtime = Float()
    type = String()
    location = String()
    price = Float()
    creditcard = Int()
    loyalty = String()
    car_id = Int()
    start_coordinates = List(String)
    end_coordinates = List(String)

class Matrices(ObjectType):
    matrix_title = String()
    matrix = List(List(Float))
    x_axis = List(String)
    y_axis = List(String)
    matrix_type = String()
    x_axis_name = String()
    y_axis_name = String()

