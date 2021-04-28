from hstest.stage_test import *
from hstest.test_case import TestCase

END_RESULT = "No one is going to be lucky"
INVALID_RESULT = "No one is joining for the party"


class BillSplitterTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["5", "Marc", "Jem", "Monica", "Anna", "Jason", "100", "Yes"],
                         attach=["5", "100", "Yes", ["Marc", "Jem", "Monica", "Anna", "Jason"]]),
                TestCase(stdin=["3", "Jake", "Sam", "Irina", "109", "No"],
                         attach=["3", "109", "No", ["Jake", "Sam", "Irina"]]),
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

        elif int(attach[0]) > 0 and len(strings) != 5:
            return CheckResult.wrong("Your code is not printing expected number of lines of output, check examples")
        elif (attach[2] == "Yes"):
            lucky_string = strings[4].split(" ")
            name = lucky_string[0]
            if (name not in attach[3]):
                return CheckResult.wrong(
                    "Expected output is a random name from dictionary keys, but we got something else")
        elif (attach[2] == "No"):
            if strings[4] != END_RESULT:
                return CheckResult.wrong("Output should be - No one is going to be lucky")
        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
