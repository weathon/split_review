# UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization

- Decision: Accept
- Avg Score: 7.20
- Scores: 6, 8, 6, 8, 8

## Abstract
Human preference plays a significant role in measuring large language models and guiding them to align with human values. Unfortunately, current comparing-based evaluation (CBE) methods typically focus on a single optimization objective, failing to effectively utilize scarce yet valuable preference signals. To address this, we delve into key factors that can enhance the accuracy, convergence, and scalability of CBE: suppressing sampling bias, balancing descending process of uncertainty, and mitigating updating uncertainty.
Following the derived guidelines, we propose UniCBE, a unified uniformity-driven CBE framework which simultaneously optimize these core objectives by constructing and integrating three decoupled sampling probability matrices, each designed to ensure uniformity in specific aspects. We further ablate the optimal tuple sampling and preference aggregation strategies to achieve efficient CBE.
On the AlpacaEval benchmark, UniCBE saves over 17% of evaluation budgets while achieving a Pearson correlation with ground truth exceeding 0.995, demonstrating excellent accuracy and convergence. In scenarios where new models are continuously introduced, UniCBE can even save over 50% of evaluation costs, highlighting its improved scalability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces UNICBE, a uniformity-driven framework for comparing-based evaluation (CBE) that simultaneously optimizes multiple objectives in language model assessment. Current CBE methods suffer from limitations related to bias, slow convergence, and lack of scalability.

### Strengths
Efficient evaluation methods are essential for increasingly large-scale LLMs, and this work addresses relevant limitations in conventional CBE.

The integration of accuracy, convergence, and scalability in a uniformity-driven approach is a valuable contribution, setting UNICBE apart from single-objective methods.

### Weaknesses
The framework assumes preference signals (particularly from automated judges like GPT-4) are consistent with human judgment, a potentially risky simplification given known limitations in automated preference evaluations.

The formulation of multi-dimensional sampling matrices and their interaction in optimizing accuracy, convergence, and scalability may be overly complex for practical implementations and difficult to interpret for further tuning or adjustment. The interaction of these matrices, especially with the proposed weighting scheme, introduces a level of abstraction that could obscure the impact of individual components on the overall performance. It's unclear how one would diagnose issues or adjust parameters when the system behaves unexpectedly, given the multiple layers of interaction.

### Questions
1. How does UNICBE perform when preference signals are less reliable, as is often the case with models lower than GPT-4 or inconsistent human annotations?

2. Could the authors elaborate on how UNICBE would handle scenarios with dynamic preference priorities, where, for example, accuracy is weighted more heavily than convergence?


3. To what extent could the uniformity constraints in the sampling matrices be relaxed while maintaining cost-effectiveness?

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
The paper presents UniCBE, a uniformity-driven comparing-based evaluation (CBE) framework designed to improve the efficiency and accuracy of evaluating large language models (LLMs) based on human preferences. UniCBE optimizes three main objectives simultaneously: reducing sampling bias, enhancing convergence by managing uncertainty, and ensuring scalability when new models are introduced. Compared to baselines like random, Arena, and AlpacaEval, UniCBE demonstrates the lowest error and highest correlation between the ground truth evaluation results.

### Strengths
- Comparing-based evaluation is an important problem in LLM evaluation. The proposed method solved a non-trivial problem.
- This paper improves the comparing-based evaluation from three perspectives (accuracy, convergence, and stability). It provides a solid theory foundation, and the experiment results also demonstrate the efficiency of its proposed method.
- Their experiments cover three dimensions well in their proposed method. They also provide ablation studies on each variant. In general, most of the variants play their roles well.

### Weaknesses
 - The motivation is not enough clear. Why the previous method cannot perform well in both accuracy, convergence, and scalability?
- The runtime of the previous CBE method ($O(NM^2)$) is one of the major limitations, and the author starts from this limitation as one of the motivations for the proposed method. However, they lack the runtime analysis for the UniCBE but only an approximate number for saving time when compared to the previous method.
- While UniCBE shows promising results for scenarios with periodically introduced new models, it may be less efficient in highly dynamic, real-time evaluation settings where new models or samples are constantly introduced at high frequencies.

### Questions
See Weakness.

### Soundness
3

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
3

### Summary
This paper studies to explore the use of preference signals with comparing-based evaluation (CBE). It proposes a unified uniformity-driven framework that can achieve CBE with better accuracy. Experiments show the proposed method saves over 17% of evaluation budgets compared to the random sampling baseline.

### Strengths
1. The study of using preference signals with lower evaluation budgets is important research direction with huge potentials for benefiting future research and development

2. This paper proposes a framework to achieve CBE with better accuracy, convergence and scalability.

### Weaknesses
1. The paper can be improved with more performance comparison with existing work and state-of-the-art performance.

2. Expect more statistical and experimental conclusions with the proposed CBE method for the scenario of large-scale preference learning.

### Questions
None.

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
4

### Summary
The paper presents UNICBE, a uniformity-driven comparing-based evaluation (CBE) framework designed to optimize model evaluation across three primary objectives: accuracy, convergence, and scalability. Existing CBE method such as random allocation, method used in ARENA and ALPACAEVAL fails to maximize these aspects simultaneously. 
UNICBE addresses this by simple yet effective approach to promote uniformity across sample and models. The proposed method incorporates three decoupled sampling probability matrices, each of them derived to ensure uniformity in accuracy, convergence, scalability to newly added models. Comprehensive experiments and ablation studies across multiple datasets highlight UNICBE's cost-efficient performance in model evaluation.

### Strengths
UNICBE introduces a novel approach to CBE by balancing three critical objectives, accuracy, convergence, and scalability, representing a straightforward yet impactful optimization techniques to advance model evaluation.
While the framework’s calculations and derivations to promote uniformity are relatively simple, its contributions are substantial given the current reliance on labor-intensive evaluation processes. 
The quality of the work is supported by extensive empirical analysis across diverse models, benchmarks, and settings, with extensive testing to support the assumptions in Section 3 and performance validation across multiple configurations in Section 5.4. 
Clarity is evident in the structured presentation of key concepts and experimental results, with details in experiment or notations clearly addressed. This paper's significance lies in its contribution to large language model evaluation, providing a scalable and efficient methodology that aligns closely with human preference signals, a crucial advancement for iterative model assessments.

### Weaknesses
The novelty of balancing accuracy, convergence, and scalability needs further justification, as similar uniform sampling strategies have been discussed in prior works that highlight the uniformity, such as Vabalas et al. (2019) for sampling biases, which could diminish its uniqueness.

Although the experiment of MT-Bench is based on human evaluator, larger portion of the evaluation is relied on AlpacaEval, as larger number of models and samples are used for the evaluation with AlpacaEval. The reliance on GPT-4 and GPT-3.5-turbo as evaluators, while useful, could benefit from validation against human judgments or additional LLMs, such as Claude, to establish greater reliability and generalizability across evaluator types.

Minor details, but the readability of all figures could be enhanced by widening the lines in each plot, which would improve clarity and interpretation for readers.

### Questions
As the UniCBE is based on three matrix, $P^{acc-l}, P^{con-l}, P^{sca-l}$, each targeting different goal of accuracy, convergence, scaliability, can user steer between those by adding hyperparameter for each matrix? Would it be also possible to quantify it through experiment?

While scalability is addressed by sequentially adding models, the paper could enhance this section by incorporating real-world scenarios, where models enter and exit dynamically, further proving UNICBE’s robustness in evolving benchmarks.

The given choice of greedy sampling over probabilistic sampling and Bradley-Terry model over Elo rating system appears significant to the framework’s success. Could the authors conduct a small experiment to demonstrate that UniCBE maintains its effectiveness across different sampling and aggregation settings?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents UNICBE, a new framework for comparing-based evaluation (CBE) to better align large language models with human preferences. Unlike traditional CBE methods that focus on single objectives, UNICBE addresses sampling bias, manages uncertainty, and optimizes preference signals through three specialized sampling probability matrices. Tested on the AlpacaEval benchmark, UNICBE achieves high accuracy with a Pearson correlation over 0.995 and reduces evaluation costs by 17%, with savings exceeding 50% when evaluating new models, highlighting its efficiency and scalability.

### Strengths
This paper tackle an important question in LLM evaluation and provide a sound solution to it. The experiments are extensive and convincing with strong results showing the advantage of the proposed methods.

### Weaknesses
I don't see any major weakness of the paper, just the presentation can be improved, especially lack in explaining why the method is better than others in an intuitive and easy to follow way.

The authors argue that to avoid bias, the budget should be allocated uniformly, if so how could this method be more sample efficient than random? I guess the reason is if model A is much better than B and model B is much better than C, then it's not necessary to compare A and C a lot. But if thats the reason why this method is more sample-efficient, it would be contradictory to the uniform assumption. Could the authors provide more insight into this?

### Questions
The authors argue that to avoid bias, the budget should be allocated uniformly, if so how could this method be more sample efficient than random? I guess the reason is if model A is much better than B and model B is much better than C, then it's not necessary to compare A and C a lot. But if thats the reason why this method is more sample-efficient, it would be contradictory to the uniform assumption. Could the authors provide more insight into this?

### Soundness
4

### Presentation
2

### Contribution
3
