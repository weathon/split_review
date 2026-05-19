# SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Evaluating aligned large language models' (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts, however, face three limitations that we address with \textbf{SORRY-Bench}, our proposed benchmark. 
\textbf{First}, existing methods often use coarse-grained taxonomies of unsafe topics, and are over-representing some fine-grained topics. For example, among the ten existing datasets that we evaluated, tests for refusals of self-harm instructions are over 3x less represented than tests for fraudulent activities. 
SORRY-Bench improves on this by using a fine-grained taxonomy of 45 potentially unsafe topics, and 450 class-balanced unsafe instructions, compiled through human-in-the-loop methods. 
\textbf{Second}, linguistic characteristics and formatting of prompts are often overlooked, like different languages, dialects, and more -- which are only implicitly considered in many evaluations.
We supplement SORRY-Bench with 20 diverse linguistic augmentations to systematically examine these effects.
\textbf{Third}, existing evaluations rely on large LLMs (e.g., GPT-4) for evaluation, which can be computationally expensive. We investigate design choices for creating a fast, accurate automated safety evaluator. By collecting 7K+ human annotations and conducting a meta-evaluation of diverse LLM-as-a-judge designs, we show that fine-tuned 7B LLMs can achieve accuracy comparable to GPT-4 scale LLMs, with lower computational cost.
Putting these together, we evaluate over 40 proprietary and open-source LLMs on SORRY-Bench, analyzing their distinctive refusal behaviors.
We hope our effort provides a building block for systematic evaluations of LLMs' safety refusal capabilities, in a balanced, granular, and efficient manner.\footnote{Benchmark demo, data, code, and models are available through \url{https://sorry-bench.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
SORRY-Bench addresses gaps in LLM safety by introducing a refined 44-class taxonomy and balanced dataset that evaluates model refusal behavior across diverse unsafe topics and linguistic variations. Testing on 50+ models reveals significant differences in refusal consistency, especially with low-resource languages and specialized dialects, underscoring the need for improved alignment in LLMs. Fine-tuned smaller LLMs are shown to be efficient, accurate safety evaluators, enabling scalable safety assessments.

### Strengths
1. The paper proposes a comprehensive coverage of unsafe topics with a refined 44-class taxonomy that captures a broader array of unsafe topics
2. The paper includes many linguistic variations and prompt styles, providing some robustness to the evaluation.
3.  Leveraging fine-tuned smaller LLMs as safety evaluators reduces computational costs while maintaining high accuracy, making large-scale safety assessments feasible and scalable.

### Weaknesses
1. By fine-tuning models to excel on SORRY-Bench, there’s a potential for overfitting, where models may perform well on specific benchmarked scenarios but struggle to generalize to unexpected, real-world unsafe requests.

2.  SORRY-Bench highlights the variability in safety performance across different LLMs, particularly in handling low-resource languages, indicating challenges in achieving consistent, universal safety standards across diverse models and user inputs.

### Questions
How can SORRY-Bench ensure that improvements in model safety performance generalize effectively to real-world scenarios beyond the specific categories and linguistic variations included in the benchmark?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SORRY-Bench, a systematic benchmark designed to evaluate the safety refusal capabilities of large language models (LLMs). The authors identify three major shortcomings in existing evaluation frameworks and address them through SORRY-Bench.

1.	They establish a fine-grained taxonomy of 44 potentially unsafe topics, compiling a dataset of 440 class-balanced unsafe instructions.
2.	They enhance the evaluation process by incorporating diverse linguistic formats and prompt variations, leading to the addition of 8,800 unsafe instructions and 20 linguistic augmentations.
3.	They develop a large-scale human judgment dataset with over 7,000 annotations to optimize the design of automated safety evaluators, revealing that fine-tuned smaller models can match or exceed the performance of larger models like GPT at a lower computational cost.

The benchmark evaluates over 50 proprietary and open-weight LLMs, highlighting significant variations in their safety refusal behaviors. The authors aim for SORRY-Bench to serve as a foundational tool for balanced and efficient assessments of LLM safety refusal capabilities.

### Strengths
1. Comprehensive Benchmark: SORRY-Bench reviews the extensive benchmarks built from previous work and systematically consolidates them into a large-scale and balanced dataset, providing a solid foundation for evaluating the safety refusal behaviors of LLMs.

2. Significant Contribution: The provided benchmark and human judgment dataset for safety refusal behaviors could be valuable for future research on LLM safety. While, the exploration of various models’ results on the benchmark is also sufficiently comprehensive.

### Weaknesses
For the further improvement in writing and content:
1. Lack of Explanation on Domain Division: The paper divides safety risks into four domains, but it does not provide a clear rationale for this division. An explanation of why these specific domains were chosen and how they align with existing work would enhance the clarity and applicability of the taxonomy.
2. Unclear Contributions: The benchmark, dataset, and experiments on the benchmark proposed in this paper are its core contributions; however, these are not clearly summarized or highlighted in the writing. A dedicated section listing the contributions could more directly showcase the paper’s contributions.
3. Lack of Background Information: the impact of research on model safety refusal on the safe deployment and practical application of language models, and whether it can help users better utilize the models. These background issues are not addressed, making it difficult for readers to fully follow this paper.
4. Insufficient Analysis of Model Differences in Safety Refusal: The paper lacks an analysis of the reasons behind the differences in safety refusal behavior among mainstream language models. It would be beneficial to discuss possible reasons for these variations, such as differences in model architecture, training data, alignment techniques, or other model-specific characteristics. This additional analysis could provide valuable insights into why certain models perform better or worse in refusing unsafe instructions and help guide future improvements.
4. Enhanced Use of Human Judgment Data: The human judgment dataset is a valuable asset, and the authors could explore ways to leverage it more effectively. For instance, they could consider integrating few-shot learning or prompt tuning techniques to refine and specialize the automated safety evaluators.

Minor Comments:
1. The paper could benefit from a brief comparison with other safety benchmarks, highlighting what distinguishes SORRY-Bench in terms of granularity, dataset size, and language diversity.
2. Clarify Contributions: It would be beneficial to clearly state the key contributions in a summary or list format within the introduction or conclusion. This could provide readers with a concise understanding of the unique value of the paper.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces SORRY-Bench - a benchmark for evaluating LLM refusal rates. Compared to prior benchmarks, this benchmark uses more fine-grained categories (44 categories, each with 10 examples), and also augments each baseline prompt with 20 linguistic variations. The authors explore various methodologies to evaluate refusal responses, and suggest fine-tuning smaller open-source models is sufficiently good. The authors then evaluate >50 LLMs on the benchmark, revealing interesting differences in refusal behavior across LLMs.

### Strengths
- The fine-grained categorizations enables real insights into differences in LLM refusal behavior.
  - Figure 4 displays non-trivial insights into the refusal behavior of various LLMs, and enables an evaluator to understand a model's refusal profile at a fine-grained level.
  - This help understand an individual model's refusal profile, and also helps compare between various models.
  - This understanding is not possible with other aggregated datasets/benchmarks.

- Creates a valuable human-annotated labeled dataset for refusals/non-refusals.
  - This is valuable within the paper for fine-tuning and evaluation purposes, but also valuable beyond the paper for future work.

### Weaknesses
- Main body lacks some important details.
  - The main body does not describe how new example instructions are generated.
  - Section 2.3 says "we further create numerous novel potentially unsafe instructions..." without describing *how* these new instructions are created.
  - Section 2.4 says "We then compile 20 linguistic mutations from prior studies into our dataset..." without describing *how* these mutations are created.
  - I think it is important to describe, at least briefly, how the new datapoints in the dataset are generated.

- Dataset is restricted by previous datasets.
  - If my understanding is correct, the categories are determined purely by categorizing instructions from prior datasets. This means that, if potentially new categories of harm will not be included in the resulting dataset.

- Fine-tuning may introduce bias in evaluation.
  - See Question 4 below.

### Questions
1. What proportion of the resulting dataset is new? What proportion is instructions from prior datasets?
    - It is not clear how much of the dataset is simply an aggregation of previous datasets. This would be a good detail to include/clarify.

2. Why is "time cost" the best metric to compare evaluation techniques? (section 3.3)
    - Evaluations can be done in parallel, so I don't think time cost seems like the right metric, or it at least needs some justification.

3. Why are generations sampled probabilistically? (section 4.1)
    - Doing greedy generation would render the results reproducible/deterministic. Doing evaluation with probabilistic sampling requires justification.

4. Might it be the case that fine-tuning evaluation models leads to bias?
    - For example, if in the training set every instruction of "self-harm" is refused, the model may learn to categorize all examples with a "self-harm" instruction as refused, regardless of the model response.
    - Is this a concern? Why or why not?

5. Could you provide some examples of disagreement between the evaluation and human evaluators? Is there a systematic pattern in the disagreements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper begins by conducting an empirical study on the limitations of current safety evaluation datasets and methods. Three main issues were identified:
1. The taxonomies of unsafe topics are overly broad, with some fine-grained topics being overrepresented.
2. Linguistic characteristics and prompt formatting are often overlooked.
3. Automated evaluations often rely on expensive models like GPT-4.

To resolve these issues, the authors propose a new benchmark called **SorryBench**, which introduces a more detailed 44-class safety taxonomy and accounts for diverse linguistic characteristics.

Additionally, the authors collected a large-scale human-annotated safety judgment dataset with over 7,000 entries. Using this dataset, they explored which design choices contribute to creating a fast and accurate safety evaluation benchmark.

Finally, the authors used SorryBench and  a fine-tuned safety evaluator, to evaluate over 50 existing models, spanning from 1.8B to 400B+.

### Strengths
1. The paper identifies significant issues in existing safety datasets and introduces a high-quality dataset and safety evaluator, which carry implications for both academic research and practical applications.
2. The systematic study on automated safety evaluators is valuable for researchers relying on such methods.
3. Comprehensive experiments were conducted on representative large language models, using **SorryBench**, with detailed analyses provided.

### Weaknesses
No apparent weaknesses.

### Questions
1. In Figure 4, GPT-3.5-turbo appears to outperform GPT-4 and 01 in terms of safety. Generally speaking, GPT-4 is considered to have superior safety mechanisms compared to GPT-3.5-turbo. Could the authors explain this discrepancy?

### Soundness
4

### Presentation
3

### Contribution
3
