## Human Reviewer 1

### Summary
This paper proposes DRE-Bench, a cognitive-level benchmark for abstract reasoning, showing that while reasoning-focused LLMs outperform general ones, all models still fail on higher-level sequential and conceptual tasks, revealing a significant gap from human fluid intelligence.

### Strengths
**Cognitive alignment:** Tasks are designed based on the psychological cognitive hierarchy (attribute, spatial, sequential, and conceptual) to structuredly evaluate the abstract reasoning ability of LLMs. This structured assessment is reasonable and meaningful.

**Dynamic robustness:** Generating diverse tasks by varying parameters to avoid data leakage while revealing the stability and generalization ability of the model under different levels of complexity, which is novel.

### Weaknesses
This paper only uses the all-right/all-wrong grid matching criterion, ignoring cases where some reasoning is correct or intermediate steps are reasonable, limiting the fine-grained analysis of model capabilities.

### Questions
1. see weaknesses

2. In your experiments with supplementary visual information, you found that text-only input outperformed both single-image and multi-image formats. I'm curious: what happens if you combine visual input with Chain of Thought (CoT) cues? Would there be a performance boost?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces DRE-Bench, a dynamic reasoning evaluation benchmark designed to assess the fluid intelligence of LLMs. The benchmark consists of 36 abstract reasoning tasks organized across four cognitive levels, with each task featuring multiple dynamic variants. The authors evaluate a range of LLMs, including general-purpose models and reasoning-specialized models. Experimental results reveal that while most LLMs perform well in low-level cognitive tasks, they struggle with high-level cognitive tasks, exhibiting limited generalization capabilities.

### Strengths
Proposes an abstract reasoning framework based on cognitive levels.
Designs verifiable code generators and solvers to ensure data quality and scalability.

### Weaknesses
Inadequate Human Experiment Design:
Alignment with human cognition is the core advantage of this Benchmark. However, the handling of this critical aspect is very weak in this paper. Although a human comparison experiment is provided, there is a lack of detailed age distribution and significance testing. Additionally, there is no explanation of how participants were motivated to complete the questionnaire seriously or how invalid responses were excluded. For the complex task of designing cognitive test questionnaires, the paper seems to lack rigor; neither the main text nor the supplementary materials provide detailed explanations of how the questionnaire design excludes potential influencing factors. This leads to the conclusion "validates the justification of our 4-level framework" appearing unreliable. This point is particularly important because if the foundation of the human experiment is unreliable, the entire Benchmark's cognitive alignment will be questioned, thereby affecting its validity as a Benchmark.

Lack of Detailed Analysis of Model Failure Modes: Specifically, error types in high-level cognitive tasks are not thoroughly explored, failing to reveal the specific reasons for model failures in complex tasks.

Key Findings Lack Depth: The paper emphasizes five key findings, but these findings do not demonstrate particularly outstanding innovation or in-depth analysis, appearing rather superficial.

Insufficient Analysis of Visual Information Impact: This is one of the key challenges in human and LLM testing. However, the analysis of how visual information affects model performance is overly simplistic, providing results for only two visualization formats and lacking deeper exploration.

### Questions
Why were only 20 annotators selected as the sample for the human comparison experiment? This number appears particularly insufficient given the multitude of potential influencing factors in this experiment. Since this is a questionnaire-based test, recruiting more participants would not have been an expensive or labor-intensive task, yet it could have significantly improved the reliability and statistical robustness of the results.

Is there sufficient statistical significance to support the conclusions?
How was the seriousness of participants and the validity of the questionnaire ensured? Were any incentives or quality control measures implemented?
Were potential cognitive biases or other influencing factors considered during the questionnaire design process? How were these interferences excluded to ensure the reliability of the experimental results?
What are the specific failure modes of the models in high-level cognitive tasks? Are there certain types of errors that repeatedly occur?

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a large-scale abstract reasoning benchmark structured along a four-level cognitive hierarchy (Attribute, Spatial, Sequential, and Conceptual). The framework is designed to evaluate Large Language Models (LLMs) on tasks of increasing cognitive complexity and to assess whether current models exhibit good fluid intelligence. Through systematically generated tasks and extensive experiments, the authors find that model accuracy declines with higher cognitive levels, especially for physics-related conceptual reasoning. Reasoning-optimized models (e.g., OpenAI-o1, DeepSeek-R1) outperform general-purpose LLMs, and the performance gap widens as task complexity increases.

### Strengths
- It is an interesting finding that the models achieve higher and more consistent accuracy in vertical (up/down) directions than in horizontal (left/right) ones in Move. Similarly, in symmetry tasks, performance is better for horizontal symmetry than for vertical symmetry
-  The authors implement a verifiable, scalable data engine capable of generating diverse reasoning tasks with controllable complexity—an important methodological contribution that ensures reproducibility and adaptability.
- The results highlight key cognitive distinctions: (a) model accuracy degrades sharply at higher cognitive levels, (b) inference-time scaling contributes mainly to lower-level reasoning, and (c) visual input may not aid abstract reasoning. These insights deepen our understanding of the limits of current LLM cognition.

### Weaknesses
- Several aspects of the experimental design and presentation require clarification and stronger consistency.
 the selection of models across figures lacks transparency and methodological coherence. For example, Figure 5 does not specify why those particular four models were chosen, Figure 6 focuses solely on DeepSeek-R1 without justification, and Figure 7 switches to yet another subset of models while testing only two tasks. 

Such inconsistent model selection makes it difficult to assess whether observed relationships are generalizable. A more systematic comparison across models, task types, and difficulty levels would provide stronger evidence for the claimed trends. Table 2 also introduces new models without explanation

- question design and ground-truth validity raise concerns. In Figure 8, certain problems might have multiple correct solutions (e.g., the Level-3 task where the path could start from one red square to the upper blue square not only the bottom one), yet only one is labeled as correct. Additionally, the prompt mislabels the target as a “red dot” instead of a “red square.”

 In the Level-4 example, two obstacle types exist, but the prompt fails to specify that only the blue obstacle is reflective, potentially confusing both human and model respondents. These ambiguities undermine the reliability of the evaluation.

- discrepancies between text and data should be addressed. 
- Line 340 claims that human accuracy decreases with task level, but Table 1 shows relatively stable human performance across Levels 1–3, except for a few specific tasks (e.g., sorting). Interestingly, these same tasks are also where models perform poorly. This suggests that further validation is needed to ensure the generated items reflect increasing cognitive difficulty rather than artifacts of task design.

### Questions
- What criteria guided the selection of models in Figures 5–7 and Table 2? Were these choices based on availability, performance tiers, or specific architectural features?
- Why was DeepSeek-R1 uniquely highlighted in Figure 6?
- How many tasks and difficulty levels were used to derive the inference-time–accuracy relationship, and do these results hold across other models or scales?
- In Figure 8, how were ground truths defined for multi-path problems, and were alternative valid solutions considered during evaluation?
- How were ambiguous or mislabeled prompts (e.g., “red dot” vs. “red square,” unspecified reflective obstacles) handled in scoring and analysis?
- Given that human performance appears stable across the first three levels, how to justify the statement that accuracy “generally decreases” with increasing cognitive level?

Suggestions:

- Unify model selection and reporting. clearly specify which models are used in each experiment and maintain consistency across figures. If subsets differ, explain the rationale.

- Broaden the inference-time analysis. test multiple models across several tasks and difficulty levels to confirm that observed correlations are not model-specific.

- Validate and disambiguate tasks. review prompts and ground truths to ensure each question has a unique, well-defined solution and that instructions are precise.

- Re-evaluate human baselines. conduct additional validation to verify that increasing task complexity indeed reflects higher cognitive difficulty, rather than inconsistencies in dataset generation.

- Clarify inconsistencies between text and data.

### Soundness
1

### Presentation
2

### Contribution
3

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
This work introduces DRE-Bench, a benchmark designed to evaluate dynamic reasoning through a hierarchical cognitive framework including 36 reasoning tasks. It frames fluid intelligence as the ability to generalize beyond memorized knowledge and reason, and designs rule-based code generators and solvers for each task. Empirical evaluations across different LLMs show that while models perform well on lower-level reasoning, they struggle with higher cognitive levels, indicating a gap from true fluid intelligence.

### Strengths
1. The task design is well aligned with cognitive psychology, clearly reflecting different types of reasoning and the varying levels of intelligence required for each task.

2. The proposed benchmark is a valuable contribution to the evaluation community, offering diverse and controllable challenging tasks.

3. The paper provides a thorough evaluation and analysis across multiple LLMs, shwoing how accuracy and stability vary with task complexity and cognitive level.

### Weaknesses
While the paper proposes a cognitively inspired hierarchy of reasoning tasks, it does not measure the time humans take to solve them. Given the small-scale human evaluation and potential variance, reporting the average solving time per task would better substantiate the claimed cognitive alignment and reveal the true difficulty gradient.

### Questions
In Table 1, why does o3-mini perform significantly better than other models on the Level-4-Mechanics tasks, achieving 31.75% accuracy while most other models show near-zero performance?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3