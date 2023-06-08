from logical_operators import CheckSolution

# Given two integers a, b, check the following statement "At least one of the numbers 'a' and 'b' is negative".
# input a = -4 b = -3 output = True, input a = -1 b = 1 output = True, input a = -10 b = 1 output True, input a = 5, b = 4 output False, input a = 0, b = 0 output False

class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(-4, -3)
        expected = True

        result = {
            "input": ["-4", "-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-1, 1)
        expected = True

        result = {
            "input": ["-1", "1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(-10, 1)
        expected = True

        result = {
            "input": ["-10", "1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(5, 4)
        expected = False

        result = {
            "input": ["5", "4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution(0, 0)
        expected = False

        result = {
            "input": ["0", "0"],
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
                print(f"input: {', '.join(test_case['input'])}")
                print(f"answer: {test_case['answer']}")
                print(f"expected: {test_case['expected']}")