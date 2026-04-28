# MAST: A Sparse Training Framework for Multi-agent Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
Deep Multi-agent Reinforcement Learning (MARL) is often confronted with large state and action spaces, necessitating the utilization of neural networks with extensive parameters and incurring substantial computational overhead. Consequently, there arises a pronounced need for methods that expedite training and enable model compression in MARL. Nevertheless, existing training acceleration techniques are primarily tailored for single-agent scenarios, as the task of compressing MARL agents within sparse models presents unique and intricate challenges. In this paper, we introduce an innovative Multi-Agent Sparse Training (MAST) framework. MAST capitalizes on gradient-based topology evolution to exclusively train multiple MARL agents using sparse networks. This is then combined with a novel hybrid TD-($\lambda$) schema, coupled with the Soft Mellowmax Operator, to establish dependable learning targets, particularly in sparse scenarios. Additionally, we employ a dual replay buffer mechanism to enhance policy stability within sparse networks. Remarkably, our comprehensive experimental investigation on the SMAC benchmarks, for the first time, that deep multi-agent Q learning algorithms manifest significant redundancy in terms of Floating Point Operations (FLOPs). This redundancy translates into up to $20$-fold reduction in FLOPs for both training and inference, accompanied by a commensurate level of model compression, all achieved with less than 3\% performance degradation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper involves sparse training for MARL to reduce the computation cost. Besides, to reduce the value estimation error, a hybrid TD($\lambda$) and Soft Mellowmax operator are incorporated. Experiments on SMAC show the proposed method significantly reduces the training cost while maintains good performance.

### Strengths
Using sparse training in MARL is relatively new and an important direction that will inspire the community.

Experiments are conducted on SMAC with extensive analysis.

### Weaknesses
The clarity of this paper needs to be improved. For example, the proposed method uses RigL to sparse the network. However, the details of RigL are missing, which makes it confusing for readers who are not familiar with the sparse training area.

The limitation of this paper is not discussed. For example, there are too many key parameters that need to be fine-tuned, making it infeasible to apply to other complex domains.

The literature review lacks some closely related work, such as [1]. So the statement 'The only existing endeavor to train sparse MARL agents' is inaccurate. Also, dual buffers have some related work like [2].

The visualization does not look very informative to the reviewer, as there are no specific patterns for the latent space distribution. Perhaps projecting what connections are removed and what connections are remaining and analyzing why it is like that will be interesting.

### Questions
Please see the pros and cons part.

Could you explain more about why 'larger values under a sparse model compared to a dense network' in Section 4.1? Do you mean overestimations?

The well-known method to deal with overestimation is double Q-learning, have you compared this with SM? Which one is better and why?

How do you select the value of $\omega$ as 5 and 10? 

Why does the value in Table 1 exceed 100%? How do you calculate it?

The common evaluation metric in SMAC is average success rate, why do you use average reward? Do you normalize all tasks' rewards to the same scale?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces MAST, a novel sparse training framework for deep MARL, utilizing gradientbased topology evolution to efficiently explore network configurations in sparse models. MARL faces significant challenges in ultra-sparse models, including value estimation errors and training instability. Their experiments show the contribution on FLOPs and performance.

### Strengths
1.The problem that the authors focus on is very important and valuable to explore.
2.A lot of experiments have been conducted to prove their contribution.

### Weaknesses
1.The writing logic is bad, making readers hard to follow. For example, what is the relationship of the sparse model in SL, single-agent RL and multi-agent RL? Why does MASK apply to QMix series approaches and when MAST is applied to QMIX series algorithms and leverage the RigL method for topology evolution? The authors use too many words on the related work and basic knowledge of MARL, but not clarify the logic clearly.
2.Some of the formulas are not numbered.
3.Cannot the discount rate in RL be 1?
4.The experiment is conducted only on 4 seeds, which is not enough and strong in RL scenarios.
5.“These topology adjustments occur infrequently throughout the training process, happening every 200 episodes (about 10,000 steps) in our specific configuration.” How about under other configurations?
6.Algorithm 1 of the overall procedure is in supplementary, I suggest to contain it in the main text.

### Questions
Please see the weakness above. Can the authors give a clear logic of the paper? And the innovative solutions in an easy-understood way?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Multi-Agent Sparse Training (MAST) framework, which aims to expedite training and enable model compression in MARL. MAST utilizes gradient-based topology evolution to train multiple agents using sparse networks, incorporating a hybrid TD-lambda schema and the Soft Mellowmax Operator to establish reliable learning targets in sparse scenarios. Experiments on the SMAC benchmarks demonstrate the effectiveness of the proposed method.

### Strengths
1.	The proposed sparse training framework contributes to making MARL systems applicable to resource-limited devices.
2.	MAST can be applied to different methods with the CTDE training framework.
3.	Experiments on the SMAC benchmarks provide evidence of the effectiveness of the proposed

### Weaknesses
1.	The paper utilizes multiple technologies, such as RigL, hybrid TD targets, the Soft Mellowmax operator, and dual buffers, which may make it difficult to discern the specific kernel contribution and novelty. The combination of these techniques, while potentially effective, obscures the individual impact of each component. For instance, it's unclear how much performance gain is attributable to the hybrid TD-lambda target versus the Soft Mellowmax operator, or whether the dual buffer provides a significant advantage over a single buffer in this sparse training context. This lack of clarity makes it challenging to assess the core innovation of the proposed method.
2.	If the motivation lies in the algorithm, the contribution may seem incremental. Additionally, if the paper aims to design an effective framework, it would be necessary to conduct experiments on other benchmarks, such as Google Research Football, to demonstrate its superiority. The current experiments, while showing promise on SMAC, do not fully establish the generalizability of the proposed framework. The specific characteristics of SMAC might favor the proposed approach, and testing on more diverse and complex environments like Google Research Football would be crucial to validate its broad applicability and effectiveness. Without such validation, the contribution remains somewhat limited to the specific scenarios tested.

### Questions
1.	I would like the authors to clarify their main contribution to help me better understand the paper.
2.	Some curves in the results do not appear to converge at the end. Could this be due to the figures being drawn with smooth weight?
3.	The results were obtained with 4 random seeds. Could you provide information about the variance? Is the method stable?
4.	The paper utilizes many technologies, such as hybrid TD-lambda, which introduces several hyperparameters. How do you decide on these hyperparameters in different scenarios, especially in real-world applications? Do you have any suggestions?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
