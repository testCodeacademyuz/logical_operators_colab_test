from logical_operators import CheckSolution

# Given integer a, check the following statement "The integer is three-digit number".
# input a = 23 output False, input a = 3 output False, input a = 123 output True, input a = 10 output False, input a = -10 output False, input a = -100 output False

class TaskEleven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(23)
        expected = False

        result = {
            "input": ["23"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(3)
        expected = False

        result = {
            "input": ["3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(123)
        expected = True

        result = {
            "input": ["123"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(10)
        expected = False

        result = {
            "input": ["10"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution(-10)
        expected = False

        result = {
            "input": ["-10"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_6(self, solution):
        answer = solution(-100)
        expected = False

        result = {
            "input": ["-100"],
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
            self.test_case_5(solution),
            self.test_case_6(solution)
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