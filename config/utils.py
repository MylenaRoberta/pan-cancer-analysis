import json

import requests

def gdc_api_request(endpoint, fields, filters={}, size=1):
    """
    Send a request to a GDC API endpoint with the specified parameters.

    Parameters:
    -----------
    endpoint : str
        The URL of the endpoint to send the request to.
    fields : list of str
        A list of fields to include in the response.
    filters : dict, optional
        A dictionary of filters to apply to the request. Default is an empty dictionary.
    size : int, optional
        The number of results to retrieve. Default is 1.

    Returns:
    --------
    list
        A list of hits (data items) retrieved from the endpoint response.
    """
    # Parameters used in the endpoint request
    params = {
        'fields': ','.join(fields),
        'filters': filters,
        'size': str(size)
    }
    
    # Request the objects of interest to the endpoint
    response = requests.post(
        url=endpoint,
        headers={'Content-Type': 'application/json'},
        json=params
    )

    # Convert the response content to a JSON
    json_response = json.loads(response.content.decode('utf-8'))

    return json_response['data']['hits']