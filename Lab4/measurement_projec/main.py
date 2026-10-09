import logging
import json
from pathlib import Path
from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_max, find_min

Path("logs").mkdir(exist_ok=True)
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


LOG_FILE = Path(config["log_file"])


def init_session() -> int:
    session_number = 1

    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            session_number = content.count("=== СЕССИЯ ") + 1

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        prefix = "\n" if session_number > 1 else ""
        f.write(f"{prefix}=== СЕССИЯ {session_number} ===\n")

    return session_number

session_id = init_session()

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)


def main():
    logging.info(f"Старт сессии {session_id}. Рабочий каталог: {Path.cwd()}")

    file_path = Path(config["input_file"])

    try:
        numbers = read_numbers(file_path)
        validate_numbers(numbers)
    except FileNotFoundError:
        logging.error("Такого файла нет")
        return
    except ValueError as error:
        logging.error(f"Ошибка данных: {error}")
        return

    logging.info(f"Прочитано значений: {len(numbers)}")
    logging.info(f"AVG: {calculate_average(numbers)}")
    logging.info(f"MAX: {find_max(numbers)}")
    logging.info(f"MIN: {find_min(numbers)}")
    logging.info("Программа завершена")


if __name__ == "__main__":
  main()