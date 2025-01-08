from graphene import ObjectType, Field, List, Schema, String, Float
from graph.types import *
from db.mongo import find_one, find_all, find

class Query(ObjectType):
    numb_purchases_per_location = List(NumbPurchasesPerLocation, locations=List(String))
    comparing_purchases_of_pairs = List(ComparingPurchasesOfPairs, locations=List(String))
    purchases_over_time = List(PurchasesOverTime, starttime=Float(), endtime=Float(), locations=List(String),
                               types=List(String))
    matrices = Field(Matrices, matrix_title=String(), matrix_type=String())
    feature_collection = Field(FeatureCollection)
    location = List(Location)
    employee_location_clusters = List(EmployeeLocationCluster)
    combined_data = Field(CombinedData)

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

        return [
            ComparingPurchasesOfPairs(
                location=purchase["location"],
                absolut_cc=purchase["absolut_cc"],
                absolut_loyalty=purchase["absolut_loyalty"],
                absolut_cars_in_area=purchase["absolut_cars_in_area"],
                absolut_card_pair=purchase["absolut_card_pair"],
                absolut_car_card_pair=purchase["absolut_car_card_pair"],
                absolut_no_car_card_pair=purchase["absolut_no_car_card_pair"],
                absolut_no_pair=purchase["absolut_no_pair"],
                percent_cc=purchase["percent_cc"],
                percent_loyalty=purchase["percent_loyalty"],
                percent_cars_in_area=purchase["percent_cars_in_area"],
                percent_card_pair=purchase["percent_card_pair"],
                percent_car_card_pair=purchase["percent_car_card_pair"],
                percent_no_car_card_pair=purchase["percent_no_car_card_pair"],
                percent_no_pair=purchase["percent_no_pair"],
                avg_amount_cc=purchase["avg_amount_cc"],
                avg_amount_loyalty=purchase["avg_amount_loyalty"],
                avg_amount_cars_in_area=purchase["avg_amount_cars_in_area"],
                avg_amount_card_pair=purchase["avg_amount_card_pair"],
                avg_amount_car_card_pair=purchase["avg_amount_car_card_pair"],
                avg_amount_no_car_card_pair=purchase["avg_amount_no_car_card_pair"],
                avg_amount_no_pair=purchase["avg_amount_no_pair"]
            ) for purchase in purchases_data
        ]

    def resolve_purchases_over_time(self, info, starttime=None, endtime=None, locations=None, types=None):
        query_append = []
        if locations:
            query_append.append({"location": {"$in": locations}})
        if types:
            query_append.append({"type": {"$in": types}})
        if starttime:
            query_append.append({"$or": [{"starttime": {"$gt": starttime}}, {"starttime":{"$eq": starttime}}]})
        if endtime:
            query_append.append({"$or": [{"endtime":{"$lt": endtime}}, {"endtime":{"$eq": endtime}}]})

        if len(query_append) == 1:
            purchases_data = find("purchases_over_time", query_append[0])
        elif len(query_append) > 1:
            purchases_data = find("purchases_over_time", {"$and": query_append})
        else:
            purchases_data = find_all("purchases_over_time")

        return [
            PurchasesOverTime(
                starttime=purchase["starttime"],
                endtime=purchase["endtime"],
                type=purchase["type"],
                location=purchase["location"],
                price=purchase.get("price", None),
                creditcard=purchase.get("creditcard", None),
                loyalty=purchase.get("loyalty", None),
                car_id=purchase.get("car_id", None),
                start_coordinates= purchase.get("start_coordinates", None),
                end_coordinates= purchase.get("end_coordinates", None)
            ) for purchase in purchases_data
        ]

    def resolve_matrices(self, info, matrix_title=None, matrix_type=None):
        if matrix_title == "Matching Cars and Credit Cards":
            possible_matrix_types = ["relative_cc_matrix", "relative_car_matrix", "absolute_matrix"]
            if matrix_type not in possible_matrix_types:
                matrix_type = "absolute_matrix"
            collection = "car_matrices"
        else:
            matrix_title = "Matching Credit and Loyalty Cards"
            possible_matrix_types = ["relative_cc_matrix", "relative_loyalty_matrix", "absolute_matrix"]
            if matrix_type not in possible_matrix_types:
                matrix_type = "absolute_matrix"
            collection = "card_matrices"
        matrix_data = find_one(collection, {"matrix": matrix_type})
        x_axis = find_one(collection, {"x_axis": {"$exists": True}})
        y_axis = find_one(collection, {"y_axis": {"$exists": True}})

        return Matrices(
                matrix_title=matrix_title,
                matrix=matrix_data["data"],
                x_axis=x_axis["data"],
                y_axis=y_axis["data"],
                matrix_type=matrix_data["matrix"],
                x_axis_name=x_axis["x_axis"],
                y_axis_name=y_axis["y_axis"]
            )

    # Test Data
    def resolve_person(self, info, name):
        person_data = find_one("test", {"name": name})
        if person_data:
            return PersonType(name=person_data["name"], age=person_data["age"])
        return None

    def resolve_people(self, info):
        people_data = find_all("test")
        return [PersonType(name=person["name"], age=person["age"]) for person in people_data]


    def resolve_feature_collection(self, info):
        feature_collection_data = find_all("AbilaMap")

        return [
            FeatureCollection(
            type=feature_collection_data["type"],
            name=feature_collection_data["name"],
            crs=CRS(
                type=feature_collection_data["crs"]["type"],
                properties=CRSProperties(
                    name=feature_collection_data["crs"]["properties"]["name"]
                )
            ),
            features=[
                Feature(
                    type=feature["type"],
                    properties=Properties(**feature["properties"]),
                    geometry=Geometry(
                        type=feature["geometry"]["type"],
                        coordinates=feature["geometry"]["coordinates"]
                    )
                ) for feature in feature_collection_data["features"]
            ]
        )
    ]

    
    def resolve_location(self, info):
        location_data = find_all("LocationCluster")

        return [
            Location(
                id=loc["id"],
                name=loc["name"],
                geometry=LocationGeometry(
                    type=loc["geometry"]["type"],
                    coordinates=loc["geometry"]["coordinates"]
                )
            ) for loc in location_data
        ]


    def resolve_employee_location_clusters(self, info):
        employee_location_cluster_data = find_all("EmployeeClusters")
        return [
            EmployeeLocationCluster(
                cluster_id=cluster["cluster_id"],
                location=cluster["location"],
                employees=[
                    EmployeeCluster(**employee) for employee in cluster["employees"]
                ]
            ) for cluster in employee_location_cluster_data
        ]

    
    def resolve_combined_data(self, info):
        feature_collection_data = find_all("AbilaMap")
        location_data = find_all("LocationCluster")
        employee_location_cluster_data = find_all("EmployeeCluster")

        return CombinedData(
            feature_collection=FeatureCollection(
                type=feature_collection_data["type"],
                name=feature_collection_data["name"],
                crs=CRS(
                    type=feature_collection_data["crs"]["type"],
                    properties=CRSProperties(
                        name=feature_collection_data["crs"]["properties"]["name"]
                    )
                ),
                features=[
                    Feature(
                        type=feature["type"],
                        properties=Properties(**feature["properties"]),
                        geometry=Geometry(
                            type=feature["geometry"]["type"],
                            coordinates=feature["geometry"]["coordinates"]
                        )
                    ) for feature in feature_collection_data["features"]
                ]
            ),
            locations=[
                Location(
                    id=loc["id"],
                    name=loc["name"],
                    geometry=LocationGeometry(
                        type=loc["geometry"]["type"],
                        coordinates=loc["geometry"]["coordinates"]
                    )
                ) for loc in location_data
            ],
            employee_location_clusters=[
                EmployeeLocationCluster(
                    cluster_id=cluster["cluster_id"],
                    location=cluster["location"],
                    employees=[
                        EmployeeCluster(**employee) for employee in cluster["employees"]
                    ]
                ) for cluster in employee_location_cluster_data
            ]
        )

schema = Schema(query=Query)