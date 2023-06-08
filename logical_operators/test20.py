from logical_operators import CheckSolution

# A number consisting of one and zero is given (the number starts at once). If the number of ones is greater than zero, true, otherwise False is returned. n five-digit number.
# input a = 10111 output True, input a = 11111 output True, input a = 10000 output False, input a = 110 output True, input a = 11100 output True

class TaskTwenty(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(10111)
        expected = True

        result = {
            "input": ["10111"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(11111)
        expected = True

        result = {
            "input": ["11111"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(10000)
        expected = False

        result = {
            "input": ["10000"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(110)
        expected = True

        result = {
            "input": ["110"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution(11100)
        expected = True

        result = {
            "input": ["11100"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"input: {test_case['input']}")
                print(f"answer: {test_case['answer']}")
                print(f"expected: {test_case['expected']}")