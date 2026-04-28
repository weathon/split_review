# Unsupervised Reinforcement Learning by Maximizing Skill Density Deviation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Unsupervised Reinforcement Learning (RL) aims to discover diverse behaviors that can accelerate the learning of downstream tasks. Previous methods typically focus on entropy-based exploration or empowerment-driven skill learning. However, entropy-based exploration struggles in large-scale state spaces (e.g., images), and empowerment-based methods with Mutual Information (MI) estimations have limitations in state exploration. To address these challenges, we propose a novel skill discovery objective that maximizes the deviation of the state density of one skill from the explored regions of other skills, encouraging inter-skill state diversity similar to the initial MI objective. For state-density estimation, we construct a novel conditional autoencoder with soft modularization for different skill policies in high-dimensional space. To incentivize intra-skill exploration, we formulate an intrinsic reward based on the learned autoencoder that resembles count-based exploration in a compact latent space. Through extensive experiments in challenging state and image-based tasks, we find our method learns meaningful skills and achieves superior performance in various downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an unsupervised reinforcement learning algorithm that maximizes inter-skill state visitation diversity and intra-skill exploration through a clean formulation. It provides solid theoretical analysis as well as good empirical experimental results on the unsupervised reinforcement learning benchmark under both state-based and image-based settings.

### Strengths
1. The presentation and writing of this paper is clear.
2. The proposed inter-skill state deviation and intra-skill exploration objectives are clean, with detailed and solid theoretical analysis.
3. The main experiments, visualization, and ablation studies demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Experiments are not convincing enough.

    The method is mainly tested using standard URLB evaluation protocol, which can be questionable. DDPG is pre-trained with intrinsic rewards. Its value function will mismatch the fine-tuning distribution with extrinsic rewards. Also using "random selection" or "regress-meta" is not convincing enough to show if the agents can truly learn useful skills during pre-training, since the policy and value are *largely re-learned after the reward distribution change*. It couples the RL online sample efficiency with the skill discovery pre-training, which is not a good standalone metric for skill discovery.
    
    Instead, [1] uses a high-level controller that learns to select from **frozen skills** learned from pre-training, and also measures the total state coverage, which is a better metric for exploration and skill discovery during pre-training. [1] also provides more visualizations of the learned skills in broader domains, while this paper only showcased the maze examples. It could be more convincing if this paper could also achieve SoTA using a better metric but not limited to URLB's evaluation.

2. Comparisons are not fair. The proposed method benefits from soft modularization, but the MI-based baselines do not use soft modularization. The performance of the proposed method *without* the soft modularization cVAE should be reported in the main experiments.
3. The method could be sensitive to hyperparameters, e.g. softmax temperature. From Figure 10 (a), it seems the temperature can have a large impact on the performance. Is that true if the temperature is close to 1 (the default choice)? What's the number of modules ($m$) in cVAE?

### Questions
1. Why use PPO for the maze visualization example, while DDPG is used as the main results in URLB?
2. Line 210, of length $l+1$ -> of layer $l+1$ , or of shape $m \times m$? Also softmax temperature is not mentioned in Line 212.
3. In the robustness experiment: "We conduct experiments in noisy domains of URLB by adding noise during pre-training". The noise is added on states, or transitions (states and actions)?
4. The results in Table 2 and Table 3 are partially highlighted, which is confusing.
5. What's the number of modules ($m$) in cVAE?  It's not shown in the appendix, and also ablations on the numbers are needed.

The reviewer is willing to adjust the score if the above questions and concerns are properly addressed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a novel unsupervised reinforcement learning (URL) approach named State Density Deviation of Different Skills (SD3).
SD3 maximizes skill density deviation to make the skill distinguishable and utilizes the KL divergence between the posterior distribution and the prior distribution of the latent variable as the exploration bonus for state coverage. To estimate skill density $d_z^\pi(s) = p(s|z)$, SD3 adopts a routing-network-based conditional variational autoencoder to estimate its lower bound.
SD3 is evaluated against a range of existing URL baselines on both state-and pixel-based URL Benchmark (URLB) to show it effectiveness.

### Strengths
In general, this paper is well-written and easy to follow. The experiments are extensive, involving multiple baseline methods across both state- and pixel-based URL environments. Especially,

**The skill-density perspective of mutual information is interesting.**

As one of the main contributions, SD3 presents a new perspective of mutual information, that is,

$$I(S;Z) = \mathbb{E}\_{z,s} [\log\frac{ p(s|z)}{p(s)}] = \mathbb{E}\_{z,s} [\log\frac{ p(s|z)}{p(s|z)p(z) + \sum\_{z'\neq z}p(s|z')p(z')}].$$

By calling $p(s|z):=d\_z^\pi(s)$ the "skill density", SD3 proposes a soft mutual information as

$$I_{\text{SD3}}(S;Z) = \mathbb{E}\_{z,s} [\log\frac{ {\color{red}\lambda}p(s|z)}{{\color{red}\lambda}p(s|z)p(z) + \sum\_{z'\neq z}p(s|z')p(z')}.$$

**Introducing the routing network to model the skill-conditioned state encoder is novel.**

Introducing the routing network to model the skill-conditioned state encoder is novel for me. However, I have some concerns about the adoption of this architecture, which was originally designed for a multi-task policy network. I will discuss this in the weaknesses part.

### Weaknesses
The paper presents interesting contributions but suffers from several key weaknesses that diminish its impact.

**W1: The motivation for introducing ${\color{red}\lambda}$ in $I_{\text{SD3}}(S;Z)$ is unclear and lacks theoretical grounding.**

While it’s established that $\max I(S; Z) = \max I_{\text{SD3}}(S; Z) = \max H(Z)$, indicating that maximizing mutual information between $S$ and $Z$ implies $H(S|Z) = H(Z|S) = 0$, the purpose of incorporating ${\color{red}\lambda}$ into the optimization objective remains ambiguous. The authors state (Line 145) that “increasing ${\color{red}\lambda}$ will weaken the gradient of SD3, reducing the state densities of other skills and preventing skill collapse in SD3.” However, the link between reducing state densities and preventing skill collapse is not self-evident and warrants further explanation. Specifically, a detailed analysis of how the gradient changes with varying values of $\lambda$ is needed to support this claim. Furthermore, the term 'skill collapse' requires a more precise definition within the context of this work. It is not clear how manipulating the gradient magnitude directly addresses this issue, and a more rigorous justification is required.

**W2: Extending the intra-skill exploration bonus $r_z^{\text{exp}}$ to continuous state spaces is problematic.**

With $r(h)$ set as a standard Gaussian $\mathcal{N}(\textbf{0}; \textbf{1})$ (Line 244), $r_z^{\text{exp}} = D_{\text{KL}}[Q(h|s,z) || r(h)]$ represents the KL divergence between Gaussian distributions since $h = \mu(s,z) + \sigma(s,z) * \epsilon$ is a Gaussian distribution (Appendix B.2, Line 1059). This allows for an analytic expression of $r_z^{\text{exp}}$:

$$
r_z^{\text{exp}} = \frac{1}{2} \{\mu^{T}\mu + \text{tr}\{\sigma\} - k - \log|\sigma|\}.
$$

However, this form of $r_z^{\text{exp}}$ lacks a clear connection to state novelty or surprise, a critical component of exploration. Established methods encourage exploration by approximating state novelty with pseudo-counts $r \approx 1/p(s)$ or information content $r \approx -\log p(s)$. In contrast, $r_z^{\text{exp}} = D_{\text{KL}}[Q(h|s,z) || r(h)]$ does not exhibit such properties, making it unclear how it incentivizes novel state visits. Although Theorem 3.2 implies that $r_z^{\text{exp}}$ resembles a count-based exploration bonus in tabular MDPs, its role in continuous cases requires further clarification. Since all the experiments are carried out in continuous cases, providing the analysis only in simple tabular cases is not convincing. The components of the KL divergence, namely $\mu^T\mu$, $tr(\sigma)$, and $-\log|\sigma|$, need to be individually analyzed in the context of novel state visits to justify their use as an exploration bonus. It is not immediately clear how these terms relate to the frequency of state visitation or the uncertainty associated with novel states.

By the way, there is a typo on Line 238, where $D_{\text{KL}}[Q(h|s,z) || P(h)]$ should be referenced as the upper bound of $I(S; H|Z) = D_{\text{KL}}[Q(h|s,z) || P(h|z)]$.

**W3: Lack of a detailed description of the routing-based CVAE’s critical module.**

Although Figure 1 outlines the high-level architecture, a detailed description of the core module in the routing-based CVAE would enhance clarity. This additional explanation would help convey the structural intricacies that underpin the architecture. Specifically, the number of layers, the activation functions used, and the specific routing mechanism within the CVAE need to be clearly described. Without these details, it is difficult to assess the complexity and effectiveness of the proposed architecture.

**W4: Experiments in the Maze environment are misleading.**

The Maze environment is primarily a visualization tool for 2D skills, yet SD3 only uses CIC as a baseline here. Given that SOTA methods such as BeCL and CeSD outperform SD3 in this setting, omitting these baselines could mislead readers about SD3's comparative performance. BeCL’s results in Figure 4, comparable to CIC in state-based URLB, further highlight the need for a fairer baseline selection. The argument that the maze environment's limited spatial extent constrains the visual insights is not convincing. It is the authors' responsibility to design an appropriately complex maze environment to evaluate SD3 and CeSD instead of simply avoiding mentioning CeSD. The current experimental setup does not provide a comprehensive evaluation of SD3's performance in a visually interpretable setting.

**W5: Missing SOTA baselines in state-based URLB.**

Although the authors include SMM, DIAYN, ICM, APS, Disagreement, CSD, RND, Metra, ProtoRL, and APT baselines, these approaches are not sufficiently competitive. More recent SOTA methods like MOSS (NeurIPS'22), EUCLID (ICLR'22), and CeSD (ICML'24) should also be considered. Moreover, as demonstrated in the paper, the performance gains of SD3 over CIC—a weaker baseline than MOSS, BeCL, and CeSD—are marginal. Thus, the current baselines in both the Maze and URLB settings fail to support SD3’s effectiveness convincingly. The lack of comparison with these state-of-the-art methods makes it difficult to assess the true contribution of SD3.

**W6: Robustness experiments lack rigor.**

A key claim of SD3 is that $r_z^{\text{exp}}$ offers more robustness than the entropy-based bonus $r = -\log p(s)$. However, as noted in W2, the relationship between $r_z^{\text{exp}}$ and a pseudo-count bonus $r \approx 1/p(s)$ in continuous state spaces remains unclear. Additionally, the robustness evaluation design is unconventional; measuring performance on downstream tasks does not adequately reflect the robustness of the policy network. A more effective approach would involve injecting noise during the fine-tuning phase to assess resilience against adversarial perturbations. This design aligns with robustness assessments in adversarial learning, where robustness-accuracy trade-offs are common. Finally, robustness might also depend on the model’s parameter count, so a parameter comparison between SD3 and CIC is essential for fair comparison. The current robustness evaluation lacks a clear methodology and does not provide sufficient evidence to support the claim of improved robustness.

1. **[MOSS]** Zhao, Lin, Li, Liu, & Huang. *A Mixture Of Surprises for Unsupervised Reinforcement Learning.* NeurIPS, 2023.
2. **[CeSD]** Bai, Yang, Zhang, Xu, Chen, Xiao, & Li. *Constrained Ensemble Exploration for Unsupervised Skill Discovery.* ICML, 2024.

### Questions
Please see the weakness part for detailed questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes a novel unsupervised reinforcement learning (RL) framework called SD3, aimed at improving skill discovery by maximizing state density deviation across skills. Unlike traditional entropy-based or Mutual Information (MI) techniques that often struggle in large state spaces, SD3 uses a conditional autoencoder with soft modularization to estimate skill-specific state densities, enabling robust and scalable skill discovery. It incorporates an intrinsic reward resembling count-based exploration in a latent space to encourage inter-skill diversity and intra-skill exploration. Extensive experiments demonstrate that SD3 yields diverse, meaningful skills significantly enhancing performance across various downstream tasks.

### Strengths
1. The paper is well-written and effectively compares the proposed method with baselines, providing a thorough analysis that includes detailed mathematical proofs.
2. The paper employs soft modularization for better estimation of the state density across all skills, which is known to be challenging to estimate.
3. The paper performs ablation studies to assess the influence of various design choices made in this research.

### Weaknesses
1. The exploration reward represented by the KL term does not guarantee that it always reaches the ‘outer’ region (i.e., frontier states) of ‘all’ skills, implying it may not serve as an optimal reward for exploration. Additionally, since the CVAE encoder is trained simultaneously with RL, this effect could be even more pronounced. Specifically, the KL divergence might plateau as the CVAE learns to reconstruct frequently visited states, thus reducing the incentive to explore novel regions within each skill's state space. This could lead to the agent getting stuck in local optima, especially in environments with sparse rewards or complex state spaces.
2. Choreographer[1] uses VAE and a KL term reward for exploration. While they use a world model for skill learning, it is quite similar to the proposed method. The authors should compare and explain the differences. The core similarity lies in the use of a VAE to learn a latent representation of the state space and the use of KL divergence to encourage exploration. A detailed comparison should highlight how the proposed method's soft modularization and density deviation maximization differ from Choreographer's approach, particularly in how these differences affect skill discovery and exploration.
3. The overall algorithm is limited to a discrete skill space due to the architectural design of soft modularization. This limitation restricts the potential for discovering a richer set of skills, as the method cannot inherently handle continuous skill spaces. This is a significant constraint, especially when compared to methods that can learn a continuous skill manifold, potentially leading to a more nuanced and diverse set of behaviors.
4. Minor Comment: The visualization of soft modularization in Figure(1)-a could be improved to make it more intuitive and easier to understand at a glance.

### Questions
1. In the state-based URLB experiments (Figure 4), I have some questions regarding the comparison with baselines:
    1. When the baseline algorithm allows for both continuous and discrete skill spaces, which one did you choose?
    2. How did you determine the dimensionality of the skill space?
    3. Additionally, did you perform fine-tuning over all skills or did you select a specific skill $z^*$ that performed best on the downstream task before fine-tuning?
    
    For instance, in the case of METRA[1], both discrete and continuous skills are possible, and it's also possible to obtain $z^*$ in a zero-shot manner. I’m curious if this was taken into consideration.
    
2. I'm curious why BECL[2] was not included in the comparison for the tree-like maze in Figure 6. According to the BECL report, it appears to explore a broad region in the same tree-like maze and shows competitive skill distinguishability. Given that BECL also optimizes skill distinguishability using a contrastive style while considering exploration, it seems appropriate to include it in the comparison.


[1] Park, Seohong, Oleh Rybkin, and Sergey Levine. "Metra: Scalable unsupervised rl with metric-aware abstraction." arXiv preprint arXiv:2310.08887 (2023).

[2] Yang, Rushuai, et al. "Behavior contrastive learning for unsupervised skill discovery." International Conference on Machine Learning. PMLR, 2023.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of discovering meaningful skills in large-scale spaces. The authors propose a novel skill discovery objective that maximizes state density deviation for each skill, introducing a CVAE with soft modularization. Additionally, to promote intra-skill exploration, they provide an intrinsic reward with theoretical proof in tabular MDP settings.

### Strengths
- The overall framework architecture, which incorporates a soft modularization technique to maximize state-density deviation in skill discovery for large-scale observations, is novel.
- The authors propose effective solutions to address both inter-skill state diversity and intra-skill exploration.
- The authors conduct comprehensive experiments across various algorithms and environments, including both state-based and pixel-based observations.
- Ablation studies further highlight the design choices of SD3.

### Weaknesses
 - It would be beneficial for the authors to visualize the activations of different networks for various skills, especially in state-based observations. In such environments, SD3 may potentially use similar networks for different skills, as the observation spaces are relatively low-dimensional. 
- It would be beneficial for the authors to visualize skill discovery in SD3 for both state-based and pixel-based environments, as shown on the left side of Figure 2. Specifically, it is unclear how the learned skills manifest in the state space, and visualizing the trajectories or state distributions associated with each skill would be highly informative.
- Is the same network size used for both SD3 and the baseline algorithms? I wonder if SD3, which utilizes soft modularization with a CVAE architecture, requires a larger network size. If so, the authors should provide additional experiments using the same network parameters for the baselines. Furthermore, the computational overhead of the soft modularization technique should be discussed, as it introduces additional routing networks and multiple modules, which may increase the training time and memory consumption.

### Questions
- The authors should specify which environments were used for each experiment. Were the robustness and ablation experiments conducted under pixel-based observation settings?
- SD3 considers a discrete skill space Z, and the number of skills is a hayperparameter. Is this setting identical for all other algorithms? 
- I am willing to increase my score, if the authors address the questions above.

### Soundness
3

### Presentation
3

### Contribution
3
