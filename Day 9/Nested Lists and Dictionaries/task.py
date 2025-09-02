capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

#Nested list in Dictionary

# travel_log = {
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }

# print(travel_log["France"])
# print(travel_log["France"][1])
# print(travel_log["Germany"])
# print(travel_log["Germany"][1])

nested_lists = ["A", "B", ["C", "D"] ]
print(nested_lists[2])
print(nested_lists[2][1])
print(nested_lists[-1][1])

#Nesting a Dictionary inside a Dictionary

travel_log = {
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits": 5
    },
}
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["Germany"]["cities_visited"][2])
