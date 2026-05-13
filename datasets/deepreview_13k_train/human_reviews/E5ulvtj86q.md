# Spatial-aware decision-making with ring attractors in Reinforcement Learning systems

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
This paper explores the integration of ring attractors, a mathematical model inspired by neural circuit dynamics, into the reinforcement learning (RL) action selection process. Ring attractors, as specialized brain-inspired structures that encode spatial information and uncertainty, offer a biologically plausible mechanism to improve learning speed and predictive performance. They do so by explicitly encoding the action space, facilitating the organization of neural activity, and enabling the distribution of spatial representations across the neural network in the context of deep RL. The application of ring attractors in the RL action selection process involves mapping actions to specific locations on the ring and decoding the selected action based on neural activity. We investigate the application of ring attractors by both building them as exogenous models and integrating them as part of a Deep Learning policy algorithm. Our results show a significant improvement in state-of-the-art models for the Atari 100k benchmark. Notably, our integrated approach improves the performance of state-of-the-art models by half, representing a 53\% increase over selected baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose adapting the ring attractor network, a long-studied, biologically inspired neural network architecture, as a stochastic action selection module for reinforcement learning. The authors demonstrate mathematically how this model can integrate input uncertainty and convert it to probabilistic attractor states, which could be used to control action choices. The authors further embed the ring network model with existing deep reinforcement learning models, including BDQN, DDQN and EfficientZero and show significant boost in performance on the Atari game suite.

### Strengths
The ring attractor model is a prevalent and important biological architecture with demonstrated fucntion in sensory integration and decision-making. Testing its utility as part of a deep reinforcement learning module is an interesting and promising direction. The mathematical formulation of the model is well presented. An extensive list of empirical evaluation has been done showing significant boost of performance from the EfficientZero baseline.

### Weaknesses
1) Novelty: The ring attractor model itself has been proposed decades ago and many theoretical work has examined how this model architecture integrate information to output perceptual or action decisions. The ability of the ring attractor network to integrate or compute uncertainty has also been analyzed theoretically (e.g. Kutschireiter et al., PNAS 2023). So the novelty of the work does not lie on the theoretical analysis on the ring attractor model, but on its application as a action-selection module in RL. While the empirical evaluation appears promising, there is no strong theoretical insight on why this model excels over existing algorithms for action selection (see more details below).
2) Insight on why the model excels at action sampling: The authors claim that the ring attractor-based action selection introduces uncertainty awareness (UA) into action selection. However, the BDQN algorithm, which served as the baseline for BDQN-UA, already performs uncertainty estimation and action selection through approximate Thompson-sampling. While the ring attractor model may bring additional level of stochasticity into action sampling, it is unclear what the key mechanism that brings about the boost in empirical performance. In fact, as shown in Kutschireiter et al. PNAS 2023, computation in the ring attractor network essentially implements Bayesian inference. Since Bayesian inference is already done through BLR in the BDQN model, the goal performing another round of inference through the ring network appears unnecessary.
3) While EffZeroRA should remarkable performance on the Atari suite, it is unclear whether the performance boost arise due to uncertainty estimation through the BLR on action values, or through the deployment of the ring attractor. Perhaps an ablation study comparing EffZero with BLR/Thompson sampling against EffZeroRA could help isolate the role of the ring attractor
4) Compatibility of ring structure to arbitrary action spaces: A feature in the dynamics of the ring attractor model is that nearby units tend to have correlated activity (due to strong excitatory connections). When used for action selection, this structure feature could introduce correlation in the sampling probability of actions represented by close-by units on the ring. However, this correlation in sampling probability may not be desirable for all RL tasks, hence hindering the generality of the ring attractor as an action selection module. It is unclear how the spatial relationships between actions are determined and whether this mapping is always beneficial. For example, in a game where actions are not spatially related, such as selecting different items in an inventory, the ring structure might impose an arbitrary and potentially detrimental correlation.
5) Implementation details--could the authors comment on: 1. Are the ring weights fixed or updated during training? 2. If updated, how is the appropriate decay of excitation weights maintained? 3. Does DDQN-RA use BLR for uncertainty estimation like BDQN-RA? 4.What specific role does neuronal spiking play in the exogenous model, and is it necessary?

### Questions
Could the authors comment on:
1) mechanistic insights on why the ring attractor model adds a performance boost on top of BDQN, which already performs Bayesian uncertainty estimation and posterior sampling of actions?
2) whether the sampling implicit bias in the ring model (i.e. sampling probability of “close-by” actions may be correlated due to local excitation among ring units) could impact its generality in RL applications?
3) provide more implimentation details as listed in point 5 above.

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
This paper proposed a method for using a ring attractor mode as the final layer of a model-free reinforcement learning model on an agent with discrete actions for tasks in a 2D space. Given an observation and all actions, with the ring attractor, the Q value estimation can take advantage of prior knowledge of space sense for a better action decision. The experiments report that three models with this method outperformed the original baseline models in 2D video games.

### Strengths
This work contributes to an important concept in decision-making during reinforcement learning in a task with space: how to associate values with directions. This paper presents a method to do it with a ring attractor which plays a role in Q value fusion with a prior of space.

### Weaknesses
To my understanding, this method implicitly assumed that each action is associated with a direction, the Q value of different actions is a Gaussian distribution in different directions, and Q values in different directions can be summed up. These assumptions, which are not always true, were not discussed clearly in the paper. For example, given a task, not all actions are associated with a direction. In this case, optimising the ring attractor with gradient decent could lead to the degeneracy of dynamics. This paper should show if the ring attractor still works as expected after training.

The paper also did not present ring attractor models correctly, which contains fundamental errors. In section 3.1, the title claims that the ring attractor model being presented is a spiking neural network, however, the presented model is a firing-rate model without spikes. The equations describing the model look like an inappropriate combination of two different models because the definitions are not consistent. For example,  $i_n$ in equation (4) and (5) are different.  There are many other mathematical errors in the paper, although some of them are just typos, but impact the quality and soundness of the paper.

In the experiments, three different models that were not clearly reviewed or mentioned are presented. The name abbreviation of the models appears abruptly, thus a reader has to guess what they are, even the models this paper tried to propose are in this case. For example, what is BDQNRA, BDQNRA-UA, and EffZeroRA? And how they come from? Although the basic method to combine a network with the ring attractor is presented, the specific models as a result of the method should be introduced before presenting the results.

### Questions
1. Line 30. The ring attractor model was proposed much earlier than 2017, the original paper should be cited.
2. Line 128, 131, 169, 416. None of the models presented in this paper are spiking.
3. The content in Section 3.1.1 is not the contribution of the work. It should be in the related work or background.
4. In Lines 159 and 160, $i$ was referred to as an input signal, however, it is used as an index in later paragraphs. They are very different concepts.
5. Equation (2)(3). A mixture of differential and difference equations, especially "$u_{+\Delta t}$" is a confusing term.
6. Line 178, should $\Delta t$ be a constant in the context of ODE?
7. Equation (2)(3). What is $i_n$ given that there is only one inhibitory neuron? The equation in Line 193 about the weights from the inhibitory neuron to excitatory neurons is confusing.
8. Equation (4)(5) results different definitions of $i_n$.
9. Equation (6). Define $w^{I \rightarrow I}$.
10. Equation(7). Define $\alpha$ when it is not a function.
11. Equation(8). Wrong parentheses.
12. Line 249. The equation in this line contains a standalone parenthesis.
13. Equation(9). Why there is a normalisation?
14. Line 266 introduced $\Phi$ as an algorithm, but used as a function in later equations. What is the output of the function?
15. Line 264, 265 and 268, why $Q(s,a)=\Phi_\theta(s)=\theta ^ T x(s)$? Prove it or cite a reference.
16. Line 286 and 295, does $w_a$ represent the weights or the outputs of the upstream model?
17. Equation (11). What are $y$, $x'$ and $\Phi_{\theta_{target}}$?
18. Equation (13). Does the equation assume there are more than one inhibitory neurons? It is different from the early sections. $abs$ is in Italic thus not a good format to be a function. $d(m,n)$ defined twice and differently here. Why does the second definition of  $d(m,n)$ contain a term $(m-m$?
19. Table 1. What does the double ring mean? It is not explained mathematically.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose incorporating ring attractors, a biologically-inspired neural circuit model for spatial information encoding, into reinforcement learning (RL) agents to improve action selection, particularly in spatially structured environments. 
The authors explore two ring-attractor implementations on RL tasks: first, an exogenous spiking neural network (SNN) and second, a regular RNN based ring attractor.
They report significant performance improvements over baselines on the Atari 100k benchmark.

### Strengths
# Strengths
* It was interesting to see how a neural architecture found in biology was integrated into a machine learning setting. Physical ring attractors are found in biological organisms, such as the Drosophila fruitfly, and offer a strong inductive bias that could be used to increase sample efficiency as was done in this paper. (Note reservations below)
* Incorporating uncertainty in addition to tracking the mean is a nice contribution, potentially leading to more robust and adaptive behavior.
(Note reservations below)

### Weaknesses
# Weaknesses
* It was not clear at all to me why Spiking Neural Networks need to be involved in this paper. Regular "rate coding" RNNs should be enough to encode a ring-attractor. To the best of my knowledge, ring attractors in biology encode internal/cognitive/state variables, and aren't directly encoding action spaces. This discrepancy raises concerns about the biological relevance of the proposed approach. Specifically, the paper does not adequately justify why a spiking neural network implementation is necessary, given that the core functionality of a ring attractor can be achieved with a standard rate-based RNN. The biological examples of ring attractors, such as those found in Drosophila, are primarily involved in encoding internal states like heading direction, not directly mapping to action spaces. The paper needs to clarify how the SNN implementation provides a unique advantage over a rate-based RNN, especially given the added complexity and computational cost.
* More clarity is needed on why the baselines chosen are justified. I think a better baseline would be to use a continuous 1-D circular variable (e.g. encoded as <sin \theta, cos \theta>) as the action space and then discretize it to match the action-space of the environment. This would be a more appropriate baseline to isolate the benefits of the ring attractor architecture itself. The current baselines do not sufficiently isolate the impact of the ring attractor architecture. A more appropriate baseline would involve representing the action space as a continuous 1-D circular variable, such as using a sine and cosine encoding of an angle, and then discretizing this representation to match the environment's action space. This would provide a clearer comparison by controlling for the representational capacity of the action space and would better isolate the benefits of the ring attractor architecture itself.
* The paper doesn't fully explain the role and impact of uncertainty quantification. Maybe the authors should be exploring a simpler ring-attractor model which doesn't include uncertainty quantification. The paper introduces uncertainty quantification but does not fully explore its role and impact on the ring attractor model. It is unclear if the added complexity of uncertainty quantification is necessary, or if a simpler ring attractor model without this feature would perform similarly. The authors should provide a more thorough analysis of the necessity and benefits of uncertainty quantification, possibly by comparing the performance of the uncertainty-aware model with a simpler version that does not include this feature.

### Questions
# Additional suggestions for improvement
* L135: "spatial exploitation"?
* L193: what are m and n here?
* L265: what is algorithm referring to here in "function approximation algorithm"?
* L343: typo: abs(m - m)
* L377: could you clarify how one neuron corresponding to one (s,a) still makes this a ring-attractor
* L406: typo: cummulative
* L408: How was \pi/6 chosen?
* L417: Can you clarify where this comes from -- "mean computational overhead ...."?
* L460: Can you provide at least one example each for how a game's action space has been mapped to Single and Double configurations
* The paper could use an overhaul in its organization. e.g. the ablation tests are essential to justify/clarify how the ring-attractor helps.

Related recent research worth citing
* Kutschireiter et al, "Bayesian inference in ring attractor networks", PNAS 2023
* Singh et al, "Emergent behaviour and neural dynamics in artificial agents tracking odour plumes", Nature Machine Intelligence 2023
* RI Wilson, "Neural Networks for Navigation: From Connections to Computations", Annual Review of Neuroscience 2023
* Xiong and Sridhar, "Understanding the Influence of Uncertainty and Noise on Spatial Decision Dynamics", Conference on Cognitive Computational Neuroscience 2024

Note that I did not spend significant time on the supplement

12/3: Increased my score from 5 to 6 for the authors' efforts revising the manuscript and responding to my feedback.

### Soundness
2

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
4

### Summary
This paper proposes a novel approach to reinforcement learning (RL) that incorporates ring attractors—models inspired by neural mechanisms that encode spatial information—into the action selection process. By organizing actions on a ring structure and decoding decisions through neural activity, the method aims to improve learning speed, prediction accuracy, and stability in deep RL. When evaluated on the Atari 100k benchmark, it reported a 53% performance increase over baseline models, particularly in games with spatial components.

### Strengths
It is interesting to consider using ring attractor structure for decision making in RL. 

The paper is well organized.

### Weaknesses
In the first approach, the rationale for using action values and their variances as connection weights is not well established. For instance, is there any prior work that employs Q-values as connection weights within a sub-network? Additionally, how should cases be handled when the Q-value exhibits very low variance? In Equation 7, adding the variance in the denominator of the weight calculation can lead to instability or weight divergence when the variance is close to zero. This is a critical concern that could severely impact the model's training and performance, especially if the variance is not properly bounded or regularized.

The second approach, as presented in Section 3.2: “DL-based ring attractor integrated into the RL agent” is not well motivated. From “RNNs perform well in modeling sequential data and in capturing temporal dependencies for decision making ” to state that “RNNs mirror ring attractors’ temporal dynamics, with their recurrent connections and flexible architecture emulating the interconnected nature of ring attractor neurons. ” The relationship between the two parts, if any, are hard to find. The authors need to provide a more concrete explanation of how the recurrent connections in the RNN are directly analogous to the specific dynamics of a ring attractor network, beyond the general notion of recurrent processing. The current explanation lacks the necessary mechanistic detail to justify the claim.

Ungrounded claims.  “Spiking neural networks (SNNs) are employed for their biological plausibility and efficient temporal information processing, which closely mimic natural neuronal behavior.” In this work, there is no spiking neural network. The ring attractor used a rectified linear unit, which is a rate unit, rather than a spiking unit.  The model in this work is also not "biologically plausible model” (Line 122). Both of the above claims are misleading and inaccurate. The use of rate-based units with ReLU activation functions is a significant departure from the dynamics of biological neurons, and the authors should avoid such strong claims about biological plausibility without proper justification.


### Questions
How the \mu_a in Eq. 12 be used in the model? Is it the mean in the expression of x_n in Eq. 1? But it was denoted as \alpha_a in Eq. 7.
Could the authors explicitly explain the relationship between these variables and their usage throughout the model?

Is there ring attractor at all in the model? The units interact through Eq. (5-6) COULD develop a ring attractor, but not all system interact like this actually develop ring attractor. This work did not spend any effort to confirm the system actually develop a ring attractor when using Q value as the connection weight. Could the authors provide specific evidence or analyses that would demonstrate the emergence of a ring attractor in their system? This can be achieved through visualizations or metrics that confirm the presence of ring attractor dynamics, as demonstrated in previous studies, such as Seung (1996, PNAS) and Kim (2017, Science). Although the 2017 Science paper is cited in this work, it is important to note that the concept of ring attractors in the brain has a longer history and a rich literature, tracing back to the 1996 PNAS study.

### Soundness
2

### Presentation
2

### Contribution
3
