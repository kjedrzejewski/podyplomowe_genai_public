import json

def parse_nested_json(value):
    """
    Jeśli wartość jest łańcuchem znaków i da się ją zdekodować jako JSON,
    to zwracamy zdekodowaną strukturę. Jeśli jest listą lub słownikiem,
    to rekurencyjnie "rozpakowujemy" każdą wartość.
    """
    # jeśli to jest string, próbujemy sparsować:
    if isinstance(value, str):
        try:
            decoded = json.loads(value)
            return parse_nested_json(decoded)
        except json.JSONDecodeError:
            # jeśli parsowanie się nie powiedzie, to zwróć oryginalny string
            return value

    # jeśli to lista, to rekurencyjnie przetwarzamy jej elementy
    if isinstance(value, list):
        return [parse_nested_json(item) for item in value]

    # jeśli to słownik (dict), to rekurencyjnie przetwarzamy wartości
    if isinstance(value, dict):
        return {k: parse_nested_json(v) for k, v in value.items()}

    # w pozostałych przypadkach zwracamy wartość bez zmian
    return value