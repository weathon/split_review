# KOR-Bench: Benchmarking Language Models on Knowledge-Orthogonal Reasoning Tasks

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
In this paper, we introduce \textsc{Knowledge-Orthogonal Reasoning (KOR)}, which minimizes the impact of domain-specific knowledge for a more accurate evaluation of models' reasoning abilities in out-of-distribution scenarios. Based on this concept, we propose the \textsc{Knowledge-Orthogonal Reasoning Benchmark (\our)}, encompassing five task categories: Operation, Logic, Cipher, Puzzle, and Counterfactual. \our{} emphasizes the effectiveness of models in applying new rule descriptions to solve novel rule-driven questions. O1-Preview and O1-Mini achieve accuracies of 72.88\% and 70.16\%, significantly outperforming Claude-3.5-Sonnet and GPT-4o, which score 58.96\% and 58.00\%, revealing considerable performance gaps and highlighting KOR-Bench's effectiveness.
We conduct thorough analyses to identify bottlenecks in the Cipher task using Stepwise Prompting, discovering that two rounds of Self-Correction yield optimal results. Complex Task Processing evaluates model performance across three integrated tasks, while we also explore the impact of Tricks on the Puzzle task and visualize rule-focused attention to enhance our understanding of model behavior.
\our{} aims to enhance reasoning evaluation and support further research in this field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents KOR-Bench, a new benchmark that tests LLMs' reasoning abilities across five categories: Operation, Logic, Cipher, Puzzle, and Counterfactual. The key innovation in the design of the benchmark is the concept "knowledge orthogonality", which refers to the property of problems requiring minimal dependence on the domain-specific knowledge the model is exposed to during training. The authors maintain that their knowledge orthogonal tasks can examine how LLMs reason about new rules, concepts, and situations, thus constituting a good testbed for the out-of-distribution reasoning abilities of LLMs. A large number of LLMs, including both chat and base models are evaluated on this benchmark. While SoTA models such as Claude 3.5 and GPT-4o perform the best, all models have large room for improvement. In particular, the cipher and puzzle categories are especially challenging for LLMs based on the evaluation results. The authors also carried out fine-grained and targeted analysis to better understand model behaviors and error patterns. Overall, the experimental results contribute to diagnosing current model limitations, and the benchmark may help assess reasoning capabilities of future models.

### Strengths
- The presentation of the paper is generally clear and thorough. It provides good examples of the categories and problems, reasonable details of the benchmark statistics and creation process, and informative tables and figures.

- Benchmarking reasoning in reliable ways is an important topic and is timely, which this work targets.

- The proposed benchmark is fairly diverse with respect to reasoning. Some of the five categories are related, but they together cover a wide range of reasoning tasks.

- The authors conducted comprehensive evaluations across many models. I appreciate the effort of running models of different sizes and different kinds (open vs closed, chat vs base). The results suggest that most of the benchmark is challenging for most of the models.

### Weaknesses
 - The biggest weakness of the current version of the paper is that the notion of "knowledge orthogonality" is not well articulated enough. There are two aspects. One is about what the notion means. The authors write it "means that the rules within the
benchmark are independent of the domain-specific knowledge the model is exposed to during pre-training" (Lines 76-77). What do you mean by "independent" here? Does it just mean "likely absent"? Could you clarify this central notion more in-depth? The other aspect is whether the five categories satisfy knowledge orthogonality. For example, one could argue that the Puzzle example in Figure 2 is basically the minesweeper game, which is a famous and popular game LLMs know a lot about. I am wondering how you would argue that is "knowledge orthogonal". Moreover, in the Counterfactual category, most of the cover stories are culturally well-known (e.g., Pokemon and Avengers). In what sense are they "independent" of pre-training data?

- Relatedly, in Section 3.2 the authors mention that the raw rules/problems taken from other sources are "adjusted/refined/modified/etc." for this benchmark. How was that process done? What did the authors do to ensure that the end results "meet the specific challenges of KOR-Bench"? It would be good to see more explanations, since this is important given the nature of the proposed benchmark.

- For the evaluation, in terms of prompting strategies this work only studies zero-shot and few-shot settings. We know that prompting matters for LLM reasoning, and there are many methods that can improve reasoning performance (e.g., most notably chain-of-thought/CoT). It would have been a stronger paper if the authors had evaluated the problems with at least one more sophisticated method. Or, if CoT sometimes/often happens automatically and the authors intend that to the case, it should be discussed explicitly in the paper.

- The size of the benchmark is not particularly large, as the authors note. It is still good, and the authors indicate the plan to expand it.

- I think the writing of Section 6 can be improved, especially 6.2 and 6.3. "Self-correction" is introduced rather abruptly with minimal setup/context, and I am not sure that I fully understand what "complex task processing" is about. I recommend that the authors elaborate on those analyses.

### Questions
See the "Weaknesses" section.

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
3

### Summary
This paper introduces the concept of Knowledge-Orthogonal Reasoning (KOR), aiming to reduce the interference of existing pre-trained knowledge by introducing new rules that are orthogonal to it, thus allowing for a more precise assessment of a model's intrinsic reasoning capabilities. Based on this concept, the paper proposes the Knowledge-Orthogonal Reasoning Benchmark (KOR-Bench), which covers five task categories: Operation, Logic, Cipher, Puzzle, and Counterfactual. The benchmark is designed to evaluate how well models can apply new rule descriptions to solve novel, rule-driven problems. The study reveals that even state-of-the-art models, such as Claude-3.5-Sonnet and GPT-4o, perform far from optimally on KOR-Bench, achieving accuracies of 58.96% and 58.00%, respectively. The paper also conducts in-depth analyses using methods like Stepwise Prompting to identify performance bottlenecks in specific tasks, such as the Cipher task, and explores the impact of self-correction techniques and tricks on puzzle-solving, along with visualizing rule-focused attention. These contributions provide new perspectives and tools for assessing and enhancing models' reasoning abilities, fostering further research in the field.

### Strengths
1. This paper proposes a new method for testing the reasoning capabilities of large models and conducts extensive experiments and tests using both open-source and proprietary large models across multiple aspects. During the assessment, this work reduces the impact of pre-training knowledge. Most existing benchmarks, such as MMLU, GPQA, and CommonsenseQA, primarily evaluate a model's ability to accumulate and recall data, often making it difficult to distinguish whether the model is performing genuine reasoning or simply recalling learned patterns. KOR-Bench reduces this dependency by introducing new rules independent of existing pre-trained knowledge, thereby more accurately assessing the model's intrinsic reasoning and planning capabilities.
2. This assessment is more comprehensive and challenging. KOR-Bench covers a variety of reasoning scenarios and task types, including operations, logic, cryptography, puzzles, and counterfactual reasoning across five categories. These tasks are designed to be novel and challenging for models, testing their ability to handle unseen rules and frameworks. Even the most advanced models achieve relatively low accuracy rates (e.g., Claude-3.5-Sonnet scores 58.96%, and GPT-4o scores 58.00%), demonstrating its significant challenge and discriminative power.
3. The authors provide a comprehensive and detailed introduction to the code and data through appendices and open-source releases.
4. The tables and graphs in this article are clear and beautiful.

### Weaknesses
1. There are clerical errors in some parts of the article, such as the model name "Clause-3.5-Sonnet" on lines 308 and 309, and it is critical to be rigorous when doing scientific research.
2. This paper lacks theoretical and experimental evidence on how to ensure the objectivity and impartiality of the assessment.

### Questions
1. Can the authors provide more experimental evidence or theoretical proof to ensure the fairness and objectivity of the model evaluation?
2. How does the author intend to implement the plan proposed in line 539, and briefly explain how the results of this paper can be extended to multimodality?

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
4

### Summary
The paper introduces KOR-Bench, a benchmark specifically designed to evaluate the reasoning and problem-solving abilities of LLMs independent of their pre-existing, pretrained knowledge. This benchmark employs a “Knowledge-Orthogonal Reasoning” approach to assess LLMs across five challenging task categories: Operation, Logic, Cipher, Puzzle, and Counterfactual Reasoning. Each task type introduces new rules and problem-solving frameworks that are orthogonal to domain-specific knowledge, focusing on the model’s ability to reason based on novel rules rather than relying on memorized patterns.

### Strengths
1. The introduction of knowledge orthogonality is an innovative approach to eliminate biases from pre-existing knowledge, offering a fresh perspective on evaluating true reasoning capabilities in LLMs.
2. By incorporating diverse tasks such as logical puzzles, cryptographic challenges, and hypothetical scenarios, KOR-Bench provides a robust testbed for examining LLMs’ adaptability to unfamiliar rules.
3. This paper conducts comprehensive experiments and provides a thorough analysis of model errors, identifying specific challenges within task sub-steps. This analysis offers valuable insights into model limitations and potential areas for improvement.

### Weaknesses
1.	There are already existing benchmarks for evaluating the similar capabilities of current LLMs. For example, as mentioned in the related work, we have logic games [1] for logical reasoning and datasets like [2] for counterfactual reasoning. If the authors argue that these datasets might have been included in current model training data, it would be helpful to explain how KOR-Bench avoids this, such as by concealing the test set or employing other safeguards.
2.	The data scale of KOR-Bench may be a concern, as the current version includes only a small dataset for each task category, potentially limiting the robustness and generalizability of the benchmark findings.

### Questions
I have no further questions; the analysis in the main body and appendix is highly comprehensive.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces the concept of Knowledge-Orthogonal Reasoning (KOR), which focuses on evaluating a model's intrinsic reasoning and planning abilities by minimizing reliance on pre-existing knowledge. This is achieved by introducing new rules that are independent of the knowledge the model was exposed to during pretraining. The authors propose the Knowledge-Orthogonal Reasoning Benchmark (KOR-Bench), which includes five task categories: Operation, Logic, Cipher, Puzzle, and Counterfactual. KOR-Bench challenges models by introducing new elements and rules, pushing them beyond traditional reasoning frameworks.

### Strengths
1. **Important Direction**: The paper addresses a crucial aspect of evaluation by focusing on how to avoid shortcuts when constructing reasoning benchmarks, which is vital for accurately assessing model capabilities.

2. **Comprehensive Scope**: It involves a substantial workload, providing a thorough examination across various dimensions, ensuring a well-rounded evaluation of model reasoning abilities.

3. **Detailed Presentation**: The benchmark is presented with detailed statistics and information, offering clear insights into its structure and the performance of different models.

### Weaknesses
1. **Ensuring Orthogonality**: There is a lack of clarity on how the constructed problems are guaranteed to be orthogonal to the knowledge in LLMs. The paper does not provide evaluation results to support this claim. Specifically, the paper does not define a metric to quantify the degree of orthogonality, making it difficult to assess how well the benchmark achieves its goal of minimizing reliance on pre-existing knowledge. The authors should provide a more rigorous explanation of how they ensure that the constructed problems are not solvable using only pre-trained knowledge.

2. **Evaluation of Base Models**: The purpose of evaluating base models alongside chat models is unclear. The distinct advantages of base models over chat models are not well articulated. It is not clear why the authors chose to evaluate base models, especially given that the primary focus of the paper is on evaluating reasoning abilities, which are often considered to be enhanced in chat models through alignment. The paper should provide a clear rationale for including base models in the evaluation.

3. **Lack of Benchmark Comparison**: The study does not compare results with other benchmarks, which makes it difficult to highlight the unique contributions of KOR-Bench. Without a comparison to existing benchmarks, it is hard to determine whether KOR-Bench provides a unique challenge or if it overlaps with existing evaluations. The authors should include a comparison with other relevant benchmarks to demonstrate the novelty and significance of their work.

4. **Benchmark Construction Process**: The process of constructing the benchmark is unclear, particularly whether it was done manually or with LLM assistance. The paper should provide more details on the data construction process, including the number of annotators, the guidelines used, and the quality control measures taken. It is important to know if the benchmark was created manually or with the help of LLMs, as this can affect the overall quality and reliability of the benchmark.

5. **Missing Related Work**: The paper does not reference a relevant study https://arxiv.org/abs/2306.09479# that proposes a similar concept, which could help in emphasizing the novelty of this work.

Minor comments:
1. **Section 5 Clarity**: The section is somewhat disorganized. The "Reasoning Process Performance" paragraph lacks insights and supportive data, while "Single Task Analysis" is presented without deeper discussion.

2. **Conclusion Content**: The conclusion includes too much focus on future plans, which might be better placed elsewhere in the paper.

3. **Appendix Content**: The appendix contains irrelevant materials, which should be organized more effectively.

5. **Few-Shot Testing**: It would be interesting to test if LLMs can solve problems based on few-shot examples without explicit rules, to assess their ability to derive abstract rules.

6. **Knowledge Orthogonality vs. Contradiction**: The concept of knowledge orthogonality is confused with knowledge contradiction, especially in counterfactual questions.

### Questions
See questions in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
