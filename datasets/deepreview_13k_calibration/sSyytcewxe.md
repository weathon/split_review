# Divide and not forget: Ensemble of  selectively trained experts  in Continual Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Class-incremental learning is becoming more popular as it helps models widen their applicability while not forgetting what they already know. A trend in this area is to use a mixture-of-expert technique, where different models work together to solve the task. However, the experts are usually trained all at once using whole task data, which makes them all prone to forgetting and increasing computational burden. To address this limitation, we introduce a novel approach named SEED. SEED selects only one, the most optimal expert for a considered task, and uses data from this task to fine-tune only this expert. For this purpose, each expert represents each class with a Gaussian distribution, and the optimal expert is selected based on the similarity of those distributions. Consequently, SEED increases diversity and heterogeneity within the experts while maintaining the high stability of this ensemble method. The extensive experiments demonstrate that SEED achieves state-of-the-art performance in exemplar-free settings across various scenarios, showing the potential of expert diversification through data in continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an (exemplar-free) ensemble method for Class Incremental Continual Learning (CIL). A fixed number of experts are trained on a stream of tasks. At each task, only one expert is finetuned. The result is a diverse expert ensemble which is reported to perform very well on several benchmarks.

### Strengths
I believe this paper advances the field of continual learning.

Specifically,

- Tackles a popular continual learning scenario.
- Good empirical results. Show significant improvements on several datasets.
- Well written and clear.
- Sound experiments with several ablation studies.

### Weaknesses
No major weaknesses. Perhaps just the fact that several models (experts) have to be trained and stored (but this is inherent in ensemble methods).





### Questions
1. In Page 8, it's written that *"SEED uses a regularization method known from LwF"*. Are you actually using LwF for each expert? I don't recall reading it in other places in the paper. Please clarify.
1. How are the hyperparameters of EWC and LwF set in the experiments ? For instance, Figure 7 shows $\lambda\in [100,10000]$ without any justification.
1. In Page 1, the authors mention *"The trend is evident... results steadily improve over time"*. What time?
1. In Table 1, how many repetitions are performed per experiment?
1. In Table 1, why aren't there results for ImageNet-Subset for two algorithms?
1. In Figure 5, the presented metric is "relative accuracy". Relative to what?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new class-incremental learning algorithm which relies on a set of expert models with a shared backbone. In each training step, only one expert is trained on the new task. This expert is chosen based on how well it separates the new classes. At inference time, all experts make predictions but their contribution to the final prediction is conditioned on the input.
Experiments are conducted on three different datasets in two variants and for task-agnostic and task-aware cases.
The authors provide several ablation studies on core components of the method.

### Strengths
The authors make an interesting observation by showing that some methods work significantly better if more data is available initially.
They propose a method that improves over the baselines, in particular in the case where few data is available initially. The method and description is good and reminds me of S-Prompts which has a similar setup but works with pretrained transformer models.
As far as I can tell, all important aspects are covered by ablation studies, leaving only room for few questions.

### Weaknesses
A not fully covered discussion is the number of parameters vs accuracy tradeoff. The proposed methods requires significantly more parameters than some of the baselines which might be a limitation if the models are extremely large. Furthermore, training from scratch is a rather uncommon scenario. It is unclear how this method would work if a pretrained model is used. The analysis lacks a detailed breakdown of the computational cost associated with training multiple experts, especially in comparison to single model approaches. This includes not only the number of parameters but also the training time and memory requirements, which could be a significant practical limitation. Additionally, the paper does not explore the sensitivity of the method to the number of experts. While ablation studies are provided, a more systematic analysis of how performance varies with different numbers of experts would be beneficial. Finally, the method's reliance on a shared backbone might limit the diversity of features learned by each expert, potentially hindering performance on complex tasks.

### Questions
Figure 7 (right): what is the difference between SEED with 1 expert and finetuning? What is your explanation that your method is doing very well in this particular setup?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the class incremental learning (CIL) problem from the mixture-of-experts (MOE) angle where only a subset of the model (expert) is activated for each task. To this end, the authors propose SEED that selects one expert per task during continual training and aggregates the experts during evaluation. Thus, SEED promotes diversity representations while requiring no task identifiers during inference. Experiments on various CIL benchmarks show promising results of SEED.

### Strengths
- This work studies the MoE for CIL, which has been gaining interests as a promising approach to CIL.
- The proposed method is simple yet demonstrated encouraging results.
- The authors conduct various ablation studies to explore different aspects of SEED.

### Weaknesses
## Major concern - experiment
- In table 1 and 2, although it is clear that SEED performs better than the baselines, different methods have different memory footprint (model parameters and other components) or training complexities. Thus, it is difficult to judge if the gains come from the proposed method or from the additional complexities. Specifically, the comparison is not fair since methods like SSRE use a complex multi-phase training with expansion and pruning, while others might have different memory requirements for storing past exemplars or maintaining auxiliary networks. The reported performance gains could be attributed to these differences in training and memory overhead rather than the core algorithmic contribution of SEED. A more controlled comparison, where methods are evaluated under similar parameter budgets and computational costs, is needed to isolate the effect of the proposed approach.

## Major concern - conceptual drawback of SEED
- SEED implies that the number of experts should be smaller than the number of tasks and there is only one expert activated per task. Thus, it is inevitably that some experts will be reused in the future, leading to catastrophic forgetting especially when the tasks are conflicting. The use of LwF regularization might not be helpful if the expert stay inactive for a long period. Furthermore, the assumption that a single expert can effectively capture the nuances of a task, especially in complex scenarios, is questionable. The method's reliance on a fixed number of experts and a one-to-one task-expert mapping could limit its scalability and adaptability to diverse task sequences. The potential for interference between tasks assigned to the same expert, especially when those tasks are semantically dissimilar, is a significant concern. Together with with the ambiguity in the experimental settings and results, the contribution of this work seems marginal.

## Minor concern 
- Additional baselines: A recent related method [A] that seems to outperforms SEED should be discussed.
- There are two different references for CoSCL in the Introduction.

### Questions
- Performance comparison under a fair setting.
- How could SEED avoid forgetting when the number of tasks is significantly larger than the number of experts.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Selection of Experts for Ensemble Diversification (SEED), an algorithm that tackles exemplar-free class-incremental learning (CIL). Existing exemplar-free CIL algorithms incrementally trains new local experts on new tasks, and SEED provides a task selection technique to diversify trained experts, mitigate forgetting, and maintain plasticity. Specifically, an expert is a Bayes classifier that targets a distinct set of classes, with each class corresponding to a Gaussian distribution. To diversify expert selection, the next task is selected via the highest KL-divergence from encountered distributions. Inference is done by averaging the logits output from each expert and selecting the class with highest probability.

### Strengths
1. The paper clearly identifies a problem of task diversification in CIL.
2. The language is easy to follow.

### Weaknesses
1. Lack of novelty: selecting the next task based on largest KL divergence in continual learning is not a novel strategy. So is the expandable MoE architecture and the inference method.
2. Overhead growth: one biggest disadvantage of architecture expansion is that the memory overhead grows linearly with respect to the number of tasks. That is, it needs K experts for K tasks with nothing reusable. SEED omits the selection procedure to decide the number of experts needed even if the number of tasks is large. This is not scalable in continual learning, where the number of tasks can be unbounded.

### Questions
Please address the two weakness points above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
