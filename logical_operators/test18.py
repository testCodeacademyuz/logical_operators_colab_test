from logical_operators import CheckSolution

# Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
# input a = 12345 output True, input a = 74321 output False, input a = 13579 output True

class TaskEighteen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(12345)
        expected = True

        result = {
            "input": ["12345"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(74321)
        expected = False

        result = {
            "input": ["74321"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(13579)
        expected = True

        result = {
            "input": ["13579"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(11111)
        expected = False

        result = {
            "input": ["11111"],
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