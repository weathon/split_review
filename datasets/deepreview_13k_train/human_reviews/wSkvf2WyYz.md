# SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
We propose Step-by-Step Coding (SBSC): a multi-turn math reasoning framework that enables Large Language Models (LLMs) to generate sequence of programs for solving Olympiad level math problems. After each turn/step, by leveraging the code execution outputs and programs of previous steps, the model generates the next sub-task and the corresponding program to complete it. This way, SBSC, sequentially navigates to reach the final answer. SBSC allows more granular, flexible and precise approach to problem-solving compared to existing methods. Extensive experiments highlight the effectiveness of SBSC in tackling competition and Olympiad-level math problems. For Claude-3.5-Sonnet, we observe SBSC (greedy decoding) surpasses existing state-of-the-art (SOTA) program generation based reasoning strategies by absolute 10.7% on AMC12, 8% on AIME and 12.6% on MathOdyssey. Given SBSC is multi-turn in nature, we also benchmark SBSC’s greedy decoding against self- consistency decoding results of existing SOTA math reasoning strategies and observe performance gain by absolute 6.2% on AMC, 6.7% on AIME and 7.4% on MathOdyssey.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a step-by-step prompting technique for solving math problems using large language models (LLMs). In this approach, the model is prompted to generate sub-tasks in code format at each step, which are then executed to produce intermediate outputs. These outputs, along with the code from previous steps, are used to prompt the model again to solve the problem sequentially. The proposed method is tested a few benchmarks, including MC, AIME, and MathOdyssey, demonstrating improvements over existing prompting techniques.

### Strengths
A key strength of this paper is the step-by-step approach, which leverages inference time compute to break down complex problems into manageable sub-tasks. For each sub-task, SymPy-based Python code is generated, and the model is instructed to include a print statement at the end of each code snippet so that intermediate execution outputs can be generated. 

This structure allows the model to build on the results of previous steps, using the executions output/feedback to condition its generation of the next step and sub-task. 

The step by step process with intermediate feedback provides the model with a chance to detect and correct errors or rewrite parts of the code. This improves the overall performance of the model.

### Weaknesses
The paper's approach relies heavily on the careful design of the step-by-step coding framework exemplars. This, with the inclusion of detailed comments within the python codes in these exemplars, seems to require considerable manual effort. While this strategy is effective for the test sets discussed, it may be overfitted to these specific benchmarks. This raises some concerns about the generalization of the method to broader problem sets or applications.

Another limitation is that the method is highly dependent on the coding capabilities of the underlying language model. While the authors acknowledge the correlation between the model's coding performance and the accuracy of the SBSC approach, the exact nature of this correlation is unclear. Specifically, it's not clear how much the performance is tied to the model's ability to generate syntactically correct code versus its ability to generate semantically correct code that accurately reflects the mathematical reasoning. In addition, the method relies heavily on SymPy, which might further limit its flexibility and adaptability, especially given that a large proportion of the questions depend on it.

The approach demands a relatively long context length, which could be a constraint in certain settings. It would be helpful if the authors specified a rough minimum context length required for the given shots and the math problem. This would help get better insights into the method's scalability. Furthermore, the method's reliance on intermediate outputs, while beneficial for debugging, might also introduce additional computational overhead.

Lastly, the discussion of the related works section seems somewhat rushed. The first sentence feels awkward and reads more like filler rather than contributing meaningfully to the content. A more thorough comparison with existing literature on program or tool-aided generation (the section following POT and PAL) could be extended, as it is the most relevant part of the discussion. This would provide deeper insights into the novelty and strengths of the proposed method.

### Questions
I believe that randomly sampling 4 examples out of a set of 10, even multiple times, may not provide sufficient variety to effectively test the sensitivity of the prompts. It's unclear how diverse the 10 exemplars are to begin with. Perhaps a more meaningful  test would be to have a larger pool of exemplars?

In figure 5, are the methods compute/token matched? What is the ratio of the tokens generated by the SBSC method compared to others such as TIR-ToRA? 

Figure 7 seems to have the wrong caption.

What is the advantage of this step-by-step approach compared to other similar methods, particularly in cases where the model is unable to revisit and revise a problematic step (e.g., Step 1) once it has progressed to later steps?

In table 1, why is there no number for maj@7 for SBSC?

How does the method perform when used with open LLMs such as LLaMA?

What types of errors are reported in Section 5.3? Are they primarily syntactic or semantic in nature?

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Step-by-Step Coding (SBSC) for solving complex mathematical problems for large language models. The authors conduct extensive experiments comparing SBSC against other state-of-the-art methods like COT, PAL, and TIR-ToRA on datasets like AIME, AMC, and MathOdyssey.

### Strengths
* The paper is easy to understand, with a well-defined problem statement that introduces multi-turn TIR as a solution for complex multi-step issues.
* The main experimental results are sufficiently thorough, providing reasonable evidence for the improvements attributed to SBSC.

### Weaknesses
 * SBSC introduces an additional step of decomposing a large problem into smaller sub-problems during the decoding phase. How to ensure that this decomposition is both correct and rational? Could this lead to the introduction of additional errors?

* Existing methods, such as TIR-ToRA, output a planning-like COT before code generation. Does this serve the same function as the multi-turn approach proposed in this paper? Is it merely a modification that incorporates multiple compiler feedback loops? The planning step in TIR-ToRA, while similar to a high-level plan, lacks the dynamic, iterative refinement of SBSC. The key difference lies in SBSC's ability to generate and evaluate intermediate steps, allowing for error correction and adaptation, whereas TIR-ToRA's planning is static and monolithic.

* The introduction of multi-turn in SBSC may result in decreased efficiency. The manuscript should include comparisons under equivalent token costs. While the authors have addressed this by comparing against self-consistency decoding of other methods, a more detailed analysis of token usage and cost per question is needed to fully assess the efficiency trade-offs.

* I strongly recommend that the authors review their writing for numerous typographical errors, particularly the inconsistent use of citet and citep.
    * line 157: "Our inference procedure is inspired by ToRA Gou et al. (2023)"
    * line 196: "AIME, AMC, MathOdyssey Fang et al. (2024) and OlympiadBench He et al. (2024)"
    * line 199: " MathOdyssey Fang et al. (2024), a popular benchmark..."
    * ....

### Questions
* Has SBSC demonstrated improvements across all domains of mathematical reasoning? Are there instances where multi-step code decomposition is not feasible or effective?

* Given the authors' claim regarding enhanced performance in Olympiad competitions, it would be beneficial to include benchmark results from:
    * JEE-Bench
    * OlympicArena
    * Omni-MATH
    * Additionally, consideration should be given to experiments involving GSM8K and MATH, as many problems in MATH derive from AMC and AIME questions.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Step-by-Step Coding (SBSC), a framework that guides Large Language Models (LLMs) to solve advanced math problems by producing a sequence of programs. SBSC operates iteratively, using the outcome of code from previous steps to inform the generation of subsequent sub-tasks and solutions. This approach is shown to be more detailed, adaptable, and accurate than existing methods. The efficacy of SBSC is supported by extensive testing on competition-level math problems. For the Claude-3.5-Sonnet model, improvements using SBSC with greedy decoding are significant, with performance gains of 10.7% on AMC12, 8% on AIME, and 12.6% on MathOdyssey over current state-of-the-art strategies. Additionally, when comparing SBSC's greedy decoding to self-consistency decoding of current methods, there are notable increases of 6.2% on AMC, 6.7% on AIME, and 7.4% on MathOdyssey.

### Strengths
- The empirical results demonstrate that SBSC achieves superior performance over state-of-the-art methods, suggesting that its iterative nature allows for more accurate problem-solving in the context of advanced math problems.
- The paper's experiments cover a variety of math competitions, indicating that SBSC is not tailored to a specific type of problem but is instead broadly applicable to Olympiad-level mathematics.
- The paper is well-structured and clearly written.
- The ablation and analysis section offers a deep analysis of the results, providing insights into why SBSC performs better than existing methods and under what circumstances it might be most beneficial.

### Weaknesses
I appreciate the efforts made in this paper to apply step-by-step partial code generation and execution within the challenging domain of Olympiad-level mathematics and the promising results. My query pertains to the aspect of novelty concerning this approach. The paper states in Line 62 that "Fundamentally, both PAL & TIR-ToRA generate a single program block to solve the entire problem", highlighting step-by-step code generation and execution as a key contribution of SBSC. However, given that the concept of language models incrementally generating code to interface with external tools has been explored in prior research, such as ReAct (https://arxiv.org/abs/2210.03629) and ToolFormer (https://arxiv.org/abs/2302.04761), and the idea is highly related to OpenAI's code interpreter and assistant APIs, I am curious about the distinctiveness of the approach presented in this paper. May I kindly suggest that the authors could provide a more explicit comparison with these precedents? An elaboration on how the proposed SBSC framework diverges from or advances these existing methods, particularly in the unique setting of mathematical problem-solving, would be enlightening. This addition would help the readers and reviewers to better understand the specific innovation and value of the proposed work in the broader context of step-by-step code generation research. Specifically, the paper needs to clarify how SBSC's iterative process differs from ReAct's interleaved reasoning and action approach, and how it goes beyond simply using a code interpreter as a tool, which is already a feature in many LLM APIs. The distinction from ToolFormer also requires further elaboration, as that framework also learns to use external tools, and the paper needs to clarify how SBSC's approach to tool use is different in the context of mathematical reasoning. The current explanation of SBSC's contribution is not sufficiently detailed to differentiate it from these existing methods.

### Questions
Apart from the issues expressed in the weaknesses section, I have no other concerns.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Step-by-Step Coding (SBSC), a multi-step reasoning framework where LLMs are prompted to break down complex questions into sub-questions and solve them iteratively with the help of generated code. The experiments demonstrate that SBSC achieves higher accuracy compared to Chain-of-Thought (CoT) and Program-Aided Language (PAL) on competition and Olympiad-level math problems, regardless of problem topics or code errors. The authors also show that self-consistency further improves SBSC's performance.

### Strengths
1. The concept of step-by-step, multi-turn coding is both intuitive and innovative. Unlike previous approaches that focus mainly on validation after the final generation or self-debugging, SBSC’s use of intermediate results from an executor provides more actionable and informative feedback. This method effectively combines task decomposition from CoT with the program-assisted capabilities of PAL, offering a promising approach.

2. The experiments on Olympiad-level math problems clearly show SBSC’s effectiveness, outperforming the baseline by a large margin.

### Weaknesses
1. While the idea has potential for broader applications, the authors only tested it on Olympiad-level math problems. Additionally, while SBSC appears promising, is it appropriate to apply this method to such difficult problems? (See more detailed discussion in question 1.)

2. The baseline comparisons could be more comprehensive. Although the comparison with CoT and PAL is sufficient to demonstrate SBSC's effectiveness, it does not fully showcase its strengths or weaknesses relative to other complementary methods, such as multi-turn program validation, self-debugging, the use of additional tools, or expert models. Even if such comparisons might be unfavorable to SBSC, they would provide valuable context for understanding the broader landscape and gauging SBSC's relative contribution.

### Questions
1. The mainly question is whether using code to solve oplymipcs-level math problem is a reasonable approach. Both baselines PaL and ToRA are not designed for such difficult problems, which often require more than basic operations or listing equations, such as some extra theorems cannot be solved by code. In Figure 1, there are several points where the LLM's use of Python code seems unnatural. First, the code is strongly based on some black-box high-level function provided by some libraries, like `summation` in `sympy` library to get a lemma "$1^3+\dots+n^3=\frac{n^4}{4}+\frac{n^3}{2}+\frac{n^2}{4}$". It is not a natural usage of codes (at least Python codes) because for more challenging tasks, the LLM could not find a propriate library provides the information. Similarly, the program's brute-force traversal from $n=1$ to $1000$ is not a typical way to solve such problems. A more natural way would involve algebraic manipulation like $$ \frac{n^4}{4}+\frac{n^3}{2}+\frac{n^2}{4}\equiv17(\mod n+5)$$ $$ n^4+2\times n^3 + n^2\equiv68(\mod n+5) $$ $$ (-5)^4+2\times(-5)^3+(-5)^2\equiv 68 (\mod n+5) $$ $$ 400 \equiv 68 (\mod n+5) $$ so that $(n+5)\mid 332 \Rightarrow n +5 =83 \text{ or } 166 \text{ or } 332 \Rightarrow n = 78, 161, 327$ then we final check these candidates and get the final answer $n=78\text{ and }161$. The process shown in Figure 1 shows that using Python code is not a natural and reasonable way to solve these problems. The authors should further compare SCSC's approach to human-like reasoning on a subset of problems or some examples, or to analyze which types of Olympiad problems are most/least suited to SBSC's code-based approach.

2. While step-by-step reasoning is a natural approach, writing and displaying code in steps is not common practice. Programmers often organize their code by defining classes and functions first, then calling them in a main function. How can we ensure that LLMs are capable of generating effective step-by-step code? I believe that the authors should add some experiments to support current LLMs have this ability. Additionally, some steps in the reasoning process may not correspond to clear intermediate results in code. For instance, what happens if a step only defines a function with no immediate output to display? I'm curious whether this decomposition approach remains effective across different problem types.

3. Does the method's effectiveness depend on delicate prompt engineering or careful selection of few-shot examples? Although the experiments in Section 5.1 suggest the method is not overly sensitive to the few-shot candidate selection, I would like more clarity on the details and principles behind crafting these 10 examples. When generalizing the method to other tasks, how should the steps be divided to ensure each step yields clear, intermediate results that aid subsequent reasoning?

2. Minor questions:
    1. The authors say "similar to NuminaMath, we remove all the answer choices from each AMC-12 question and modify the question to ensure an integer answer". But I cannot find evidence that the NuminaMath modifies questions to ensure an integer answer. Rather, it is a preprocess in original AIME dataset to keep answer as integer and Numina focuses on this problem only for decontamination. The authors should clarify this point.
    2. In Figure 4, how is the x-axis "error steps per problem" determined? A more detailed explanation of this experiment would be helpful.
    
I would raise my rating to 8 or higher if the authors can address my two main concerns (questions 1 and 2).

### Soundness
4

### Presentation
4

### Contribution
4
