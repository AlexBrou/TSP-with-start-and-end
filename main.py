import tsp
BIGVALUE = 9999999999999999999999999


def TSPWithStartAndEnd(distances, sites, start, end):

    sites.append("dummy")
    for stop in sites:
        distances[("dummy", stop)] = BIGVALUE
        distances[(stop, "dummy")] = BIGVALUE
    distances[("dummy", "dummy")] = 0

    distances[("dummy", start)] = 0
    distances[(end, "dummy")] = 0

    newDistances = {}

    for i in range(len(sites)):
        for j in range(len(sites)):
            newDistances[(i, j)] = distances[(sites[i], sites[j])]

    tspResults = tsp.tsp(list(range(len(sites))), newDistances)
    route = tspResults[1]
    cost = tspResults[0]
    route = [sites[x] for x in route]
    routeNoDummy = route[route.index(
        "dummy")+1:] + route[:route.index("dummy"):]

    return routeNoDummy, cost


if __name__ == "__main__":
    mat = [[0,   1, 1, 1.5],
           [1,   0, 1.5, 1],
           [1, 1.5,   0, 1],
           [1.5,   1,   1, 0]]  # Distance Matrix
    r = list(range(len(mat)))
    # Dictionary of distance
    dist = {(i, j): mat[i][j] for i in r for j in r}

    # lets say we want to start with node 2 and end with node 1
    print(TSPWithStartAndEnd(dist, r, 2, 1))
