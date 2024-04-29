def write_data_to_file(data, filename):
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(data)
  except FileNotFoundError as e:
    print(f"Error: File {filename} not found.")
  except PermissionError as e:
    print(f"Error: Permission denied to write to {filename}.")
  finally:
    if 'file' in locals():  # Check if 'file' variable exists (was opened)
      file.close()  # Close the file if it was opened

# Example usage
data = "This is some data to write to the file."
filename = "my_data.txt"
write_data_to_file(data, filename)


##Answer:
#The finally allows the snippet to execute the code regardless of the result of the try and except blocks. This means that it always checks to see if the file variable was opened and then closes it if it is opened. This is important because the file could or could not be opened depending on which exception is triggered, so it should always be checked to see if it is opened to ensure it gets closed. 
