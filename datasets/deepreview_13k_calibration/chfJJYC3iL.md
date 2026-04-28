# LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
\noindent Large Language Models (\llms{}) applied to code-related applications have emerged as a prominent field, attracting significant interest from both academia and industry. 
However, as new and improved \llms{} are developed, existing evaluation benchmarks (e.g., \humaneval{}, \mbpp{}) are no longer sufficient for assessing their capabilities.
In this work, we propose \livecodebench{}, a comprehensive and contamination-free evaluation of \llms{} for code, which collects \textit{new} problems over time from contests across three competition platforms, namely \leetcode{}, \atcoder{}, and \codeforces{}.
Notably, our benchmark also focuses on a broader range of code-related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation.
Currently, \livecodebench{} hosts over five hundred coding problems that were published between May 2023 and May 2024.
We have evaluated $18$ base \llms{} and $34$ instruction-tuned \llms{} on \livecodebench{}.
We present empirical findings on contamination, holistic performance comparisons, potential overfitting in existing benchmarks as well as individual model comparisons.
We will release all prompts and model completions for further community analysis, along with a general toolkit for adding new scenarios and models.%\footnote{The website is available at: \url{https:}}\footnote{The code is available at: \url{https:}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces LiveCodeBench, a lively-updated dynamic benchmark that is designed to evaluate large language models (LLMs) for coding tasks with minimized data contamination risk.

Aside from being contamination-free, LiveCodeBench also seeks to improve the data quality, difficulty, and task diversity of the benchmark.

The paper also conducts thorough experiments exposing the significant data contamination and overfitting issues.

### Strengths
## Significance

The paper addresses one of the most important issues: data contamination in the existing Code LLM evaluation process. The benchmark is highly practical and should be known and tried by the Code LLM community to encourage more rigorous evaluation of models. 


## Soundness

The paper demonstrates strong soundness through its detailed analyses of the models' performance over time, overfitting issues on HumanEval, and comparison of different types of models.


## Effectiveness

Dynamic benchmarking is indeed an effective solution to mitigate data contamination.

### Weaknesses
## Novelty

The paper presents two key contributions:

1. A comprehensive dynamic benchmark for coding takes

2. Analyses exposing the contamination issues in coding tasks

While these contributions are highly relevant and practical for the Code LLM community, it's important to note that dynamic benchmarking is a technique that has been utilized in various prior works [1,2,3,4] as early as 2021 [1]. Additionally, the issue of data contamination has been systematically examined in earlier studies [5,6], limiting the novel insights that the paper can offer to the broader ICRL community.

To enhance the paper's novelty, it may be beneficial to develop better and more efficient dynamic benchmarking techniques, or introduce new methods to alleviate more intricate contamination issues such as re-phrasing [6].




### Questions
## Discussion Questions

Have you considered addressing more intricate data contamination issues like re-phrasing within the scope of this work?

I believe that many code-specific techniques can be developed to detect re-phrasing contamination such as checking the equivalence or similarity of the test cases and canonical solutions.

I would be happy to raise my score if the authors could incorporate and address those intricate contamination issues in the revision.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Prior LLM coding benchmarks suffer from contamination and saturation issues. This paper introduces LiveCodeBench, a new benchmark that collects new problems from public programming contests (LeetCode, AtCoder, and Codeforces). Besides code completion, the benchmark also tests the self-repair and output prediction abilities of LLMs. The paper provides a comprehensive analysis on over 600 problems and over 50 LLMs, demonstrating that time-segmented evaluations are useful for detecting contamination.

### Strengths
- The paper proposes a coding benchmark with live updates, ensuring fair model evaluation by testing only on new problems after each model’s cutoff date. The time-segmented analysis also reveals a significant drop in performance of some models after release date, indicating notable contamination issues.
- The paper is well-written and organized, with a thorough appendix including discussion on legal compliance and benchmark creation details.

### Weaknesses
 - The novelty is limited. Using competitive programming problems for LLM evaluation has been well adopted. Additionally, the evaluation scenarios in this paper are also not new but borrowed or adapted from prior work (e.g., the test case output prediction can be seen as a chain-of-thought prompting solution of the code execution task). The main contribution of this paper is to scrape the problems with appropriate difficulty and analyze the results in a time-segmented way.
- The relatively small number of problems (~40 LeetCode problems every two months) raises concern about the reliability of the results. I wonder if it’s possible to estimate the variance of the pass@1 performance and the statistical significance of the comparisons.

### Questions
It seems that the drop in performance occurs only for the LeetCode problems and is smooth for other platforms like AtCoder. Do you have any explanation for this interesting phenomenon?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper worked on the evaluation of LLMs for code, proposing a benchmark named LiveCodeBench. The benchmark will be continuously updated by automatically collecting problems from online code contest sites to overcome data contamination. It contains four code-related tasks: code generation, self-repair, code execution, and test output prediction. A large-scale evaluation was conducted on 50 LLMs, which revealed the widespread contamination among LLMs, as well as overfitting and saturation of traditional coding benchmarks like HumanEval.

### Strengths
1. **Benefiting the community**: The benchmark will be continuously updated and provide code ability evaluation with less contamination.
2. **Large scale evaluation**: The authors evaluated 50 LLMs with carefulness about contamination, providing a valuable reference for the code-related capabilities of each model.
3. **Having insights**: The experiments revealed the widespread contamination among LLMs, as well as overfitting and saturation of traditional coding benchmarks like HumanEval.

### Weaknesses
1. **Unproven data representative**: Besides contamination, we also need to know how many code problems we need and how representative they are, to conduct a comprehensive evaluation. However, they were not answered in this paper. Are there mechanisms to guarantee or prove these properties, in particular for new models? The paper lacks a rigorous analysis of the dataset's statistical properties, such as the distribution of problem types, difficulty levels, and the coverage of different programming concepts. Without such analysis, it's difficult to ascertain whether the benchmark truly reflects the diversity of coding challenges encountered in practice. For example, are graph problems over-represented compared to dynamic programming problems, and how does this affect the evaluation of different models?

2. **Unevaluated workflow reliability**: While the workflow of benchmark construction is completely automated, this workflow's reliability was not evaluated. For example, the accuracy of the HTML extractor. The paper does not provide a detailed error analysis of the automated extraction process. It is crucial to understand the types of errors that might occur, their frequency, and their potential impact on the benchmark's integrity. For instance, how often are code snippets or mathematical formulas incorrectly extracted, and what are the consequences for the problem's interpretability?

3. **Unproven test case completeness**: Averaged 18 of the test case count basically is far fewer than test cases used inside the programming task websites; the completeness or sufficiency of these test cases was not analyzed in this paper. The paper needs to justify the sufficiency of the test cases used for each problem. While the paper mentions that the test cases are generated, it does not analyze the coverage of edge cases or boundary conditions. A more thorough analysis of the test case generation process, including the types of inputs generated and their ability to expose potential bugs, is needed.

4. **Biased filtering**: In the code competition scenario that this work focused on, questions with multiple correct outputs for a single input would contain many unique features or have different problem-type distributions. However, they were all removed in this work, which might lead to a bias. Further analysis of the impact of this filtering should be conducted. The removal of problems with multiple correct outputs may introduce a bias towards problems with a single, well-defined solution. This filtering process needs to be examined more closely to understand how it affects the benchmark's overall representativeness and the evaluation of models that might be better suited for problems with multiple valid solutions.

5. **Multi-step track needed**: This work's designs of four tracks were motivated by AlphaCodium. Including AlphaCodium, state-of-the-art competition-level code generation works nowadays broadly applied multi-step workflow. However, besides one-step revision, multi-step code generation was not evaluated in this work. The benchmark's evaluation of code generation capabilities is limited by its focus on single-step generation and revision. It does not adequately assess the ability of models to engage in iterative refinement, which is a crucial aspect of real-world software development. The absence of multi-step evaluation limits the benchmark's ability to capture the full spectrum of code generation capabilities.

### Questions
The contribution of this work to the community depends largely on your continued maintenance efforts. Do you have a long-term plan?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces LiveCodeBench, a new benchmark designed to evaluate LLMs for code-related tasks. 
LiveCodeBench addresses some key limitations of previous benchmarks, 
including issues like data contamination, overfitting, saturation, and limited application range. 
Unlike existing benchmarks, LiveCodeBench assesses not only code generation but also self-repair, code execution, and test output prediction. 
Alongside proposing the benchmark, 
the authors perform a comprehensive evaluation and analysis of the contamination and overfitting problem in popular LLMs. 
The paper also introduces a difficulty-guided problem curation strategy, 
which enhances the evaluation's effectiveness by creating clearer margins between model performances, 
allowing for a more meaningful comparison.
The evaluation covers 52 models, with sizes ranging from 1.3B to 70B, 
providing a fairer and more reliable understanding of model performance in code-related tasks.

### Strengths
* LiveCodeBench has a live update mechanism that mitigates data contamination and enables continuous growth. 
  This mechanism ensures that the benchmark remains useful for evaluating newer models, 
  even those with a knowledge cut-off date beyond its release.
* With the timestamps on the tasks, the authors conduct a novel "live" evaluation of code generation to directly address data contamination issues. 
  This approach offers deeper insights into the models' actual coding capabilities, focusing on genuine problem-solving rather than mere memorization.
* The difficulty guided problem curation is particularly effective in revealing performance differences between models of similar sizes, making it practical to use for meaningful evaluation.
* The paper employs a clustering method to identify models that overfit HumanEval. 
  While overfitting to older benchmarks is a well-known issue, 
  the authors' method offers empirical evidence and analysis that specifically highlights the models affected by this problem.

### Weaknesses
 * Novelty: The benchmark's construction primarily aims to create a newer and harder version of existing benchmarks. 
  However, a key issue with LLM benchmarks for code is that Olympiad in Informatics (OI) programs are not typically representative of real-world software engineering and programming languages. 
  OI programs often have a distinct style and differ in their learned representations compared to code from real software projects. 
  This has led to a shift in focus in this research area from OI competitive programming to open-source software projects, as seen in recent work like SWE-bench [1] and RepoBench [2].


### Questions
1. The tasks of *code execution* and *test case output prediction* appear to be quite similar. 
   According to the paper, the distinction lies in their prompt: 
   code execution is to predict the output based on inputs and functions in *programming language*, 
   while test case output prediction is to predict the output based on inputs and function descriptions in *natural language*. Given the similarity between these two tasks, is there any observable correlation in their results?
2. Test case generation typically is designed as predicting the entire test case from a given function implementation [3,4], 
   which is more practical in real-world software engineering and testing applications, 
   such as in tools like Copilot. 
   I'm curious why the authors choose a different approach to evaluating test generation in the form of $(I, f_{\text{NL}}) \mapsto O$, 
   where the input and natural language function descriptions are used to predict the output.
3. In the **Problem Difficulty** paragraph of Section 3.1, 
   the authors state that they collected problems of varying difficulty levels as labeled by competition platforms. 
   However, how did the authors address potential rating bias across these platforms? 
   Given that different competition platforms are designed for distinct user groups and, as the authors note, CodeForces problems are generally harder than those on other platforms, 
   there is likely a selection bias in difficulty ratings across different platforms.

[3]: Nie, Pengyu, et al. "Learning deep semantics for test completion." ICSE 2023.

[4]: Rao, Nikitha, et al. "CAT-LM training language models on aligned code and tests." ASE 2023.

### Soundness
3

### Presentation
3

### Contribution
3
