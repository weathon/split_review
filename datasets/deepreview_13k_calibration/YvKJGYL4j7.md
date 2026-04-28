# Toward Efficient Multi-Agent Exploration With Trajectory Entropy Maximization

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 8, 6, 3

## Abstract
Recent works have increasingly focused on learning decentralized policies for agents as a solution to the scalability challenges in Multi-Agent Reinforcement Learning (MARL), where agents typically share the parameters of a policy network to make action decisions. However, this parameter sharing can impede efficient exploration, as it may lead to similar behaviors among agents. Different from previous mutual information-based methods that promote multi-agent diversity, we introduce a novel multi-agent exploration method called Trajectory Entropy Exploration (TEE). Our method employs a particle-based entropy estimator to maximize the entropy of different agents' trajectories in a contrastive trajectory representation space, resulting in diverse trajectories and efficient exploration. This entropy estimator avoids challenging density modeling and scales effectively in high-dimensional multi-agent settings. We integrate our method with MARL algorithms by deploying an intrinsic reward for each agent to encourage entropy maximization. To validate the effectiveness of our method, we test our method in challenging multi-agent tasks from several MARL benchmarks. The results demonstrate that our method consistently outperforms existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Trajectory Entropy Exploration (TEE), a multi-agent exploration method that maximizes the entropy of different agent's trajectories in a contrastive trajectory representation space. Prior approaches that incentivize exploration by maximizing the mutual information between the agents' identities and their trajectories can lead to insufficient exploration, where each agent revisits familiar trajectories. In contrast, TEE trains a trajectory representation using *contrastive learning on trajectories and agent identities*, where trajectories from the same agent are pulled closer. This latent representation is then used in a *particle-based entropy estimator*, which estimates the entropy by averaging the distance of each particle to its top $k$ nearest neighbors in the representation space. The proposed method is instantiated with the QMIX algorithm, where an additional $Q$-value for the entropy rewards is learned and added to the standard $Q$-value. TEE exhibits strong empirical results across a suite of MARL environments including Pac-Men, SMAC, and SMAC 2, outperforming baselines in exploration and sample efficiency. The design choices in TEE are thoroughly validated via exhaustive ablation studies.

### Strengths
1. The paper is motivated by carefully analyzing existing multi-agent exploration methods and identifying a potential degeneracy in those methods, i.e., that maximizing the mutual information between agent identities and trajectories can lead to insufficient exploration. The proposed method -- maximizing the entropy of the mixture of trajectories while being informative about agent identities -- is a convincing solution. 
2. TEE demonstrates strong empirical results on a suite of challenging multi-agent RL environments, significantly outperforming standard MARL and MI-based exploration methods. Figure 2 in particular shows that TEE fully explores all four rooms in the Pac-Men environment whereas Q-MIX only explores two of the four rooms. Figure 5 further shows that TEE explores the map in SMAC more thoroughly than MI-based exploration methods. These lend support to the effectiveness of the exploration method.
3. The design choices in TEE are backed by thorough ablation studies in Section 4.3, Figure 6, and Table 1. The authors show the importance of parameterizing the trajectory encoder using an autoregressive model, learning the agent identities instead of fixing to one-hot, and so on.

### Weaknesses
1. The proposed method relies on a nonparametric entropy estimation that introduces additional hyperparameters, e.g. the number of neighbors $k$. This procedure also introduces additional computational overhead, since it needs to run batch KNN in each training step.
2. Some design choices of the method are not straightforward. See questions 1, 2, and 3 below.
2. The presentation of the paper can be improved. Some paragraphs are too dense (e.g. Section 4.3) and figures need more informative captions.

### Questions
1. If the limitation of methods maximizing the mutual information between trajectories and agent identities is insufficient exploration, why can't we add a max entropy term to each agent's objective, so that they explore as much as possible while being distinguishable from each other? Are there related works that do this?
2. The autoregressive trajectory encoder is trained on trajectories but only applied to a single state when estimating the particle-based entropy (according to Algorithm 1). So in principle one only needs a state encoder. Why do you train a trajectory encoder when it's only applied to states?
3. What happens if you replace the L2 distance in the entropy estimator with negative cosine similarity? Since the encoder is trained with contrastive loss, cosine sim seems a more natural metric in the latent space. 
4. In scenarios requiring homogeneous behavior (Appendix. F), do you need to tune the coefficient $\beta$ of the entropy loss?
5. Section 3.1 on learning contrastive trajectory representations is disconnected from Sections 3.2 and 3.3 on the particle-based entropy estimator and its integration with MARL algorithms. I suggest adding a paragraph in Sec. 3.3 stating that the representation is learned jointly with the policy, to provide a more complete picture.
6. I would also suggest adding a more detailed description of TEE in the caption of Figure 1 to make it self-contained.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel multi-agent exploration method, Trajectory Entropy Exploration (TEE), to address the issue of homogeneous agent behaviors resulting from parameter sharing. TEE leverages contrastive learning to encode trajectories and identities into distinguishable embeddings, utilizes a nonparametric particle-based entropy estimator to calculate intrinsic rewards, and integrates seamlessly with existing MARL algorithms such as QMIX and MAPPO. Experiments on the Pac-Men, SMAC, and SMACv2 benchmarks demonstrate its superior effectiveness.

### Strengths
- The paper is well-motivated and clearly presented. The method effectively combines maximum entropy with contrastive learning to address the diversity challenge in MARL, demonstrating strong empirical performance.
- The tricks used are both practical and easy to implement, and the authors provide thorough ablation experiments to support their approach.

### Weaknesses
 - Lack challenging MARL tasks that require diversity strategies.

 - Figure 1 is somewhat unclear. Are the agents' policies derived from the utility functions $Q_a$ or from the combined term $Q_a + \beta Q_a^{entropy}$? If it’s the latter, why not directly update $Q_a$ with $r^a + r^_{entropy}$ instead of using a separate intrinsic utility network?

 - Minor items: In Line 184, should $v_a^k$ be written as $\text{v}_a^k$?

### Questions
- As mentioned in the introduction, football games require agents to learn diverse strategies, and Google Research Football is a widely used MARL benchmark. This approach should include additional experiments on this benchmark, similar to the baselines SCDS and FoX.
- I believe it should become a community standard to adopt the evaluation protocol of [Gorsanne et al.](https://arxiv.org/abs/2209.10485) in the multi-agent setting. Not adhering to these standard practices, in my view, weakens what could otherwise be a compelling case for the effectiveness of these algorithms.
- Figure 1 is somewhat unclear. Are the agents' policies derived from the utility functions $Q_a$ or from the combined term $Q_a + \beta Q_a^{entropy}$? If it’s the latter, why not directly update $Q_a$ with $r^a + r^_{entropy}$ instead of using a separate intrinsic utility network?
- Minor items: In Line 184, should $v_a^k$ be written as $\text{v}_a^k$?

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
4

### Summary
TEE promotes agent diversity in multi-agent RL by learning a contrastive trajectory representation and using it to compute a particle-based entropy of the agent trajectories as intrinsic rewards. Combined with QMIX, TEE is evaluated in two multi-agent domains, showing increased diversity and superior empirical performances as a result.

### Strengths
- The writing is overall clear and well-organized despite some small issues, which I will mention in other sections. Figures in this paper are helpful as well, although the authors might want to change some font colors in Figure 1 to make it more readable.
- The method is interesting and novel to my knowledge, addressing issues existing in prior methods under the same topic.
- The experiments in the PacMan environment clearly demonstrate the advantages of promoting agent diversity compared with baselines.
- In SMAC, TEE has significant improvement over baselines in the harder scenes. Even in easier scenes where diversity is not required, TEE still has a small advantage, showing that empirically it can balance the diversity maximization and reward exploitation.
- Overall for empirical evaluations, there are a variaty of baselines and ablations, providing sufficient information about the proposed method.

### Weaknesses
 - I appreciate the theoretical analysis of why mutual information-based methods can have insufficient exploration in the appendix, but it would be more helpful if the authors could include some insights of the analysis into the main text.
- I would like to hear more explanation on why using $Q_a(o_t^a,u_t^a)$ as an input of $Q^{entropy}_a$ can lead to trajectory entropy maximization. This is not straightforward to me. Yes, there will be a gradient passed to $Q_a(o_t^a,u_t^a)$, but why can this gradient make $Q_a$ assign higher values to actions that have higher trajectory entropies?
- TEE is evaluated in two domains, PacMan and SMAC. PacMan to me is more of a demonstrative domain, where behavioral diversity is vital to get the maximum reward. As such, the diversity in evaluated domains feels a bit lacking.
- In the evaluations, TEE is only combined with QMIX. I'm wondering why it's not tested with other MARL algorithms as QMIX is one of the less intuitive one to combine with.

Minor writing issues:
- Using same characters for encoder $g_{\theta_e}$ and $g_{\theta_g}$ is confusing. It feels like two same networks with different parameters.
- L184 the $v$ in $v_a^k$ is italic.
- L248 you state that $Q^{entropy}_{a}$ is "shared". Why does it still have a subscript $a$?

### Questions
See other sections.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to enhance exploration in MARL by maximizing trajectory entropy (TEE). The authors propose encoding trajectories into low-dimensional vector representations through contrastive learning, calculating particle-based entropy on these representations, and maximizing it as an intrinsic reward. This method is incorporated into the QMIX algorithm and tested in grid-world and SMAC/SMAC-v2 environments, with experimental results indicating that TEE outperforms other QMIX-based exploration techniques.

Although the paper is well-structured with a coherent logic flow, I have concerns regarding its unclear motivation and potentially problematic experimental results. It shares a common shortcoming with MARL research from a few years ago. I recommend a rejection.

### Strengths
* The paper is well-written with a logical flow.

* The authors include an extensive set of experimental baselines; however, some important baselines are missing, as I elaborate in the next section.

### Weaknesses
 * **Policy-Gradient-Based Algorithms**. This paper does not address any policy-gradient-based (PG) MARL algorithms, raising two issues. First, it's unclear whether insufficient exploration is a significant problem for PG algorithms as well. Could you also include policy gradient algorithms like MAPPO [1] and HAPPO [2] in the Pac-Men experiments? At the very least, these works are relevant and should be cited. Second, policy gradient methods have proven competitive on benchmarks such as SMAC. Even if these algorithms aren't directly compared on the learning curve, their final performance should be used as a baseline so readers can see that your approach advances the MARL field. Omitting them weakens the paper's overall rigor.

[1] The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games, https://arxiv.org/abs/2103.01955

[2] TRUST REGION POLICY OPTIMISATION IN MULTI-AGENT REINFORCEMENT LEARNING, https://arxiv.org/pdf/2109.11251

* **Pac-Men Results Conflict.** Results in the Pac-Men environment appear to conflict with the published CDS paper [3]. The CDS paper shows this environment is solvable with 2 million timesteps, but in your results, it isn't. Please explain this discrepancy in detail. Additionally, while explaining your algorithm's success, you should analyze why baseline methods fail rather than providing vague reasons like "insufficient cooperation". Consider analyzing trajectories in the replay buffer, visualizing the Q-value heatmap, or conducting a more thorough breakdown.

[3] Celebrating Diversity in Shared Multi-Agent Reinforcement Learning, https://arxiv.org/pdf/2106.02195

* **Insufficient Evaluation.** The evaluation approach needs refinement. First, only six maps were selected in the SMAC environment, which raises concerns about potential cherry-picking. Second, Figure 3 shows a significant divergence from the curves in the CDS paper. Although the authors suggest this is due to differences in StarCraft engine versions, it would be best to match the version used in the CDS paper to ensure fair performance comparisons. Third, recent work has introduced more reliable MARL evaluation protocols [4,5], recommending evaluation across multiple domains (e.g., GRF, Melting Pot, SMAC) and reporting IQM scores/curves for each domain. Adopting these standards would improve the reliability of your evaluations.

[4] JaxMARL: Multi-Agent RL Environments in JAX, https://arxiv.org/abs/2311.10090

[5] Towards a Standardised Performance Evaluation Protocol for Cooperative MARL, https://arxiv.org/abs/2209.10485

### Questions
* Is the trajectory representation learned on-the-fly from the replay buffer, or is it pre-trained?

* Can your exploration method be applied to policy-gradient methods?

* Why did you choose QMIX as the base algorithm instead of QPLEX[6], which is more advanced and theoretically general?

[6] QPLEX: Duplex Dueling Multi-Agent Q-Learning, https://arxiv.org/abs/2008.01062

### Soundness
2

### Presentation
3

### Contribution
2
