# Policy-aware Reward Modeling with Uncertainty-Gradient based Data Augmentation

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has emerged as a standard and effective approach for training large language models (LLMs) with human preferences. In this framework, a learned reward model approximates human preferences and guides policy optimization, making it crucial to develop an accurate reward model. However, without the ``true'' reward function, challenges arise when the reward model is an imperfect proxy for human preference. Since the policy optimization continuously shifts the human preference training dataset's distribution. The fixed reward model suffers from this problem of off-distribution, especially the on policy methods.  While collecting new preference data can mitigate this issue, it is costly and challenging to optimize. Thus, reusing the policy interaction samples becomes a possible way to further refine the reward model. To tackle these challenges, we introduce a novel method \textbf{U}ncertainty-\textbf{G}radient based \textbf{D}ata \textbf{A}ugmentation (\textbf{UGDA} for short) to enhance reward modeling by leveraging policy samples to maintain on-distribution performance. Specifically, UGDA selects interaction samples based on the uncertainty of the reward ensembles and the gradient based influence of policy optimization. After the reward relabeling of selected samples, we use supervised learning to refine the reward ensembles, then get the retrained policy. Extensive experiments demonstrate that by leveraging UGDA to select a few samples without the costly human preference data collection, we can improve the ability of the policy and surpass the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper considers the reward learning problem in reinforcement learning from human feedback (RLHF). As a reward model is trained from preference data and can be inaccurate, it would be beneficial to allow the model to query the labels of some samples. The key question is: querying the labels of which samples can improve the model’s performance the most.

The paper proposes Uncertainty-Gradient based Data Augmentation (UGDA). The method selects samples for labeling based on a joint objective combining (1) the uncertainty of the sample’s prediction (based on an ensemble of reward models) and (2) the influence of the sample on a validation set. The model identifies samples that maximize this joint objective and queries their labels. Empirical results demonstrate that UGDA outperforms other sample selection methods in improving model performance.

### Strengths
Novelty: The algorithm is novel in using gradient-based data influence for reward learning. To the best of my knowledge, this approach has not been previously applied to reward learning in RLHF.

Motivation and Empirical Performance: The proposed method is well-motivated and well explanable. Empirical results show UGDA's effectiveness.

### Weaknesses
 **Motivation and algorithm design.** I wonder if UGDA can be over-complicated for the goal it wants to achieve. For example, can I use simpler heuristics to select samples that may lead to a larger learning gradients?

For example, does UGDA tend to select out-of-distribution samples in the training set (as these samples can lead to larger training gradients)? If we simply find samples that are outliers in the training dataset (for example, using data density distribution), would they perform similarly to UGDA?

**Evaluation.** The reward models are all finetuned from Gemma models, and Llama-2-13B model is used for evaluation. Would UGDA have similar results if tested with different model architectures?

**Presentation.**
Notational Clarity: The notation could be improved for clarity. For example, $R_v$ looks like a specific reward function, but it actually represents variance.

The paper would benefit from overall improvements in clarity and grammar. Specific issues include:
Line 18-19, ungrammatical: “Since the policy optimization continuously shifts the human preference training dataset’s distribution.”
Line 48 “Recently, there are some works [that] focus on”

### Questions
I have some questions in the weakness section above.

I didn’t see details on how the validation set is constructed. Does the validation set have the same distribution as the training set?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper study the reward modeling using LLMs in RLHF. The authors argue that the existing reward models, which serve as proxies for human preferences, become less effective as the policy optimization process shifts the distribution of the training dataset. To address this, UGDA leverages policy interaction samples, selecting them based on the uncertainty of the reward ensembles and the gradient-based influence on policy optimization. The selected samples are then used to refine the reward model through supervised learning, which in turn improves the policy. Empirical results show that UGDA can enhance policy performance without the need for costly human preference data collection, surpassing state-of-the-art methods in experiments.

### Strengths
This paper is well-motivated and well-written.

This paper aims to address the off-distribution reward overoptmization problem, which is a critical issue in RLHF.

### Weaknesses
Lacks comparisons to active learning and data augmentation baselines.

Considering that off-policy methods have become popular, additional analysis of the robustness of UGDA under different policy optimization scenarios, such as iterative DPO, could strengthen the paper.

### Questions
Could you apply the method to the full fine-tuning reward ensembles?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Uncertainty-Gradient-based Data Augmentation (UGDA), an approach to enhance reinforcement learning from human feedback for training LLMs. UGDA addresses a key issue: the limitations of an imperfect reward model that serves as a proxy for human preferences, which becomes increasingly problematic as policy optimization alters the training data distribution. UGDA aims to refine the reward model by selectively relabeling the most uncertain and impactful interaction data during policy optimization. The proposed approach follows a three-stage pipeline: Reward LoRA Ensembles, Data Selection, and Reward LoRA Refinement. Experiments demonstrate that UGDA improves policy performance without the costly requirement of additional human preference data collection.

### Strengths
1. The paper introduces a new method for selecting the uncertain and impactful interaction data during policy optimization to refine the reward model. 
2. The paper is well-organised and articulated with clarity, the complex concepts are explained in a clear and concise manner. 
3. The results, partly supported by some confidence/uncertainty based methods, demonstrate considerable potential for improving alignment of LLMs with human values.

### Weaknesses
The results have a few issues which make evaluating the contribution difficult:
1. The paper lacks a comparison with some existing works, particularly methods involve iterative PPO/DPO method that train a reward model simultaneously and  reward ensembles [1].
[1] Coste T, Anwar U, Kirk R, et al. Reward model ensembles help mitigate overoptimization.   
2. The alignment of relabeled reward data with human annotator judgments remains insufficiently validated.

### Questions
Could the authors provide a more detailed description of the process for selecting the validation dataset? Given that the impact score depends on the validation set, what are the implications if the validation dataset distribution significantly differs from the training set? Will this also introduce high bias in the impact score.

How does the computational complexity of UGDA scale with model and dataset size, considering the use of an ensemble of reward models and the validation dataset?

What if the variance in reward signals provided by different reward models for the same questions and responses remains high after refining the reward models? The paper lacks an analysis of how refining the reward models impacts the consistency of the reward signals.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a new method for improving reward model training by prioritising on-policy samples to relable to get the highest performance with the least relabelling cost. The method uses a combination of empirical uncertainty estimated by an ensemble of reward models, and gradient-based influence calculation to select data. The paper presents empirical results showing that their method outperforms baselines across a range of metrics in the HH dataset for two different reward model sizes. Their method improves both reward model performance and policy performance, and in a series of ablations the paper shows that all components of the proposed method are important for the success of the method.

### Strengths
The proposed method is interesting and novel, and shows strong improvements over reasonable baselines. The problem of reward model overoptimisation is an important and timely one, making the contribution reasonably significant. While the method adds additional complexity on top of the baselines, this does seem to pay off in improved performance, and ablations demonstrate that how each component contributes. The idea is intuitive which makes the contribution more compelling. The paper is mostly easy to read and understand. The contribution seems sufficiently original.

### Weaknesses
# lack of clarity on RLR

The RLR baseline is not explained in the main body of the paper. Could you add a description of this algorithm so that it's clear what UGDA is being compared to?

# Limited evaluation dataset

The experiments are only performed on anthropic HH. It would be beneficial to demonstrate improvements on another RLHF dataset as well. This is partially remedied by showing improvements on a range of metrics and for reward models as well as policies, but this is still a weakness of the paper.

# Lack of error bars

It would be useful to have error bars or confidence intervals on any of the reported results. I acknowledge that running experiments for additional seeds is costly, but it would make the results much more robust

### Questions
The RLR baseline is not explained in the main body of the paper. Could you add a description of this algorithm so that it's clear what UGDA is being compared to?

### Soundness
3

### Presentation
2

### Contribution
3
