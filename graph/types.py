from graphene import ObjectType, JSONString, String, Int, Float, List


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


class EmployeeCluster(ObjectType):
    car_id = String()
    LastName = String()
    FirstName = String()
    CurrentEmploymentType = String()
    CurrentEmploymentTitle = String()
    start_time = String()
    end_time = String()
    duration_of_stop_min = Float()
    latitude = Float()
    longitude = Float()

class EmployeeLocationCluster(ObjectType):
    cluster_id = Int()
    location = String()
    employees = List(EmployeeCluster)

class LocationGeometry(ObjectType):
    type = String()
    coordinates = List(List(List(List(Float))))

class Location(ObjectType):
    id = String()
    name = String()
    geometry = LocationGeometry()

class CRSProperties(ObjectType):
    name = String()

class CRS(ObjectType):
    type = String()
    properties = Field(CRSProperties)

class Geometry(ObjectType):
    type = String()
    coordinates = List(List(Float))

class Properties(ObjectType):
    Name = String()
    description = String()
    timestamp = String()
    begin = String()
    end = String()
    altitudeMode = String()
    tessellate = Int()
    extrude = Int()
    visibility = Int()
    drawOrder = String()
    icon = String()
    TLID = Int()
    FEDIRP = String()
    FENAME = String()
    FETYPE = String()
    FEDIRS = String()
    FRADDL = Int()
    TOADDL = Int()
    FRADDR = Int()
    TOADDR = Int()

class Feature(ObjectType):
    type = String()
    properties = Field(Properties)
    geometry = Field(Geometry)

class FeatureCollection(ObjectType):
    type = String()
    name = String()
    crs = Field(CRS)
    features = List(Feature)

class CombinedData(ObjectType):
    feature_collection = Field(FeatureCollection)
    locations = List(Location)
    employee_location_clusters = List(EmployeeLocationCluster)