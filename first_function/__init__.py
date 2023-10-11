import logging
import azure.functions as func

def main(request: func.HttpRequest):
    logging.info(f"Request method: {request.method}")

    if request.method == "GET":
        return func.HttpResponse("Hello")

    try:
        name = request.get_json()['name']
    except (ValueError, KeyError):
        return func.HttpResponse("Wrong json")

    return func.HttpResponse(f'Hello, {name}')