import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

for animal in animals_data:
  print(f"name: {animal['name']}")
  if 'diet' in animal['characteristics'].keys():
    print(f"diet: {animal['characteristics']['diet']}")
  if 'locations' in animal.keys():
    print(f"location: {animal['locations'][0]}")
  if 'type' in animal['characteristics'].keys():
    print(f"type: {animal['characteristics']['type']}")
  print()

  output = ''  # define an empty string
  for animal in animals_data:
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    if 'diet' in animal['characteristics'].keys():
      output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    if 'locations' in animal.keys():
      output += f"Location: {animal['locations'][0]}<br/>\n"
    if 'type' in animal['characteristics'].keys():
      output += f"Type: {animal['characteristics']['type']}<br/>\n"
    output += '</li>'
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