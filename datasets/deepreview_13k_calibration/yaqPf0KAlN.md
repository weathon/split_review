# Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Recent advancements in large language models (LLMs) have led to significant breakthroughs in mathematical reasoning capabilities. 
However, existing benchmarks like GSM8K or MATH are now being solved with high accuracy (e.g., OpenAI o1 achieves 94.8\% on MATH dataset), indicating their inadequacy for truly challenging these models. 
To bridge this gap, we propose a comprehensive and challenging benchmark specifically designed to assess LLMs' mathematical reasoning at the Olympiad level. 
Unlike existing Olympiad-related benchmarks, our dataset focuses exclusively on mathematics and comprises a vast collection of 4428 competition-level problems with rigorous human annotation. 
These problems are meticulously categorized into over 33 sub-domains and span more than 10 distinct difficulty levels, enabling a holistic assessment of model performance in Olympiad-mathematical reasoning. Furthermore, we conducted an in-depth analysis based on this benchmark. Our experimental results show that even the most advanced models, OpenAI o1-mini and OpenAI o1-preview, struggle with highly challenging Olympiad-level problems, with 60.54\% and 52.55\% accuracy, highlighting significant challenges in Olympiad-level mathematical reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work constructs Omni-MATH, a challenging math problem set of 4k over more than 33 domains and with more than 10 difficulty levels with difficulty information comes from either the AoPS website or GPT-4o few-shot result. 15 large language models are evaluated on Omni-MATH and it turns out be challenging even for the strongest OpenAI-o1-preview model. Further analysis shows that all models receives certain data leakage and GPT-4o is a reliable judgement model for determine whether the model-generated solution is consistent with the reference answer.

### Strengths
- A new benchmark contribution that demonstrate the limitation of current progress of math reasoning in large language models, the detailed difficulty information would benefit the further categorization of this benchmark.
- Careful study over the reliability of the metrics including data leakage and LLM-based judgement results.

### Weaknesses
 - The explanation of the RM-version of Qwen2.5-MATH do not outperform the vanilla version and Qwen2.5-MATH RM@256 does not out perform Qwen2.5-MATH RM@8 needs further elaboration and investigation to unveil the phenomenon.

### Questions
- What are the education background of the graduate and doctoral students getting involved?
- In Section 4.2, what the sampling strategy of the 100 subset, are all the difficulty levels covered in this subset?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces OmniMath, a new Olympiad-level mathematical reasoning benchmark. It comprises 4,428 math problems, each with an instance-level difficulty classification. The authors utilize GPT-4o as a judge to evaluate the performance of LLMs. Additionally, they have developed Omni-Judge, an open-source answer evaluation LLM designed to serve as a substitute for GPT-4o. The paper conducts some analysis of experiments involving 15 different LLMs.

### Strengths
The dataset's large size and focus on Olympiad-level problems make it a potential resource for evaluating LLMs' mathematical reasoning abilities.

The investigation into best-of-N scaling and difficulty consistency represent current areas of interest, and the analysis of these part is interesting.

The paper is well-organized and in good shape.

The experiments are comprehensive, and the analysis is thorough.

### Weaknesses
 The major concern is about the evaluation. While the authors assert that GPT-4o aligns with human annotations in 98% of cases (L398-399), crucial details are omitted (e.g., whether the 100 samples originated from the same LLM? What are the inter-agreement scores among the human annotators? What is the number of student judges involved? Are there specific examples where GPT-4o fails as a judge and why?) undermining the reliability of this claim.

Moreover, there is a notable contradiction with the results attributed to OmniJudge. According to L74-76, "Our Omni-Judge achieves over 91% consistency with GPT-4o and 86% consistency with human judgments, providing reliable feedback." Let us consider this carefully: suppose we have 100 test examples, and GPT-4o achieves alignment with human judges on 98 of them. With OmniJudge, 91 examples align with GPT-4o, implying that at most only 2 of the 91 might be judged incorrectly by OmniJudge, which would result in at least 89 out of 100 examples aligning with human judges. This seems contradictory with the reported 86% consistency with human judgments. If the results reported for OmniJudge are indeed reliable (as they seem to be, given the detailed information provided in the appendix), then GPT-4o aligns with human judgments at most 95%. This discrepancy calls into question the reliability of the results presented in Table 2.

In addition, using GPT-4o or OmniJudge as evaluators can be time-consuming and computationally (or monetarily) expensive. A more feasible approach might involve standardizing answer formats, as seen in datasets like MATH, and designing detailed, rule-based answer-cleaning and matching protocols. Model-based judging should primarily serve as a supplementary tool (like Olympic Arena) rather than a primary evaluation method.

There is also the potential for data leakage, as some models, such as NuminaMath and Qwen2Math, use examples from AoPS as part of their supervised fine-tuning datasets.

### Questions
- Regarding data annotation: Could you clarify what is meant by cross-validation in line 203? Moreover, in L831-834, it states, "Subsequently, we hired 2 annotators to inspect the entire dataset, following a set of principles." What are these principles?

- In Table 3, what do the notations "Prop." and "Avg.D." stand for? It seems these are not explained in the caption or main text. Additionally, how should we interpret the results for Qwen-2.5-MATH-instruct? Is the data leakage problem particularly severe here? Since some training sets for NuminaMath and the Qwen-MATH series are derived from AoPS, is there any overlap between this subset and OmniMath?

- Lines 398-400 omit crucial details. For instance, did the 100 samples originate from the same LLM? What are the inter-agreement scores among the human annotators? How many student judges were involved? Are there specific examples where GPT-4o fails as a judge, and what are the reasons for these failures?

- In Section 4.3, you mention investigating few-shot evaluation. Are you evaluating LLMs on OmniMath in a few-shot manner? If so, where are the prompts used for this evaluation?


Others 

- L79: should be "shown in Table 2". 

- L241-L242: we previously surveyed in Figure (where is Figure 4?)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Omni-MATH, a challenging benchmark designed to assess large language models (LLMs) in mathematical reasoning at the Olympiad level. Omni-MATH contains 4,428 competition-level problems, rigorously annotated across 33 sub-domains and ten difficulty levels. This comprehensive categorization enables a nuanced evaluation of LLM capabilities in complex mathematics.

The study reveals that existing models, including advanced ones like OpenAI o1-mini, achieve only moderate success on this benchmark, with a maximum accuracy of 60.54%. The findings highlight persistent challenges in areas like discrete mathematics, while models perform relatively better in algebra and calculus. To support this benchmark, the authors introduce Omni-Judge, an open-source evaluator achieving high consistency with human judgment (86%) and GPT-4o (91%).

### Strengths
Omni-MATH targets Olympiad-level mathematics, pushing beyond traditional datasets like GSM8K and MATH, which have reached saturation. This focus on advanced problems adds a valuable, high-difficulty benchmark for assessing and improving LLMs' reasoning abilities.

Problems are categorized into sub-domains and assigned difficulty ratings, allowing for fine-grained performance and error analysis. This detailed structure aids in identifying domain-specific strengths and challenges in model reasoning.

The study reveals limitations in test-time scaling methods (e.g., Best-of-N) and the impact of domain interactions on model performance. Such findings guide future research on improving LLMs’ mathematical reasoning and scaling capabilities.

### Weaknesses
More examples of the dataset should be presented in either main paper or appendix.

### Questions
Omni-judge is trained with GPT-40 evaluation results, but how to verify if the GPT-4o evaluations are reliable? 
Can the solutions for discrete math problems be written in code and executed to achieve accuracy?
What are the best-of-1 results? 
What is the exact number used for  "N" in Best-of-N?

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
This paper introduces *Omni-MATH*, a new Olympiad-level mathematical benchmark designed to evaluate the performance of advanced models on competition-level problems. The authors assess various strong models on this benchmark and share insightful findings from their analysis. Additionally, they propose an Olympiad-level verifier to assist in confirming the accuracy of predicted and ground truth answers. Unlike simpler datasets like gsm8k or MATH, Olympiad-level problems require more sophisticated verification techniques beyond rule-based methods due to their complexity.

### Strengths
Overall, I find this to be a strong paper.

- **Clarity**: The writing is clear and easy to follow.
- **Comprehensive Benchmark**: This paper introduces a comprehensive and in-depth Olympiad-level mathematical benchmark, featuring questions across various domains and difficulty levels.
- **Model Analysis**: It provides a thorough analysis of current advanced models on this benchmark, offering valuable insights into aspects such as Best-of-N and consistency.
- **Effective Verifier**: A notable contribution of this paper is the development of an effective verifier, which improves the accuracy of validating predicted answers, addressing the unique challenges of Olympiad-level problems.

### Weaknesses
Here are some concerns about this paper:

- **Verifier Training Details**: The details regarding the training of the verifier should be further clarified.

- **Scaling Test-Time Inference**: In the test-time inference analysis, this paper primarily relies on the best-of-N strategy. While this is generally fine, for more challenging competition-level questions, advanced search algorithms—such as tree search or Monte Carlo Tree Search (MCTS)—may be required. A discussion on these more sophisticated techniques for tackling harder questions would enhance the paper's impact.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3
