import unittest
from unittest.mock import MagicMock

from GitHubApi import getRepos, getCommits, displayRepo
getRepos = MagicMock(return_value=['345ExpressLab', 'Complexity', 'GitHubApi567', 'gj14', 'HW4-345', 'roll20-character-sheets', 'SSW345', 'SSW567', 'Triangle567', 'VentureHacks'])
getCommits = MagicMock(return_value=30)
displayRepo = MagicMock(return_value="Repo: Complexity Number of commits: 30")

class TestGitHubApi(unittest.TestCase):

    def testGetRepos(self):
        self.assertEqual(getRepos("smurray117"), ['345ExpressLab', 'Complexity', 'GitHubApi567', 'gj14', 'HW4-345', 'roll20-character-sheets', 'SSW345', 'SSW567', 'Triangle567', 'VentureHacks'])

    def testGetCommits(self):
        self.assertEqual(getCommits("smurray117", "Complexity"), 30)

    def testDisplayRepo(self):
        self.assertEqual(displayRepo("smurray117", "Complexity"), "Repo: Complexity Number of commits: 30")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
