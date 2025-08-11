import requests
import os
from dotenv import load_dotenv



load_dotenv() # not to commit the api key, it is stored in .env and loaded here. 


def fetch_data(animal_name):
    
    """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
    Fetches animal data from the API Ninjas API.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of dictionaries containing animal data, or None if the request fails.
    """
    api_key = os.getenv("API_NINJAS_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the API_NINJAS_API_KEY environment variable.")

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: {response.status_code} {response.text}")
        return None

