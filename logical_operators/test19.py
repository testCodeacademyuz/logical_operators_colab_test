from logical_operators import CheckSolution

# Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
# input x = 121 output True, input x = 10 output False, input x = 11 output True, input x = 100 output False

class TaskNineteen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(121)
        expected = True

        result = {
            "input": ["121"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(10)
        expected = False

        result = {
            "input": ["10"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(11)
        expected = True

        result = {
            "input": ["11"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(100)
        expected = False

        result = {
            "input": ["100"],
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
            self.test_case_4(solution)
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
