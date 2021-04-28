from hstest.stage_test import *
from hstest.test_case import TestCase
import ast

INVALID_RESULT = "No one is joining for the party"


class BillSplitterTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["5", "Marc", "Jem", "Monica", "Anna", "Jason"], attach="5"),
                TestCase(stdin=["3", "Jake", "Sam", "Irina"], attach="3"),
                TestCase(stdin=["0"], attach="0"),
                TestCase(stdin=["-1"], attach="-1")
                ]

    def check(self, reply: str, attach: Any) -> CheckResult:
        strings = [s for s in reply.split('\n') if s != '']
        if int(attach) <= 0:
            if len(strings) != 2:
                return CheckResult.wrong("Your code is not printing expected number of lines of output")
            elif strings[1] != INVALID_RESULT:
                return CheckResult.wrong("Expected output was No one is joining for the party!")
            return CheckResult.correct()
        elif int(attach) > 0 and len(strings) != 3:
            return CheckResult.wrong("Your code is not printing expected number of lines of output")
        try:
            output = ast.literal_eval(strings[2])
        except ValueError:
            return CheckResult.wrong('Please check your output, it should be a dictionary')
        except IndentationError:
            return CheckResult.wrong('There should not be any leading whitespace before your last output')
        if (not isinstance(output, dict)):
            return CheckResult.wrong('Please use Dictionary data structure to store user input')
        elif (len(output) != int(attach)):
            return CheckResult.wrong(
                'Please check if you have added all your friends to dictionary after taking an user input')
        elif (len(output) != 0 and max(output.values()) != 0 and min(output.values()) != 0):
            return CheckResult.wrong('Please check all values are initially equal to 0')

        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
