import random


class SquareEquationGenerator:
    """Класс генерации квадратных уравнений"""

    @staticmethod
    def generate(count: int):
        """
        Функция для генерации квадратных уравнений
        :param count: Количество сгенерированных уравнений
        :return: Функция возвращает список словарей типа {<уравнение>: {'x1': <x1>, 'x2': <x2>}}
        """
        eq_list = []
        for eq in range(count):
            x1, x2 = -1 * random.randint(-10, 10), -1 * random.randint(-10, 10)
            eq_list.append({'x^2 {0}{1}x {2}{3} = {4}'.format(('+ ' if x1 + x2 >= 0 else '- '),
                                                              str(abs((x1 + x2))),
                                                              ('+ ' if x1 * x2 >= 0 else '- '), str(abs(x1 * x2)),
                                                              str(0)): {'x1': -1 * x1, 'x2': -1 * x2}})
        return eq_list


for eq in SquareEquationGenerator.generate(5):
    print(eq)
