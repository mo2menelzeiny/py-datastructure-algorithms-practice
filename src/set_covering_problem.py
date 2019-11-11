sn = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
s = {
    'K1': {"id", "nv", "ut"},
    'K2': {"wa", "id", "mt"},
    'K3': {"or", "nv", "ca"},
    'K4': {"nv", "ut"},
    "K5": {"ca", "az"}
}


def find_best_station(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        covered_states = set()
        for station, states in stations.items():
            coverage = states_needed & states
            if len(coverage) > len(covered_states):
                best_station = station
                covered_states = coverage
        states_needed -= covered_states
        final_stations.add(best_station)

    return final_stations


print(find_best_station(sn, s))
