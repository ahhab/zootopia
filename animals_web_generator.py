import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def serialize_html(animal):
    output = ''  # define an empty string
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += f"<p class='card__text'>\n"
    if 'diet' in animal['characteristics'].keys():
      output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    if 'locations' in animal.keys():
      output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if 'type' in animal['characteristics'].keys():
      output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += "</p>"
    output += '</li>'
    return output

output = ''

for animal in animals_data:
  output += serialize_html(animal)
  print(output)


def load_html(file_path):
  with open(file_path, "r") as handle:
    return handle.read()

def write_html(file_path, html):
  with open(file_path, "w") as handle:
    handle.write(html)

html_template = load_html('animals_template.html')

html_animals = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

write_html('animals_web_output.html', html_animals)