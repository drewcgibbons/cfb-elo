import requests

"""
Fetches data from the specified URL.

Args:
    url (str): The URL to fetch data from.

Returns:
    str: The content retrieved from the URL.
    """
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        print(response.text)  # Print the response text for debugging   
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None