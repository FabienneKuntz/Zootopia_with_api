import json
import requests


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_html_data():
    with open("animals_template.html", "r",) as file:
        html_template = file.read()
        return html_template


def serialize_animal(animals_data):
    """Serializes every animal for the html file"""
    output = ""
    for animal in animals_data:
        location_list = animal.get("locations")
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if "diet" in animal.get("characteristics", {}):
            output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        if location_list:
            output += f'    <strong>Location:</strong> {location_list[0]}<br/>\n'
        if "type" in animal.get("characteristics", {}):
            output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output


def replace_info(animals_data):
    """Replaces the spaceholder of html file to actual code"""
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
        animals_data = load_data('animals_data.json')
        #print(serialize_animal(animals_data))
        print(replace_info(animals_data))
        write_new_html_file(animals_data)
    except FileNotFoundError as e:
        print(f"Couldn't find an important file! \n{e}")


if __name__ == "__main__":
    main()
    
