from logical_operators import CheckSolution

# Given two integers a, b, check the following statement "Each of the numbers A and B is odd".
# input a = 3 b = 5 output = True, input a = 2 b = 4 output = False, input a = 0 b = 1 output False, input a = 0 b = 6 output False

class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(3, 5)
        expected = True

        result = {
            "input": ["3", "5"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(2, 4)
        expected = False

        result = {
            "input": ["2", "4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(0, 1)
        expected = False

        result = {
            "input": ["0", "1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(0, 6)
        expected = False

        result = {
            "input": ["0", "6"],
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
                print(f"input: {', '.join(test_case['input'])}")
                print(f"answer: {test_case['answer']}")
                print(f"expected: {test_case['expected']}")
                