import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

for animal in animals_data:
  print(animal['name'])
  if 'diet' in animal.keys():
    print(animal['diet'])
  if 'location' in animal.keys():
    print(animal['location'][0])
  if 'type' in animal.keys():
    print(animal['type'])