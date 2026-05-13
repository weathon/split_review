# PiCO: Peer Review in LLMs based on Consistency Optimization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Existing large language models (LLMs) evaluation methods typically focus on testing the performance on some closed-environment and domain-specific benchmarks with human annotations. In this paper, we explore a novel \textbf{unsupervised evaluation direction}, utilizing \textit{peer-review} mechanisms to measure LLMs automatically without any human feedback. 
In this setting, both open-source and closed-source LLMs lie in the same environment, capable of answering unlabeled questions and evaluating each other, where each LLM's response score is jointly determined by other anonymous ones. To obtain the ability hierarchy among these models, we assign each LLM a learnable capability parameter to adjust the final ranking.
We formalize it as a constrained optimization problem, intending to maximize the consistency of each LLM's capabilities and scores. 
The key assumption behind is that high-level LLM can evaluate others' answers more accurately than low-level ones, while higher-level LLM can also achieve higher response scores. 
Moreover, we propose three metrics called PEN, CIN, and LIS to evaluate the gap in aligning human rankings. 
We perform experiments on multiple datasets with these metrics, validating the effectiveness of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an unsupervised evaluation method for large language models (LLMs) using a peer-review mechanism that operates without human feedback. This method, PiCO, allows LLMs to evaluate each other’s answers to unlabeled questions within a shared environment. The core idea is the consistency assumption, where a model’s evaluation ability correlates with its performance, leading to an optimization of model confidence weights to align LLM rankings more closely with human judgments. The effectiveness of PiCO is validated through extensive experiments.

### Strengths
1. The paper introduces a novel peer review mechanism for autonomously evaluating large language models (LLMs), which represents a significant advancement over traditional human-centric review processes. This framework leverages the models themselves as evaluators to assess each other’s answers, potentially increasing the scalability and efficiency of LLM evaluations.

2. The paper is well-written with clear and concise explanations, accompanied by informative figures and tables. These visual aids and structured content greatly enhance the readability and accessibility of the complex concepts discussed, making the methodology and results understandable to a broader audience.

3. The use of multiple well-known datasets like Chatbot Arena, MT-Bench, and AlpacaEval for testing not only demonstrates the practical applicability of the PiCO method but also underscores its effectiveness in aligning model evaluations with human judgment, thus validating the proposed approach through rigorous empirical evidence.

### Weaknesses
1. The paper does not provide detailed information on how the ground truth rankings in the experiments are established, which could impact the transparency and reproducibility of the research. This lack of detail may hinder other researchers' ability to fully replicate or build upon the work.

2. The effectiveness of the peer review process heavily relies on the design of the questions and prompts, which can significantly affect the consistency and scalability of the evaluations. Variability in the outcomes may arise as different prompts may not equally elicit discriminative responses across models. This reliance on prompt design poses a challenge to the general applicability and scalability of using a large number of LLMs for peer review, as consistency in evaluation may not be universally achievable across diverse question sets.

3.Although the paper presents a novel method for evaluating LLMs, it does not discuss specific application scenarios or domains where this method could be particularly beneficial. This omission limits understanding of the potential real-world impact and practical utility of the PiCO method.

### Questions
1. How is the ground truth ranking precisely defined and established for each dataset?
2. How can we mitigate uncertainty and bias in the evaluations conducted by models?
3. What is the application scenario of PICO?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an approach to evaluating Large Language Models (LLMs) through a peer-review mechanism without relying on human annotations. The basic idea is to create weights for each model based on the consistency between the weights and the final evaluation results. The proposed PiCO framework shows promising results in aligning LLM rankings with human preferences across various datasets and metrics.

### Strengths
- The paper is mostly well-written and easy-to-understand, except for some specific details (discussed below).
- The topic of this paper is important, and the proposed method is well described. The idea of using consistency to learn reviewer weights is interesting and well motivated.
- The authors have conducted extensive experiments to compare their method with SOTA baselines.

### Weaknesses
- The assumption that “high-level LLM can evaluate others” answers more accurately” may not be true in all cases, but this is not a big problem. The problem is that, once we assume that  “high-level LLM can evaluate others” and only use high-level LLM as reviewers, it may automatically create new types of biases that cause the cold-start problem: if a model’s response is not preferred by current reviewers, then it won’t get high scores, then it won’t get high reviewer weights, no matter whether it’s a good model or not.
- The analysis of bias with PG_hat in Section 3.2 is problematic. Because the confidence weights are all smaller than 1.0, it’s not surprising to see that PG_hat is all smaller than PG, so this cannot prove that the bias of the evaluator is reduced.

### Questions
- What’s the meaning of “average loss” in the caption of Figure 5?
- What’s the meaning of Precision@K and RBP@K in Section 3.4?
- There are other methods that select reviewers unsuperwisely, such PRE with auto exam in the original PRE paper. It would be good to compare the method in this paper with it as well.
- In Table 2, the variance of multiple baselines are 0, which seems a bit weird. Might be better to explain a bit.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes PiCO, a model that evaluates LLMs by learning the weights of reviewer LLMs through a peer-review mechanism.
The contributions are as follows:
1. It enhances the peer-review mechanism used in PRD and PRE.
2. It enables evaluation at a lower cost, as no human annotations are required, unlike in PRE.
3. The proposed Reviewer Elimination Mechanism is an improvement that can be applied not only to the PiCO model but also to other peer-review methods.

### Strengths
1. By combining learnable weights with existing peer review methods, the evaluation process has become more refined and accurate.
2. The absence of human annotation makes it more practical for real-world applications.
3. The Reviewer Elimination Mechanism, though simple, is a powerful idea that can be applied not only to the proposed method in the paper but also to other peer review approaches.

### Weaknesses
1. Baselines.
The proposed method does not experimentally demonstrate whether it can serve as a replacement for existing benchmarks. While the paper argues that benchmarks fail to adequately capture human preferences and suffer from benchmark leakage issues, it does not compare the rank similarity of the proposed method with that of existing benchmarks in the experiments.

2. Evaluations.
The proposed method uses the same models as both reviewers and those used for training and evaluation. This is akin to comparing performance using the training loss, and the experimental results do not reflect the performance on unseen models. However, if the training and evaluation were conducted using different models, then the issue lies in the paper's writing, as it fails to include this crucial information.

3. Writing.
The writing lacks academic rigor and professionalism. The notations in Equations (2) and (7) could have been expressed in a more general manner rather than illustrating a specific case. The use of > to denote the set {>,<,=} causes confusion as the set name overlaps with its elements. It is recommended to avoid such overlap for clarity. In Figure 3, while the intended message is conveyed, the exact meaning of the x-axis and y-axis is missing. It is advised to specify these axes more clearly for better precision.

### Questions
I suggest that the authors demonstrate whether the trained PiCO assigns higher ranks to models that are superior to the reviewer models used in its training. Also, it would be more realistic if the authors first separate the LLM models used for training and those used for evaluation, and present the results accordingly. Furthermore, while the paper cites Goodhart’s Law in the introduction, it appears that the current experimental setup may be susceptible to the very concerns highlighted by Goodhart’s Law.

### Soundness
2

### Presentation
2

### Contribution
2
