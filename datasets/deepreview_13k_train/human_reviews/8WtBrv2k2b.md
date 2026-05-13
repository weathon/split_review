# Dynamic Inhomogeneous Quantum Resource Scheduling with Reinforcement Learning

- Decision: Reject
- Scores: 6, 3, 3, 8

## Abstract
A central challenge in quantum information science and technology is achieving real-time estimation and feedforward control of quantum systems. This challenge is compounded by the inherent inhomogeneity of quantum resources, such as qubit properties and controls, and their intrinsically probabilistic nature. This leads to stochastic challenges in error detection and probabilistic outcomes in processes such as heralded remote entanglement. Given these complexities, optimizing the construction of quantum resource states is an NP-hard problem. In this paper, we address the quantum resource scheduling issue by formulating the problem and simulating it within a digitized environment, allowing the exploration and development of agent-based optimization strategies. We employ reinforcement learning agents within this probabilistic setting and introduce a new framework utilizing a Transformer model that emphasizes self-attention mechanisms for pairs of qubits. This approach facilitates dynamic scheduling by providing real-time, next-step guidance. Our method significantly improves the performance of quantum systems, achieving more than a 3$\times$ improvement over rule-based agents, and establishes an innovative framework that improves the joint design of physical and control systems for quantum applications in communication, networking, and computing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper tackles the issue of quantum resource scheduling, i.e., adjusting the parameters of a quantum system. The approach used is based on reinforcement learning (RL) and applies a transformer to efficiently model qubit connections. Results from a small case study are presented, where the new approach outperforms its competition.

### Strengths
The problem is interesting, important, and well motivated.

The approach seems fitting and is compared with a reasonable amount of baselines. It achieves superior performance.

The plots are well presented.

### Weaknesses
In certain parts, the paper is unnecessarily hard to understand. These issues include:
- The handling of the issue of complexity is off. Reasons for NP-hardness are given that are no real reasons and do not imply any NP-hardness proof. "Quantum" does not automatically make things harder. The comparison to MWCSP is not sufficient to establish NP-hardness, as the specific constraints and objectives of the quantum resource scheduling problem are not adequately mapped to the MWCSP. The argument that the problem is harder because of probabilistic success events is not a formal complexity argument.
- The beginning of the introduction is not well connected to the main content of the paper and has a lot of trailing references to the appendix. The motivation for the problem is not clearly established in the introduction, and the connection to the specific quantum resource scheduling problem is weak. The references to the appendix disrupt the flow of the introduction.
- All matrices appear to be named "M" with some index. The variable name "N" is similarly overused etc. A better naming scheme would greatly aid understanding. The lack of descriptive variable names makes it difficult to follow the mathematical formulations and algorithms presented in the paper. For example, using $M_A$ for the action matrix, $M_R$ for the rate matrix, and $M_S$ for the state matrix is not particularly informative, and the use of $N$ for multiple different quantities is confusing.

In a similar vein, I would greatly recommend introducing the problems more formally. The structure of the RL problem is just assumed and roughly derived from the underlying physics problem. Why is there no mapping to the standard MDP definition? This makes it hard to grasp the core of the problem. The lack of a formal MDP definition makes it difficult to understand the state space, action space, transition probabilities, and reward function. This lack of formalization hinders the reproducibility and comparability of the results.

A more standard formulation would also allow to apply a much greater range of standard algorithm running on the problem.

Most importantly, while outperformance is measured, there is not given a succinct reason. How does the approach perform on the "basis problem" MWCSP? Why is it not tested there?

While only very few formal errors persist, all citations are formatted incorrectly.

### Questions
None.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a reinforcement learning framework, "Transformer-on-QuPairs," for dynamic inhomogeneous quantum resource scheduling, addressing the challenge of optimizing quantum resource state construction in the face of qubit inhomogeneity and probabilistic control. The approach uses a digitized environment with Monte Carlo Simulation to train reinforcement learning agents, focusing on self-attention mechanisms for qubit pairs. The study highlights the potential of this framework for co-designing physical and control systems in quantum computing.

### Strengths
- The research studies a central challenge in quantum systems, which is the real-time estimation and control of inherently inhomogeneous and probabilistic quantum resources, making it highly relevant to current technological advancements.
- The proposed method achieves an improvement in quantum system performance over rule-based agents, demonstrating a substantial enhancement in efficiency.

### Weaknesses
Major Concerns:

- The proposed optimization framework requires the availability of pre-characterized system information. It is crucial for the authors to explain in more detail the process of acquiring this information and the associated resource expenditures, particularly when the framework is to be applied to an unknown quantum system. This transparency is essential for assessing the practicality and feasibility of the framework in real-world scenarios. Specifically, the authors should detail the calibration procedures required to obtain the error distributions for each physical link between qubits, including the types of quantum circuits and measurement sequences involved, and the time and resources needed for this characterization. The impact of calibration errors on the performance of the framework should also be discussed.
- The framework appears to require real-time characterization for the maximum cluster size and the error associated with each established entanglement. I am curious about the cost and difficulty of obtaining this information in real quantum systems. The authors need to specify the exact measurement techniques used to determine the entanglement error, such as Bell-state measurements, and how these measurements are scaled for larger systems. The latency and overhead of these real-time measurements should be quantified, as they could significantly impact the overall performance of the dynamic scheduling.
- The description of the framework is unclear to me. The authors should not assume that readers are familiar with their terminology. There are several points that need to be clarified further. For instance, what is the state matrix? What is the relationship between the state matrix and the pre-characterized system information? What does "the scheduling event is complete" mean? How do $f_1$ and $f_2$ function, and what are their inputs? How is the reward for the agent calculated? The authors should provide a more detailed explanation of the state matrix, including how it is initialized, updated, and used by the RL agent. The precise mathematical definitions of $f_1$ and $f_2$ should be provided, along with a clear description of their inputs and outputs. The reward function needs to be explained in detail, including the specific quantum volume metric used and how it relates to the performance of the system.
- I believe that more details on the training process need to be provided in the manuscript.

Minor comments:

- There are some misleading sentences in the related works section. For instance, the authors stated, "The Transformer model, for example, has been effectively used in various applications such as ... and quantum state reconstruction (Carrasquilla et al., 2019)." However, I do not believe that Carrasquilla et al. (2019) utilized the Transformer model in their method.

### Questions
Please see "Weaknesses" above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work addresses the challenge of optimizing quantum resource scheduling in inhomogeneous systems. The authors formulate the scheduling problem as a dynamic minimum weight connected subgraph problem (MWCSP), a known NP-hard problem, and design a reinforcement learning (RL) framework, Transformer-on-QuPairs, to efficiently tackle this problem. Using a simulated environment, they benchmark the RL-based approach against rule-based algorithms, achieving a reported 3× improvement in performance.

### Strengths
This paper provides a robust solution to the quantum resource scheduling problem, readily applicable to experimental quantum computing frameworks, and easily generalizable to different hardware architectures. This makes the work highly relevant to the quantum computing community, and has potential for widespread application in enhancing the performance of future quantum systems.

### Weaknesses
While the authors claim to tackle an NP-hard problem, the lack of comparison with existing combinatorial optimization solvers is a notable limitation. A range of algorithms and solvers—such as traditional methods (e.g., simulated annealing, parallel tempering), commercial solvers (e.g., Gurobi, Hexaly), physics-inspired approaches (e.g., Ising machines, memcomputing), quantum solvers (e.g., D-Wave), and graph neural network-based machine learning solvers—are commonly used in related optimization contexts.  Yet, the paper benchmarks only against a few rule-based algorithms, which are generally not known to effectively solve NP-hard problems. The omission of comparisons to such established solvers limits the ability to assess the true novelty and strength of the proposed RL approach.

In addition, real-world experimental validation (beyond simulations) could further strengthen the results.

The authors suggest that the problem they address is at least as hard as MWCSP, an NP-hard problem. However, the cited MWCSP reference (Haouari et al., 2013) includes positive and negative weights, which prevent reduction to a minimum spanning tree problem. In contrast, the quantum resource scheduling problem here does not appear to involve negative weights. The authors' approach of assigning zero weight to terminal nodes and a large positive weight to Steiner nodes does not correctly reduce the MWCSP to the Steiner tree problem, as it excludes Steiner nodes instead of ensuring the inclusion of terminal nodes. This misunderstanding of the MWCSP formulation raises concerns about the claimed NP-hardness of the problem. Furthermore, the deterministic version of the quantum resource scheduling problem appears to be solvable using a minimum spanning tree algorithm, which has polynomial complexity, further questioning the NP-hardness claim. This may also explain the effectiveness of the greedy algorithm, which typically struggles with NP-hard problems.

### Questions
1.	The authors suggest that the problem they address is at least as hard as MWCSP, an NP-hard problem. However, the cited MWCSP reference (Haouari et al., 2013) includes positive and negative weights, which prevent reduction to a minimum spanning tree problem. In contrast, the quantum resource scheduling problem here does not appear to involve negative weights. While the problem’s probabilistic nature may indeed make it more challenging—potentially classifying it as BPP, AM, or MA—could the authors provide a more rigorous explanation of why this specific problem is NP-hard?
2.	Can the authors benchmark their algorithm against a few established combinatorial optimization solvers? 
3.	The authors assume an all-to-all qubit connectivity; however, many quantum computing architectures are locally connected. Can the authors comment on the generalizability of their approach to architectures with different connectivity structures?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper addresses the challenge of optimising the construction of entangled resource states in networked quantum computing architectures, where quantum bits are probabilistically entangled with one another. This is an extremely challenging problem, as the optimal control and scheduling of quantum resources is affected by the inhomogeneous nature of the underlying quantum resources, their pairwise interactions and probabilistic outcomes of remote entanglement. Optimising quantum resource state production is an NP-hard problem, which the authors tackle by simulating quantum resource scheduling in a digitised environment. Connections are made to the Minimum Weight Connected Subgraph Problem and the authors introduce a novel approach using reinforcement learning agents and a Transformer model, leveraging self-attention mechanisms to optimise qubit pair scheduling. This method enhances entangled resource state construction, yielding over a 3× improvement compared to traditional rule-based agents, with applications for a variety of quantum systems. Detailed benchmarks for different fidelity inhomogeneities, number of qubits for various rule and RL based algorithms underscore the results and show the superiority of the transformer-on-QuPairs method.

### Strengths
The paper outlines an important and extremely challenging problem which is physically motivated and underscored with a detailed physics model in the Appendix. The system level optimisation approach for optimising dynamic resource scheduling has not been tackled in the literature previously and this therefore makes this a valuable contribution. Moreover, the difficulty of the problem is well put by framing it as a more complicated version of the MWCSP. The applicability of this to various hardware architectures (photonics, ions, atoms, spins etc..) for networked quantum computing architectures also underscores the relevance of this work.

Moreover, the application of a transformer with different encodings (pre-information, dynamic and position) is a creative approach to solve a challenging problem in the control and design of large scale quantum experiments which has not emerged previously in the literature.

The benchmarks provided are comprehensive and clear. Table 1,2 an Figure 4 show very clear advantages of using the transformer approach which becomes increasingly more advantageous as the qubit number increases and the environment becomes more inhomogeneous (sigma(F) increases).

### Weaknesses
The scaleability and comparison in training times over different algorithms is largely omitted. A more detailed analysis and perhaps discussion of the limitations of particular approaches as the number of qubits scale would be extremely helpful, particularly for the Results shown in Table 3. This would make the analysis of the experiment more complete and strengthen the overall paper.

The manuscript is not as clear as it could be and the framing of the problem is not as strong as it could be either. In the abstract the authors claim a 3x improvement over rule based agents but no reference to a metric with which this improvement is quantified is made. Moreover, the authors use a quoted upper bound in fidelity from IBM ( a superconducting device), but the general networked architecture seems to be based on "a quantum control architecture tailored to a unique class of quantum resources featuring a spin-photon (Appendix A.8, Fig.6) interface conducive to remote entanglement routing" and has applications to trapped ions or neutral atoms. Moreover, the reference (IBM Website) does not provide any details on this upper bound used in the manuscript. Fidelities for networked architectures generally seem to be lower than this as shown in Ref. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.110501 (fidelity of 94%) and so some more justification or a clearer explanation would strengthen the manuscript. Additionally, the authors work simulates real physical interactions and the success of the proposed Transformer-on-QuPairs model relies on inhomogeneity in the fidelities (i.e. a high sigma(F)), but little discussion, of why such inhomogeneity arises in physical systems, nor any reference to existing work which shows qubit inhomogeneity is made. Providing a stronger case for the relevance of the highly inhomogeneous fidelity scenario would strengthen the benchmarks significantly.

The results in table 2 are somewhat confusing. It seems as though for a perfectly homogeneous fidelity, the different methods should perform exactly the same, but there are small but non-negligible differences. Is this a real result? Given the two uncertain (two sigma deviation) is larger than the absolute differences across methods it is not clear how to interpret these results. Some more clarity from the authors would help.

The framing of the problem as an NP-hard problem is not entirely clear. The authors connect the problem to the Minimum Weight Connected Subgraph Problem (MWCSP), but the reduction is not explicitly shown, and the assignment of a zero weight to all terminal nodes is confusing. A more rigorous explanation of the problem's complexity and its connection to MWCSP would be beneficial.

### Questions
What are the limitations of specific approaches when scaling the number of qubits in terms of runtime/memory, and how do they affect the results presented in Table 3?

How does the manuscript account for the inhomogeneity in fidelities that the Transformer-on-QuPairs model advantage relies on, and what causes this inhomogeneity in real quantum systems? Could examples and explicit references be provided.

Can the authors further justify the use of an upper bound in fidelity from superconducting qubits for a networked architecture?

Why do the methods in Table 2 show small differences in performance even for perfectly homogeneous fidelities, and how should these results be interpreted given the uncertainties?

Why is the static minimum spanning tree (MST) approach... anticipated to be an effective heuristic when the quantum system’s coherence time is indefinitely long or has a deterministic success probability during entanglement attempts.? Could the authors elaborate on this.

### Soundness
2

### Presentation
2

### Contribution
3
