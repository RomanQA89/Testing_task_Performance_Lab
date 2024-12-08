import sys
import json


def update_test_values(test_structure, values_dict):
    """Обновление значений value в файле tests.json на основе файла values.json."""
    for test in test_structure:
        test_id = test["id"]
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        if "values" in test:              # Если в tests.json есть вложенные value, то рекурсивно обновляем их значения
            update_test_values(test["values"], values_dict)


def make_report(tests_file, values_file, report_file):
    """Функция для создания и записи данных в файл report.json."""
    with open(tests_file, 'r') as f:                  # Считываем данные из tests.json
        tests_data = json.load(f)

    with open(values_file, 'r') as f:                 # Считываем данные из values.json
        values_data = json.load(f)

    # Проходимся по списку словарей в values_data и преобразуем его в словарь, где будут id тестов и их статус.
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Обновляем значения в структуре тестов
    update_test_values(tests_data["tests"], values_dict)

    with open(report_file, 'w') as f:                 # Записываем обновленную структуру в report.json
        json.dump(tests_data, f, indent=2)


if __name__ == "__main__":                            # Запуск через консоль
    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    make_report(tests_file, values_file, report_file)
