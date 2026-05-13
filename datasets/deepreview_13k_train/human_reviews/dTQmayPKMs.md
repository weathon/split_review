# Understanding Impact of Human Feedback via Influence Functions

- Decision: Reject
- Scores: 6, 8, 5, 6, 8, 5

## Abstract
In Reinforcement Learning from Human Feedback (RLHF), it is crucial to learn suitable reward models from human feedback to align large language models (LLMs) with human intentions. However, human feedback can often be noisy, inconsistent, or biased, especially when evaluating complex responses. Such feedback can lead to misaligned reward signals, potentially causing unintended side effects during the RLHF process. To address these challenges, we explore the use of influence functions to measure the impact of human feedback on the performance of reward models. We propose a compute-efficient approximation method that enables the application of influence functions to LLM-based reward models and large-scale preference datasets. In our experiments, we demonstrate two key applications of influence functions: (1) detecting common forms of labeler bias in human feedback datasets and (2) guiding labelers to refine their strategies to align more closely with expert feedback. By quantifying the impact of human feedback on reward models, we believe that influence functions can enhance feedback interpretability and contribute to scalable oversight in RLHF, helping labelers provide more accurate and consistent feedback.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to analyzing the effects of human feedback in RLHF. It introduces influence functions to quantify the impact of individual feedback on the performance of reward models, which can help detect biases and improve labeling strategies in RLHF systems. Two primary applications of influence functions are highlighted: detecting biases like length and sycophancy in human feedback and guiding labelers to align their feedback with expert standards.

### Strengths
1. The use of influence functions to analyze the impact of human feedback is a promising direction that adds a layer of interpretability in RLHF, which is essential for aligning LLMs with human values.
2. The paper introduces a compute-efficient method that enables scalable application of influence functions, potentially reducing computational demands by 2.5 times, a significant improvement over previous methods.
3. The methodology, experimental design, and results are presented clearly, with well-structured figures and examples to support the claims.

### Weaknesses
 1. The study’s limitations in real-world scenarios, where expert and non-expert labelers may not share sub-objective scores, could reduce the generalizability of the approach. This is particularly concerning because the method relies on the assumption that labelers can provide granular feedback aligned with specific sub-objectives, which may not hold true when dealing with diverse labeler backgrounds and varying levels of expertise. The lack of shared understanding of these sub-objectives could lead to inconsistent and unreliable influence function calculations, limiting the practical applicability of the method.
2.  While the paper shows effectiveness in detecting length bias, sycophancy bias remains challenging, as it involves understanding nuanced human agreement tendencies that may vary by context. The difficulty arises from the fact that sycophancy is not a simple, easily quantifiable metric; it is deeply intertwined with the subtleties of human communication and the specific context of the interaction. This makes it hard to create a universal, robust detection mechanism using influence functions, as the interpretation of sycophancy can be highly subjective and context-dependent.

### Questions
1. Could the reliance on targeted validation sets be reduced by adapting influence functions to work with more generalized validation samples?
2. How does the approach scale with increasingly large datasets or models beyond the experiments presented, and would there be additional trade-offs in compute efficiency?

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
5

### Summary
The paper addresses the challenge of noise and misalignment in human feedback within RLHF, which can lead to flawed reward signals. By using influence functions, it quantifies the impact of individual data points on reward model performance. For each data point, the influence function captures how parameter adjustments would occur when the weight of that point changes. The approach assumes a small validation set is available to calculate overall influence and utilizes an approximate inverse Hessian to enable efficient computation. Results indicate improved AUC in addressing length bias and sycophancy bias compared to GPT-4o and Gemini models.

Additionally, the paper explores the potential of guiding non-expert labelers to align more closely with expert labeling. It assumes that labelers use a list of linearly combined, weighted sub-scores in their scoring process. By identifying data points that negatively impact alignment, non-expert labelers can adjust weights and improve their performance. Results suggest that with a few samples, non-expert labelers demonstrate notable improvement.

### Strengths
This paper excels in identifying data points that negatively influence reward models through the application of influence functions. Given the common issue of noise in human-labeled data, particularly in RLHF, this approach enhances transparency and is valuable in managing labels from non-expert labelers. The methodology effectively addresses computational challenges using an approximation function, which is highly practical aiming for reliable AI.

The experiments are well-defined, and the performance results are convincing. The paper is well-articulated regarding both analytical rigor and technical details. Additionally, the authors explore ways to improve labeler performance, which is a good extension of the study.

### Weaknesses
While the application of influence functions to assess the contribution of individual data points is compelling, the methodology relies heavily on manually curated validation sets, as evidenced by the ablation experiments. There are two primary concerns:

1) Dependence on Domain Knowledge: The construction of validation sets requires domain-specific knowledge, which could limit generalizability. Although addressing verbosity and sycophancy is valuable, the methodology appears capable of handling other issues if suitable validation sets are available. However, this adaptability is currently contingent on creating each validation set by hand.

2) Risk of Conflicting Improvements: It is unclear how the approach manages potential conflicts between multiple improvement directions. For instance, in the main results (Figure 2), Influence shows higher TPR than GPT-4o at the same FPR, which is promising. However, it raises the question: Does this improvement come at the expense of other metrics? To fully assess the model’s overall robustness, it would be beneficial to provide additional statistics comparing the base model and the Influence-based approach to ensure that the latter does not merely overfit to specific biases, such as length.

Furthermore, as noted in the limitations, the feasibility of improving labelers’ performance in real-world settings may be limited, especially when human labelers’ judgments involve complex decision-making beyond linear reward models. The authors could strengthen their argument by including results from human subjects whose labeling strategies demonstrably improve with guidance. Alternatively, if the current scope remains focused on bias correction within datasets, it would be beneficial to clarify this in the introduction to avoid misleading interpretations about broader applicability.

### Questions
1) Will focusing on improving a single aspect of bias impact other performance metrics?

2) Beyond runtime speedup, does approximating the inverse Hessian lead to any performance degradation?

3) Could you provide insights on why Entropy underperforms significantly in addressing Sycophancy Bias relative to other baselines?

4) In Appendix B2, five weights are selected for B. Could you elaborate on the rationale for these specific weights? Were they chosen randomly, and are any particularly extreme?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel approach to evaluate and refine the reward models in RLHF by employing influence functions. The authors argue that human feedback, which is integral to training reward models for LLMs, can be noisy and biased, leading to misaligned rewards. To mitigate this, they introduce a compute-efficient method to approximate influence functions, allowing for the measurement of individual data points' impact on reward model performance. The paper claims two main applications: detecting labeler bias in feedback datasets and guiding labelers to align more closely with expert feedback. The authors demonstrate the effectiveness of their approach through experiments and argue that it enhances feedback interpretability and contributes to scalable oversight in RLHF.

### Strengths
The paper introduces a novel approach to enhance the interpretability of reward models. By applying influence functions, the authors provide a method to quantify the impact of individual feedback on the model's performance, offering insights into how human feedback shapes the reward model's outcomes.

The idea of using influence functions to measure the impact of human feedback is innovative and has the potential to contribute to the broader goal of scalable oversight in RLHF. This approach can help in detecting and mitigating labeler bias, which is a common challenge in training robust and aligned AI systems.

### Weaknesses
As far as I am concerned, the authors simpy apply the approach in [1] to the reward modeling scenario, which greatly limits the novelty of the paper. I suggest that the author summarize the main contributions.

While the experiments show promise, establishing reward models with various LLMs and evaluating with more downstream alignment tasks, such as direct alignment algorithms, could further validate the generalizability of the approach.

### Questions
Could you provide further insights into how the method performs when handling intentionally misleading or adversarial feedback? Are there specific patterns or checks in place to identify and mitigate such cases?

Please provide more specifics on how the method scales with increasingly large datasets. What computational trade-offs may arise as the dataset grows?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper discusses using influence funcitons to identify potential bias of human labelers in human feedback data for LLM alignment. To enable effcient estimation of incluence functions under the LLM context, DataInf and OPORP are introduced to ease the burden of computation and storage respectively. Empirical results demonstrate that the proposed method can effectively identify lengthy and sycophancy bias compared to baselines and querying powerful LLMs. Specially, the authors show that influence functions can help align non-expert labelers' strategies to experts' labeling strategy, which I believe is important for preference data annotation in LLM alignment.

### Strengths
1. The discussed topic is practical and important.

2. Through approximation and compression, the proposed method can estimate influence functions efficiently.

3. Empirical results are promising (although no comparison to concurrent works)

### Weaknesses
1. The proposed method mainly integrates existing techniques to the LLM context (although I do not think this is a serious issue as long as they work properly)

2. Mistakes in fig.4 legend (AUC=0.8 for both Concise and Verbose?)

3. Empirical study only show the efficacy in identifying bias, but discussion on data quality improvement with such detechtion is missing.

### Questions
1. "we reduce the size of a single gradient vector from 160MB (42M dimensions) to 256KB (65K dimensions)"

How do you calculate the size of gradient vectors? Why is the gradient vector size 160MB (Llama-3-8B in your experiment has around 15GB model size)

2. Could you provide some performance improvement results on real-world dataset after filtering biased data with incluence functions?

3. I notice you only use four dimensions of Helpsteer2 in section 5.2.1 (the four-dimensional weight vector]). Why do you make such alteration?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper describes the use of influence functions to evaluate the influence of preference samples in reward modeling. The authors apply recent methods for computing influence functions for large neural networks/LLM to reward model training. By using a validation set demonstrating preferences for specific qualities, the influence of examples is highlighted. The authors also propose a compression scheme to enable efficient storage of gradient vectors for dot products. The authors apply the method for the detection of biased data samples, and outline guidance of human labelers.

### Strengths
Positive:
- The paper is well written and polished, I found it easy to follow
- The main presented methods seems to work well, and is evaluated appropriately
- The different use cases (bias detection and user guidance) are presented well and relevant
- Limitations are discussed (such as the dependence on validation set composition), and runs (although limited) ablations on the effects of different compositions
- The quality of experiments seems high, both qualitative and quantitative results are generally convincing
- Description of experiments/data sets is sufficient for reproducibility
- The paper presents a nice application of influence functions

Overall, I enjoyed reading the paper, and am convinced by its research quality. While strict technical novelty or theoretical insights are limited, I think it still provides a meaningful contribution to the field.

### Weaknesses
Negative:
- The methdological novelty is limited, i.e. just the application of existing methods to a new use case
- The dependency of the method on validation set  composition seems like a core limitation, which might make wide application difficult
- The use case of user guidance is just on a proof-of concept level, and it’s unclear how it would transfer to an actual human scenario, however (again) this is appropriately acknowledged by the authors

### Questions
Questions/Needs clarification:
- You mention “L.140 been extended beyond the model parameter to any univariate quantity of interest f(θ), such as validation loss”. Can you make the reference to using a validation dataset more explicit? Instead of the chained references at the section below (Koh&Liang, …)
- How did you decide on the Mahalanobis distance as a baseline measure? Has this been considered before for this kind of task?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the noise, inconsistency, and bias in the reward model of RLHF tasks. The authors introduce a method using influence functions to quantify the impact of human feedback on reward models, enhancing understanding of both feedback and the models themselves.

### Strengths
1.	The authors present a novel perspective on evaluating how human feedback affects the performance of reward models.

2.	They employ vector compression techniques to approximate influence functions, reducing computational costs.

3.	The paper highlights two potential applications of influence functions: detecting bias and assisting labelers.

### Weaknesses
1.  Evaluation Set Requirement: The method requires a high-quality evaluation set for each alignment task, ideally annotated by experts. While this constraint is noted in the "Limitations" section, it presents a significant obstacle for real-world applications.

2.  Computational Complexity: The influence function requires calculating the inverse of the Hessian matrix. Although the authors approximate it using DataInf (Eq. 6) and vector compression technology, it also necessitates summing the data in the training set, which may compromise computational precision.

3.  Bias Detection Methodology: The approach of identifying bias when the influence score exceeds a specified threshold is debatable. This threshold is difficult to determine, and not all samples surpassing it should be considered biased.
4.  Experimentation Concerns (Sec 5.2, Fig 6):

    a.  Finding expert labelers for every aspect is challenging in practical scenarios.

    b.  This method may reduce the diversity of the generated responses, potentially negatively impacting model training.

    c.  The experiment relies on training an SVM, which incurs additional computational costs and may lack accuracy.

    d.  It might be more reasonable for the weight of non-experts to be adjusted based on the attribute and value of different rewards rather than introducing another labeler.

### Questions
1.	Evaluation Set Size: How should the evaluation set size be determined? Is there any analysis on how performance improves with an increased number of samples?

2.	Bias Types: Have you tested your method on biases other than length and sycophancy?

3.	Metric Choice: Why does the paper report ROC curves instead of other metrics?

4.	Dependent Rewards: In real-world applications, rewards are often not independent. How does the proposed method address this in Sec 5.2?

### Soundness
3

### Presentation
3

### Contribution
2
