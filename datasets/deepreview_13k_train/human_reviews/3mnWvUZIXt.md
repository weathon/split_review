# Towards Principled Representation Learning from Videos for Reinforcement Learning

- Decision: Accept
- Scores: 8, 8, 5, 8

## Abstract
We study pre-training representations for decision-making using video data, which is abundantly available for tasks such as game agents and software testing. Even though significant empirical advances have been made on this problem, a theoretical understanding remains absent. We initiate the theoretical investigation into principled approaches for representation learning and focus on learning the latent state representations of the underlying MDP using video data. We study two types of settings: one where there is iid noise in the observation, and a more challenging setting where there is also the presence of exogenous noise, which is non-iid noise that is temporally correlated, such as the motion of people or cars in the background. We study three commonly used approaches: autoencoding, temporal contrastive learning, and forward modeling. We prove upper bounds for temporal contrastive learning and forward modeling in the presence of only iid noise. We show that these approaches can learn the latent state and use it to do efficient downstream RL with polynomial sample complexity. When exogenous noise is also present, we establish a lower bound result showing that the sample complexity of learning from video data can be exponentially worse 
than learning from action-labeled trajectory data. This partially explains why reinforcement learning with video pre-training is hard. 
We evaluate these representational learning methods in two visual domains, yielding results that are consistent with our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces theoretical analysis for pre-trained representation learning using video data and focuses on two settings: where there is iid noise in the observation and where there is also exogenous noise in the observations. 

More specifically the paper investigates three methods for video pre-training - autoencoding, temporal contrastive learning, and forward modeling, and introduces two main theorems. The first theorem provides an upper bound for the setting where there is only iid noise, and the second provides a lower bond when the observations also include exogenous noises. The first theorem leads to the conclusion that learning a representation from videos is provably correct when there is no exogenous noise, while the second means that learning is exponentially hard when there is exogenous noise (in contrast to learning from trajectory data, where the corresponding actions are available). The proofs were provided for temporal contrastive learning, and forward modeling, while evaluation and comparison to learning form trajectory data (ACRO) are provided for all three learning procedures (vector quantized variational autoencoder, temporal contrastive learning, and forward modeling).

### Strengths
This work introduces, for the first time, theoretical analysis and justification for pre-trained representation learning of policies from video data (under certain assumptions). In addition, the paper validates the theoretical analysis in practice, by experimenting on two challenging visual domains (GridWorld and ViZDoom). 

The paper is well organized and clear to read and understand.

### Weaknesses
Although tested empirically, the paper does not provide a theoretical analysis for autoencoder-based approaches. Adding this analysis would make this work more complete. Specifically, the paper lacks a formal treatment of the representational capacity of the autoencoder, and how this capacity interacts with the complexity of the video data. A theoretical analysis should consider the conditions under which the autoencoder can learn a useful representation, and how the dimensionality of the latent space affects the quality of the learned representation. Furthermore, the paper does not discuss the potential for the autoencoder to learn spurious correlations in the data, which could lead to poor generalization performance. 
In addition, the observation that temporal contrastive representation fails in the presence of exogenous noise is only empirical, justified with intuition, and lacks a more formal proof. The paper should provide a more rigorous analysis of why temporal contrastive learning is more susceptible to exogenous noise compared to forward modeling. This analysis should consider the specific objective functions used by each method and how they are affected by the presence of exogenous noise. For example, a formal analysis could investigate how the contrastive loss is influenced by the noise, and why this influence is more detrimental than the effect of noise on the forward prediction loss. 

The analysis is restricted to training a fixed representation using only video data, without any fine-tuning stage of the learned representation. It would be nice to see an analysis of the common scenario of the fine-tuning stage. This analysis should consider how the learned representation is adapted to a specific downstream task, and how the fine-tuning process affects the quality of the representation. The analysis should also consider the potential for catastrophic forgetting during fine-tuning, and how this can be mitigated. 

The evaluation for iid noise with varying strength is missing (evaluation similar to Figure 6 but with iid noise). This evaluation is important for reliably comparing the performance of the setting with iid noise to that with exogenous noise. Without this, it is difficult to assess how the performance of the different methods degrades as the noise level increases, and to understand the relative robustness of each method to different types of noise.

### Questions
I would like to ask the following questions:

1. Why are encoder-based approaches harder to analyze?

2. If Assumption 3 (Margin Assumption) holds also for the exogenous noise in addition to the endogenous states, would learning from video data still be exponentially worse than learning from trajectory data? If the answer is yes, it means that learning a representation from videos is provably correct for cases where the margin assumption holds for all the transitions in the data. 

3. In addition to the intuition, is it possible to prove the observation that temporal contrastive representation falls short in the presence of exogenous noise, compared to the forward model?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies representation learning from videos in the context of reinforcement learning. In particular, this work focuses on representation learning in the presence of noice, either iid or exogenous. The theoretical results show that while the current methods should be able to work well with iid noise, the agent may need exponentially more samples when exogenous noise is present.
The experiments are conducted on GridWorld and VizDoom, and show that existing representation learning methods such as ACRO [1], temporal contrastive learning, VQ-VAE can learn with iid noise. 

[1] Agent-Controller Representations: Principled Offline RL with Rich Exogenous Information, Islam et al, https://arxiv.org/abs/2211.00164

### Strengths
- The work presents thorough theoretical analysis of representation learning from videos with iid and exogenous noise and arrives at an interesting conclusion
- The experimental results shed light on how temporal contrastive method performs compared to models that output images

### Weaknesses
The experiments feel a little bit detached from the theoretical results: the are no experiments with iid noise, and the results with exogenous noise seem to mainly point to the fact that some representation methods are better than others, not that exogenous noise breaks everything. Only in Figure 6 do we see exogenous noise breaking forward modeling, while ACRO still works. The experimental section lacks a clear set of hypotheses that the experiments are designed to test, making it difficult to interpret the results in the context of the theoretical claims. For example, while the theory suggests an exponential sample complexity gap in the presence of exogenous noise, the experiments do not directly demonstrate this exponential relationship, instead showing a more gradual performance degradation. Furthermore, the experiments do not explore the limits of iid noise, and it is unclear how much iid noise the methods can tolerate before performance degrades significantly. The experiments also do not explore the effect of different types of exogenous noise, such as structured noise or noise that is correlated with the agent's actions, which could further challenge the robustness of the representation learning methods. The comparison between different representation learning methods is also not sufficiently detailed, and it is unclear why some methods are more robust to exogenous noise than others, beyond the high-level explanation that ACRO uses trajectory data. A more detailed analysis of the learned representations and their sensitivity to noise would be beneficial.

Section 4.2: "remembering all of them can easily overcome the network’s capacity focusing on the agent’s state can better help the future predictions." reads weird.
Page 2: "probne" should be "prone".
Above Equation 2, given $(x^{(i)}, k^{(i)}$ is missing a parenthesis
Assumption 1: noisy-free should be noise-free
Justification for Assumption 3: missing parenthesis in P_for

### Questions
Can authors explain the connection between the theoretical part and experiments better? What do the results say in relation to the theoretical conclusions?

In Figure 4, the results seem to show that forward modeling and VAE are actually able to handle the exogenous noise. This is contrary to the theoretical result, is that right?
Only in Figure 6 do we see that indeed when noise is strong enough the forward modeling objective fails.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides theoretical and empirical results for representations learning for decision-making using video data (without explicit knowledge of the actions). Two settings are studied: one where there is iid noise in the observation, and a setting where there is "exogenous noise, which is non-iid noise that is temporally correlated, such as the motion of people or cars in the background". Three techniques are compared: autoencoding, temporal contrastive learning, and forward modeling. Theoretical and empirical results are provided.

### Strengths
- Interesting research questions that can have a big scientific impact
- overall well-written
- experiments follow good practice

### Weaknesses
 - Some parts of the text are not clear/accurate (see the remarks and questions below in the "questions" section). There are also typos, e.g. "(...) temporal contrastive learning is probne to fail (...)"
- It is unclear how the key messages that are supposed to come from the theorems are actually deduced (see questions below).

Unclarities in the text:
- The abstract mentions "We evaluate these representational learning methods in two visual domains, proving our theoretical findings." Empirical evaluation can never prove theoretical results except if it looks at all possible cases for instance. In general, it can only illustrate them.
- Beginning of Section 3, it is mentioned that "Our goal is to learn a decoder $\phi : X \rightarrow [N]$ that learns information in the underlying endogenous state $\phi^*(x)$ while throwing away as much irrelevant information as possible.". I don't understand this sentence. Isn't it an encoder that is learnt? What is an endogenous state and what is $phi^*$?
- "ACRO achieves optimal performance across all tasks.": do the authors mean better than other algorithms instead of optimal? (the optimal is not exactly reached and also basically not known.

Theorems
- What is $\alpha$ in Theorem 1?
- For Theorem 1, unless I'm mistaken, the only discussion that is directly about the theorem mentions "These upper bound provide the desired result which shows that not only can we learn the right representation and near-optimal policy but also do without the online episodes scaling with ln |Φ|." How can that interpretation be made from the theorem?
- For theorem 2, it also unclear how the interpretations can be deduced from the theorem itself.

- In Theorem 1, $\alpha$ is now introduced as a "bijection mapping". Why do yo need this one to one mapping?
- In theorem 1, what does it mean that $\phi^*(x)=s$? Does it mean that you have access to the true state?

### Questions
Unclarities in the text:
- The abstract mentions "We evaluate these representational learning methods in two visual domains, proving our theoretical findings." Empirical evaluation can never prove theoretical results except if it looks at all possible cases for instance. In general, it can only illustrate them.
- Beginning of Section 3, it is mentioned that "Our goal is to learn a decoder $\phi : X \rightarrow [N]$ that learns information in the underlying endogenous state $\phi^*(x)$ while throwing away as much irrelevant information as possible.". I don't understand this sentence. Isn't it an encoder that is learnt? What is an endogenous state and what is $phi^*$?
- "ACRO achieves optimal performance across all tasks.": do the authors mean better than other algorithms instead of optimal? (the optimal is not exactly reached and also basically not known.

Theorems
- What is $\alpha$ in Theorem 1?
- For Theorem 1, unless I'm mistaken, the only discussion that is directly about the theorem mentions "These upper bound provide the desired result which shows that not only can we learn the right representation and near-optimal policy but also do without the online episodes scaling with ln |Φ|." How can that interpretation be made from the theorem?
- For theorem 2, it also unclear how the interpretations can be deduced from the theorem itself.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study offers a theoretical analysis of representation learning from video-based observations without labeled actions. The problem is formulated as a block Markov Decision Process with exogenous noise. Endogenous states are acquired through an encoder trained with one of three methods: a temporal contrastive loss, a single-state reconstruction loss (autoencoder), or a future state reconstruction loss.

The primary contribution of this paper is the establishment of a theorem that sets an upper bound on representation learning for future state prediction and the contrastive learning approach without noise. It also provides a lower bound in the presence of exogenous noise for these approaches, indicating that agents cannot distinguish between exogenous and endogenous noise. These results are further validated through experiments conducted in both a grid world and a visual environment. In cases without exogenous noise, representation learning proves successful, but it fails in its presence.

### Strengths
- The paper is well-written, and the proofs are clear and concise.
- The results address a significant and novel problem, namely, representation learning from noisy video-based data, which is of great interest in the current Reinforcement Learning (RL) community.
- The theoretical results quantitatively address a major challenge in current methods.
- The empirical results align well with the theoretical findings.
- The study explores multiple approaches for representation learning.
- Assumptions are thoroughly explained and justified.

In conclusion, I believe this work should be accepted, as it offers significant and relevant insights to the action-free RL research community. The paper's strengths and contributions make it a valuable addition to the field.

### Weaknesses
 - While the paper is strong in many aspects, it would be beneficial to expand the experimental evaluation to a wider variety of environments to further validate the results.
- Minor errors, such as unclosed brackets in equations under Assumption 3, should be corrected for clarity and correctness.

### Questions
Could we see some additional experiments in the revision?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
