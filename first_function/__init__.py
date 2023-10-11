import logging
import copy
import itertools
import random
from shapely import Polygon, MultiPolygon, LineString, affinity

import azure.functions as func

def perform_experiments(dot_coordinates):
    return dot_coordinates[0]

def main(request: func.HttpRequest):
    logging.info(f"Request method: {request.method}")
    if request.method == "GET":
        return func.HttpResponse("Hello")

    try:
        name = request.get_json()['name']
        coord1 = request.get_json()['coord1']
        coord2 = request.get_json()['coord2']
    except (ValueError, KeyError):
        return func.HttpResponse("Wrong json")

    my_list = [0, 0, 0, 100, 100, 100, 100, 0]
    test1 = perform_experiments(my_list)

    return func.HttpResponse(f'Hello, {name}, {coord1}, {test1}')
