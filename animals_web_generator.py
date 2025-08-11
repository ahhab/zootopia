import json


def load_data(file_path):
    """
    Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal_to_html(animal):
    """
    Serializes a single animal's data to an HTML list item.

    Args:
        animal (dict): A dictionary containing animal data.

    Returns:
        str: An HTML string representing the animal.
    """
    output = '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>"
    output += "<p class='card__text'>"
    if 'diet' in animal['characteristics']:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>"
    if 'locations' in animal:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>"
    if 'type' in animal['characteristics']:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>"
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
    return "".join(serialize_animal_to_html(animal) for animal in animals_data)


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
    # Load animal data
    animals_data = load_data('animals_data.json')

    # Generate HTML for animals
    animal_html = generate_animal_html(animals_data)

    # Load the HTML template
    html_template = load_template('animals_template.html')

    # Replace the placeholder with the generated animal HTML
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_html)

    # Write the final HTML to the output file
    write_output('animals_web_output.html', final_html)


if __name__ == "__main__":
    main()
