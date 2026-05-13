# Effi-Code: Unleashing Code Efficiency in Language Models

- Decision: Reject
- Scores: 6, 3, 6, 1

## Abstract
As the use of large language models (LLMs) for code generation becomes more prevalent in software development, it is critical to enhance both the efficiency and correctness of the generated code.
Existing methods and models primarily focus on the correctness of LLM-generated code, ignoring efficiency.
In this work, we present \dataset, an approach to enhancing code generation in LLMs that can improve both efficiency and correctness. We introduce a Self-Optimization process based on Overhead Profiling that leverages open-source LLMs to generate a high-quality dataset of correct and efficient code samples. This dataset is then used to fine-tune various LLMs. Our method involves the iterative refinement of generated code, guided by runtime performance metrics and correctness checks. Extensive experiments demonstrate that models fine-tuned on the \dataset show significant improvements in both code correctness and efficiency across task types.
For example, the pass@1 of DeepSeek-Coder-6.7B-Instruct generated code increases from \textbf{43.3\%} to \textbf{76.8\%}, and the average execution time for the same correct tasks decreases by \textbf{30.5\%}.
\dataset offers a scalable and generalizable approach to improving code generation in AI systems, with potential applications in software development, algorithm design, and computational problem-solving.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new dataset Effi-Code, a high-quality dataset of correct and efficient code samples, which is then used to fine-tune various LLMs, by iteratively refining the generated codes by LLMs based on the overhead profiling. It shows that it improves both the correctness and efficiency of the DeepSeek Coder family

### Strengths
- The paper tackles an important problem in the literature.
- The idea of iteratively refining the generated codes based on overhead profiling is novel.

### Weaknesses
1. The papers lack a comprehensive evaluation of the proposed dataset:

- The paper can benefit from a more extensive comparison of Effi-Code Benchmarks across different open-source LLMs.
- The paper can benefit from a concrete example to show how SOAP’s iterative refinement improves the quality of the solutions.
- The profiling metrics setup lacks robustness. Execution time and memory usage are highly sensitive to system noise and can vary significantly across platforms (e.g., desktops, cloud environments). Given that execution times are generally brief (on the order of seconds), these metrics may not effectively demonstrate the efficiency of the generated code.

2. The paper’s structure is somewhat challenging to follow. For example, sections 3.2 and 3.3 discuss filtering out ‘non-algorithmic’ tasks and ‘inefficient’ solutions, yet the exact criteria for these decisions are not clearly specified.

### Questions
- Can the authors please further expand the evaluation process?
- What percentage of solutions improved in efficiency but showed degraded correctness, if any?
- Minor comments: In Table 3, the pass@1 results do not consistently increase as the proportion of Effi-Code used for fine-tuning grows. Could the authors elaborate on this inconsistency?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Effi-Code, a new Python fine-tuning dataset, as well as the pipeline to curate such data, to improve both the efficiency and correctness of function-level code.

The approach aggregates and filters data from open-source datasets and then employs Self-Optimization based on Overhead Profiling (SOAP) [3] to iteratively refine code by analyzing runtime performance.

Experiments fine-tuning Qwen2.5-Coder-7B and DeepSeek-Coder-6.7B (both instruct and base models) on Effi-Code demonstrate significant improvements in HumanEval and EffiBench regarding Execution Time, Max Memory Usage, Total Memory Usage, and Correctness [2].


[1] [Learning Performance-Improving Code Edits (Shypula et al., 2024)](https://arxiv.org/abs/2302.07867)

[2] [EffiBench: Benchmarking the Efficiency of Automatically Generated Code (Huang et al., 2024)](https://arxiv.org/abs/2402.02037)

[3] [EffiLearner: Enhancing Efficiency of Generated Code via Self-Optimization (Huang et al., 2024)](https://arxiv.org/abs/2405.15189)

### Strengths
## Significance

Code optimization is indeed a less-explored problem compared to correctness. The problem is essential for practical applications, particularly in performance-sensitive and resource-constrained environments.

## Soundness

As pointed out by both the PIE [1] and EffiBench [2] papers, benchmarking on (different) real hardware can lead to randomness in the efficiency metrics, so the paper provides 5 independent evaluations with their mean and standard deviation. In addition, the paper conducts thorough ablations on the size of the training set and the size of the off-the-shelf models, which demonstrates the robustness of their main results.


## Effectiveness

Fine-tuning on Effi-Code exhibits significant absolute improvements compared to the off-the-shelf models in all metrics: Execution Time, Max Memory Usage, Total Memory Usage, and Correctness


[1] [Learning Performance-Improving Code Edits (Shypula et al., 2024)](https://arxiv.org/abs/2302.07867)

[2] [EffiBench: Benchmarking the Efficiency of Automatically Generated Code (Huang et al., 2024)](https://arxiv.org/abs/2402.02037)

[3] [EffiLearner: Enhancing Efficiency of Generated Code via Self-Optimization (Huang et al., 2024)](https://arxiv.org/abs/2405.15189)

### Weaknesses
## Novelty

The paper's data curation pipeline includes 4 main stages: aggregating existing open-source data, applying filters on the raw data, applying SOAP [2] to synthesize efficiency-enhanced code, and post-filter the synthesized code.

While this approach successfully consolidates established methods, the raw data sources in Stage 1 and the SOAP [2] method in Stage 3 are not developed within this work. As a result, the novelty of Effi-Code primarily lies in the thoughtful integration of existing methodologies rather than in the development of new ones.

This aspect has the most impact on my Overall Rating and Contribution Rating. I would be glad to reconsider and potentially raise these scores, if the authors could provide further justifications for the unique methodologies or modifications that set Effi-Code apart from prior work, especially SOAP [2].


## Significance

The paper’s evaluations are conducted using HumanEval and EffiBench, both of which are Python benchmarks focusing on function-level competitive programming. Additionally, as mentioned in **Step 1 of Section 3.2, "filter out tasks that are not written in Python"**, the Effi-Code training data is exclusively comprised of Python code.

While these choices are reasonable given Python’s widespread use and popularity among LLM researchers, it is important to note that many real-world, performance-sensitive applications, especially competitive programming, do favor languages like C and C++ due to their finer control over low-level operations.

Evaluating the models on a C/C++ benchmark could provide a more accurate and comprehensive assessment of their code optimization capabilities. Expanding the Effi-Code training set to include C/C++ code might enhance the model's potential for more complicated and more fine-granular code optimization such as I/O choices, data structure choices, and initialization of variables. It would also be interesting to see how the model's performance increases on a Python benchmark when fine-tuning on a C/C++ dataset.


## Soundness

As mentioned in **Step 4 of Section 3.2, "we filter out tasks that do not involve algorithms. The key reason for this is that non-algorithmic tasks usually do not have optimization potential"**, the focus of Effi-Code is on algorithmic optimization.

However, the claim that **"non-algorithmic tasks usually do not have optimization potential"** is not entirely sound. As pointed out by the PIE [1] paper, algorithmic optimization accounts for 34.15% of 120 model optimization samples. Other types of optimizations like I/O, data structure, etc. should also be considered. For example, the mere I/O change from `cin` to `scanf`, or the mere data structure change from Python `list` to `numpy.array` can result in substantial execution time improvements, even if these changes do not affect the Big-O complexity.

Broadening the scope to include non-algorithmic optimizations will not only improve the soundness of the paper, but can also strengthen the significance of Effi-Code in terms of real-world implications.



## Effectiveness

While the Effi-Code pipeline exhibits significant absolute improvements, the relative improvements compared to baseline datasets or data curation pipelines remain unclear. In particular:

1. What would be the baseline performance of the models fine-tuned on the un-optimized version of the final filtered data? This ablation would help isolate the effect of all filters and establish a clearer understanding of their importance in the entire Effi-Code pipeline.

2. What would be the baseline performance of the models fine-tuned on the raw data directly optimized by SOAP without any filtering? This ablation would help isolate the effect of SOAP and establish a clearer understanding of its importance in the entire Effi-Code pipeline.

3. **The evaluation of models fine-tuned on PIE (C++ training set) is conducted on EffiBench (Python test set), which is expected to be lower than the models fine-tuned on Effi-Code (Python training set).** What would be the results if the models fine-tuned on Effi-Code are evaluated on the test set of PIE instead of EffiBench?
This cross-evaluation could reveal how well the Effi-Code generalizes across different programming languages and types of code optimizations, which offers a truly fair comparison to PIE regarding cross-language generalization.


This aspect has a secondary impact on my Overall Rating and Contribution Rating. I would be glad to reconsider and potentially raise these scores, if the authors conduct these specific ablation studies and cross-language evaluations to justify the novel contributions of their approach.


### Questions
## Clarification Questions

1. It's mentioned in **Step 3 of Section 3.2** that **"we analyze whether each test case generated by GPT-3.5-turbo is correct"**. Could you please elaborate on the analysis method used in this process?

2. It's mentioned in **Step 4 of Section 3.2** that **"we filter out tasks that do not involve algorithms"**. Could you please elaborate on the precise definition of "task that does not involve algorithms" and how you filter them?


## Discussion Questions

1. I am curious about your perspective on the evaluation of code optimization. What are your thoughts on the merits and challenges of evaluating code performance on real hardware platforms like EffiBench [2] versus using simulated hardware environments such as PIE [1]?

2. In Table 4, the Max Memory Usage of fine-tuned DeepSeek-Coder-33b-base decreases, and the Execution Time significantly decreases. Have you observed any trade-offs between time optimization and space optimization in this case?


[1] [Learning Performance-Improving Code Edits (Shypula et al., 2024)](https://arxiv.org/abs/2302.07867)

[2] [EffiBench: Benchmarking the Efficiency of Automatically Generated Code (Huang et al., 2024)](https://arxiv.org/abs/2402.02037)

[3] [EffiLearner: Enhancing Efficiency of Generated Code via Self-Optimization (Huang et al., 2024)](https://arxiv.org/abs/2405.15189)

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to address a gap in current approaches to generating synthetic data for post-training LLMs for code. Typically, researchers focus on executability and correctness of the generated code, yet often overlook efficiency, resulting in models that produce functionally correct but computationally inefficient solutions. This paper introduces EFFI-CODE, a dataset and methodology designed to enhance both the efficiency and correctness of LLM-generated code, thereby addressing this common oversight.

EFFI-CODE employs a model-based self-optimization process using overhead profiling feedback, iteratively refining generated code samples to optimize efficiency. 
Results show that LLMs fine-tuned with EFFI-CODE achieve notable improvements in both correctness and efficiency. For example, the pass@1 of DeepSeek-Coder-6.7B-Instruct increased from 43.3% to 76.8%, while the average execution time dropped by 30.5%. This work demonstrates that prioritizing efficiency alongside executability and correctness can yield LLMs that are not only accurate but also resource-efficient.

### Strengths
The paper’s focus on optimizing efficiency in LLM-generated code, alongside correctness, which is quite an important and practically relevant aspect of synthetic data generation. EFFI-CODE’s rigorous data curation process, including iterative optimization cycles and runtime profiling, results in measurable improvements in real-world benchmarks, making it valuable for performance-critical applications in resource-constrained environments.

The paper is well-structured, with clear explanations and supportive visuals, and the authors' commitment to open-sourcing EFFI-CODE fosters reproducibility and encourages broader research on efficiency-focused fine-tuning for code generation.

### Weaknesses
Limited comparison with baselines: While the paper presents significant improvements, it could benefit from a broader comparison with existing methods focused on code efficiency, to better contextualize EFFI-CODE's advancements. Adding these comparisons could strengthen the paper.

Focusing solely on algorithmic performance may be too narrow; efficiency gains could also be achieved by addressing issues related to third-party library usage. Besides that, EFFI-CODE is focused exclusively on Python, it woudl be good to check the generalizability to compiled languages (e.g., C++) and managed languages (e.g., Java) with distinct memory management and execution models.

Parallelization and Concurrency: While EFFI-CODE emphasizes efficiency, it does not explicitly address parallelizable or concurrent code patterns, which can be essential for improving performance in multi-core systems and distributed applications.

### Questions
Have you tried generating tests based solely on the problem and function signature, rather than conditioning on the problem and solution, to reduce the risk of overfitting? Additionally, how many tests are generated per problem - is it typically just one, or are multiple tests used to capture edge cases?

How do you evaluate the test quality in EFFI-CODE? Specifically, do you assess validity based on the presence of assertions and invocation of focal code, or do you also check for stronger criteria, such as line test coverage?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces a new benchmark (Effi-Code) for fine-tuning existing LLMs to generate more efficient code. More specifically, the authors collect code snippets from existing code generation tasks and apply multiple pre-processing steps. These steps include filtering code snippets with risky operations, generating test cases for validating generated code, etc. Moreover, the authors employ Self-Optimization based on overheAd Profile (SOAP) for optimizing the collected code snippets for efficiency. The code snippets are executed against generated tests to collect the execution time and memory usage of code snippets. The profiling results are then provided to a judge LLM (DeepSeek-Coder) along with source code and description to construct an efficient version of the code. The generated efficient code snippets are then used to fine-tune open-source LLMs (deepseek-coder, qwen-code). LLMs fine-tuned on efficient code snippets significantly outperforms the base version of themselves both in terms of efficiency (e.g., execution time, memory usage) and correctness (e.g., pass@1) on HumanEval and Effibench datasets. The authors further perform certain ablation studies to understand other research questions.

### Strengths
- Studying the efficiency of code generated by LLM is an important problem. The authors propose a technique to generate efficient code snippets which can be used for fine-tuning existing LLMs.
- Empirical results performed by the authors depict significant increase in performance of LLMs, both in terms of efficiency and correctness
- A comparison study is performed to compare the performance of Effi-Code with PIE.

### Weaknesses
False claims / Repititive work:
- In the abstract, the authors falsely claim "We introduce a Self-Optimization process based on Overhead Profiling", however, this contribution is already made in a published paper (Soap: Enhancing efficiency of generated code via self-optimization. arXiv preprint arXiv:2405.15189).

- The test case generation technique used in this paper is already made in a published paper (Effibench: Benchmarking the efficiency
of automatically generated code. arXiv preprint arXiv:2402.02037). There is not enough novelty for test case generation in this work.

Too much reliance on LLM:
- The authors decided to fully rely on LLMs when filtering code snippets for risky operations and test case generation. However, in the case of filtering, a simple static analysis approach (without executing the code) could have been used given that static analysis is more sound than using LLMs.
- As for the test case generation, I am wondering why didn't the authors consider using off-the-shelf tools like CODAMOSA (https://dl.acm.org/doi/10.1109/icse48619.2023.00085) and other SOTA test generators from SE community. Again, relying only on GPT-3.5 is not sufficient in generating proper test cases.
- There is no background work on the use of LLM as a judge. I don't see any soundness in using DeepSeek-Coder to construct efficient code snippets.

Presentation issues:
- Some parts of the paper is not well-written. For instance please see lines 73-76.

There are some descrepancies in the paper as well:
- You mention in the instruction that you collected data from 8 sources, however, in section 3 it says seven sources.

### Questions
- Why should somebody trust the filtering for risky operations done by the LLM? Is there any manual investigation of what has been flagged by the LLM as risky operation? Are there any False Positives or False Negatives?
- What is the novelty in test case generation component of Effi-Code? Is it any different from Effibench?
- How do the authors support the use of LLM as a judge for constructing efficient solutions?
- What is the quality of generated test cases by GPT-3.5? Specifically, is it possible to get the code coverage, branch coverage, etc.?
- How do the authors filter non-algorithmic tasks.
- Have the authors performed a deep investigation on why the pass@1 scores of the model increases significantly? For instance, the pass@1 value of deepseek-coder-6.7b-base goes from 7.3 to 59.8. What are the chances the "quality" of these code snippets regardless of them being efficient is causing the increase in performance?

### Soundness
1

### Presentation
2

### Contribution
1
