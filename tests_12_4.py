import logging
import unittest
from runner import Runner

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r1 = Runner("Вася", -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(f"Неверная скорость для Runner")

    def test_run(self):
        try:
            r2 = Runner(2, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(f"Неверный тип данных для объекта Runner:")