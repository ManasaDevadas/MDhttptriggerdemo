import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    place = req.params.get('place')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not place:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            place = req_body.get('place')

    if name and place :
        return func.HttpResponse(f"Hello {name}, {place} is an awesome place ,  The function is triggered successfully")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and place in the query string or in the request body for a personalized response.",
             status_code=200
        )
