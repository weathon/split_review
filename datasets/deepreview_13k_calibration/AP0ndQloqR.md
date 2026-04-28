# Geometry of Neural Reinforcement Learning in Continuous State and Action Spaces

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Advances in reinforcement learning (RL) have led to its successful application in complex tasks with continuous state and action spaces. Despite these advances in practice, most theoretical work pertains to finite state and action spaces. We propose building a theoretical understanding of continuous state and action spaces by employing a geometric lens to understand the locally attained set of states. The set of all parametrised policies learnt through a semi-gradient based approach induce a set of attainable states in RL. We show that training dynamics of a two layer neural policy induce a low dimensional manifold of attainable states embedded in the high-dimensional nominal state space trained using an actor-critic algorithm. We prove that, under certain conditions, the dimensionality of this manifold is of the order of the dimensionality of the action space. This is the first result of its kind, linking the geometry of the state space to the dimensionality of the action space. We empirically corroborate this upper bound for four MuJoCo environments and also demonstrate the results in a toy environment with varying dimensionality. We also show the applicability of this theoretical result by introducing a local manifold learning layer to the policy and value function networks to improve the performance in control environments with very high degrees of freedom by changing one layer of the neural network to learn sparse representations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the Manifold hypothesis for deterministic continuous state and action environments in RL. In particular they show that the set of reachable states for a certain class of analytically tractable neural network policies learned using stochastic policy gradient lies on a manifold with a dimension upper bounded by a linear function of the action space dimension. They demonstrate this upper bound in empirical experiments and show that using a sparse representation can help in learning in complex environments.

### Strengths
The paper is well-written and rigorous. 
The analysis of the manifold hypothesis for RL using neural network policies is novel to my knowledge, and a significant contribution to the area.

### Weaknesses
I don’t have any major comments on the weaknesses of the paper, I feel that the authors adequately mention the limitations in Section 6.  

Minor:
- There were a few awkward or incomplete sentences that I did not understand:
  - L263-265: “In theoretical frameworks ….”
  - Caption of Figure 3
  - L462: “A common of a fully …”
  - The paragraph under Equation (14), and specifically the sentence in L475-478.
- The fonts in Figures 2,3, and 4 were too small to read.

### Questions
- In Figure 2, I thought that the upper bound is supposed to be $2d_a + 1$ but the caption says that the green line is $d_s$ and the estimated dimensionality is below it. Also what is the red line in this figure?

- In Figure 4, what is “Group” in the legend referring to?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a novel theoretical and empirical analysis of reinforcement learning (RL) within continuous state and action spaces by employing a geometric framework. The authors propose that the set of attainable states in RL systems is constrained within a low-dimensional manifold, which is directly influenced by the dimensionality of the action space. Specifically, they examine the structure of locally attainable states using semi-gradient updates in actor-critic learning, aiming to identify and exploit low-dimensional representations for RL in high-dimensional environments. This approach is validated through experiments on MuJoCo environments, demonstrating the practical implications and performance gains of using low-dimensional manifold learning in RL settings with high degrees of freedom.

### Strengths
- Strong theoretical insights: The authors look at the geometry of RL dynamics in continuous-time MDP with continuous spaces in order to link the dimensionality of the attainable state manifold to the action space. Theorem 1 is the main contribution in this reward. The theorem formally shows that the dimension of this manifold is related to the dimensionality of the agent's action space rather than the full state space. Specifically, the dimension of the manifold is approximately $2 \times (action dimension) + 1$. I found this insight quite interesting. It looks like the theorem suggests that by understanding this low-dimensional structure, we can design more efficient policies or networks, as we don’t need to account for the full high-dimensional state space, as seen in results in section 5.3.

- Interesting empirical experiments on multiple MuJoCo environments that support the theoretical claims (see above comment). By measuring the dimensionality of the attainable state space, the results indicate consistency with the derived bounds, highlighting the empirical validity of the proposed approach.

### Weaknesses
 - The mathematical presentation is too complex: The derivation and presentation of the theoretical framework are mathematically dense, which could limit accessibility for a broader audience. The notation and terminology, especially in the sections on Lie series and vector fields, may be difficult for readers less familiar with differential geometry. It would be great if there could be some better insights following each main step.

-  There is little discussion on scalability: While the results are validated empirically, the paper could benefit from further discussion on the computational complexity and scalability of the approach, particularly in scenarios with much larger state-action spaces or image input space.

### Questions
- Q1: Is the sparsification layer computationally efficient compared to fully connected layers, particularly as the number of states and actions grows?

- Q2: How does this work compare in performance with other state representation techniques, such as latent variable models in RL?

In overall, the paper is generally well-written, with each section following logically from the previous one. However, the introduction to differential geometry concepts (e.g., Lie derivatives, exponential maps) could be more concise, as this level of detail might obscure the main contributions. The plots provided for MuJoCo environments are helpful, but additional figures explaining the theoretical framework would improve clarity.


This submission is a strong contribution to theoretical RL research and provides significant insights into the geometric structure of attainable states in continuous environments. The empirical validation in MuJoCo environments further solidifies the practical value of the proposed method. 

* Minor comments

- Figure 2: What is the red line?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a theoretical approach to understanding reinforcement learning in continuous state and action environments using a geometric perspective. Unlike traditional theoretical RL models that focus on finite state and action spaces, this work introduces the concept of a low-dimensional manifold that captures the space of states achievable by RL agents trained with actor-critic methods. By demonstrating that the dimensionality of this manifold is bounded by the dimensionality of the action space, the authors establish that RL agents operate within a constrained subset of the full state space.

### Strengths
By proving that RL agents operate within a low-dimensional manifold of attainable states, the authors offer a mathematically rigorous insight that connects the geometry of state spaces to the action dimensionality. 
This theoretical framework is supported by empirical evidence from simulated environments, such as MuJoCo, showing that training dynamics in RL indeed produce a low-dimensional representation. The paper presents a practical application by incorporating a manifold-learning layer in policy and value networks, which improves performance in complex control tasks.

### Weaknesses
The analysis assumes deterministic transitions and access to an exact value function, which is often impractical in dynamic, stochastic environments. 
The simulation setups may not fully capture the complexity and variability of real-world tasks where environmental noise and high-dimensional data structures can complicate learning dynamics. 
Lastly, the mathematical framework is limited to two-layer neural networks, which may oversimplify the behaviors of deeper architectures commonly used in modern RL, potentially limiting the generalizability of the findings to more complex neural network models.

### Questions
How could the theoretical framework be adapted to account for stochastic transitions and noisy reward functions, which are common in real-world environments?
Can the manifold-learning approach be tested with deeper and more complex neural network architectures to better reflect the structure of contemporary RL models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work shows that training dynamics of a two layer neural policy induce a low dimensional manifold of attainable states embedded in the high-dimensional state space.

### Strengths
theoretical understanding

### Weaknesses
1. The manuscript is difficult to follow. Section 2 introduces a large number of mathematical concepts, including manifolds, fields, and Lie algebras. However, the connections between these mathematical concepts are fragile. I did not see the main storyline and the author's contribution clearly before page 7. The introduction of these concepts feels somewhat disconnected from the core RL problem, and their relevance to the subsequent analysis is not immediately apparent. Specifically, the paper does not clearly articulate how these mathematical structures are directly used to derive the low-dimensional manifold of attainable states. The motivation for using these specific tools is not well-established, leaving the reader struggling to understand their purpose.
2. The paper primarily considers two-layer neural networks with GeLU activation. However, the subsequent theoretical analysis depends on linear approximation. I cannot tell the difference between this and single-layer neural networks and the impact of approximation errors on the proof results. The reliance on linear approximation raises concerns about the validity of the results for non-linear regimes. The paper does not provide a clear justification for why the linear approximation is sufficient to capture the essential dynamics of the two-layer network. Furthermore, the analysis does not address the potential impact of approximation errors on the derived low-dimensional manifold. Besides, extending the analysis to other network architectures and activation functions would strengthen the claims of universality. The lack of analysis for different architectures and activations limits the generalizability of the findings.

### Questions
1. What does $\mathbb{B}_{W_{k \eta}}$ below equation (9) represent? Why does batch data need to come from SDE? Which research works on continuous time policy gradients have used this concept? 
2. Does $G(W)$ in equation (10) contain $\eta$? 
3. Since similar proof techniques were used, what are the innovative points of this manuscript compared to Ben Arous et al. (2022)?
4. The paper studied MDP for continuous-time systems. However, the simulation case is MuJoCo for discrete-time systems. 
5. The gradient of policy network parameters for DDPG and SAC algorithms in simulation work deviates from the continuous time policy gradient. To what extent can simulation work verify the effectiveness of theoretical results?

### Soundness
2

### Presentation
2

### Contribution
3
