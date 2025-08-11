import json
import os
import data_fetcher

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
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data is not None:
        animal_html = generate_animal_html(animals_data)
        html_template = load_template('animals_template.html')
        final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_html)
        write_output('animals_web_output.html', final_html)
        print("Website was successfully generated to the file animals_web_output.html.")


if __name__ == "__main__":
    main()
