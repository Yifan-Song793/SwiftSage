# Instruction

You are a reward model. You will be given a problem, a solution. You will then evaluate the solution based on the criteria provided.

## Problem
<problem>

### Current Reasoning Steps
<reasoning>

## Current Answer
<current_solution>


## Your Evaluation

We are not sure if the current answer is correct. Please evaluate the current solution based on the following criteria:

1. Correctness
2. Completeness

- You should review the original problem to analyze the solution step by step, and provide feedback by pointing out any mistakes or missing parts in the solution.
- Take care and do not give false information in the critical feedback.
- The final answer is the output of the code snippet provided in the solution, so if the code snippet is correct, the final answer should be correct as well.
- Note that you should not ask for any input from the console in the code. The code should be self-contained and print the final answer at the end.
- Provide a score from 1 to 3 and a brief explanation. 
    - score=1 means the provided answer is totaly wrong.
    - score=2 means the provided answer is mostly correct, but there are still a few issues in the Python code or the reasoning step.
    - score=3 means the provided answer is perfectly correct.
- If you are not sure about the reasoning, provide a score of 1 and explain why you are not sure about the final answer.
- If the answer is perfectly correct, but the reasoning step is not comprehensive or the Python code is not very efficient or the Python code lacks comments, you can still give a score of 3. 


## Output Format

Remember to present your output in the following format:

<feedback>
Your critical feedback here.
</feedback>


<score>
Your score here. From 1 to 3.
</score>

# Important Notes

You must follow the format strictly, do not miss any field. Start your output by "<feedback>" and end your output by "</score>".