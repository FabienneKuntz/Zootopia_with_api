import requests
import os
from dotenv import load_dotenv

load_dotenv()

ANIMALS_API_KEY = os.getenv("ANIMALS_API_KEY")
if not ANIMALS_API_KEY:
    raise RuntimeError("ANIMALS_API_KEY is missing")


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
      """
    res = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key={ANIMALS_API_KEY}")
    animal_data = res.json()
    return animal_data