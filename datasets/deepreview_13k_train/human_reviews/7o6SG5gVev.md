# TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Code generation models can help improve many common software tasks ranging from  code completion to defect prediction. Most of the existing benchmarks for code generation LLMs focus on code authoring or code completion. 
Surprisingly, there has been far less effort dedicated to benchmarking software testing, despite the strong correlation between well-tested software and effective bug detection.
To address this gap, we create and release \benchmark, a large-scale benchmark to measure test generation performance. Based on SWEBench, \benchmark comprises 68,647 tests from 1,210 code and test file pairs across 11 well-maintained Python repositories. It covers initial tests authoring, test suite completion, and code coverage improvements. 
Test authoring simulates the process of a developer writing a test suite from scratch, while test completion mimics the scenario where a developer aims to improve the coverage of an existing test suite. 
We evaluate several popular models, with sizes ranging from 7B to 405B parameters.
Our detailed analysis highlights \benchmark's contribution to a comprehensive evaluation of test generation performance. In particular, models struggle to generate high-coverage test suites, with the best model, GPT-4o, achieving an average coverage of only 35.2\%. This is primarily due to models struggling to reason about execution, and their frequent assertion errors when addressing complex code paths.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a new LLM for test generation benchmark, TestGenEval. It builds on the same repositories as SWEBench, but focuses on extracting the test files and code-test pairs. TestGenEval studies two tasks: test suite generation (generating an entire test suite given a codebase) and test completion (generating test methods to a partial test suite). The generated tests are not only compared against human-written tests based on similarity, but also based on code coverage and mutation score, which are more important metrics for test quality. This paper benchmarked several recent LLMs across different sizes on TestGenEval, and found that generating and completing test suites are challenging tasks for current LLMs.

### Strengths
+ Included the measurement of code coverage and mutation score as part of the evaluation metrics, which are important metrics for measuring the quality of generated tests.

+ Conducted a comprehensive set of experiments using LLMs of different sizes and different configurations.

+ Performed an interesting analysis on the current LLMs' performance on TestGenEval, including the correlation with existing benchmarks and common error types.

+ Paper is well-written and easy to follow.

### Weaknesses
 - Not sure if it is the best to include only the tests appeared in the PRs used by SWEBench; this may miss the other tests that did not appear in those PRs (i.e., don't have recent bug-fixing changes), making the data collection process biased.



### Questions
- What is the key difference between the newly created benchmark and the evaluation sets used in prior work on ML for test generation/completion (e.g., Rao et al. 2023, Nie et al. 2023, Dinella et al. 2022, Tufano et al. 2020)? Namely, Rao et al. 2023 had a pretty large dataset for pre-training, and evaluated on the task of generating first/last/additional tests. Both Rao et al. 2023 and Nie et al. 2023 also used runtime metrics (compile and pass).

- line 142, "we next extract code test file pairs from the code and test files run in the PR": do you only consider the tests that appeared in PRs in SWEBench? Or all the tests in those repositories?

- line 189, "This setup is in line with current test completion work Rao et al. (2023); Nie et al. (2023).": this may not be true. The "test completion" in Rao et al. 2023 and Nie et al. 2023 was statement-level completion, but yours is method-level completion, which sounds more like the "test method generation" task in Rao et al. 2023.

- Which mutation tool and mutants did you use? And how many mutants do you generate for each example?

- For test suite generation task, consider renaming "Pass @ 1" to "Any Pass @ 1" to reduce confusion.

- line 361, "the most common error is not generating tests with asserts": but will that lead to a runtime error, and if not, how do you detect them? Also, do you count the generated tests without asserts as pass or not pass?

### Soundness
3

### Presentation
4

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
This paper constructs TestGenEval, a comprehensive and proper benchmark for testing unit test generation abilities of existing LLMs. The benchmark unprecedentedly incorporates mutation scores into their evaluation metric. It also considers multiple generation scenarios including full, first, last, and extra test generation. 10 models including a massive Llama 405B is evaluated on the benchmark and detailed results are given in the main paper and the appendix. 
This paper is leaning towards the rejection side since 1. the author did not make effort to evaluate if the generated test matches the definition of a unit test and merely add in mutation score to evaluate further the test effectiveness, and 2. the model selected for evaluation is questionable.

### Strengths
- The introduction of mutation score improves on previous benchmarks and ensures a more proper benchmark
- The work introduces the most comprehensive benchmark dedicated to test generation so far
- The work evaluated on a large set of models, even on a very expensive 405B Llama
- Extensive quantitative/correlation analysis, contamination check, and also detailed qualitative analysis, which shows the good quality of the dataset

### Weaknesses
### Major
- The evaluation runs the 405B Llama model, which is quite impressive. However, it is unclear why is Llama model evaluated but not other closed-source ones (which are much easier to run comparing to Llama 405B) ones like Claude and Gemini.
- The paper acknowledges that test generated by the LLM can be very different from what human might write. However, there is no procedure in the paper to guarantee that the model generates actually “unit tests” as deemed by human developers (except for the prompt). This means that the model can just generate one big complicated test case for all of the generation scenarios considered (full, first, last, extra), which is against the purpose of unit tests in the first place.
- The task of test generation is generally more solvable by agents or by providing example usages. However, the paper only evaluates on vanilla models and didn’t evaluate even the simple case of adding dependencies into the prompt related to the task.

### Misc
- Citations are not wrapped in brackets (Like Jain et al. when discussing R2E), which is mildly annoying

### Questions
- Why is the massive Llama 405B selected in the evaluation rather than other better-performing models like Claude and Gemini?
- What effort does the benchmark made to ensure the test matches the conventional definition of a unit test?
- Why isn't any agents/tools evaluated in the evaluation?

### Soundness
2

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
4

### Summary
The theme of this paper is the introduction and evaluation of a large-scale benchmark named TESTGENEVAL, which is designed to measure the performance of test generation and test completion. 

TESTGENEVAL is constructed based on the SWEBench dataset and includes 68,647 test cases from 1,210 code and test file pairs across 11 well-maintained Python repositories. 

This benchmark aims to fill the gap in existing code generation language model (LLM) benchmarks that focus less on software testing, despite the strong correlation between well-tested software and effective bug detection. 

TESTGENEVAL covers tasks such as initial test authoring, test suite completion, and code coverage improvement, aiming to comprehensively assess test generation performance. 

The paper also evaluates several popular models with parameter sizes ranging from 7B to 405B and provides a detailed analysis of TESTGENEVAL's contribution to the evaluation of test generation performance.

### Strengths
1. Continuous Improvement of Test Suites: TESTGENEVAL supports not only the generation of test suites from scratch but also the completion of existing test suites, which is particularly important for test optimization in continuous integration and continuous deployment (CI/CD) processes.

2. Evaluating and Comparing Different Models: TESTGENEVAL provides a standardized environment to evaluate and compare various code generation models, including both open-source and proprietary models, helping researchers and practitioners understand the performance of different models in real-world software testing tasks.

3. Test Generation for Real-World Use Cases: TESTGENEVAL is built based on real-world projects, meaning it is closer to actual development testing needs rather than being limited to academic research or toy problems.

### Weaknesses
1. Dependence on Prompts and Temperature Settings:
Model performance is highly dependent on the prompts and temperature parameters used. The paper focuses mainly on 0-shot performance, asking each model to generate an entire test suite or complete a test given the code under test, which may limit the model's performance. This approach neglects the potential benefits of few-shot learning or more sophisticated prompting strategies that could significantly improve results. The reliance on a single, potentially suboptimal, prompt strategy makes it difficult to assess the true capabilities of the models.

2. Risk of Data Contamination:
There is a risk of data contamination in the pre-training data of models. Although the paper suggests that data contamination is unlikely by comparing the perplexity of tests in TESTGENEVAL with common GitHub code of similar length, it remains a potential issue. The comparison to general GitHub code might not be sufficient, as models could have been exposed to the specific structure or patterns within the SWEBench dataset, even if not the exact code. In addition, since TESTGENEVAL is adapted from the SWEBench dataset, there is a risk of models overfitting to this specific dataset. This is especially concerning given the relatively small size of the dataset compared to the scale of pre-training data.

3. Computational Cost:
The computational cost of calculating mutation scores is high. Each synthetic bug introduced to the code under test requires an additional test suite execution. This makes the benchmark computationally expensive to run, especially for large models or when exploring different hyperparameter settings. The high cost could limit the accessibility of the benchmark and hinder more extensive experimentation.

4. Assumptions of Test Generation:
All test generation benchmarks assume that the code under test is correct. Generated tests may fail on the code under test while exposing bugs in the code under test (a phenomenon known as the oracle problem). This assumption limits the applicability of the benchmark in real-world scenarios where code is often buggy, and it does not account for the possibility of tests revealing issues in the code rather than just validating it.

### Questions
1. I would like to know what is the cost involved in executing TestGenEval? Including length of prompt, required GPU memory, running time and more cost analysis?

2. How do the authors ensure the quality of the dataset, including but not limited to possible leakage of data and semantic correctness of the given code?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces TestGenEval, 
a novel benchmark designed to evaluate neural test generation models on real-world Python projects. 
TestGenEval is built upon 11 popular Python repositories selected from the patch generation benchmark SWE-Bench.
It assesses neural test generation from two key perspectives: test generation from scratch and test completion based on some existing test functions. 
Both aspects, particularly test completion, are valuable for real-world software engineering applications, such as IDE plugins. 
The authors evaluate several popular LLMs on TestGenEval, 
pointing out that even the best-performing model GPT-4o struggles with achieving high code coverage.

### Strengths
* A standard, real-world project-based benchmark for test generation is crucial and useful for advancing software testing research.
* TestGenEval is the first benchmark to incorporate mutation score as a metric, a commonly used measure in software engineering to assess the robustness of test cases.
* It offers Docker images instrumented with coverage and mutation score, ensuring the reusability of the artifacts.
* TestGenEval is also the first benchmark to evaluate file-level test completion, which aligns well with the real-world software development workflows.
* The authors perform a comprehensive quantitative analysis of the results, demonstrating the correlations and effects of various components within the benchmark.

### Weaknesses
 * This paper lacks details on mutation score calculation.
  The authors do not provide specifics on how mutation score is measured in the benchmark. 
  In traditional software engineering, mutation testing is creating mutants of the code under test to evaluate the robustness of the test cases in detecting these modifications. 
  However, the paper does not clarify the process used to construct program mutants for test generation, 
  which is a non-trivial task that requires further clarification.


* The authors claim that real-world unit testing involves reasoning over complex *files*, 
  generating tests for a given *class under test*. 
  The authors also point out that the other related benchmark only measure the individual test method rather than an entire test suite is a weakness. 
  This claim is not well supported with reference nor evidence, 
  and is not commonly adopted by the software engineering community. 
  Unit testing aims to validate the correctness of the smallest building block (and hence, an "unit") in a complex software project.
  In modern software engineering, the "units" of software are often functions in the codebase.
  If these functions are tested/verified to be correct, then the composition should be correct without further testing.
  Therefore, the best practices often suggest to write functions that are independent and de-coupled.
  The more recent and popular programming languages, for example Rust, often abandon class and favor function composition
  over inheritance.
  Are these languages not related to "real-world unit testing"?

* The authors claim that real-world unit testing requires reasoning over complex *files* and generating tests for a given *class under test*. 
  They argue that other benchmarks' focus on individual test methods,
  rather than entire test suites, is a weakness. 
  However, this claim is not well-supported by references or evidence and is not commonly adopted by the software engineering community.

  Unit testing aims to validate the smallest building blocks of software, or so-called "units," 
  which are often functions rather than entire classes. 
  In modern software engineering, if individual functions are tested and verified to be correct, 
  the composition of them is expected to be correct without additional testing. 
  Consequently, best practices emphasize writing independent and de-coupled functions.

  Furthermore, more recent programming languages, such as Rust, 
  favor function composition over inheritance, reflecting a shift away from class-based design. 
  This raises the question of whether these languages fall outside the scope of "real-world unit testing" as claimed by the authors, 
  despite their increasing relevance in software development.

* The lack of quantitative analysis results in the main text is a significant weakness. 
  While the authors conduct five different quantitative analyses, all results are placed in the Appendix. 
  If an analysis is mentioned in the main text, it would be more effective to present the corresponding results alongside the discussion. 
  For space consideration, the authors could include only the most important analyses and results in the main text, 
  while moving less critical details to the Appendix. 
  This approach should also be applied to qualitative analyses for better readability and impact.


* Minor writing issue: the authors cite all references without using parentheses, regardless of context. 
  In some cases, using `\citep` instead of `\cite` would enhance the reading experience by making the citations more contextually appropriate. 
  Adjusting this would improve the flow and clarity of the text.

### Questions
Pleased address the concerns in **Weakness**.

### Soundness
3

### Presentation
2

### Contribution
3
