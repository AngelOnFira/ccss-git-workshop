import random

def gen_problems(steps, num_problems):
    problems = []
    for i in range(num_problems):
        this_problem = []
        this_problem.append([random.randint(1, 10) for i in range(len(steps) + 1)])
        answer = this_problem[0][0]
        for i, step in enumerate(steps):
            if step == 0:
                answer += this_problem[0][i + 1]
            elif step == 1:
                answer -= this_problem[0][i + 1]
            elif step == 2:
                answer *= this_problem[0][i + 1]
        this_problem.append(answer)
        problems.append(this_problem)
    return problems

with open('names.txt', 'r') as filehandle:  
    names = [name.replace("\n", "") for name in filehandle.readlines()]

outfile = ""
testfile = "import unittest\nfrom calculations import *\n\nclass TestAllFunctions(unittest.TestCase):\n"

step_list = ["+", "-", "*"]

for name in names:
    steps = []
    for x in range(2):
        steps.append(random.randint(0,2))
    steps.sort(reverse=True)

    outfile += "# " + name + "'s function\n"
    outfile += "# this should take the input and then apply these steps\n"
    
    testfile += "    def test_" + name.lower().replace(" ", "_") + "(self):\n"

    step_text = "# num1 "
    for i, step in enumerate(steps):
        step_text += step_list[step] + " num" + str(i + 2) + " "

    problems = gen_problems(steps, 5)

    for problem in problems:
        testfile += "        self.assertEqual(" + name.lower().replace(" ", "_") + "_function(" + str(problem[0][0]) + ", " + str(problem[0][1]) + ", " + str(problem[0][2]) + "), " + str(problem[1]) + ")\n"

    testfile += "\n"
    step_text += "\n"
    outfile += step_text

    outfile += "# please return the result\ndef " + name.lower().replace(" ", "_") + "_function(num1, num2, num3):\n    pass\n\n"

testfile += "if __name__ == '__main__':\n    unittest.main()"

with open("../calculations.py", "w") as text_file:
    print(outfile, file=text_file)

with open("../test.py", "w") as text_file:
    print(testfile, file=text_file)