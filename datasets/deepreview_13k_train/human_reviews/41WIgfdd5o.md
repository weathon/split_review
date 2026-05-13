# Learning a Fast Mixing Exogenous Block MDP using a Single Trajectory

- Decision: Accept
- Scores: 8, 1, 8, 8

## Abstract
In order to train agents that can quickly adapt to new objectives or reward functions, efficient unsupervised representation learning in sequential decision-making environments can be important. Frameworks such as the Exogenous Block Markov Decision Process (Ex-BMDP) have been proposed to formalize this representation-learning problem \citep{efroni2022provably}. In the Ex-BMDP framework, the agent's high-dimensional observations of the environment have two latent factors: a \textit{controllable} factor, which evolves deterministically within a small state space according to the agent's actions, and an \textit{exogenous} factor, which represents time-correlated noise, and can be highly complex. The goal of the representation learning problem is to learn an encoder that maps from observations into the controllable latent space, as well as the dynamics of this space. \cite{efroni2022provably} has shown that this is possible with a sample complexity that depends only on the size of the \textit{controllable} latent space, and not on the size of the noise factor. However, this prior work has focused on the episodic setting, where the controllable latent state resets to a specific start state after a finite horizon.

By contrast, if the agent can only interact with the environment in a single continuous trajectory, prior works have not established sample-complexity bounds. We propose \textbf{STEEL}, the first provably sample-efficient algorithm for learning the controllable dynamics of an Ex-BMDP from a single trajectory, in the function approximation setting. STEEL has a sample complexity that depends only on the sizes of the \textit{controllable} latent space and the encoder function class, and (at worst linearly) on the \textit{mixing time} of the exogenous noise factor. We prove that STEEL is correct and sample-efficient, and demonstrate STEEL on two toy problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose Single-Trajectory Exploration for Ex-BMDPs via Looping (STEEL), an algorithm to learn the endogenous (controllable) states in an Exogenous Block Markov Decision Process (Ex-BMDP) when the agent is dealing with one continuous infinite trajectory without resetting to some known states. STEEL achieves this by taking actions that result in a predictable cycle of states and iteratively updating the list of known controllable states and their transitions. They show theoretically the sample complexity and correctness of STEEL with simulations on some small environments.

### Strengths
- The introduction and related work highlight this work really well. It explains the existing work nicely and shows where the gaps lie and how this work attempts to extend it.
- The algorithm stands out in terms of the settings it covers compared to existing work. It deals with infinite trajectories, partial observability, and optimization with function approximators all while providing sample complexity guarantees.
- The algorithm itself is designed very well and has a lot of interesting features which include: forcing a cycle of states through the repetition of actions and detecting the unique states in a cycle using a classifier oracle.
- The limitations of the algorithm are clearly discussed with useful insights on how to extend this work in the future.

### Weaknesses
 - Section 4 can be a bit hard to follow. To quite understand how the algorithm exactly works one has to switch between reading the section text, the pseudocode, and parts of the Appendix. I suggest moving the pseudocode to the appendix and providing further explanation of the algorithm in the main text such that the reader can get a high-level idea of how the Algorithm works from just reading section 4.
- There are parts of the algorithm that are not very intuitive and might require some further discussion. For example, it is mentioned that the dataset $D_0, D_1$ used in the CycleFind subroutine are generated in a way such that they are disjoint if $n'_{cyc}$ is equal to $n_cyc$. Intuitively, how does the selection process achieve this? Specifically, the process of selecting data points for $D_0$ and $D_1$ based on the current cycle length $n_{cyc}$ and the candidate cycle length $n'_{cyc}$ needs more clarification. It's not immediately clear how the algorithm ensures that the datasets are disjoint when these lengths are equal, especially when the data is generated from a continuous trajectory. The mechanism for ensuring that the data points used to train the classifier in CycleFind are truly representative of distinct cycles, and not overlapping segments of the same cycle, needs to be more explicit.
- In the experiments section, the authors mention that previous work by Lamb et al.(2023) and Levine et al. (2024) don't have theoretical correctness guarantees, which can be why it seems to have better sample efficiency than STEEL. I suggest also including the percentage of runs where these baselines get the correct states and transition probabilities and how often they fail compared to STEEL which is proven to get it right with high probability. This can add additional value to how STEEL outperforms the baselines in terms of correctness. The current presentation focuses solely on sample efficiency, but a more comprehensive comparison should also include the reliability of the baselines in terms of accurately identifying the underlying state space and transitions.

### Questions
- In the Appendix in equations 33 and 35, could you further explain how the sets $\mathcal{D}_i^\mathcal{A}$ and  $\mathcal{D}_i^\mathcal{B}$ are constructed?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The authors violated the instructions and reduced the font size substantially for Algorithm 1 and 2. Given they took a whole 10 pages, I decided to recommend desk rejection. If the AC decides differently, please inform me accordingly.

### Strengths
NA

### Weaknesses
 The authors violated the instructions and reduced the font size substantially for Algorithm 1 and 2. Given they took a whole 10 pages, I decided to recommend desk rejection. If the AC decides differently, please inform me accordingly.

### Questions
NA

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
2

### Summary
The paper proposes a representation learning method for Ex-BMDP called STEEL. This method identifies the small latent state space of Ex-BMDP - which encodes the essential controllable part of the MDP - while jointly learning an encoder that maps observations to the latent state. Notably, this approach can be applied without requiring "reset" commands, allowing the algorithm to learn from a single trajectory. The key idea is to repeat sequences of actions to detect cycles in the latent state space, which enables the collection of multiple i.i.d. samples to discover the latent space structure. The sample complexity of the algorithm is shown to be polynomial in the size of the latent space, the mixing rate of the Markovian exogenous process, and the complexity of the encoder function class. The algorithm is demonstrated on two problem scenarios.

### Strengths
* The paper is clearly written, and the analysis of the key result - specifically, the sample complexity of STEEL being polynomial in the latent space size - is supported by solid mathematical arguments. The algorithm's description is intuitive and effectively conveys its core concepts.
* Furthermore, representation learning from a single episode has been a long-standing interest in the RL community, making this paper's contribution highly relevant to the field.
* The paper provides a comprehensive literature review, effectively demonstrating the novelty of the work and differentiating it from recent existing works.

### Weaknesses
 * The method relies on several assumptions, particularly concerning the latent state space $\mathcal{S}$. For example, the assumptions of deterministic latent dynamics and the reachability condition of the latent state space are critical for STEEL's CycleFind to function. The deterministic latent dynamics assumption is particularly restrictive, as it requires that the transition between latent states is fully determined by the current latent state and action, which is rarely the case in real-world scenarios where stochasticity is inherent. The reachability condition, which requires that any latent state can be reached from any other latent state, also limits the applicability of the method to environments where the latent state space is fully connected. Addressing these assumptions seems non-trivial, and overcoming them is posed as future work.
* Although the sample complexity of STEEL is polynomial in the size of the latent state space, the numerical simulations show that a substantial number of samples (millions) are required. This high sample complexity, even with polynomial scaling, raises concerns about the practical applicability of the algorithm in scenarios where data collection is expensive or time-consuming. The large number of samples needed suggests that the algorithm might not be suitable for real-world applications with limited data availability.

### Questions
* A discussion of the block assumption on $\mathcal{Q}$ with respect to $\mathcal{S}$ would be helpful. In many practical scenarios, the noisy nature of the emission (or observation) function can make distinguishing between two latent states directly from observations challenging, necessitating filtering techniques. It would be beneficial to clarify whether this assumption is not overly restrictive or if it cannot be easily weakened but is widely adopted.
* Is there a known lower bound for the sample complexity of Ex-BMDP under deterministic latent dynamics? Is STEEL nearly optimal under this assumption, or is there potential for further improvement?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies a structured class of MDPs called an Ex-BMDP, where the latent factors of the observations decompose into a lower-dimensional controllable factor (which evolves deterministically according to the agent's action) and high-dimensional exogenous factor (which evolves independent of actions). This paper focuses on the single-episodic setting and proposes sample-efficient algorithms for learning controllable dynamics of an Ex-BMDP with sample complexity that depends only on the sizes of the low-dimensional controllable state, the encoder function class, and the mixing time of the exogenous noise factor. The paper also empirically tests the proposed STEEL algorithm on the infinite-horizon variations of the "combination lock" and "multi-maze" environments.

### Strengths
- The class of Ex-BMDP studied in this paper is a general class of structured POMDPs. It captures problems where, despite having high dimensional observation, the majority of the states are exogenous and only a small controllable state matters for learning. It therefore allows more sample-efficient learning by filtering out the exogenous factors and reducing to a smaller MDP depending only on the controllable states. Such setting fits many applications and gives insight to how to best exploit these hidden structures to optimize learning.
- The main novelty of this paper compared with prior work in Ex-BMDP is that instead of the episodic setting in Efroni et al. (2022) where one gets to reset to starting state, it assumes the agent interacts with the environment in a single episode. This setting is more challenging given it is more difficult to collect samples of a given latent state without the episodic resets. 
- The paper also assumes a more general assumption on the state and emission function, where only the partial inverse with respect to the controllable state exists, but places no such assumption on the exogenous states. This is more general than assumption a block structure in prior works which allows a full inverse from observation to state.

### Weaknesses
 - The proposed algorithm is highly dependent on the assumptions that (1) the dynamics of the latent controllable states is deterministic; (2) the mixing time of the exogenous dynamics. Intuitively, assumption (1) leads to to a cycle of latent states of bounded length that is repeatedly visited and allows repeated collection of the same latent state, which on a high-level is similar to "resetting" the environment; assumption (2), given the looping behavior, can wait out the mixing time of the exogenous dynamics and collect near i.i.d. samples of each latent state. However, assuming deterministic dynamics and bounded mixing time seems restrictive, and possibly does not capture many practical setting. How sensitive is the algorithm to the violation of both assumptions? Does non-deterministic dynamics of the controllable latent states break the proposed algorithm?

 - The paper presumes the availability of an encoder hypothesis class $\mathcal{F}$, where the true decoder $f(x)$ is included, and the final complexity depends on the size $\log\mathcal{F}$. However, it does not seem to specify how to choose this hypothesis class. The simulation section gives an example of $\mathcal{F}$ that is specific to the examples. Is there any general procedure for selecting $\mathcal{F}$ with a reasonable size that also guarantees to include the correct decoder? In general settings beyond the specific examples given in the paper, can you provide guidelines or heuristics for selecting an appropriate hypothesis class?
- Given $\mathcal{F}$, the paper also assumes access to a training oracle that optimally distinguishes two sets of observations (e.g., similar to minimizing 0-1 loss). What would be an example of such an oracle without prior knowledge of the true classifier? And what is the sample/computation cost of constructing such an oracle?
- The STEEL algorithm assumes access to an upper bound on the mixing time $t_{mix}$ for the exogenous dynamics. For a general setting with unknown exogenous latent factors and dynamics, how do you get such an upper bound? Can you discuss potential methods or heuristics for estimating or bounding the mixing time in settings where the exogenous dynamics are not fully known?

### Questions
- The paper presumes the availability of an encoder hypothesis class $\mathcal{F}$, where the true decoder $f(x)$ is included, and the final complexity depends on the size $\log\mathcal{F}$. However, it does not seem to specify how to choose this hypothesis class. The simulation section gives an example of $\mathcal{F}$ that is specific to the examples. Is there any general procedure for selecting $\mathcal{F}$ with a reasonable size that also guarantees to include the correct decoder? In general settings beyond the specific examples given in the paper, can you provide guidelines or heuristics for selecting an appropriate hypothesis class?
- Given $\mathcal{F}$, the paper also assumes access to a training oracle that optimally distinguishes two sets of observations (e.g., similar to minimizing 0-1 loss). What would be an example of such an oracle without prior knowledge of the true classifier? And what is the sample/computation cost of constructing such an oracle?
- The STEEL algorithm assumes access to an upper bound on the mixing time $t_{mix}$ for the exogenous dynamics. For a general setting with unknown exogenous latent factors and dynamics, how do you get such an upper bound? Can you discuss potential methods or heuristics for estimating or bounding the mixing time in settings where the exogenous dynamics are not fully known?

### Soundness
3

### Presentation
3

### Contribution
2
