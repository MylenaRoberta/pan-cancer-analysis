import json
import logging
import os
from time import sleep
from typing import List, Dict

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

import requests

from config.constants import GDC_API_ENDPOINTS

def gdc_api_request(endpoint: str, fields: List[str], filters: Dict={}, size: int=1) -> List[Dict]:
    """
    Send a request to a Genomic Data Commons (GDC) API endpoint with the specified parameters.

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
    response.raise_for_status()

    # Convert the response content to a JSON
    json_response = json.loads(response.content.decode('utf-8'))

    return json_response['data']['hits']

def gdc_api_files_download(files: List[Dict], path: str, retries: int=3, delay: int=5) -> None:
    """
    Downloads files from the Genomic Data Commons (GDC) API and saves them locally.

    Parameters:
    -----------
    files : list of dict
        A list of dictionaries where each dictionary contains metadata for a file. 
        Expected keys in each dictionary:
        - 'file_id' (str): Unique identifier for the file.
        - 'experimental_strategy' (str): Description of the experiment type.
        - 'data_format' (str): File format (e.g., 'TXT', 'CSV').
    path : str
        The local directory where downloaded files will be saved.
    re
    """
    for file in files:
        # Define all file metadata
        file_id = file['file_id']
        file_type = file['experimental_strategy'].lower()
        file_format = file['data_format'].lower()
        file_name = f'{file_type}_{file_id}.{file_format}'
        file_path = os.path.join(path, file_name)

        # Retry logic
        for attempt in range(retries):
            try:
                # Request the object of interest to the endpoint
                logging.info(f'Downloading {file_id} (Attempt {attempt + 1})...')
                response = requests.get(
                    url=os.path.join(GDC_API_ENDPOINTS['data'], file_id),
                    headers={'Content-Type': 'application/json'},
                    timeout=30
                )
                response.raise_for_status()

                # Write the file in the external data folder
                with open(file_path, 'wb') as output_file:
                    output_file.write(response.content)

                # Exit retry loop on success
                logging.info(f'Downloaded and saved to {file_path}')
                break

            except requests.exceptions.RequestException as req_err:
                logging.error(f'Request failed for {file_id}: {req_err}')
            except OSError as os_err:
                logging.error(f'File write failed for {file_path}: {os_err}')
                break  # File system errors shouldn’t be retried
            except Exception as e:
                logging.error(f'Unexpected error for {file_id}: {e}')

            if attempt < retries - 1:
                logging.info(f'Retrying in {delay} seconds...')
                sleep(delay)
            else:
                logging.warning(f'Failed to download {file_id} after {retries} attempts')