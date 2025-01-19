import  runnerTest
import tournamentTest
import unittest


test_all = unittest.TestSuite()
test_all.addTest(unittest.TestLoader().loadTestsFromTestCase(runnerTest.RunnerTest))
test_all.addTest(unittest.TestLoader().loadTestsFromTestCase(tournamentTest.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_all)




