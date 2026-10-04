import logging
import sys
import math


def setup_logger():

    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("logs/file_txt.log", encoding="utf-8")
        ]
    )

    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")

def get_sides():
    side1 = input("Введите длину стороны A: ")
    side2 = input("Введите длину стороны B: ")
    side3 = input("Введите длину стороны C: ")
    return side1, side2, side3

def parse_sides(side1, side2, side3):

    sides = []

    for side in [side1, side2, side3]:
        try:
            value = float(side)
            logging.debug(f"Строка '{side}' преобразована в {value}")

            if value <= 0:
                logging.warning(f"Сторона '{side}' не положительная (={value})")
                return None, None, None, "invalid"

            sides.append(value)

        except ValueError:
            logging.warning(f"Не удалось преобразовать '{side}' в число")
            return None, None, None, "non_numeric"

    a, b, c = sides
    logging.info(f"Стороны преобразованы: a={a}, b={b}, c={c}")
    return a, b, c, None

def check_triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        logging.info("Треугольник существует")
        return True
    else:
        logging.warning("Треугольник не существует (нарушено неравенство треугольника)")
        return False

def get_triangle_type(a, b, c):

    if a == b == c:
        triangle_type = "равносторонний"
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    logging.info(f"Тип треугольника: {triangle_type}")
    return triangle_type

def calculate_vertices(a, b, c):

    x1, y1 = 0.0, 0.0
    x2, y2 = a, 0.0
    x3 = (a ** 2 + c ** 2 - b ** 2) / (2 * a)
    y3 = math.sqrt(c ** 2 - x3 ** 2)

    logging.debug(f"Исходные координаты: ({x1},{y1}), ({x2},{y2}), ({x3},{y3})")

    max_x = max(x1, x2, x3)
    max_y = max(y1, y2, y3)

    scale = 1.0
    if max_x > 100 or max_y > 100:
        scale = 100.0 / max(max_x, max_y)
        logging.debug(f"Применён масштаб: {scale}")

    v1 = (int(round(x1 * scale)), int(round(y1 * scale)))
    v2 = (int(round(x2 * scale)), int(round(y2 * scale)))
    v3 = (int(round(x3 * scale)), int(round(y3 * scale)))

    vertices = [v1, v2, v3]
    logging.info(f"Координаты вершин: {vertices}")
    return vertices


def main():
    setup_logger()


    side1, side2, side3 = get_sides()
    logging.info(f"Получен ввод: '{side1}', '{side2}', '{side3}'")


    a, b, c, error_type = parse_sides(side1, side2, side3)


    if error_type == "non_numeric":
        logging.error("Нечисловые входные данные")
        triangle_type = ""
        vertices = [(-2, -2), (-2, -2), (-2, -2)]


    elif error_type == "invalid":
        logging.error("Невалидные числовые данные (сторона <= 0)")
        triangle_type = "не треугольник"
        vertices = [(-1, -1), (-1, -1), (-1, -1)]


    else:
        if not check_triangle(a, b, c):
            triangle_type = "не треугольник"
            vertices = [(-1, -1), (-1, -1), (-1, -1)]
        else:
            triangle_type = get_triangle_type(a, b, c)
            vertices = calculate_vertices(a, b, c)


    print(f"\nРезультат:")
    print(f"Тип треугольника: '{triangle_type}'")
    print(f"Координаты вершин: {vertices}")

    logging.info(f"Результат: тип='{triangle_type}', вершины={vertices}")
    logging.info("Приложение завершено")


if __name__ == "__main__":
    main()