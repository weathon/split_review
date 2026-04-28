# MHPP: Exploring the Capabilities and Limitations of Language Models Beyond Basic Code Generation

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Recent advancements in large language models (LLMs) have greatly improved code generation, specifically at the function level. For instance, GPT-4o has achieved a 91.0\% pass rate on HumanEval. However, this draws into question the adequacy of existing benchmarks in thoroughly assessing function-level code generation capabilities. Our study analyzed two common benchmarks, HumanEval and MBPP, and found that these might not thoroughly evaluate LLMs' code generation capacities due to limitations in quality, difficulty, and granularity. To resolve this, we introduce the Mostly Hard Python Problems (MHPP) dataset, consisting of 210 unique human-curated problems. By focusing on the combination of natural language and code reasoning, MHPP gauges LLMs' abilities to comprehend specifications and restrictions, engage in multi-step reasoning, and apply coding knowledge effectively. Initial evaluations of 26 LLMs using MHPP showed many high-performing models on HumanEval failed to achieve similar success on MHPP. Moreover, MHPP highlighted various previously undiscovered limitations within various LLMs, leading us to believe that it could pave the way for a better understanding of LLMs' capabilities and limitations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a function-level code generation benchmark comprising 7 distinct problem types. With state-of-the-art models like GPT-4o achieving a Pass@1 of 51.1, this benchmark offers a valuable resource for advancing future work in the community.

### Strengths
- A key question about whether current LLMs have mastered function-level code generation, and the detailed breakdown of 7 challenge types effectively motivate the need for this benchmark.

### Weaknesses
 - The benchmark includes 210 problems, which, while comparable to HumanEval’s 164, may be insufficient for broader generalizability. Note that recent benchmarks, like BigCodeBench [1], offer over 1K problems.

- Current code generation benchmarks including this work are vulnerable to future data contamination as the test set is often public. To mitigate this, splitting the benchmark into validation and hidden test sets, with evaluations on the test set limited to submissions, may be advisable, following NL2SQL [2, 3].

### Questions
- While not essential, including results for GPT-o1-preview could further underscore the point that current LLMs have yet to fully master function-level code generation, particularly if its performance is lower.

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
5

### Summary
The paper introduces a new dataset called Mostly Hard Python Problems (MHPP), consisting of 210 unique, human-curated Python programming problems designed to evaluate LLMs' abilities across seven manually identified challenges. Next, it presents experiments on 26 LLMs providing empirical insights.

### Strengths
* **Benchmark and Error Analysis.** The authors analyze existing benchmarks MBPP and HumanEval identifying mistakes and contamination. They also produce a manual categorization of mistakes made on HumanEval
* **New benchmark.** The authors provide a manually curated benchmark of 210 problems focusing on mistakes identified on 
HumanEval. This provides confidence in the quality of the benchmark problem statements
* **Qualitative Analysis.** The authors provide insights into model failures through detailed qualitative analysis on existing and proposed benchmarks.

### Weaknesses
 * **Benchmark Size.** The benchmark only consists of 210 benchmark problems. The benchmark size is limited and puts concerns over empirical findings in question. This is an even more serious concern for problem for the category-wise results presented where the number of benchmark samples would be around 30-40 (Tables 2, 3 and Figure 4) -- potentially increasing noise levels to over 10/15% making the results unreliable.

* **Confidence Intervals.** As I understand, section 5.1 computes the confidence intervals for noise introduced due to temperature sampling. This should be properly clarified since it does not account for variability due to the limited size of the benchmark which is a considerably bigger source of noise. This is also a known issue with HumanEval (see [1]).

* **Related Work.** The paper does not clarify or distinguish from many programming benchmarks released in the past year including but not limited to xCodeEval, CodeScope, RepoEval, RepoBench, ClassEval, LiveCodeBench, EvoEval, BigCodeBench. 

MHPP is particularly similar to EvoEval [2] which identifies overlapping sets of problem types `Difficult, Creative, Subtle, Combine, and Tool Use` against `Redefinition, Distraction, Shortcut, CommonSense, Cornercase, Complexity and Codesense` studied in this work. [2] additionally proposed an approach to automatically curate problems from existing benchmarks -- however at the cost of not providing sufficient guarantees on problems - a strength of manual curation performed by the authors. The related works should be discussed and differences clarified appropriately 

* **Novelty.** While collected through manual curation, the paper does not challenge existing empirical performance trends (beyond the reduced performance on the more challenging benchmark). However, this should not diminish the usefulness of the benchmark problems considering saturation in HumanEval.

### Questions
* Can the authors clarify the confidence intervals constructed differentiating the types of noise observed? Additionally, it might be useful to measure the noise in evaluating the performance of 30/40 samples using a bootstrapping-based approach (sample n problems out of 210 and measuring noise).

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new coding benchmark that is intended to be more challenging for Code LMs than MBPP and HumanEval. It also undertakes an analysis of the standard failure modes of models on existing benchmarks as well as leakages of existing benchmarks in the pre-training data.

### Strengths
1. The benchmark is human-created and (for the moment) is unlikely to be a part of any pre-training corpora
2. The authors show that the problems are challenging enough to leave some headroom, even for the SOTA models

### Weaknesses
Overall, I do not see the point of this benchmark in terms of bringing something to the field that is not already out there:

1. ~14 tests on average per sample makes it better than HumanEval and MBPP but is still far outmatched by benchmarks such as EvalPlus [1]
2. In terms of being a challenging test for CodeLMs, due to limitations in chosen domains, library usage and question difficulty, it is, on average, well outdone by existing benchmarks like BigCodeBench [2], ClassEval [3] and SWE-Bench [4].
3. It is also a Python-native benchmark, which leaves out medium and low-resource programming languages that existing benchmarks like McEval [5], Multipl-e [6] or MxEval [7] cover.

### Questions
It would be very useful for the authors to more explicitly situate this benchmark in terms of existing work and what it uniquely brings to the table.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MHPP, a new benchmark for code generation that seeks to address the limitations of existing benchmarks like HumanEval and MBPP, which have become too simple for current high-performing language models such as GPT-4. MHPP contains 210 human-curated Python problems, designed in a similar code completion style to HumanEval but with enhanced diversity and difficulty across various problem types (categorized as 7 challenges). Evaluation results on 26 LLMs reveal that models performing well on HumanEval do not achieve comparable results on MHPP, highlighting the increased complexity of this benchmark. Additional analysis also examines the types of errors made by models like GPT-4 and confirms a correlation in performance trends with HumanEval.

### Strengths
Overall, it is a good attempt to address the limitations of existing code generation benchmarks with more finegrained and complex evalution. Extensive evaluation show that this increase in complexity helps reveal the performance limits of advanced LLMs, which perform well on simpler benchmarks but struggle with MHPP.

### Weaknesses
 - **Incremental Contribution**: While this paper makes a commendable attempt to address the limitations of prior code generation benchmarks by offering a more fine-grained evaluation, its novelty and technical contributions are relatively incremental. It aligns with a line of research that introduces increasingly challenging benchmarks to highlight the limitations of LLMs without substantially advancing our understanding of how to overcome these challenges. Additionally, the insights drawn from the results are somewhat **limited**, especially considering that other more complex code generation benchmarks, such as LiveCodeBench, already exist. To make it more solid work, the authors should provide more insights from the results and how they guige targeted improvements to model architectures or training. For example, they can analyze patterns in the errors to gain insights into fundamental limitations of current LLM approaches.
- **Unsystematic Problem Curation**: The problem categories and challenges are curated manually, which may affect consistency, coverage, and diversity. The lack of an automated, systematic process for problem generation could limit the scalability and reproducibility of this benchmark, making it harder to ensure high quality and comprehensive coverage across problem types.

### Questions
* How to ensure high diversity and comprehensive coverage of fully human-crafted benchmarks?
* Could you provide a summary of the key insights derived from the experimental results?
* Are there any potential approaches to enhance LLMs to better handle these challenges uncovered by MHPP?

### Soundness
3

### Presentation
2

### Contribution
2
