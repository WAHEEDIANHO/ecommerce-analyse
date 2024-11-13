from collections import defaultdict

stops = {
    "Main Gate": {
        "name": "Main Gate",
        "prev": [],
        "next": ["Queen Hall", "Access Bank"]
    },
    "Queen Hall": {
        "name": "Queen Hall",
        "prev": ["Main Gate"],
        "next": ["BookShop", "SUB", "UI Hotel", "Mosque"]
    },
    "BookShop": {
        "name": "BookShop",
        "prev": ["Queen Hall"],
        "next": ["Tedder"]
    },
    "Mosque": {
        "name": "BookShop",
        "prev": ["Queen Hall"],
        "next": ["Faculty of Agric."]
    },
    "Tedder": {
        "name": "Tedder",
        "prev": ["BookShop"],
        "next": ["Mellanby"]
    },
    "Mellanby": {
        "name": "Mellanby",
        "prev": ["Tedder"],
        "next": ["SUB"]
    },
    "SUB": {
        "name": "SUB",
        "prev": ["Queen Hall", "Mellanby"],  # Corrected
        "next": ["Faculty of Sci.", "Faculty of Art", "Faculty of Tech"]
    },
    "Faculty of Sci.": {
        "name": "Faculty of Sci.",
        "prev": ["SUB"],
        "next": ["Faculty of Soc."]
    },
    "Faculty of Soc.": {
        "name": "Faculty of Soc.",
        "prev": ["Faculty of Sci."],
        "next": []
    },
    "Faculty of Tech": {
        "name": "Faculty of Tech",
        "prev": ["SUB"],
        "next": []
    },
    "Faculty of Art": {
        "name": "Faculty of Art",
        "prev": ["SUB"],
        "next": ["Faculty of Agric."]
    },
    "Faculty of Agric.": {
        "name": "Faculty of Agric.",
        "prev": ["Faculty of Art", "Mosque"],
        "next": ["Vet."]
    },
    "Vet.": {
        "name": "Vet.",
        "prev": ["Faculty of Agric."],
        "next": []
    },
    "UI Hotel": {
        "name": "UI Hotel",
        "prev": ["Queen Hall"],
        "next": ["Abadina"]
    },
    "Abadina": {
        "name": "Abadina",
        "prev": ["UI Hotel"],
        "next": ["Ajiibode Gate"]
    },
    "Ajiibode Gate": {
        "name": "Ajiibode Gate",
        "prev": ["Abadina"],
        "next": []
    },
    "Access Bank": {
        "name": "Access Bank",
        "prev": ["Main Gate"],
        "next": ["Micro Finance"]
    },
    "Micro Finance": {
        "name": "Micro Finance",
        "prev": ["Access Bank"],
        "next": ["Zik"]
    },
    "Zik": {
        "name": "Zik",
        "prev": ["Micro Finance"],
        "next": ["Indy"]
    },
    "Indy": {
        "name": "Indy",
        "prev": ["Zik"],
        "next": []
    }
}

passenger_requests = [{
    "start": "Main Gate",
    "end": "Faculty of Soc.",
    "userId": 1
}, {
    "start": "Main Gate",
    "end": "Faculty of Tech",
    "userId": 2
}, {
    "start": "Queen Hall",
    "end": "Faculty of Sci.",
    "userId": 3
}, {
    "start": "Main Gate",
    "end": "Tedder",
    "userId": 4
}, {
    "start": "Queen Hall",
    "end": "Faculty of Agric.",
    "userId": 5,
}, {
    "start": "Main Gate",
    "end": "Zik",
    "userId": 6
}, {
    "start": "Access Bank",
    "end": "Indy",
    "userId": 7
}]


def trace_all_routes(stops, start, stop, current_route=None):
    if current_route is None:
        current_route = [stop]  # Start with the current stop

    # If we've reached the starting point, return the current route
    if stop == start:
        return [current_route[::-1]]  # Reverse to show route from start to stop

    routes = []  # List to store all the valid routes

    # Recursively trace all the previous stops
    for prev_stop in stops[stop]["prev"]:
        new_route = current_route + [
            prev_stop
        ]  # Add the previous stop to the current route
        routes.extend(trace_all_routes(stops, start, prev_stop,
                                       new_route))  # Recurse
    # print(stop, len(routes), '\n')
    return routes


# Function to process all passenger requests and find their routes
def find_all_passenger_routes(requests, stops):
    passenger_routes = []

    for request in requests:
        start = request["start"]
        end = request["end"]
        userId = request["userId"]

        # Trace all possible routes for the given request
        traced_routes = trace_all_routes(stops, start, end)

        # Store the traced routes with the userId
        for route in traced_routes:
            passenger_routes.append({"userId": userId, "route": route})

    return passenger_routes


traced_routes_output = find_all_passenger_routes(passenger_requests, stops)
print(traced_routes_output)
# for trace in traced_routes_output:
#     print(trace)


# Function to match passengers by common subpaths
def match_passengers_by_paths(traced_routes):
    map_route = defaultdict(list)
    for route in traced_routes:
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
                    if (route['userId'] in map_route[str]):
                        continue
                    map_route[str].append(route['userId'])
                    # print("out here")
        else:
            # print("am first here? ")
            map_route[str].append(route['userId'])
    return map_route


print(match_passengers_by_paths(traced_routes_output))