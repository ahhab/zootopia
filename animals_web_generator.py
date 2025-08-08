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