def config_parser(config_path):
    with open(config_path, 'r') as config_file:
        config = dict()
        lines = config_file.readlines()
        for line in lines:
            k, v = line.split(' = ')
            config[k] = v.split('\n')[0]
        return config


def parse_roads(data, id_courort):
    lifts = []
    trails = []
    for i in range(len(data)):
        data[i].append(id_courort)
        if data[i][0] == 'lift':
            lifts.append(data[i])
        else:
            trails.append(data[i])
    return lifts, trails
