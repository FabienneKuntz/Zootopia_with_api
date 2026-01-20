import requests
import os
from dotenv import load_dotenv

load_dotenv()

ANIMALS_API_KEY = os.getenv("ANIMALS_API_KEY")
if not ANIMALS_API_KEY:
    raise RuntimeError("ANIMALS_API_KEY is missing")


def load_data(animal):
  """Fetches information from the API"""
  res = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal}&X-Api-Key={ANIMALS_API_KEY}")
  animal_data = res.json()
  return animal_data


def read_html_data():
    """Reads the HTML data from template file"""
    with open("animals_template.html", "r", ) as file:
        html_template = file.read()
        return html_template


def serialize_animal(animals_data):
    """Serializes every animal for the html file"""
    output = ""
    for animal in animals_data:
        location_list = animal['locations']
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        if location_list:
            output += f'    <strong>Location:</strong> {location_list[0]}<br/>\n'
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output


def replace_info(animals_data):
    """Replaces the placeholder of html file to actual code"""
    html_template = read_html_data()
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", serialize_animal(animals_data))
    return new_html


def write_new_html_file(animals_data):
    """Creates the final html code"""
    new_html = replace_info(animals_data)
    with open("animals.html", "w") as file:
        file.write(new_html)


def main():
    try:
        animals_data = load_data("Fox")
        replace_info(animals_data)
        write_new_html_file(animals_data)
        print("Website was successfully generated to the file animals.html.")
    except FileNotFoundError as e:
        print(f"Couldn't find an important file! \n{e}")


if __name__ == "__main__":
    main()
