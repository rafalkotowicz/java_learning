from hstest.stage_test import *
from hstest.test_case import TestCase
import ast, math

INVALID_RESULT = "No one is joining for the party"


class BillSplitterTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["5", "Marc", "Jem", "Monica", "Anna", "Sam", "100"], attach=["5", "100"]),
                TestCase(stdin=["7", "Marc", "Jem", "Monica", "Anna", "Jason", "Ben", "Ned", "41"], attach=["7", "41"]),
                TestCase(stdin=["3", "Jake", "Sam", "Irina", "109"], attach=["3", "109"]),
                TestCase(stdin=["0", "100"], attach=["0", "100"]),
                TestCase(stdin=["-1", "-5"], attach=["-1", "-5"])
                ]

    def check(self, reply: str, attach: Any) -> CheckResult:
        strings = [s for s in reply.split('\n') if s != '']
        if int(attach[0]) <= 0:
            if len(strings) != 2:
                return CheckResult.wrong("Your code is not printing expected number of lines of output")
            elif strings[1] != INVALID_RESULT:
                return CheckResult.wrong("Expected output was No one is joining for the party!")
            return CheckResult.correct()
        elif int(attach[0]) > 0 and (len(strings) != 4):
            return CheckResult.wrong("Your code is not printing expected number of lines of output, check examples")
        try:
            output = ast.literal_eval(strings[3])
        except ValueError:
            return CheckResult.wrong("Please check your output, it should be a dictionary")
        except IndentationError:
            return CheckResult.wrong('There should not be any leading whitespace before your last output')
        if (not isinstance(output, dict)):
            return CheckResult.wrong("Please use Dictionary data structure to store user input")
        elif (len(output) != int(attach[0])):
            return CheckResult.wrong(
                "Please check if you have added all your friends to dictionary after taking an user input")
        try:
            bill_list = list(output.values())
            bill = sum(bill_list)
        except TypeError:
            return CheckResult.wrong("Dictionary Values should be of integer type")
        if (len(output) != 0 and (math.ceil(bill) != float(attach[1]) and math.floor(bill) != float(attach[1]))):
            return CheckResult.wrong("Please update dictionary with correct split values")
        elif (len(output) != 0 and len((str(bill_list[0]).split("."))[1]) > 2):
            return CheckResult.wrong("Please round off split values to two decimal places")
        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
