import numpy as np
import random


# Основной класс генерации систем линейных уранений
class LinearEquationSystemGen:

    # Основная функция генерации
    def generate(self, eq_count: int, eq_in_system_count: int):
        systems_list = []
        index_range = range(-6, 7)
        right_side_range = range(-10, 11)
        sys_num = 0
        while sys_num < eq_count:
            left_side, right_side = [], []
            for eq in range(eq_in_system_count):
                left_side.append(
                    [random.randrange(index_range.start, index_range.stop) for _ in range(eq_in_system_count)])
                right_side.append(random.randrange(right_side_range.start, right_side_range.stop))
            left_side_np, right_side_np = np.array(left_side), np.array(right_side)
            try:
                solve = np.linalg.solve(left_side_np, right_side_np)
                systems_list.append(self.__to_tex(left_side_np, right_side_np, solve))
                sys_num += 1
            except:
                pass
        return systems_list

    # Функция для перевода сгенерированных систем уравнений в формат TeX
    def __to_tex(self, left_side, right_side, solve):
        variable_list = ['x', 'y', 'z', 'm', 'n']
        eq_list = ''
        for index in range(len(left_side)):
            eq = ''
            for ind, el in enumerate(left_side[index]):
                new_el = el
                if ind != 0:
                    if '-' in str(el):
                        new_el = '- ' + str(el).replace('-', '')
                    else:
                        new_el = '+ ' + str(el)
                eq += str(new_el) + str(variable_list[ind]) + " "
            eq += "= " + str(right_side[index])
            eq_list += ('\\' if eq_list != '' else '') + str(eq)
            solve_dict = {}
            for ind, ans in enumerate(solve):
                solve_dict[variable_list[ind]] = ans
                # solve_dict
        return {r"\begin{cases}" + eq_list + r"\end{cases}": solve_dict}


print(LinearEquationSystemGen().generate(1, 3))
