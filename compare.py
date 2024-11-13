from collections import defaultdict

route_arr = [
    {'userId': 1, 'route': ['Main Gate', 'Queen Hall', 'SUB', 'Faculty of Sci.', 'Faculty of Soc.']},
    {'userId': 1, 'route': ['Main Gate', 'Queen Hall', 'BookShop', 'Tedder', 'Mellanby', 'SUB', 'Faculty of Sci.', 'Faculty of Soc.']},
    {'userId': 2, 'route': ['Main Gate', 'Queen Hall', 'SUB', 'Faculty of Tech']},
    {'userId': 2, 'route': ['Main Gate', 'Queen Hall', 'BookShop', 'Tedder', 'Mellanby', 'SUB', 'Faculty of Tech']},
    {'userId': 3, 'route': ['Queen Hall', 'SUB', 'Faculty of Sci.']},
    {'userId': 3, 'route': ['Queen Hall', 'BookShop', 'Tedder', 'Mellanby', 'SUB', 'Faculty of Sci.']},
    {'userId': 4, 'route': ['Main Gate', 'Queen Hall', 'BookShop', 'Tedder']},
    {'userId': 5, 'route': ['Queen Hall', 'SUB', 'Faculty of Art', 'Faculty of Agric.']},
    {'userId': 5, 'route': ['Queen Hall', 'BookShop', 'Tedder', 'Mellanby', 'SUB', 'Faculty of Art', 'Faculty of Agric.']},
    {'userId': 5, 'route': ['Queen Hall', 'Mosque', 'Faculty of Agric.']},
    {'userId': 6, 'route': ['Main Gate', 'Access Bank', 'Micro Finance', 'Zik']},
    {'userId': 7, 'route': ['Access Bank', 'Micro Finance', 'Zik', 'Indy']}
]

map_route = defaultdict(list)
for route in route_arr:
    str = "".join(route['route']).replace(" ", "")
    # print("outide")
    # map_route[str].append(route['userId'])
    map_key = map_route.keys()
    if len(map_key) > 0:
        mapKey_length = len(map_key)
        for key in list(map_key):
            # print("key is ", key)
            if str in key:
                # print("here in if")
                map_route[key].append(route['userId'])
            elif key in str:
                # print("here in elif")
                map_route[str].append(map_key[key])
                map_route[str].append(route['userId'])
            else:
                # print("here in else")
                if(route['userId'] in map_route[str]):
                    continue
                map_route[str].append(route['userId'])
                # print("out here")
    else:
        # print("am first here? ")
        map_route[str].append(route['userId'])
print(map_route)
