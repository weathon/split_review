# EnsemW2S: Can an Ensemble of LLMs be Leveraged to Obtain a Stronger LLM?

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
label{sec:abs}
How can we harness the collective capabilities of multiple Large Language Models (LLMs) to create an even more powerful model? This question forms the foundation of our research, where we propose an innovative approach to weak-to-strong (w2s) generalization—a critical problem in AI alignment. Our work introduces an easy-to-hard (e2h) framework for studying the feasibility of w2s generalization, where weak models trained on simpler tasks collaboratively supervise stronger models on more complex tasks. This setup mirrors real-world challenges, where direct human supervision is limited. To achieve this, we develop a novel AdaBoost-inspired ensemble method, demonstrating that an ensemble of weak supervisors can enhance the performance of stronger LLMs across classification and generative tasks on difficult QA datasets. In several cases, our ensemble approach matches the performance of models trained on ground-truth data, establishing a new benchmark for w2s generalization. We observe an improvement of up to 14\% over existing baselines and average improvements of 5\% and 4\% for binary classification and generative tasks, respectively. This research points to a promising direction for enhancing AI through collective supervision, especially in scenarios where labeled data is sparse or insufficient.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
ENSEMW2S explores weak-to-strong (w2s) generalization by combining the capabilities of multiple LLMs to enhance model performance. It presents an easy-to-hard (e2h) approach, inspired by AdaBoost, to use weaker models on simpler tasks to supervise and train stronger models for more complex tasks. This ensemble-based approach is validated through experiments on binary classification and generative tasks.

### Strengths
- The paper addresses a highly relevant and timely topic within the machine learning community. Many efforts are being made to leverage smaller models for most practical applications.
- The authors have conducted extensive experiments, exploring the performance of multiple LLMs.

### Weaknesses
 - The manuscript lacks sufficient clarity, making it challenging for readers to follow the paper
- The novelty of the proposed approach appears limited, as it closely resembles the traditional Adaboost method
- The analysis throughout the paper, such as the statement on line 345 ("we aim to recover the performance gap (PGR) and elicit the full capability of the strong model using an ensemble of weak models"), frequently emphasizes the importance of the Performance Gap Recovery (PGR). However, in Section 5.1, Better Metric, the authors appear to question the adequacy of PGR as a metric.

- typo: choice is written as choise a couple of times in the paper.

### Questions
- Can the authors please clearly state the difference between their approach and the baseline, Burns et al.?
- Can the authors report std for different runs in the experiments sections? 
- Have the authors experimented with additional values for the rounds, beyond the examples of 5 and 10 for binary and multi-choice scenarios?? 
- In Section 5, are the data splitting strategies essentially random vs hard splits?
- Can we please have clear quantitative reports between different models instead of just the bar plots?
- From the bar plots, it appears that the performance gap narrows under the easy-hard settings. Have the authors explored this observation?

### Soundness
3

### Presentation
2

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
This paper explores the problem of weak-to-strong (w2s) generalization in language models, particularly for complex tasks where human-labeled data is limited or unavailable. It introduces an approach using an "easy-to-hard", where weak models trained on simple tasks guide stronger models to tackle more difficult ones. Inspired by AdaBoost, the proposed method integrates multiple weak models to generate robust pseudo-labels for challenging tasks, simulating human supervision.

### Strengths
1.	The authors propose an AdaBoost-inspired ensemble method that combines multiple weak LLMs to provide stronger supervision for training a more powerful model.
2.	The paper introduces a new algorithm that combines multiple weak LLMs by adjusting token probabilities through a voting mechanism. In some cases, a strong model trained with pseudo-labels from weak models outperforms the same model trained with real labels on complex tasks.

### Weaknesses
1.	The concept of weak-to-strong (w2s) was first introduced by Burns et al. (2023), and this paper is seen to be only an improvement of the Burns et al. (2023) approach by extending single weak model supervision to multiple weak model supervision. At the same time, the integration of multiple weak models is seen as a direct use of the AdaBoost algorithm.
2.	Applying the concept of AdaBoost to ensemble learning with large language models (LLMs) could lead to significant computational overhead in practical applications. However, the paper fails to provide a detailed analysis of the computational cost or propose strategies for efficient implementation.
3.	The paper title and abstract emphasize the notion of creating a stronger model through the ensemble of weak models, but this idea is not sufficiently highlighted in the main text. It is only mentioned in Appendix A that the performance improves after AdaBoost training compared to a single weak model. In contrast, the experimental results in the main text primarily show that the ensemble of weak models serves to generate pseudo-labels to address the lack of labeled data. That is, compared to using real labels, weak model supervision enables the strong model to maintain performance on complex tasks without significant degradation.
4.	The ablation study lacks experiments treating each sample, rather than each token, as an independent unit. Although Appendix Figures 12 and 13 show the minimal impact of different window lengths on token processing, the claim that sample-level weight updating performs worse than token-level updating is unsubstantiated.
5.	The results compare only random splits and easy-hard data separation. However, performance gains in weak-to-strong models are not evident in the easy-hard split and are noticeably inferior to the random split. This raises questions about whether weak models also need training on hard tasks. Additionally, random split analysis does not account for potential gains attributed to a progression from easy to hard data.
6.	The method shows favorable performance on models with smaller parameters, as indicated in the scaling analysis. However, it lacks demonstration on larger-scale models, such as 7B, or evidence of broad applicability across different model families, like LLaMA or Qwen.

### Questions
1.	The three parts in Figure 1 lack clear distinction. The placement of the "Test Data" label in red font in the middle is somewhat unclear, and the process for generating pseudo-labels for the hard data is insufficiently detailed. Additional labeling would improve clarity.

### Soundness
2

### Presentation
2

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
The paper proposes a framework that enhances weak models through an iterative AdaBoost-based sampling and reweighting approach, enabling them to generate pseudo-labels for hard data as an improved ensemble. These pseudo-labels are then used to train a transfer model, effectively narrowing the performance gap with a strong model trained on fully labelled hard data. This framework combines established techniques—including AdaBoost, ensembling and pseudo-labeling—to address the trending weak-to-strong (w2s) generalization problem.

### Strengths
1.	The paper is well-motivated by addressing critical challenges in prior work: the Single Weak Supervisor Limitation, Lack of Focus on Weak Model Enhancement, and Overlooking Task Complexity.
2.	It introduces an ensemble-based easy-to-hard (e2h) framework that extends weak-to-strong (w2s) generalization by structuring supervision as a progression from simpler tasks to more complex ones.
3.	The successful adaptation of AdaBoost from traditional machine learning to the w2s setting, particularly in iteratively enhancing weak models, demonstrates improved supervision for strong models tackling complex tasks.

### Weaknesses
My main concern is the method’s generalizability to real-world settings, where weak supervision datasets may not fully cover or have distributional shifts from, challenging test sets.

Specifically, the current evaluation relies on internal correlations, with weak and strong models trained on splits of the same dataset. Cross-dataset performance could provide a more robust test: for example, can weak models trained on easy tasks from Dataset A effectively bridge the gap for hard tasks in Dataset B? Comparing this with setups where both weak and strong models are trained within either Dataset A or Dataset B would further clarify the method’s generalizability.

### Questions
**Questions (to be addressed)**
1. How does this approach compare to a direct ensemble?
2.	How sensitive is the method to the distribution shift cross-dataset?
3.	Could voting from weak models introduce error to the stronger transfer model, for example, if multiple weak models agree on an incorrect answer?
4.	How is the AdaBoost round  T  determined, and how does this choice impact results?
5.	Line 5 in Algorithm 2 is unclear—the parameter update of $\theta$ via the minimization objective needs clarification and is not well-represented in Figure 7.
6.	Would be nice to have some cost analysis provided.

**Additional feedback (minor comments)  to improve the paper and not necessarily part of my decision assessment.**

1.	In Figure 2 (bottom), the colour map and x-axis denote model parameters, which seems redundant.
2.	Figure 7 and Algorithm 2 are essential elements but are placed in the appendix, requiring frequent reference back and forth. Moving them upfront or referring them after Algorithm 1 would be helpful.
3.	In Figure 1 (right), the last arrow in the second line needs correction.
4.	There is a naming inconsistency in Figure 1—while the left plot uses “strong/weak teacher/student,” the caption refers to “strong/weak model.”
5.	On line 174,  T  is introduced in the main text but is not defined.
6.	In Algorithm 2,  m  is not defined.
7.	For line 10 in Algorithm 1, it would be helpful to provide intuition for the weight update, such as assigning higher weight to samples with higher error rates.
8.	Figures 10-13 in the appendix lack a legend.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper contributes to the field of weak-to-strong (w2s) generalization by introducing an EnsemW2S-AdaBoost algorithm that utilizes ensembles of weak supervisors to enhance the performance of stronger language models. It emphasizes the concept of easy-to-hard (e2h) data learning, which is crucial for addressing the challenges posed by difficult-to-label data.  Experimental results are provided to illustrate the effectiveness in tasks including binary classification and question-answering.

### Strengths
Overall, I believe this research makes significant contributions in terms of idea, design, and community impact. The supplementary materials also provide extensive code, which I hope will be open-sourced for broader review and to enhance reproducibility.

**Originality**: The authors reasonably enhance the work of Burns et al. by expanding the concept from a single weak supervisor to multiple weak supervisors, thereby increasing both generality and practicality. The adaptation of the AdaBoost algorithm takes into account the autoregressive nature of language models and effectively addresses the challenges of complex token sequence generation tasks, demonstrating diligent design efforts.

**Significance**: The introduction of the easy-to-hard (e2h) framework, along with the adaptation of AdaBoost, offers valuable insights for practitioners in related fields. These contributions may promote research on super-alignment.

### Weaknesses
While the overall idea of this work appears reasonable and promising, some sections lack sufficient clarity and quality. I have a basic understanding of weakly supervised learning and ensemble learning, which makes the explanations regarding the easy-to-hard framework (Section 2) and the experimental demonstrations (Section 5) quite understandable. However, the core section on the adaptation of AdaBoost (Section 3) is somewhat obscure and lacks clear background context.

Furthermore, the experiments are only conducted on simple binary classification and limited QA tasks (ARC and Quartz), which I believe do not provide sufficient support for the claims made. Given that the paper's foundation is super-alignment, it should ideally validate its approach on more challenging benchmarks (like in DataComp-LM or FineWeb). I am not necessarily expecting state-of-the-art performance, but rather a demonstration of how the method performs across a broader range of tasks.

In lines 222-224, the prior term $\log\left(\frac{1}{1-\epsilon} - 1\right)$ and the final equation for $\alpha$ are presented in a specific form. However, I did not find a clear derivation for this formulation. Could you clarify the reasoning behind choosing this particular expression?

As noted in lines 410-411, "PGR is not very informative, as it can produce extremely large or even negative values." Why, then, does the paper still utilize PGR as a performance metric for binary classification tasks? This seems somewhat contradictory.

In line 358, the authors state, "We pick the best w2s performing round for our plots." I believe this approach can be misleading. Although Figures 2 and 4 show an apparent improvement in performance from weak-to-strong models compared to weak model performance, Tables 1 and 2 in the appendix indicate that this is not always the case. When AdaBoost employs different values of $T$, the weak-to-strong model sometimes shows improved performance and sometimes declines. This unstable performance variation raises doubts about the true effectiveness of the proposed method. In other words, achieving good performance with a specific combination of weak and strong models requires careful tuning across different values of $T$ , and this $T$ is not universal. This reliance on hyperparameter selection suggests that the method may lack generalizability, which contradicts the pursuit of weak-to-strong **generalization** stated in the paper.

### Questions
1. In lines 222-224, the prior term $\log\left(\frac{1}{1-\epsilon} - 1\right)$ and the final equation for $\alpha$ are presented in a specific form. However, I did not find a clear derivation for this formulation. Could you clarify the reasoning behind choosing this particular expression?

2. As noted in lines 410-411, "PGR is not very informative, as it can produce extremely large or even negative values." Why, then, does the paper still utilize PGR as a performance metric for binary classification tasks? This seems somewhat contradictory.

3. In line 358, the authors state, "We pick the best w2s performing round for our plots." I believe this approach can be misleading. Although Figures 2 and 4 show an apparent improvement in performance from weak-to-strong models compared to weak model performance, Tables 1 and 2 in the appendix indicate that this is not always the case. When AdaBoost employs different values of $T$, the weak-to-strong model sometimes shows improved performance and sometimes declines. This unstable performance variation raises doubts about the true effectiveness of the proposed method. In other words, achieving good performance with a specific combination of weak and strong models requires careful tuning across different values of $T$ , and this $T$ is not universal. This reliance on hyperparameter selection suggests that the method may lack generalizability, which contradicts the pursuit of weak-to-strong **generalization** stated in the paper.

### Soundness
3

### Presentation
2

### Contribution
2
