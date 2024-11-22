"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    each_wagons_id = each_wagons_id[2:] +  each_wagons_id[:2]
    return  each_wagons_id[:1] + missing_wagons + each_wagons_id[1:]


def add_missing_stops(*args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_route = args[0]
    stops = [
    value for key, value in sorted(
            kwargs.items(),
            key=lambda item: int(item[0].split('_')[1])
        )
    ]
    updated_route['stops'] = stops
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    re_order=[]
    for i in range(len(wagons_rows)):
        re_order.append([row[i] for row in wagons_rows])
    return re_order
