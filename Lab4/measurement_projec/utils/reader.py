def read_numbers(file_path):
  with open(file_path, "r") as file:
    return [float(line.strip()) for line in file if line.strip()]
def validate_numbers(numbers):
  if len(numbers) == 0:
    raise ValueError("Список измерений пуст")