# Towards Empowerment Gain through Causal Structure Learning in Model-Based RL

- Decision: Accept
- Scores: 5, 6, 8, 6, 6

## Abstract
In Model-Based Reinforcement Learning (MBRL), incorporating causal structures into dynamics models provides agents with a structured understanding of the environments, enabling efficient decision. 
Empowerment as an intrinsic motivation enhances the ability of agents to actively control their environments by maximizing the mutual information between future states and actions. 
We posit that empowerment coupled with causal understanding can improve controllability, while enhanced empowerment gain can further facilitate causal reasoning in MBRL. 
To improve learning efficiency and controllability, we propose a novel framework, Empowerment through Causal Learning (ECL), where an agent with the awareness of causal dynamics models achieves empowerment-driven exploration and optimizes its causal structure for task learning. 
Specifically, ECL operates by first training a causal dynamics model of the environment based on collected data. We then maximize empowerment under the causal structure for exploration, simultaneously using data gathered through exploration to update causal dynamics model to be more controllable than dense dynamics model without causal structure. In downstream task learning, an intrinsic curiosity reward is included to balance the causality, mitigating overfitting. 
Importantly, ECL is method-agnostic and is capable of integrating various causal discovery methods. 
We evaluate ECL combined with $3$ causal discovery methods across $6$ environments including pixel-based tasks, demonstrating its superior performance compared to other causal MBRL methods, in terms of causal discovery, sample efficiency, and asymptotic performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a framework called Empowerment through Causal Learning (ECL), designed to integrate empowerment with causal reasoning in model-based reinforcement learning. ECL operates by training a causal dynamics model, maximizing empowerment under this structure, and updating the model through data gathered from exploration.

### Strengths
1. **Detailed Experimental Validation**: The framework is evaluated extensively across multiple environments, including both state-based and pixel-based tasks, showcasing its adaptability and effectiveness in real-world scenarios.
2. **Clear Presentation**: The paper is well-organized and clearly presents concepts, making it accessible and allowing readers to follow the progression of ideas and experimental setups with ease.

### Weaknesses
1. **Minor Contribution**: The current framework appears more like a combination of existing approaches rather than a novel advancement. Causal structure learning in model-based RL has been extensively studied in prior work, such as [1-2], as has empowerment in RL [3-4]. This may limit the perceived originality of the contribution, as it builds on established methodologies without significantly advancing them.

2. **High Computational Cost**: The framework’s iterative process of empowerment maximization and causal model updating may result in substantial computational requirements, potentially limiting its scalability in large or dynamic environments.

[1] Huang B, Feng F, Lu C, et al. Adarl: What, where, and how to adapt in transfer reinforcement learning[J]. arXiv preprint arXiv:2107.02729, 2021.

[2] Huang B, Lu C, Leqi L, et al. Action-sufficient state representation learning for control with structural constraints[C]//International Conference on Machine Learning. PMLR, 2022: 9260-9279.

[3] Zhang J, Wang J, Hu H, et al. Metacure: Meta reinforcement learning with empowerment-driven exploration[C]//International Conference on Machine Learning. PMLR, 2021: 12600-12610.

[4] de Abril I M, Kanai R. A unified strategy for implementing curiosity and empowerment driven reinforcement learning[J]. arXiv preprint arXiv:1806.06505, 2018.

### Questions
1. As shown in Figure 2, what is the collection policy $\pi_{collect}$, and how do the authors gather the initial dataset (s, a, r, ...) in the buffer?

2. In line 231, the authors state, "the dynamics encoder learned in Step 1 remains fixed, allowing for a focused optimization of both the causal structure and the empowerment in an alternating manner." I am wondering how the authors can fix the optimization of the encoder while still optimizing the causal structure, as shown in Eq. (5)?

3. The proposed framework optimizes iteratively. How is the iteration cycle determined? Will this approach result in high computational costs and longer training times? Could the authors also provide a comparison of training times?

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
3

### Summary
The authors present ECL, an agent that integrates empowerment with causal reasoning to better learn to control an environment, to then perform better in downstream tasks. First, ECL learns a causal dynamics model (dense dynamics model + causal mask) and reward model to maximize the likelihood of observed trajectories, with a regularization term on the causal mask encouraging the use of as few features as possible. Second, ECL alternates between updating a policy that leverages the causal mask to maximize empowerment, and using the data generated by running the policy to improve the causal mask and reward model. Finally, the learned models can be used to learn policies for downstream tasks, mitigating overfitting of the causal model with an intrinsic reward for observing transitions where the dense model fits better than the causal model. The authors demonstrate that ECL performs well in terms of both reward and sample efficiency compared to existing methods across environments, and accurately learns the true causal structure of the environments.

### Strengths
The approach appears to be novel. The integration of causal discovery, which by itself can be quite passive, with Empowerment, to emphasize controllability, is very interesting.

The authors tested on a wide spread of environments with different types of dynamics, showing impressive causal discovery and task performance.

### Weaknesses
The presentation of the algorithm is vague and unclear, with many technical details skimmed over. For instance:

 - The causally-factored MDP is difficult to understand and the explanations are very brief; it would be helpful to show the causal masks and adjacency matrices for the example environment in figure 1, and provide more explanation/intuition for what each term in the equations represents. See the questions section.

 - How the causal models are used for downstream tasks is not specified anywhere except a single line of the Appendix “the CEM planning” 

The dynamics encoder predicts an independent probability for each feature of the next state given the current state and action- how realistic is this? On a similar vein, this method seems dependent on a well-defined feature space for the states and actions.

The choice of “standard MBRL” baselines to complement the causal baselines do not seem very standard- why not compare against state of the art MBRL algorithms such as [1]? 

More minor writing issues:

 - The use of Dense dynamics model/dynamics encoder interchangeably to describe the same thing is confusing

 - Section 4 is quite repetitive of section 3

[1] Hafner, Danijar, et al. "Mastering diverse domains through world models." arXiv preprint arXiv:2301.04104 (2023).

### Questions
In the dynamics function f in equation (2), it’s not clear how exactly the adjacency matrices indicate the influence of current states and actions on the next state, what the output of each dot product represents and how they can be combined to get the ith dimension of the next state?

What is the relationship between the causal mask M and the adjacency matrices?

How can the mask be updated without also having to update the dynamics encoder? If the mask was very bad at Step 1, wouldn’t the dynamics encoder also be very suboptimal and not appropriate to continue using as the mask is improved in step 2?

Why does it not work to simply maximize the empowerment given the causal dynamics model, rather than the difference between that and the empowerment under the dense model?

It is not explained in section 3 where the reward from step 1 and 2 comes from. Section 4 describes a reward function formulated to select transitions covering more state-action pairs. How sensitive is the method to the design of this reward function? Reward functions can be notoriously hard to design; a lot of the difficulty of the problem might be obfuscated in this part. 
In Step 3 of Algorithm 1 it says the learned reward predictor predicts $r_{task}$- how can it predict that if it was learnt during step 1 and 2 in the absence of any downstream tasks? And why are the $r_i$ in the transitions collected in line 2 ignored? Step 3 of section 4 implies that the causal model is only used to generate curiosity intrinsic rewards (which does not rely on the learned reward predictor at all) so this is inconsistent with Algorithm 1.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces the empowerment through Causal Learning (ECL) framework to enhance controllability and learning efficiency in model-based RL. The framework combines empowerment, a measure of an agent’s ability to control its environment through causal structure learning. ECL enables agents to understand causal relationships within the environment, improving decision-making and policy learning. ECL was evaluated with different causal discovery methods across three environments, showing improved sample efficiency, accurate causal inference, and higher episodic rewards than other causal MBRL approaches​.

### Strengths
- Overall, I think this is a good paper. The idea is interesting. The authors provide enough details and explanations in the technique section. The experiments are thorough and enough to demonstrate the advantages of ECL.
- ECL combines causal learning with empowerment-driven exploration, which is novel. By leveraging causal structures, the model enables agents to control their environments more effectively and make informed decisions, adding depth to RL's traditional empowerment approach. Through empowerment-driven exploration, ECL enhances the agent’s ability to efficiently sample relevant experiences, reducing the data requirements compared to conventional MBRL methods. This leads to faster learning and less dependence on extensive data.
- ECL has been tested across different environments, such as chemical, manipulation, and physical tasks, showing strong performance in sample efficiency, causal discovery accuracy, and episodic rewards.
- By incorporating a curiosity reward during policy learning, ECL encourages exploration while reducing the risk of overfitting specific causal structures. This helps the agent generalize better to new or out-of-distribution tasks.

### Weaknesses
Refer to the questions.

### Questions
1. Curiosity-driven exploration in RL is often sensitive and can be challenging to implement effectively. Are there different settings for setting curiosity in different experimental environments? Whether ECL is sensitive to curiosity rewards?
2. Given the complexity of the ECL structure, the ablation studies should not be omitted, i.e., ablations on reward design, basic model and other related parts should be added.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel framework named Empowerment through Causal Learning (ECL), which integrates causal structure learning with empowerment-driven exploration in Model-Based Reinforcement Learning (MBRL) by (1) causal model learning, (2) empowerment maximization, and dynamic model updating and (3) policy learning. The proposed method is agnostic to causal discovery methods and outperforms existing causal MBRL methods across several environments.

### Strengths
1. The writing is clear and the paper is in general easy to follow.
2. Actively applying causal discovery to learn environment dynamics (updating through newly collected data) is a novel approach.
3. The experiments cover a diverse set of environments, including state-based and pixel-based tasks. Both analysis on the learned causal dynamics and on the average return demonstrate substantial improvements compared to other methods and provide strong evidence of ECL across various tasks.

### Weaknesses
1. The framework aims at learning a consistent causal structure, thus cannot deal with scenarios when the causal dynamics change (change of number of objects, etc.) that might correspond to different behavior components. Maybe consider discuss potential extensions or modifications to their framework that could handle changing causal dynamics. 
2. Other issues please refer to questions.

### Questions
1. In the motivating example, why do we merely focus on improving controllablility (row 2 and 3) and do not care about whether the agent find the true target? (L79-l87) And further, how to detect the "controllable" trajectories? Could you provide more specific details on how controllable trajectories are identified and measured?
2. While maximizing mutual information I(s;a), would it be helpful to also take into account the causal structure, i.e. maximizing the state and action dimensions that are dependent in the dynamics graph? Potential benefits and challenges of incorporating the related s,a dimension into the mutual information objective could be made clearer.
3. The result in Fig. 24 in DMC environment CHeetah and Walker seem to have not converged yet. Could the author compare ECL and IFactor when they both converge? I agree that the learning curve of ECL is already going up faster and steadier than that of IFactor, and I think it could also be helpful to see the convergence point of the policies.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose ECL (Empowerment through Causal Learning) that has two main components: (1) a causal dynamics model of the environment that is learned from data and (2) a mechanism to "empower the causal structure for exploration, simultaneously using data gathered through exploration to update the causal dynamics model". The objective of the causal structure for exploration is to obtain a dynamics model that "could be more controllable than dynamics models without the causal structure". On top of this, an intrinsic curiosity reward is developed "to mitigate overfitting during downstream task learning".


--
Given some improvements made to the paper, I increase my score to 5.
--
Given some additional improvements made to the paper, I increase my score to 6 (see comments below)

### Strengths
The objective of learning a model with some causal structure that can be used for instance in the context of exploration is an important research topic.

### Weaknesses
Main weaknesses:
- Notations are not clearly defined. For instance, the causal mask $M$ is introduced (i) without clear mathematical definition and (ii) it's not $M$ that is used later but $M^{s \rightarow s'}$ in Equation 5 (see lines 204 to 215). This makes the methodology unclear.
- The vocabulary does not relate to clearly defined concepts, e.g. "causal understanding", "causal reasoning" in lines 153-155. 

Additional comments:
- Key elements are described in the appendix instead of the main text, e.g. end of page 4: the causal loss that represents "the objective term associated with learning the causal structure" are given in Appendix D.2.

### Questions
- How can a curiosity-based reward prevent "overfitting during task learning" (lines 270-272)?
- Figure 5: is it the result of only one seed? Why is there only one seed used?

### Soundness
3

### Presentation
2

### Contribution
3
