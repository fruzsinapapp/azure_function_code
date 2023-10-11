import logging
import azure.functions as func

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

    return func.HttpResponse(f'Hello, {name}, {coord1}, {coord2}')
