import json

# Invalid JSON data
data = "{\"invalid_json_key\": \"value\"}"

try:
  # Attempt to load the JSON data
  json.loads(data)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")
else:
  print('Succesfully Loads Json')
