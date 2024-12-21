import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(unittest.TestCase):
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

    def test_one(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[1].name == 'Усэйн')
        self.assertTrue(results[2].name == 'Ник')

    def test_two(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[1].name == 'Андрей')
        self.assertTrue(results[2].name == 'Ник')

    def test_three(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[3].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
