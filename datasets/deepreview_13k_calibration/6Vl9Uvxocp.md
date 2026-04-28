# Evolution guided generative flow networks

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
\acrfull{gfn} are a family of probabilistic generative models that learn to sample compositional objects proportional to their rewards. One big challenge of \acrshort{gfn} is training them effectively when dealing with long time horizons and sparse rewards. To address this, we propose \acrfull{egfn}, a simple but powerful augmentation to the \acrshort{gfn} training using \acrfull{ea}. Our method can work on top of any \acrshort{gfn} training objective, by training a set of agent parameters using \acrshort{ea}, storing the resulting trajectories in the prioritized replay buffer, and training the GFlowNets agent using the stored trajectories. We present a thorough investigation over a wide range of toy and real-world benchmark tasks showing the effectiveness of our method in handling long trajectories and sparse rewards.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes using an Evolutionary Algorithm to fill a Prioritized Replay Buffer with (more) diverse trajectories to enhance the training process of Generative Flow Networks.

### Strengths
Overall, the proposed approach is well-explained and illustrated. The paper provides various empirical results in a simple exemplary task, as well as molecule generation tasks, to demonstrate real-world applicability.  For a fair comparison, it provides various baselines and ablations. The empirical results show improved performance, particularly in sparse reward scenarios and large state spaces. Furthermore, the authors provide a discussion on potential limitations and provide reasoning for the advantages of the proposed approach based on an intuitive empirical analysis

### Weaknesses
Regarding the proposed method, the EA does not seem to influence the actual training process beyond providing diverse experiences to be sampled. In that regard, an evaluation comparing the performance of the population to the star agent to validate the assumptions would have been helpful. Also, in addition to the provided baseline comparison, I am missing a comparison based on the number of evaluated trajectories to assess the sample complexity advantages of the proposed approach. While improving in sparse scenarios, the proposed approach seems to perform slightly worse in the more generic tasks despite being computationally more intense. Regarding the baselines used, especially GAFN and MARS, I am missing a short introduction, explanation, or comparison. Also, the sparsity levels shown in Fig. 4 should be elaborated more concretely. Regarding the presentation, the overall writing might be slightly improved, e.g., regarding grammar. 

Minor comments:

- p.3 l.109f.: abbreviations FM, DB, and TB should be introduced first. 
- Alg. 1, l.181: P^*_F should be P_F? Alternatively, the reason the star agent is used to evaluate the population should be elaborated on.
- Alg. 1 l.182f.: vars for online and offline trajectories should differ

### Questions
What is the computational overhead of maintaining a whole population of GFN agents that must be evaluated in addition? 

Why not train all agents in the population or train the best agent(s) in the population instead of maintaining a separate star agent?

How do the authors ensure a fair comparison to the provided baseline regarding the number of evaluated trajectories?  (And how is the PRB filled for the baselines?)

Regarding the ablation EGFN-PRB-mutation, how is the EA connected with the training of the star agent?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Evolution guided generative flow networks (EGFN), a new algorithm equipped with an evolutionary algorithm (EA) for better generative flow network (GFN) training. EGFN collects diverse and high-reward samples using a population of GFNs that evolves throughout the training procedure. The collected samples are then utilized to train a target *star* GFN agent in an off-policy manner. EGFN showed faster learning capability in one synthetic and three biochemical tasks, especially when the reward signal is sparse.

### Strengths
1. The idea of using Evolutionary algorithm that evolves a population of GFlowNets is new, though similar approaches have already been introduced in reinforcement learning to enhance exploration [1, 2].
2. The proposed algorithm is validated through various experiments, including real-world biochemical tasks. I also enjoyed their analysis of why the proposed algorithm works (section 5).

[1] Salimans, Tim, et al. "Evolution strategies as a scalable alternative to reinforcement learning." arXiv:1703.03864 (2017).  
[2] Khadka, Shauharda, and Kagan Tumer. "Evolution-guided policy gradient in reinforcement learning." NeurIPS (2018).

### Weaknesses
1. In its current form, the paper contains several ambiguous or incorrect claims in Section 2.1. Here are some key issues I noticed:
  1-1. **Lines 93 - 102**: The DAG structure should be defined first to clearly specify the action space according to the DAG’s edges. Additionally, the phrase “sample proportionally to different peaks of reward” in line 101 (and line 34) is misleading. The description of the DAG structure lacks sufficient detail, particularly regarding how the edges are determined and how they relate to the action space. A more rigorous definition is needed to avoid ambiguity. The claim about sampling proportionally to different reward peaks is also problematic, as it does not clearly articulate how this proportionality is achieved within the GFN framework, and it risks misrepresenting the underlying sampling mechanism.
  1-2. **Line 112**: The notation $F(\tau)$ has never been defined but is used to define $F(s)$.
  1-3. **Line 118**: There’s an incorrect use of the prime ( ` ) symbol. Moreover, the equation $P_F(s' | s, \theta) = F(s \to s')$ is inaccurate. The RHS should be divided by $F(s)$. A similar issue appears in **lines 124-125**. The use of the prime symbol is indeed incorrect, and the equation for the forward policy is improperly defined, lacking the necessary normalization by the flow of the current state. This misrepresentation of the forward policy undermines the theoretical foundation of the method.
  1-4. **Line 133**: The expression $\sum_x R(x) = \sum_{s:s_0 \to s\in \tau \forall \tau \in \mathcal{T}} P_F(s|s_0;\theta)$ needs more explanation. At first glance, it doesn’t seem to hold generally. The equation relating the sum of rewards to the sum of probabilities over all trajectories is not clearly justified and seems unlikely to hold in general. A more thorough explanation and justification of this equation is required.

2. I’m unclear on why EGFN improves credit assignments. The star agent in the EGFN framework uses conventional learning objectives like DB or TB, and I couldn’t find any specific design element that enhances credit assignment. From what I understand, EGFN’s main advantage is its evolving population of GFNs, which provides more diverse experiences for the star agent to learn from. This should enhance exploration, which is especially beneficial in sparse environments. The core mechanism of EGFN seems to revolve around enhanced exploration through a diverse population of GFNs, rather than a fundamental improvement in credit assignment. The use of standard learning objectives for the star agent further suggests that any credit assignment improvements are likely a byproduct of better exploration rather than a direct algorithmic enhancement.

3. I have some concerns about the experiments:
  3-1. Experiment Setup (Reward Calls): Were all algorithms given the same number of reward calls? All learning progress figures use training steps as the x-axis, but I suspect EGFN might use additional reward calls per training step due to the rewards needed for fitness calculation (line 173). However, in real-world applications where reward evaluation is costly (e.g., in vitro experiments), sample efficiency is often more critical than learning efficiency [3, 4]. Therefore, I recommend including results with a fixed number of reward calls, especially for biochemical sequence generation tasks. The comparison based on training steps is potentially misleading if EGFN uses more reward calls per step. In real-world applications, sample efficiency is paramount, and a comparison based on a fixed number of reward calls would provide a more accurate assessment of the practical value of the method.
  3-2. **(minor) Line 304 and 898**: The paper states the number of modes for the hypergrid task is $2^D$, but this doesn’t seem correct. There are indeed $2^D$ reward “regions” if a region is defined as a collection of adjacent modes. However, the actual number of modes could be $2^D \times M$, where $M$ represents the number of modes in each region, potentially increasing with $H$.

4. (minor) The reference is outdated and not well organized. Some of them, but not limited to, are: in line 663, Pan et al. 2023a was accepted by ICML 2023, and in line 728, Zhang et al. 2023b was accepted by TMLR. Also, there are two references for "Generative augmented flow networks."

### Questions
1. How many reward calls are used per training step for EGFN and each baseline?
2. The biochemical tasks appear to share many similarities. Is there a specific reason for dividing them into three sections (4.2, 4.3, and 4.4)?
3. In lines 254-259, two prioritization methods are introduced: proportional sampling and percentile-based heuristics. Which one is actually used in the experiments?
4. I suspect that memory consumption increases linearly in $K$ (the population size). Is this true?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a variant of GFlowNets which is trained via evolutionary optimization. The key argument is that GFlowNets are a generative process which are learned via a reward signal, however the propagation of this reward throughout the time horizon is tricky. The paper proposes the use of classical evolutionary techniques to alleviate these issues. A population of networks are maintained, then selection + crossover + mutation are performed over the parameters during the evolutionary step. The evolutionary step is interleaved with traditional gradient descent.

### Strengths
The idea to apply evolutionary algorithms to GFlowNets is a new direction. Bootstrap-based methods such as GFlowNets often suffer from collapse or poor gradient flow, thus motivation evolutionary algorithms as a potential solution. The proposed method is simple, and outperforms previous methods on synthetic tasks. The proposed method consistently outperforms other GFLowNet settings, and discovers more modes of a solution.

### Weaknesses
The method introduces additional complexity in the form of the evolutionary optimization, but does not analyze why such a decision would improve performance. The evolutionary algorithms applied are well-known, and the combined algorithm boils down to an ad-hoc fitting of EA and gradient descent sequentially. The added complexity results in slower training speed, as mentioned in the paper. This paper would strongly benefit from a more principled look at the training dynamics of GFlowNets, and a stronger opinion on *why* evolutionary algorithms help learning. Given the smaller-scale nature of the tasks considered, this is a reasonable desire. The authors do not provide sufficient justification for the specific choice of evolutionary algorithm, nor do they explore the sensitivity of the method to different EA hyperparameters, such as population size, mutation rate, and crossover strategy. The lack of ablation studies on these parameters makes it difficult to assess the robustness of the proposed approach and understand the contribution of each component. Furthermore, the paper does not address the potential for the evolutionary algorithm to introduce instability or oscillations in the training process, which could be a concern when interleaving it with gradient descent.

### Questions
- Can GFlowNets be applied to more traditional generative modelling tasks? (e.g. images, etc). 
- In Figure 4, it would help to clear up which of the labelled methods are RL, MCMC, or GFlowNet variants.
- In page 2 paragraph 2, it would be good to re-clarify what TB stands for, and introduce these prior objectives together.
- How are neural network weights mixed in the crossover step? Is this an important detail, or is a naive strategy good enough?

### Soundness
2

### Presentation
3

### Contribution
2
