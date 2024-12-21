import unittest
from tournament import Runner
from tournament import Tournament


def frozen_check(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_check
    def test_walk(self):
        runner = Runner("TestRunner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @frozen_check
    def test_run(self):
        runner = Runner("TestRunner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @frozen_check
    def test_challenge(self):
        runner1 = Runner("TestRunner3")
        runner2 = Runner("TestRunner4")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усэйн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result = {k: v.name for k, v in value.items()}
            print(result)

    @frozen_check
    def test_one(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[1].name == 'Усэйн')
        self.assertTrue(results[2].name == 'Ник')

    @frozen_check
    def test_two(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[1].name == 'Андрей')
        self.assertTrue(results[2].name == 'Ник')

    @frozen_check
    def test_three(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[3].name == 'Ник')
