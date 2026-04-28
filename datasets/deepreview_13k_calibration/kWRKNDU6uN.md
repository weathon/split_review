# Diffusing States and Matching Scores: A New Framework for Imitation Learning

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 6, 8, 8

## Abstract
Adversarial Imitation Learning is traditionally framed as a two-player zero-sum game between a learner and an adversarially chosen cost function, and can therefore be thought of as the sequential generalization of a Generative Adversarial Network (GAN). 
    However, in recent years, diffusion models have emerged as a non-adversarial alternative to GANs that merely require training a score function via regression, yet produce generations of a higher quality. In response, we investigate how to lift insights from diffusion modeling to the sequential setting. We propose diffusing states and performing \textit{score-matching} along diffused states to measure the discrepancy between the expert's and learner's states. Thus, our approach only requires training score functions to predict noises via standard regression, making it significantly easier and more stable to train than adversarial methods. 
    Theoretically, we prove first- and second-order instance-dependent bounds with linear scaling in the horizon, proving that our approach avoids the compounding errors that stymie offline approaches to imitation learning. Empirically, we show our approach outperforms both GAN-style imitation learning baselines and discriminator-free imitation learning baselines across various continuous control problems, including complex tasks like controlling humanoids to walk, sit, crawl, and navigate through obstacles.
    \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on imitation learning from observations through the introduction of SMILING (Score-Matching Imitation LearnING). SMILING proposes to match the state distributions of experts and imitators by leveraging a diffusion model. 
This study presents theoretical results related to SMILING, specifically regarding first and second-order approximation bounds of suboptimality. Additionally, the authors theoretically demonstrate that score-matching methods can achieve superior data efficiency compared to traditional f-divergence or Integral Probability Metric (IPM) matching methods, particularly under deterministic transition scenarios.

### Strengths
This work presents a straightforward yet powerful objective: to match the score functions of expert and imitator state distributions. Despite its simplicity, this objective is strongly supported by theoretical results grounded in plausible assumptions. It is expected that the proposed method, SMILING, will show enhanced data efficiency relative to traditional imitation learning (IL) methods where the expert's (cumulative) cost is nearly deterministic as supported by the analysis in line 368.

### Weaknesses
I have main concerns in this study as follows:

**1. Insufficient comparative analysis with other diffusion-based IL methods:**

While this work introduces new theoretical contributions to the score-matching IL objective, the method itself lacks novelty. 
Previous studies [A, B, C, D] have already explored integrating diffusion models with imitation learning. 
However, the manuscript does not provide a detailed comparison between SMILING and these existing approaches, both conceptually and empirically. 
For instance, what are the key distinctions or what is the novelty compared to these methods? Under what conditions does the proposed method offer advantages over similar methods? Such discussions should be provided to clarify the novelty of this work.

This work appears to attempt to distinguish itself from other approaches by addressing the more specific problem of LfO, rather than standard IL. However, the manuscript does not show specific considerations for LfO; the stated objective could readily apply to state-action matching, as demonstrated in experiments (Figure 4).

**2. Weak Experimental Evaluations:**

The experimental evaluation presented also raises concerns. In the manuscript, SMILING is compared only against two obsolete baselines: BC and DAC. It is recommended to include comparisons with recent state-of-the-art IL methods such as ValueDICE [E], IQlearn [F], etc.
Moreover, the absence of comparisons with similar diffusion-based IL methods (e.g. DiffAIL [A], Diffusion-KDE [B], DBC [C], DRAIL [D] ...) further weakens the empirical validation. 
Such comparisons are insufficient to establish SMILING as a competitive method. 

In addition, the lack of experimental validation on theoretical results makes the paper less compelling. 
Given the theoretical emphasis on data efficiency in Section 5, experiments quantifying the relationship between the number of expert trajectories and the converged normalized score are essential for substantiating these claims. 
Additionally, providing experimental outcomes in both stochastic and deterministic cost scenarios would enhance the reliability of the theoretical results as well.

### Questions
Q1. Is the theoretical result specific to state-matching only? or can it also be applied to (state-action)-pair score matching?

Q2. LobsDICE [G] highlights a limitation of the state-matching objective, specifically that $D_f (d_E(s) | d_\pi (s))$ fails when it ignores the directionality of expert trajectories, and they suggest using $D_f (d_E(s,s’) | d_\pi (s,s’))$ instead (see the appendix of [G]). 
Can the score-matching objective $D_{DS}$ circumvent these issues?

**Reference** 

[G] Kim et al., “LobsDICE: Offline Learning from Observation via Stationary Distribution Correction Estimation”, NeurIPS 2022.

### Soundness
3

### Presentation
3

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
This paper addresses the problem of online imitation learning. To this end, the paper proposes an algorithm that matches the learner's distributions to the expert's using a cost function computed by a diffusion model. Theoretical derivations demonstrate the advantages of minimizing the proposed Diffusion Score Divergence. However, the experiment results are currently insufficient to fully support the effectiveness of the proposed approach.

### Strengths
**Motivation and intuition**
- The motivation behind the proposed Diffusion Score Divergence is convincing, as diffusion models have demonstrated a strong capability for distribution modeling.

**Theoretical contribution**
- This paper presents solid theoretical contributions, including well-defined assumptions, lemmas, and derivations. Additionally, it discusses related topics such as sample efficiency, second-order bounds and comparisons between score functions and discriminators.

**Clarity**
- The writing is clear overall, providing both theoretical and intuitive explanations. The notations, formulations, and theorems are well-explained and easy to follow.

### Weaknesses
 **Experiment setup**

The experiments are not sufficient. While the claims look promising, the proposed method only compares two baselines, behavior cloning (BC) and discriminator actor-critic (DAC), which is not sufficiently convincing.

First, recent adversarial imitation learning baselines, such as DiffAIL [1], should be considered. 
Although these methods do not explicitly learn reward functions but instead train discriminators, I am not convinced that this work is orthogonal to these previous works. They are feasible in the experimental setup in this paper, which includes limited expert demonstrations and online learner demonstrations.

Second, prior works [2,3] demonstrate that diffusion models are effective policies for offline imitation learning. Although offline methods can suffer from compounding error issues, it is still necessary to compare to one of the above methods to show that the proposed score-matching approach is beneficial when online learner demonstrations are accessible. 

**Experiment details**
- The details of the expert policy are missing. Since all experiments are normalized by the performance of the expert and random policies, the authors should report the specific performance values of these policies as reference points; otherwise, the reported results remain unclear.
- The number of environment steps used to train the expert policy is also missing, which makes it difficult to draw conclusions about sample efficiency from the results in Figures 3, 4, and 5. Specifically, online imitation learning aims to leverage expert demonstrations to improve sample efficiency. If the number of training steps for the expert policy is on a similar scale (e.g., 10^6), directly applying reinforcement learning to learn the expert policy could be a simpler solution.

Furthermore, the paper lacks clarity regarding how the expert demonstrations were generated. The description implies that the expert policy was trained using RL, and then trajectories were sampled from this policy. However, it is unclear what specific RL algorithm was used, what reward function was optimized, and what the training details were. This ambiguity makes it difficult to assess the quality of the expert demonstrations and the overall experimental setup.

### Questions
As noted in the weaknesses section, I have the following questions:

- Are there any results that compare the proposed method to recent adversarial imitation learning baselines, such as DiffAIL?
- Are there any results that compare the proposed method to offline imitation methods that utilize diffusion models?
- Could the authors provide the performance and learning details of both the expert policy and the random policy?

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
2

### Summary
This paper proposes a new imitation learning method using score-based diffusion models. Specifically, the authors perform score-matching to minimize the difference between the expert’s and learners’  state distributions. In this way, they can perform IL using states only and also state-action pairs. They provide theoretical bounds on sample complexity when score functions are used, and show that they provide tighter bounds than when IPMs or discriminators are used. The empirical results show that their method SMILING performs favorably compared to other baselines.

### Strengths
- The paper's contributions seem fair. They apply previously established score matching using diffusion models to IL. There have been many methods that used diffusion models in imitation learning (Section 2) and thus I rate the novelty as low. However, the authors provide new theoretical bounds and comparisons to discriminator-based methods. 

- The paper is fairly well-written and straightforward. I did not check for the correctness of the proofs and thus cannot comment.

### Weaknesses
 - The paper's contributions seem fair. They apply previously established score matching using diffusion models to IL. There have been many methods that used diffusion models in imitation learning (Section 2) and thus I rate the novelty as low. However, the authors provide new theoretical bounds and comparisons to discriminator-based methods. 

- The paper is fairly well-written and straightforward. I did not check for the correctness of the proofs and thus cannot comment.

 - The framing of the method in terms of inverse reinforcement learning confused me. As far as I know, inverse reinforcement learning infers a reward function from the state-action-next state tuples and uses that to learn a policy. However, this method seems to be pure imitation learning where actions are learned directly from states or state-action pairs. Section 2 seems to imply that SMILING does IRL but I  see this method as an imitation learning method (without a discriminator). Can the authors clarify if a reward function is inferred or clarify on how SMILING is indeed an IRL method?
- Some parts of the paper are disconnected with the rest of the paper and might possibly be left over from previous drafts  (e.g. connection to IRL, SAC/DreamerV3, etc.).
   - Lines 267-269: Were SAC and DreamerV3 used in the experiments? The experiments compared against DAC and BC. 
- It's unclear how Section 6.3 helps to show that score functions are more expressive than discriminators. The results just seem to exploit a known weakness with adversarial training (mode collapse). Does the expressivity here mean that score matching does not suffer from mode collapse?

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Traditionally in Inverse Reinforcement Learning (IRL), when expert demonstrations are available, a generative and adversarial setup is often used. In this setup, the discriminator’s goal is to learn the distribution of the desired behavior from expert demonstrations, while the generator’s goal is to produce behaviors that fit the distribution implicitly defined by the discriminator. Methods such as GAIL have proven powerful but come with a drawback: the optimization process. In these settings with a generator and discriminator, the optimal solution is a saddle point; however, it is often difficult to achieve due to issues like mode collapse and instability in training dynamics. In this work, the authors propose using diffusion models as an alternative. They achieve this by learning the score of the state distribution from expert demonstrations and then applying the DS divergence, which measures the difference in scores throughout the diffusion process. This metric is then used as the reward function to train the policy. The authors demonstrate impressive results on challenging humanoid tasks, particularly the Humanoid Walk task.

### Strengths
Impressive experimental results, clearly demonstrating the benefit from not having a GAN approach for IRL. 
Clear motivation and formulation and writing is of good quality.

### Weaknesses
I think there are prior work with a similar motivation.  Can you elaborate on how your is novel compared to the following:

https://openreview.net/pdf?id=NN60HKTur2
https://arxiv.org/pdf/2004.09395
https://arxiv.org/abs/2407.00626

I think the novelty compared to these works needs to be more clearly articulated, particularly concerning the specific use of diffusion models for score matching in the context of IRL. The current discussion lacks a detailed comparison of the technical differences and advantages of the proposed approach over these existing methods. For instance, the cited work on energy-based models also uses score matching for imitation learning, and it is not immediately clear how the diffusion-based approach offers a significant advantage in terms of performance or training stability. Furthermore, the work using diffusion models for policy learning in inverse RL presents a different perspective that should be more thoroughly contrasted with the current method's focus on reward learning.

I think there can be additional clarifications in the method: Algorithm 1, would be good to define $c^{(k)}$ explicitly either in the algorithm pseudocode or in the accompanying text. Additionally, adding how $c^{(k)}$ relates to the score functions mentioned earlier and if it's connected to the cost function in Eq. 3 would provide a more comprehensive understanding of the algorithm.

### Questions
The paragraph at line 081 could be clarified for readability and comprehension.

Could the authors elaborate on the sentence: "We first fit a score function to the expert demonstrations. Then, at each iteration of our algorithm, we fit a score function to the state distribution of the mixture of the preceding policies, before using the combination of these score functions to define a reward function for the policy search step." Specifically, what does "mixture of the preceding policies" mean?

Your explanation of the algorithm here is helpful, but this part could be more precise. For example, does "mixture of preceding policies" refer to averaging the state distributions from previous iterations, or does it imply some other form of combining past policies? It would also improve clarity if you could provide a concrete example or a diagram illustrating how this mixture is constructed and applied in the algorithm. These additions would address potential confusion and make the process more accessible to readers.

I think there can be additional clarifications in the method: Algorithm 1, would be good to define $c^{(k)}$ explicitly either in the algorithm pseudocode or in the accompanying text. Additionally, adding how $c^{(k)}$ relates to the score functions mentioned earlier and if it's connected to the cost function in Eq. 3 would provide a more comprehensive understanding of the algorithm.

### Soundness
4

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
3

### Summary
This paper introduces an Inverse Reinforcement Learning (IRL) algorithm called SMILING, which replaces the commonly used f-divergence with a novel approach called Diffusion Score Divergence. This new method measures the discrepancy between the expert's and the learner's state distributions along the same forward diffusion process. The proposed algorithm achieves significantly tighter first- and second-order instance-dependent bounds, supported by thorough error analysis throughout the entire algorithm. Experimental results demonstrate the effectiveness of SMILING across various standard control benchmarks.

### Strengths
I appreciate the numerous contributions and the excellent presentation of this paper:

- The idea is an innovative application of score matching techniques to model the state distributions of the policy. Unlike previous approaches that rely on training a discriminator between expert and learner data, the theoretical results demonstrate that the score-based method is more effective and sample-efficient, avoiding issues such as unstable training and mode collapse.
- The presentation is clear and highly informative. I particularly enjoyed the writing in Section 5.1, which intuitively explains why the score-based approach is more expressive than discriminators, especially in the context of linear models. The analysis in Section 5.1 is further validated by the experiments in Section 6.3, which is a great reinforcement of the theoretical insights.
- Across various benchmarks, the method provides a significant improvement over baseline techniques in the experiments, showing strong empirical results.

Overall, the paper's theoretical and experimental results convincingly demonstrate the novelty and effectiveness of the proposed method. This approach could potentially inspire other fields that rely on training discriminators to explore score-based techniques.

### Weaknesses
Although this paper presents promising results, there are three primary weaknesses that should be addressed to some extent. I will consider any responses to these concerns when recalibrating my final score.

- **Time Complexity of Evaluating the Cost Function $c^k(s)$ in Eq.3**:
  - The main concern is the time complexity associated with evaluating the cost function. In the experimental sections, the authors employ a DDPM framework with over 5,000 steps. This implies that evaluating the cost function for a given state requires 5,000 evaluations of the model, which could be prohibitive for more complex scenarios, particularly with higher-dimensional state spaces.
  - If the authors are using a single randomly sampled time step to estimate Eq.3, the variance of this estimation across time should be incorporated into the final theoretical results. However, this issue is not addressed in the current analysis, raising questions about the method's scalability to high-dimensional state spaces.
- **Choice of Data Aggregation**:
  - In Line 3 of the algorithm, the score matching target aims to force $g(s_t, t)$ to model the marginal score of the state distributions from a mixture of policies $\pi^{(1:k-1)}$. However, the paper lacks a clear justification for using this mixture-based approach instead of the more intuitive choice of selecting the prior learned policy $\pi^{k-1}$. While the theoretical results focus on the mixture of policies, it would be valuable to demonstrate the necessity of this choice.
  - Providing more empirical or theoretical results to verify the effectiveness of this data aggregation technique during training would help clarify its benefits. For instance, comparing the proposed approach with a baseline that only uses $\pi^{k-1}$ could offer insights into the significance of data aggregation.
- **Assumption (c) and the Rate of $\epsilon_{RL}$ in Continuous State-Space Settings**:
  - The rate of $\epsilon_{RL}$ should be discussed in more detail, especially considering that score matching is typically applied in continuous spaces. Although some recent algorithms extend score matching to discrete spaces [1, 2], incorporating them into the current framework may not be straightforward.
  - It would be beneficial to discuss how the proposed framework might be adapted or fit into established theoretical results in discrete spaces. This could include exploring potential modifications or providing insights into the limitations of the current approach when dealing with discrete settings.

Addressing these concerns would significantly strengthen the paper by enhancing its scalability, clarifying the choice of data aggregation, and broadening the discussion on the applicability of the proposed framework in various state-space settings.

### Questions
The same with the weaknesses I mentioned above.

### Soundness
3

### Presentation
3

### Contribution
3
