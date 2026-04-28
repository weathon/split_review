# Rethinking logic in AI: A novel benchmark inspired by polynomial analogue of Gandy's fixed point theorem

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
This paper introduces a novel benchmark for evaluating the logical reasoning capabilities of Large Language Models (LLMs), grounded in the polynomial analogue of Gandy's classical fixed point theorem. Since this theorem can be used to describe the P-complete HornSAT problem, and our benchmark is based on this theorem, our benchmark thus covers all problems from class P and shows that serious problems have already arisen in this class, not to mention those benchmarks whose complexity classes are NP-complete and NP-hard. Drawing on concepts from mathematical logic, we design a parameterized set of recursively definable problems where the objective is for LLMs to predict whether a problem belongs to an inductively definable set of polynomial complexity. By varying the parameters, we generate problem instances of differing complexity. Our experiments reveal that current state-of-the-art LLMs with zero-shots promts fail to reliably solve even the most straightforward cases despite an effective deterministic algorithm existing. Even advanced models like GPT-4 exhibit significant biases in solving benchmark problems. These findings highlight the limitations of modern LLMs as code interpreters, even in basic scenarios, and underscore the necessity for hybrid LLM/interpreter systems. Furthermore, they emphasize the importance of developing quantitative tests for reasoning, given the increasing reliance on LLM-based systems in decision-making applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method to generate functions that will be evaluated by a LLM in order to study how LLLMs perform as interpreters\

### Strengths
The paper addresses a pertinent ptoblem

The proposal seems sound and allows for a number of parameters

The evaluation is interesting and includes both open and closed source systems.

### Weaknesses
Reading this work, I got the feeling that it may be too early for such in-depth analysis, we should first improve LLMs :). 

The paper does provide some insight on problems with bias, but the results seem quite independent of parameter variation. Again, raises the question of whether we are pushing the LLMs too hard?

Finally, do you consider the parameters representative of what the LLMs will find?

pg 6: being easy to verify in one’s mind -> that's an interesting point, the paper does not discuss this basic question much,

There are some typos, namely Eq?? in 3

### Questions
The title starts very strongly: RETHINKING LOGIC IN AI. Are you actually doing that?

Abstract: The abstract seems to have redudant text
eg, 
Even advanced models like GPT-4 exexhibit significant biases in solving benchmark problems

and then 
even the most advanced GPT-4 models exhibit biased behavior while
solving recursive problems.

5 on the results of mathematical logic -> it is not very clear what you refer to here

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study the reasoning capabilities of LLMs by studying their capabilities to decide recursively defined properties of nested lists. They formulate the properties to be tested so that they are polynomial time testable. They implement a generator that generates these problem instances with varying complexity; pairs consisting of a nested list and recursively defined property. They consider two kinds of encodings of their problems to LLMs; inputs to conversational LMs and inputs to code completion LMs. They then compare the reasoning capabilities of different LLMs.

They found out that the LLMs they tested were not capable of deciding the recursive properties.

### Strengths
It is interesting to study the capabilities of LLMs using mathematically defined objects.  It is a nice idea to study whether LLMs can decide PTIME-computable recursive problems before tackling more complex ones.

### Weaknesses
In summary, the authors study the capabilities of LLMs by studying how well they can decide recursively defined properties of nested lists. While to have understanding on the capabilities of LLMs is important, the paper itself seems to me more like a good student project to showcase the limits of the current capabilities of LLMs, than a research paper ready to be published. In particular, the main contribution of the paper is the idea to study capabilities of LLMs by inputing pairs consisting of nested lists and recursively defined properties of those lists, the task being to decide whether the list satisfied the properties given. The authors then test various LLMs on the inputs they generate.

The theoretical contribution of the submission is to consider recursively defined properties and inputs to decide, and the technical contribution is to generate these inputs and tabulate the results with respect to different LLMs. I do not think that either contribution of the paper suffices for a publication in a top general conference in machine learning. The choice of using nested lists, while mathematically sound, does not seem to provide a significant advantage over other P-complete problems, such as Horn-SAT. The paper lacks a strong justification for why this specific problem representation is more insightful for understanding LLM reasoning than other established P-complete problems. Furthermore, the empirical evaluation, while thorough, primarily demonstrates a negative result (LLMs fail on these tasks), which, while useful, does not provide a deep understanding of *why* they fail or how to improve their reasoning capabilities. The paper also lacks a clear connection to existing benchmarks or theoretical frameworks for evaluating LLM reasoning, making it difficult to place the results in a broader context.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel benchmark for evaluating the logical reasoning capabilities of Large Language Models (LLMs). 

The proposed approach involves generating [object, condition] pairs, where objects are nested lists of elements (for example, numbers) and conditions are expressed with recursive functions. The task of the LLM is to determine whether the object satisfies all conditions.
The source code of the benchmark is publicly available.

The main finding of the paper is that current state-of-the-art LLMs fail to reliably solve even the most straightforward cases, thus pointing to significant limitation in their logical reasoning capabilities.

======================================================

Update after rebuttal: in the light of the discussion during the rebuttal period, I am happy to raise my score.

### Strengths
1) The challenge of assessing precisely the reasoning capabilities of LLMs is extremely important to the development of LLMs themselves. This paper makes a contribution in this sense by introducing what looks like an interesting benchmark.
However, why the proposed benchmark is actually important is not developed enough in the submission.

2) The experimental evaluation is rather in-depth, with several important LLMs considered, both proprietary and publicly available.

### Weaknesses
1) The paper is only 8 pages long, two pages shorter than the page limit. 
It is not clear why the authors didn't include some of the material appearing in the appendix, for instance.

2) The authors define their class of problems through the Polynomial Analogue of Gandy’s Fixed Point Theorem (which I am not familiar with). However, it is not clear why this specific class is so important as to represent a benchmark for LLMs.

Also, the authors might consider to clarify the relation with standard propositional Boolean logic (which I assume is the non-nested version).

3) The related literature is not discussed at any length. It almost looks like there has not been any other effort to assess the reasoning capabilities of LLMs, including logic-based reasoning.

### Questions
1) Why is the class of problems considered in this submission so relevant as to represent a benchmark for LLMs?

2) How does this contribution compare to the current state of the art?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new benchmark dataset for evaluating the reasoning ability of LLMs, based on the PAG theorem. The problems in the dataset contain a theorem that returns boolean output based on a given nested list. The dataset is created using a condition generator and a probe generator to generate the theorems and the nested list instances respectively. The theorem and the assignment are represented in text as Python functions and lists. The paper then prompts LLMs to predict whether a theorem is satisfied or not by the given nested list, and finds that state of the art LLMs are unable to when prompted in a zero shot setting.

### Strengths
The proposed dataset can be generated parametrically, which varies its difficulty level. 

The proposed dataset is difficult for existing LLMs. 

The dataset generators are well-defined.

### Weaknesses
To me, the dataset is not strongly motivated. I agree that new reasoning benchmark datasets are important for LLMs, but why this specific dataset is needed is unclear. What is the advantage of this dataset over, for example, a set of problems that include SAT formulas in CNF and the set of assignments to the variables, where the LLM is asked to verify if the solution is valid?

It seems that the LLMs are only evaluated on this dataset using zero-shot prompting. Extensive literature has shown that LLM reasoning abilities can be significantly enhanced by chain-of-thought [1], tool-using [2], self-consistency [3] etc. Therefore, it is hard to draw a definitive conclusion on LLM reasoning abilities from zero-shot prompting results alone.

By representing the problem in Python code, the dataset is limited to evaluating LLM’s reasoning ability in the specific context of executing Python, which may not represent LLM’s reasoning ability in the general case. For example, by asking the conversational LLM to output the result of print(is_member_0(x)), the LLM needs to understand the Python syntax on top of the logic of whether x satisfies f or not.

### Questions
The problem is prompted to the LLMs in the format of python code. Why not represent the problems using text? Were other representations considered to represent the problems?

Were there any further analysis performed on the results shown in Figure 1? Would simply negating the solution from GPT-4-turbo achieve 90%+ accuracy? Does a model getting the wrong answer 90% of the time mean it is consistently doing (wrong) reasoning internally?

### Soundness
2

### Presentation
2

### Contribution
1
