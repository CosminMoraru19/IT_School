import unittest
import HtmlTestRunner

# ca si mentiune, pentru a folosi fisiserul ca atare va trebui sa va creati un folder numit "Intalnirea10" fara inainte de 10

from Intalnirea10.test3_alerts import Alerts
from Intalnirea10.test6_keys import Keyboard
from Intalnirea10.test5_context_menu import ContextMenu
from Intalnirea10.test4_auth import Authentication
from Intalnirea10.test2_firefox import Browser
from datetime import datetime


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Browser)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Report'
            )

        runner.run(teste_de_rulat)
