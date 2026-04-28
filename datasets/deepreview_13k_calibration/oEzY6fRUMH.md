# State Chrono Representation for Enhancing Generalization in Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 8, 3

## Abstract
In reinforcement learning with image-based inputs, it is crucial to establish a robust and generalizable state representation. Recent advancements in metric learning, such as deep bisimulation metric approaches, have shown promising results in learning structured low-dimensional representation space from pixel observations, where the distance between states is measured based on task-relevant features. However, these approaches face challenges in demanding generalization tasks and scenarios with non-informative rewards. This is because they fail to capture sufficient long-term information in the learned representations. To address these challenges, we propose a novel State Chrono Representation (\methodname/) approach. \methodname/ augments state metric-based representations by incorporating extensive temporal information into the update step of bisimulation metric learning. It learns state distances within a temporal framework that considers both future dynamics and cumulative rewards over current and long-term future states. Our learning strategy effectively incorporates future behavioral information into the representation space without introducing a significant number of additional parameters for modeling dynamics. Extensive experiments conducted in DeepMind Control and Meta-World environments demonstrate that \methodname/ achieves better performance comparing to other recent metric-based methods in demanding generalization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a set of losses for effectively learning representations for efficient downstream RL.

### Strengths
- This paper studies an interesting problem of learning effective representations for reinforcement learning
- This paper proposes a variety of different losses for temporal representation learning

### Weaknesses
 - The writing seems to be overly grandiose, for instance in the conclusion "Our novel metric-based framework, State Chrono
Representation (SCR), emerges as a beacon in this realm, drawing on the temporal essence of RL.".

- Several of the theorems in the paper aren't theorem but definitions -- the authors should rename the statements as such

- The writing of the theorems are not fully clear -- for instance, in Thererom 1, A is never defined

- The different losses proposed in the paper appear to be a bit ad-hoc to me -- more justification on the precise forms used would be helpful

- The results in the paper are not convincing, many of the confidence intervals overlap with each other

- The evaluation in the paper seems limited, it is only evaluated on different variations of Mujoco -- it would be good to provide other results in domains such as RL-Bench, Minecraft, Antmaze etc...

### Questions
1) Can the author elaborate in the related work how this differs from prior works in the representation learning space?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method, the State Chrono Representation (SCR), integrating long-term information alongside the bisimulation metric learning.
They tackle with the problem of a robust and generalizable state representation, especially the issue of long-term behaviors within their representations. 
The deep bisimulation metric approaches transforms states into structured representation spaces, allowing the measurement of distances based on task-relevant. However, in sparse rewards scenarios, due to its one-step update approach the generalized state issue still remains.
Capturing long-term behaviors within their representations are expected.
To solve this problem, they SCR approach, integrating long-term information alongside the bisimulation metric.
They showed that SCR has comparable results with the augmentation method DrQ and the state-of-the-art behavioral metric approach SimSR.

### Strengths
As the authors point out, capturing long-term behaviors is a key issue in RL.
To fuse temporal relevance to metric learning is a straight forward and interesting approach. 
SCR shows better performance in some cases than SOTA methods about sample-efficiency and generalization with corresponding experiments.
They also clarify the contribution of each component by removing some components of SCR that clarify the detailed analysis and contributions of SCR.

### Weaknesses
Performance comparisons vary depend on tasks.
Some are better and some are worse.
Analysis of are limited and the insights into reasons for those better and worse performances are not enough to support their claims.

### Questions
The main issue of the paper is to solve the problem of long-term behaviors within their representations. 
Experimental analysis are only from the viewpoint of sample efficiency and generalization, but few analysis about the long-term behaviors. With additional analysis from the long-term behavior  views would support the authors' claims more.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new representation learning approach that can be seamlessly integrated with any reinforcement learning algorithm. Central to this method is the enhancement of traditional bisimulation/MICo metrics [0].  
The authors innovatively incorporate long-term information into the representation. This is achieved by applying a form of MICo distance on the joint embeddings of the representations of both the initial and terminal states of sub-trajectory pairs.   
Additionally, they introduce a *temporal measurement* which quantifies the difference in values between these states, further enriching the long-term information within the representations.  
Unlike conventional bisimulation or MICo metrics that predominantly capture immediate one-step relations and often overlook long-term dynamics, these added objectives ensure a holistic capture of both immediate and long-term behaviors.   
Empirical validations demonstrate the method's efficacy, as it showcases robust performance in learning optimal policies on the dm-control suite benchmark. Moreover, the approach demonstrates impressive generalization abilities in test scenarios with distracting elements.

[0] MICo: Improved representations via sampling-based state similarity for Markov decision processes
Pablo Samuel et al. Neurips 2021

### Strengths
The paper is clearly written, making it relatively easy to follow for readers.  
The authors provide a sound motivation behind each component of the method they introduce.  
They offer a modified distance for the MICo metric, which simplifies its implementation and could improve its numerical stability.  
An ablation study is included, highlighting the effects of individual components of the method.  
Notably, the method demonstrates good performance and an ability to handle distracting factors, even though it doesn't have explicit mechanisms to counteract these distractions.

### Weaknesses
Certain concepts introduced in the paper, specifically the Łukaszyk-Karmowski distance and the Interval Quasimetric Embedding, would benefit from further elucidation for clarity. The description of the Łukaszyk-Karmowski distance lacks specifics on how the probability density functions $f(x)$ and $g(y)$ are estimated in practice, which is crucial for its practical implementation. Similarly, the explanation of the Interval Quasimetric Embedding (IQE) is high-level, and it would be beneficial to detail how the vector segments are chosen and how the 'max' and 'mean' operations are precisely applied across the component distances. On the implementation front, several pertinent details are lacking, which could hinder attempts at reproducing the method faithfully. For instance, in computing the *chrono embeddings* $\psi(x_i, x_j)$, the method doesn't specify how the number of steps between $i$ and $j$ are determined. Given the potential significance of this hyper-parameter on the chronological behavioral metric, addressing its determination and providing further discussion would have added depth to the paper.

Additionally, the role and necessity of the encoder $\phi$ EMA parameter isn't evident. While one might speculate it's used for targets in $L_\phi$ and $L_\psi$​, explicit clarification is absent. It is unclear whether this parameter is used to compute the targets for the loss functions or if it serves a different purpose. The lack of clarity on this point makes it difficult to fully understand the training procedure.

A major concern revolves around the method's adaptability to various RL environments. The paper describes chrono embeddings based on MICo metrics over trajectory pairs, suitable for capturing long-range similarities in deterministic settings, such as the DM-control environments. However, its behavior in stochastic environments remains questionable. For example, in games like Mario, two visually identical states from separate levels might seem alike using bisimulation metrics, but the proposed chronological behavioral metric could consider them as vastly dissimilar due to the ensuing trajectory differences. This raises concerns about the robustness of the method in environments with high stochasticity or partial observability. The inclusion of experimental validation on varied environments, such as procgen, would further enhance the paper by addressing these concerns comprehensively.

**Minor issues observed:**

*    In Theorem 2, the end of the equation should reference $d(x',y')$ rather than $d(x,y)$.
*    There seems to be inconsistency with terminologies, as the DBC is mentioned between definitions 3.1 and 3.2 without prior introduction.
*    Theorem 5 should align with the subsequent explanation by utilizing $d^{\pi}_\phi$.
*    A typo is present post equation 4 with "TThe encoder..."
*    In Figure 5, the left figure's legend incorrectly labels two types as CR, when one should be SCR.

### Questions
* Can the authors discuss about the impact of the number of steps between $i$ and $j$ when computing the *chrono embeddings*
* Are the gradient stopped for computing the targets used in $L_\phi$ and $L_\psi$​ or are they computed with a target encoder?
* Could the authors measure the impact of the introduced diffused metric on MICo for exemple in the ablation study.
It would help to assess its individual contribution.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method to learn state representation based on bisimulation-like measurement for deep reinforcement learning. The whole model consists of three modules: i) a bisimulation-based module to capture behavior differences between states, which includes a novel diffuse metric; ii) a chronological embedding module to capture long-term temporal information; and iii) a temporal measurement module to capture discounted cumulative reward of sub-trajectories. The empirical results show their performance improvements over the previous representation approaches, not only in default settings but also in more challenging distractor settings.

### Strengths
This paper is easy to follow. The authors provide experimental evidence to support the performance improvement of the proposed method on different variations of DeepMind Control Suite.

### Weaknesses
Many of the statements and explanations in this article seem to be questionable, which consequently lead to a decrease in the overall soundness of the paper. I will now enumerate some of these problems:

1. In the fourth paragraph of the introduction section, "*behavioral metrics only capture immediate, one-step information, neglecting the broader long-term context*". However, behavioral metrics consider both immediate rewards and long-term behavioral differences, instead of only capturing one-step information. This is the reason why bisimulation was initially chosen to learn state representations. The poor performance of behavioral metrics in sparse environments is not due to a lack of consideration of long-term information but rather because the supervision signal provided by rewards is too limited in sparse reward settings, which makes updates challenging. This issue is similar to the value iteration in sparse reward environments.

2. In the paragraph after Definition 3.1, "*SimSR utilizes the cosine distance, derived from the cosine similarity, albeit
without fulfilling the triangle inequality and the non-zero self-distance*". In fact, cosine distance is indeed zero self-distance as the fact that $d(u, u) = 0$.

3. In the first sentence of Section 3.1.1, "*The loss $L_\phi(\phi)$ in Equation 2 leans heavily on a one-step update mechanism*". It should be referred to as **temporal-difference update mechanism** rather than a **one-step update mechanism**.

4. The proof for Theorem 5 appears somewhat ambiguous. Indeed, if we assume that $x_j$ and $y_j'$ are fixed states, then this proof seems to be reasonable. However, upon the algorithm in Appendix A.2.4, it appears that neither of these states is actually fixed. Consequently, the proof for Theorem 5 is entirely different from that of Theorem 3. One potential solution could be to see the combination of $x_i$ and $x_j$ as one auxiliary state and the combination of $y_i' $and $y_j'$ as another auxiliary state, then iterate the bisimulation operator in the auxiliary state space. However, in this setting, the mapping from the state space to the auxiliary state space would be dimensionality-increasing, which is contrary to our intended goal. Therefore, I'm somewhat uncertain about the validity of this theorem.

5. Equation 9 also seems to be strange. $m$ should represent the cumulative rewards under the optimal policy. However, on the right-hand-side of Equation 9, the policy associated with $d$ is somewhat unclear or uncertain. i) If it is the current policy during the optimization, then it could possibly be zero initially. In extreme cases where the initial value of $m$ is the same and sufficiently large for all state pairs, it's possible that, under the conditions of Equation 9, Equation 8 could be consistently equal to 0, leading to a situation where $m$ does not get updated. ii) If the policy on the right-hand-side of Equation 9 is the optimal policy, then as the optimal policy is unknown, we also cannot obtain the corresponding $d^{π^*}$. In such cases, Equation 10 would indeed not hold.

6. I would like to recommend that the authors include a performance curve to illustrate the trend. Furthermore, providing the code would enhance the soundness of the paper.

Minor issue:

1. Legend in Figure 5:  "CR" -> "SCR"

2. Figure 6 -> Table 3

### Questions
1. What is the future state? How can we sample it? Is it randomly selected from uniform distribution or what?

2. In the Experiment section, does the "*500K step*" refer to environment steps or gradient steps?

3. How does it perform if we only use $\mathcal{L}_\phi(\phi)$?

4. How many random seeds are used in Table 2 and Figure 6?

5. What was the experimental setup for distraction settings? Are the training environment and the evaluating environment the same or different?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
