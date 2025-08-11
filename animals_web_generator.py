import json
import os
import requests
from dotenv import load_dotenv

load_dotenv() # not to commit the api key, it is stored in .env an loaded here. 


def get_animal_data(animal_name):
    """
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


def serialize_animal_to_html(animal):
    """
    Serializes a single animal's data to an HTML list item.

    Args:
        animal (dict): A dictionary containing animal data.

    Returns:
        str: An HTML string representing the animal.
    """
    output = '<li class="cards__item">'
    output += f"<div class='card__title'>{animal.get('name', 'N/A')}</div>"
    output += "<p class='card__text'>"
    characteristics = animal.get('characteristics', {})
    if 'diet' in characteristics:
        output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>"
    if 'locations' in animal and animal['locations']:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>"
    if 'type' in characteristics:
        output += f"<strong>Type:</strong> {characteristics['type']}<br/>"
    output += "</p>"
    output += '</li>'
    return output


def generate_animal_html(animals_data):
    """
    Generates HTML for a list of animals.

    Args:
        animals_data (list): A list of animal dictionaries.

    Returns:
        str: An HTML string of all the animals.
    """
    if not animals_data:
        return "<h2>No animals found.</h2>"
    output = ""
    for animal in animals_data:
        output += serialize_animal_to_html(animal)
    return output


def load_template(file_path):
    """
    Loads an HTML template from a file.

    Args:
        file_path (str): The path to the HTML template file.

    Returns:
        str: The content of the HTML template.
    """
    with open(file_path, "r") as handle:
        return handle.read()


def write_output(file_path, content):
    """
    Writes content to a file.

    Args:
        file_path (str): The path to the output file.
        content (str): The content to write to the file.
    """
    with open(file_path, "w") as handle:
        handle.write(content)


def main():
    """
    Main function to generate the animals web page.
    """
    animal_name = input("Enter a name of an animal: ")
    animals_data = get_animal_data(animal_name)

    if animals_data is not None:
        animal_html = generate_animal_html(animals_data)
        html_template = load_template('animals_template.html')
        final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_html)
        write_output('animals_web_output.html', final_html)
        print("Website was successfully generated to the file animals_web_output.html.")


if __name__ == "__main__":
    main()
