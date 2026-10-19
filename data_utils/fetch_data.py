import json, requests

"""
Fetches data from the specified URL.

Args:
    url (str): The URL to fetch data from.

Returns:
    json: The content retrieved from the URL.
    """
def fetch_data(url : str, api_key : str) -> dict | None: 
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        #print(response.json())  # Print the response JSON for debugging   
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None