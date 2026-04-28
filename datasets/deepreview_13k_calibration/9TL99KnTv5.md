# Align Your Intents: Offline Imitation Learning via Optimal Transport

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Offline Reinforcement Learning (RL) addresses the problem of sequential decision-making by learning optimal policy through pre-collected data, without interacting with the environment.
As yet, it has remained somewhat impractical, because one rarely knows the reward explicitly and it is hard to distill it retrospectively.
Here, we show that an imitating agent can still learn the desired behavior merely from observing the expert, despite the absence of explicit rewards or action labels. 
In our method, AILOT (Aligned Imitation Learning via Optimal Transport), we involve special representation of states in a form of intents that incorporate pairwise spatial distances within the data. 
Given such representations, we define intrinsic reward function via optimal transport distance between the expert's and the agent's trajectories. 
We report that AILOT outperforms state-of-the art offline imitation learning algorithms on D4RL benchmarks and improves the performance of other offline RL algorithms by dense reward relabelling in the sparse-reward tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers learning from offline data in settings where reward may be difficult to specify, but one (or multiple) expert trajectories demonstrating the behavior may be found. The general idea is to assign rewards within a trajectory based on an optimal transport distance between trajectories in the offline data, and this optimal trajectory. The primary innovation is to use a dynamical distance (ICVF) to parameterize a more semantically meaningful cost function for the optimal transport problem. The evaluation demonstrates improvement over prior approaches in this problem setting on all state-based D4RL tasks (including locomotion, antmaze, and adroit).

### Strengths
The problem setting is topical, and the method is simple and well-motivated -- Figure 1 in particular illustrates clearly the benefit of parameterizing distances in a latent space instead of the raw state space (or equivalent).

The experiments clearly demonstrate performance improvement over prior approaches (both based on optimal transport, or other imitation learning) in the D4RL suite. Admittedly, these tasks are relatively toy and now saturated, but even so, the results seem convincing. 

The related work throughout the paper (in intro, related work, and method section) contextualizes the contributions of this paper well.

The appendix (and experimental section) thoroughly describes the comparisons and the benchmark setting.

### Weaknesses
I found the writing in the paper to be difficult to comprehend at many parts, making it difficult to understand the method exactly and what the exact contributions are relative to prior work in this space (e.g. Luo et al). 

For instance, the introduction barely touches on the method being proposed, instead discussing in great detail the motivation for IL methods, for optimal transport, etc. This makes it difficult to understand and contextualize the specific contributions of the method being proposed in the paper.

The paper is most closely related to Luo et al, 2023 (OTR), but within the method section, does not distinguish between what ideas come from Luo et al, and which are newly introduced in this paper. For readers who may not be familiar with this prior work, this can lead to misattribution of ideas. It would be useful (whether in the related work, background, or method) to more clearly lay out what is done in Luo et al, and what new ideas are being considered. 

The novelty of the idea (to my understanding) over Luo et al is relatively low -- this, in itself, is not a bad thing. However, given the simplicity of the idea, it would have been nice to see more thorough ablations and analyses to understand how e.g different dynamical distances perform, what types of data this is most helpful with, the importance of both components of the cost function. Another axis that could improve the thoroughness of the paper is to evaluate on more challenging domains beyond where standard cost metrics succeed (for example, in image-based domains). One other possible avenue of improvement here may be to thoroughly investigate what the actual computed rewards look like between this method and prior work. 

As it stands right now, while the method demonstrates mild improvements on D4RL, the paper could be much improved by expanding the analysis on the axes why the learned representation is much more useful, or by testing on a more difficult suite of tasks.

### Questions
1. Why is there minimal benefit to scaling the number of expert trajectories? How well would this method handle using expert trajectories that take different behaviors to solve the same problem (for example, the Push-T task from Diffusion Policy)

2. Could you explain better what the two different components of the cost function are doing? The text didn't well-motivate why these were chosen in this way.

3.  How sensitive is the method to `k`?

4. Would be nice to expand the discussion about how this method handles sub-optimal / orthogonal data compared to traditional offline algorithms -- Can this method "stitch" trajectories together?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on practical offline reinforcement learning tasks with only expert observations, avoiding the requirements for expert actions and reward labels. Specifically, this paper proposed AILOT (Aligned Imitation Learning via Optimal Transport), which defines the intrinsic rewards using optimal transport distance between the intention representations of the expert’s and agent’s trajectories. Through dense reward relabeling, AILOT outperforms state-of-the-art offline imitation learning methods and improves other offline reinforcement learning methods on the D4RL benchmarks.

### Strengths
1.	The proposed AILOT method eliminates the requirements of expert rewards and actions. Instead of performing Optimal Transport matching, AILOT maps the initial state space to the space of intentions and aligns the intents of the agent with those of the expert via Optimal Transport.  This approach involves several steps: 1) training general-purpose value functions from the expert dataset to learn the metric-aware representations; 2) solving the Optimal Transport alignment to obtain the coupling matrix; 3) reward labeling for the expert observations using the coupling matrix; and 4) training RL using the expert dataset with labeled rewards to obtain the final policy. 
2.	The intent differences between the k-step state representations have a linear dependence on the step count. This near-monotone function reflects the global geometric dependencies between states in the expert dataset. This good property is important for defining the cost function of Optimal Transport alignment learning. 
3.	The dense reward from AILOT can also boost the performance of other offline reinforcement learning methods. The performances of offline imitation learning and offline reinforcement learning have been demonstrated in the extensive experiments on D4RL benchmarks.

### Weaknesses
1.	AILOT is built on top of OTR, following the idea of performing reward relabeling through optimal transport. The most interesting part of AILOT is to perform Optimal Transport alignment in the space of intention instead of the original state space. However, the intention learning method is an existing work called ICVF, which limits the novelty. 
2.	Optimal Transport introduces additional runtime overhead compared to the offline RL algorithms, with the benefits of reward labeling.

### Questions
1.	In the experiments, AILOT is applied with Implicit Q-Learning (IQL) because it is a simple and robust offline RL algorithm. Is there any special reason or motivation for using IQL here, and will AILOT also perform well with any other offline RL algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses how to effectively imitate expert behavior in **offline reinforcement learning** with **sparse rewards** and without action labels or ground truth rewards. Previous methods used optimal transport to measure similarity between agent and expert trajectories as a reward signal, but relied on raw state distances. This paper introduces **AILOT**, which uses "intent alignment" and "optimal transport" in an intent space to calculate intrinsic rewards, enabling the agent to learn expert behavior more effectively and improve performance in sparse reward tasks.

### Strengths
1.	**Novel approach within the scope of existing methods:** While optimal transport has been used in similar imitation learning research, AILOT applies it uniquely by focusing on “intent alignment” in a metric-aware latent space, which differentiates it from other OT-based approaches.
2.	**Demonstrated performance improvement:** AILOT outperforms several baseline models, including those using OT, in various benchmark tasks, indicating it successfully optimizes OT alignment in a manner that strengthens offline RL without explicit reward signals.
3.	**Robust integration with other RL algorithms:** The method is designed to enhance the performance of other offline RL algorithms, making it versatile for broader applications.

### Weaknesses
1.	**Overlap with existing research:** The approach shares similarities with prior work that applies optimal transport to offline imitation learning, such as Optimal Transport for Offline Imitation Learning (arXiv:2303.13971) and Combining Expert Demonstrations in Imitation Learning via Optimal Transport (arXiv:2307.10810). These papers also use OT to create reward signals from expert trajectories, raising concerns about the novelty of AILOT’s contribution. Although AILOT introduces intent alignment as a distinct feature, further justification of how this approach advances beyond these prior works would strengthen the contribution. Specifically, the paper needs to more clearly articulate how the intent space and its associated metric fundamentally differ from simply using a learned state embedding as a basis for optimal transport, and how this difference leads to improved performance. The current explanation lacks sufficient detail to fully justify the novelty of the approach.
2.	**Limited comparison with recent state-of-the-art methods:** The paper does not include comparisons with more recent imitation learning algorithms, such as O-DICE (ODICE: Revealing the Mystery of Distribution Correction Estimation via Orthogonal-gradient Update, arXiv:2402.00348), which have demonstrated strong performance in offline imitation learning tasks. Including such comparisons would provide a clearer understanding of AILOT’s relative performance and contributions. The absence of these comparisons makes it difficult to assess whether AILOT represents a significant advancement over the current state of the art, or if its performance gains are marginal compared to more recent methods.
3.	**Dependency on well-defined intents:** AILOT’s performance may be compromised if the expert’s behavior is ambiguous or multi-modal, making alignment challenging. This is especially relevant when handling multi-intent expert demonstrations, an area where existing OT-based methods may also encounter limitations. The paper should include a more thorough discussion of how the method handles situations where expert behavior is not easily distilled into a single, clear intent, and what the limitations of the approach are in such cases.
4.	**Lack of clarity in training configuration:** While the paper provides an estimated runtime on an NVIDIA RTX 3090 GPU (10-25 minutes), it lacks specific details on training configurations, such as the number of samples or epochs used. Including this information would improve reproducibility and allow readers to better assess the computational efficiency of AILOT. The paper should also specify the batch sizes used for training, as well as the learning rates and optimization algorithms used for both the intent encoder and the policy network. This level of detail is crucial for ensuring that the results can be replicated by other researchers.

### Questions
1.	**Clarification on Dataset Size and Training Configuration:** Could the authors provide specific details on the number of samples and epochs used during training? This information would help clarify the computational efficiency of the method, beyond the hardware and runtime specifics provided.
2.	**Comparison with Modern State-of-the-Art Methods:** Have the authors considered including comparisons with more recent state-of-the-art methods in imitation learning, such as O-DICE or other recent 2024 approaches? This would offer a more comprehensive view of AILOT’s performance relative to current advancements in the field.
3. **Comprehensive Sensitivity Analysis for Cost Function and Hyperparameters:** While the paper includes a limited ablation study with only two configurations (α=5, τ=0.5 and α=1, τ=1), a broader exploration of these hyperparameters would provide a clearer picture of AILOT’s robustness. Could the authors expand the sensitivity analysis with more variations in these parameters or offer additional insights into how these choices affect the model’s performance across different tasks?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Aligned Imitation Learning via Optimal Transport (AILOT), a method for offline reinforcement learning that uses optimal transport to align an agent's behavior with an expert's in a "intent" space. The intent space is learned with some previously suggested method. AILOT outperforms existing methods on benchmark tasks, especially in sparse-reward environments.

### Strengths
- Strong empirical performance

### Weaknesses
 - This paper is basically a souped-up version of (Luo et al., 2023), where the optimal transport between state is replaced with the optimal transport between intentions. Since the intention space is also learned with the previously suggested method, the contribution of the paper is  1) idea of using intention instead of state itself, and 2) the design of the cost matrix in Eq. (10). However, the design of the cost matrix Eq. (10) is not well analyzed in the paper, neither theoretically nor empirically. In my opinion, the idea of using intention instead of state is straightforward, and the paper for ICLR should contain more messages than it.

- SInce the usage of intention on OTR is the key contribution of the paper, I would expect the paper to analyze on what aspects do we need to improve from state space OTR methods. However, the paper relies on a single intention learning method and do not discuss on why the used intention learning method improves.

### Questions
- The paper argues that learning expert states alone (without actions nor rewards) is one strong contribution of the paper. Are previous works incapable of doing that (e.g., (Luo et al., 2023))?

### Soundness
2

### Presentation
2

### Contribution
2
