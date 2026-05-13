# BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions

- Decision: Accept
- Avg Score: 9.00
- Scores: 8, 8, 10, 10

## Abstract
Task automation has been greatly empowered by the recent advances in Large Language Models (LLMs) via Python code, where the tasks ranging from software engineering development to general-purpose reasoning. While current benchmarks have shown that LLMs can solve tasks using programs like human developers, the majority of their evaluations are limited to short and self-contained algorithmic tasks or standalone function calls.
Solving challenging and practical tasks requires the capability of utilizing \textbf{\textit{diverse function calls as tools}} to efficiently implement functionalities like data analysis and web development.
In addition, using multiple tools to solve a task needs compositional reasoning by accurately understanding \textbf{\textit{complex instructions}}. Fulfilling both of these characteristics can pose a great challenge for LLMs.
To assess how well LLMs can solve challenging and practical tasks via programs, we introduce \bench{}, a benchmark that challenges LLMs to invoke multiple function calls as tools from 139 libraries and 7 domains for 1,140 fine-grained tasks.
To evaluate LLMs rigorously, each task encompasses 5.6 test cases with an average branch coverage of 99\%. 
In addition, we propose a natural-language-oriented variant of \bench{}, \benchi{}, that automatically transforms the original docstrings into short instructions only with essential information. Our extensive evaluation of 60 LLMs shows that \textbf{\textit{LLMs are not yet capable of following complex instructions to use function calls precisely, with scores up to 60\%, significantly lower than the human performance of 97\%}}. The results underscore the need for further advancements in this area.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces BigCodeBench, a novel code generation benchmark that improves existing ones like HumanEval by incorporating more diverse function calls and complex instructions. BigCodeBench comprises 1,140 Python code generation tasks, necessitating the use of 139 libraries across 7 domains. The dataset was constructed through a semi-automated framework leveraging collaboration between LLMs and human experts. In this process, LLMs are prompted to generate coding tasks based on sampled code snippets, performing both initial generation and refinement of programs and test cases, while human annotators continuously provide feedback to enhance quality. Extensive experimental evaluations reveal that current LLMs struggle with accurately executing complex instructions and function calls, achieving scores of up to 60%, significantly below the human performance of 97%. These results highlight the ongoing challenges and the need for further advancements in the field of code generation.

### Strengths
- The paper makes a valuable contribution to code generation benchmarks by incorporating diverse function calls and complex instructions, offering a novel perspective on evaluating LLM capabilities in library and tool use. Results indicate that even top-performing LLMs face challenges with these tasks, highlighting opportunities for further advancements.
- The paper is well-structured and easy to follow. The benchmark curation framework is technically sound, back with a systematic design and thorough quality checks. The extensive evaluation provides some insights into how current LLMs handle library usage and follow complex instructions.

### Weaknesses
 - The technical contribution of the benchmark curation framework appears incremental, as the collaborative approach between LLMs and human is already widely adopted in LLM research.
- While Python libraries are essential for task solutions in this benchmark, the rapid evolution and versioning of these libraries can introduce compatibility issues. The authors should consider methods to mitigate the effects of version incompatibility in the evaluation process.

### Questions
- The Python libraries used in this study are mostly popular ones, likely present in the pretraining data of most LLMs. Future work could explore how LLMs adapt to newer, domain-specific libraries that may not have been included in their training data.
- Based on the benchmark results, what potential approaches could improve the performance of existing LLMs in handling complex instructions and function calls? Insights on targeted training techniques or model adjustments would be valuable.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel benchmark to evaluate the ability of cutting-edge LLMs in function calling and complex instruction following for code generation.

### Strengths
- The proposed benchmark introduces a challenging task that involves diverse function calls as tools and complex instruction-following for code generation. Current state-of-the-art LLMs achieve up to 60% Pass@1, while human performance reaches 97%, providing a clear benchmark for future research to improve on.
- By evaluating a wide range of both open-source and closed-source LLMs on this benchmark, the study establishes a strong foundation and adds credibility to the proposed framework.

### Weaknesses
 - There is a risk of future data contamination [1, 2]. To mitigate this, it may be beneficial to release only the validation set while keeping the test set hidden, similar to practices used in NL2SQL benchmarks [3,4].

- Some domains, such as visualization tasks returning graph outputs, would benefit from examples illustrating how the test cases are constructed for evaluation.

### Questions
- How to prevent future data contamination? 
- How are test cases constructed to evaluate visualization tasks requiring graph outputs?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The authors present BigCodeBench, a massive high-quality benchmark to test Large Language Models (LLMs) ability to perform diverse function calls and solve complex code instructions. BigCodeBench comprises 1,140 fine-grained Python programming tasks after proper cleaning and filtering and covers functionality from 139 widely adopted programming libraries. Specifically, the benchmark evaluates two common programming scenarios (1) Code completion based on structured docstrings, and (2) the completion of programming tasks based on natural language instructions. The authors used powerful LLMs to source programming tasks, refactor code, and generate test cases, under constant human supervision. This construction process is a remarkable example of a perfect balance between LLM automation and human curation to ensure data quality and reliability. The authors conduct an extensive evaluation of state-of-the-art LLMs on BigCodeBench. Among others, the results show that LLMs are not yet capable of following complex instructions to use function calls precisely.

### Strengths
### Originality
The benchmark proves to be original for the following reasons:
- It contains diverse code, sourced from widely adopted Python libraries from seven domains. 
- It contains more complex programming tasks than other benchmarks. Specifically, the authors report on task cyclomatic complexity compared to other function-level Python programming benchmarks, and a larger coverage of function calls compared to state-of-the-art function calling benchmarks. 

### Quality

#### Benchmark Construction
The authors followed best practices to select, clean, and filter the seed data. They also integrate the use of LLMs into the process by keeping humans in the loop when needed. Moreover, code execution in a controlled environment is performed to ensure code quality.

#### Validation
- The authors extensively evaluate 60 state-of-the-art LLMs on BigCodeBench-Complete (code-completion based on docstrings) and 35 instruction-tuned LLMs on BigCodeBench-Instruct (programming tasks based on natural language instructions). 

### Clarity
- The benchmark construction and evaluation processes are remarkably explained.
- Limitations of the dataset as well as future work are addressed in detail as part of the appendix.

### Significance
As BigCodeBench will be open-sourced it represents a significant contribution to the research community. Moreover, the study reveals interesting observations about the ability of LLMs in complex code-completion tasks, which sets a roadmap for the development of new training datasets to improve these capabilities.

### Weaknesses
 Please fix the typo in line 182 (refractor -> refactor) to make even better this amazing work.

### Questions
- How do you distill observations such as "Interestingly, we observe that instruction-tuned LLMs can omit the essential import statements of the given prompts", do you rely on static analysis of automatic error logs? are humans also involved in the process?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This benchmark paper proposes improved execution-based evaluation for solving complex real-time application like code generation problems. It focuses on both the effective instruction query and the detailed test case setup for unit test sets, curated using human-LLM collaboration.

### Strengths
Quite a thorough analysis and structured approach of generation of benchmark is taken into account. With detailed literature review of past works in the field, the paper also demonstrates its effectiveness as an improved code generation benchmark and evaluation.

### Weaknesses
Apart from tiny bits of improvements needed, the paper is quite detailed in its analysis. However, it lacks the essence of what are the areas where these LLM are failing on the new benchmark, and a compared analysis of how an expert human would perform in the same. So as to note the scope of baseline improvement.

### Questions
- With respect to line 237, what were the reasons or examples of model failure in the dataset that was improved and captured by the annotators? Subsequently, what steps were taken to overcome it?
- In case of BigCodeBench-Instruct benchmark, each user query is structured well in terms of sequence and format of instruction for code generation. This might not be the case when it comes to user-like query. Analysis on part of robustness to ambiguity in NL, variation in structured format needs to be further analyzed and presented within the paper.
- Line 300, 'PL: Programming Language', is not used within context of the table and is unnecessary.
- Table 1: Tool Statistics, # Call column, format the column to have all '/' inline, like the adjacent columns.
- Perhaps, Figure 6 can be more visually summarized using scatter plot with grid colored based on size of parameter of LLM. Can be updated, if it helps provide better display of story.
- A definition of what calibrated scores should be added in description.
- Table 3 comparison can also be done against other datasets like MBPP Plus dataset, NaturalCodeBench and EvalPlus.
- Add on analysis of how new benchmark overcomes the issue of data contamination due to the benchmarks being used as training data in several LLM. What rephrasing or variation in query structuring is ensured to tackle this?
- Add in example of failure cases and categorize to why LLM still fails on new benchmark. 
- How well does an expert perform comparatively?

### Soundness
4

### Presentation
4

### Contribution
4
