# Equivariant Quantum Graph Neural Network for Mixed-Integer Linear Programming

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
Mixted-integer linear programming (MILP) is an essential task for operation research, especially for combinatorial optimization problems. Apart from the classic non-learning solvers that often resort to heuristics, recent machine learning-based models have been actively studied, and graph neural networks (GNNs) have been dominantly adopted. However, recent literature has shown that the GNNs based on message passing mechanism suffer fundamental expressiveness limitations in MILP instance representation, in the sense that two different MILP instances could be eventually embedded into exactly the same feature. In this paper, we resort to the quantum mechanism and develop a tailored quantum counterpart of GNNs, called equivariant quantum GNN (EQGNN), which can guarantee to distinguish any two MILPs, i.e., leading to different graph embeddings. EQGNN designs a novel quantum parametric circuit that can encode node and edge features while maintaining the property of permutation equivariance. To enhance the expressivity power of the model, we also introduce an auxiliary layer with an optional number of auxiliary qubits. Experimental results demonstrate the effectiveness of the method in solving MILP problems and the trainability of the model with increasing system scale. Compared with GNN, EQGNN can achieve better separation power and generalization performance with fewer parameters.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a quantum counterpart of GNN, called equivariant quantum GNN (EQGNN), that is tailor-made for solving mixed-integer linear programming (MILP). The key feature of EQGNN is the preservation of the permutation equivariance in the GNN. This feature allows EQGNN to demonstrate better expressiveness compared to other GNNs, in the sense that EQGNN can distinguish pairs of *foldable* MILPs that existing GNN design is not able to. Therefore, EQGNN can accurately predict the feasibility of general MILPs. Extensive numerical experiment results are presented to show that EQGNN has faster convergence and attains better generalization with less data compared to GNNs.

### Strengths
This work presents a novel variant of Graph Neural Network (GNN) based on quantum parametric circuits. This so-called Equivariance Quantum Graph Neural Network (EQGNN) consists of the feature encoding layer, graph message interaction layer, and optional auxiliary layer, all expressed as parametrized quantum circuits. This new design allows EQGNN to overcome a fundamental limitation of traditional GNNs (i.e., GNNs can not distinguish pairs of foldable MILP instances). Compared to other quantum GNN architecture, EQGNN incorporates the feature of the edges, which renders it a problem-inspired model and does not suffer from the barren plateau issue. 

The numerical results appear to be very strong. Compared to prior arts, EQGNN demonstrates much better separation power for foldable MILP instances. For general MILP tasks, EQGNN has better predictions for the optimal value with much fewer parameters (~100), while traditional GNN requires approx. $\sim 10^4$ parameters to achieve similar performance. 

The paper is well-written and the mathematical formulation is easy to follow.

### Weaknesses
In section 3.6, the authors claim that "we can prove that the whole model conforms to permutation equivariance by ensuring that each layer conforms to equivariance". However, I was not able to find a theorem statement in the PDF (including appendices).

Many plots use the "rate of errors" as a performance metric. How is this "rate of errors" defined and evaluated in the experiments? Does it require the ground truth of the tested MILP instances? How to get the ground truth?

### Questions
1. From the numerical experiments, it appears that an EQGNN deployed on a small- to intermediate-size parametric quantum circuit outperforms a traditional GNN-based model with many more parameters. Can we directly employ this new GNN design on a classical computer to outperform other models requiring similar classical computing resources? 

2. Is the equivariance feature unique to quantum parametric circuits? If not, I wonder if it's possible to obtain a quantum-inspired equivariance GNN for MILPs that is native to classical computing architecture but still outperforms traditional GNN models.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission presents Equivariant Quantum Graph Neural Network (EQGNN), a Variational Quantum Circuit (VQC), as a parametric model for data-driven Mixed Integer Linear Programming (MILP) solutions. The weighted bipartitle graph for MILP contains two types of nodes for decision variables and constraints, with the edges only connecting nodes of different types. Such a constructed graph is used as the input for VQC to predict the feasibility, optimal value and solution for MILP. The authors show that the feasibility, optimal value and solution to MILP are either equivariant or invariant to the permutation on the order of nodes and edges of the graph, and propose a VQC to encode the information into quantum states, which satisfy the equvariant or invariant properties of the weighted bipartitle graph representation of MILP. The main idea is the diagonality of $R_{zz}(\theta)$ gate and to use a shared set of parameters for nodes of the same type. Experiments show the potential capability of proposed model to solve MILP problems.

### Strengths
1. Carefully chosen gates for feature encoding and massage passing in EQGNN help achieve permutation equivariance or invariance, with the corresponding reasoning. 
   
2. Experiments were performed to demonstrate the potential of EQGNN for MILP.

### Weaknesses
### weaknesses:
 1. In Section 1, the claim "We propose a so-called (for the first time) Equivariant Quantum Graph Neural Network (EQGNN) capable of representing general MILP instances without the need for dataset partitioning." lacks clarity. Specifically, the meaning of "without the need for dataset partitioning" and its significance to the proposed method are not adequately explained. It is unclear how this claimed advantage differentiates EQGNN from existing approaches and what practical implications it holds for solving MILP problems. The authors should elaborate on the specific challenges associated with dataset partitioning in the context of MILP and how EQGNN overcomes them.

2. The assertion in Section 1 that "We both theoretically and empirically show the separation power of EQGNN can surpass that of GNNs in terms of representing MILP graphs." is not fully substantiated. While the paper presents empirical results, it lacks a rigorous theoretical analysis of EQGNN's separation power. A formal comparison of the representational capacity of EQGNN and GNNs, perhaps using graph isomorphism or a similar framework, would strengthen this claim. Without such theoretical grounding, the statement remains a conjecture.

3. The comparison of parameter counts between classical and quantum neural networks in Section 4.1 requires further clarification. The rationale behind the chosen criteria for comparing these fundamentally different models is not explicitly stated. Additionally, in Section 4.2, the selection of classical neural networks with 2,096 and 7,904 parameters as baselines appears arbitrary without a clear justification. A more meaningful comparison might involve contrasting the proposed model with established non-data-driven methods for solving MILP, providing a clearer benchmark for performance evaluation.

4. The paper contains several typographical errors, inconsistencies, and instances of unclear notation. For example, the term "Foladable MILP instances" in Section 2 is likely a misspelling. In equation (4), $R_x$ gates are used for encoding, while Figure 5 depicts $R_z$ gates for the same purpose. The indexing of decision variables and constraints should be consistent throughout the paper, particularly in the bipartite graph representation in Section 2. These issues detract from the paper's overall clarity and should be addressed in a revised version.

### questions:
 1. Is it possible for two MILP problems with distinct feasible/optimal solutions to be encoded into identical quantum states using the same VQC parameters? This question probes the potential for information loss or ambiguity in the encoding process.

2. While node permutation equivariance or invariance is inherent to graph representations, the paper should explicitly attribute the claimed generalizability, expressiveness, and efficiency to either EQGNN or VQC. What are the core technical contributions that distinguish this work from prior art? How do these contributions align with the existing landscape presented in Table 1? Furthermore, the omission of the referenced work by Schatzki et al. (2022) from Table 1 needs justification.

3. A detailed description of how the VQC learning problems are formulated for MILP feasibility, optimal solutions, and optimal values based on the proposed EQGNN is necessary. This should be included either in the main text or the appendix. The authors should also elaborate on how binary measurements can approximate the often non-discrete optimal values. If multiple measurements are employed to recover the approximated quantum state, the number of measurements required for the results presented in the experimental sections should be clearly stated.

4. How expressive is the proposed model? A quantitative measure or a theoretical analysis of the model's capacity to represent complex relationships within MILP instances would be beneficial.

### Questions
1. Is that possible for two MILP problems with different feasible/optimal solutions to be encoded into the same quantum state with the same VQC parameters? 

2. Node permutation equivariance or invariance comes naturally with graph representations. The authors need to clearly state whether the claimed generalizability, expressiveness, and efficiency should be attributed to EQGNN or VQC? What are the main technical contributions? How shall they be positioned in the context of Table 1? Also, why the mentioned reference Schatzki et al. (2022) was not included in Table 1? 

3. The author should clearly describe how the VQC learning problems are formulated for MILP feasibility/optimal solutions/optimal values based on the proposed EQGNN respectively either in the main text or appendix. The author should also clearly specify how the binary measurements can be used to approximate the optimal value which is often a non-discrete value. If multiple measurements are performed to recover the approximated quantum state of the VQC, the author should also clearly specify how many measurements are needed for the results provided in experiment sections. 
   
4. How expressive is the proposed model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes equivariant quantum graph neural networks (EQGNN) to solve mixed-integer linear programming (MILP) problems. In particular, their EQGNNs solve the issue of GNNs not being able to distinguish between so-called foldable instances; that is, MILP instances which have the same MILP-induced graph (up to permutations).
It is emphasized that their ansatz respects equivariance, since a permutation of the graph vertices results in the same permutation of the variables.
In addition, they conduct experiments which show good trainability and several other advantages over standard GNNs, including faster convergence, fewer parameters needed, and better generalization.

### Strengths
- In general, the presentation is fairly clear, and I can easily understand the overall motivations and contributions of this work.
- They are attempting to solve mixed-integer LP in an interesting and unique way. At the least, I have not seen MILPs solved this way.
- The experiments seem to be somewhat promising, showing benefits over GNNs.

### Weaknesses
 - I feel that many parts of the construction of the ansatz is not well motivated. However, this seems to be a typical issue for quantum neural networks, perhaps even moreso than classical neural networks.
- Unless I am misunderstanding something, I feel that this permutation equivariance is not particularly insightful. For instance, the equivalent circuits in Figure 7 seem obvious, just that the circuit wires are drawn to either have different input order or output order. Perhaps it would be more useful to show a construction that fails to satisfy permutation equivariance.
- There are some details that I feel are important (at least for understanding) but left out (see Questions).

### Questions
Comments:
- In the definition of the feasible region $X_{fea}$ in Section 2, the constraint $l \leq x \leq u$ is missing.
- In Figure 6, I feel the circuit for $R_{zz}$ gates is somewhat misleading. The cross symbol is typically used for the SWAP gate. Also, the $R_{zz}$ is symmetric with respect to the two qubits it acts on, so there is no difference between choosing which is the target and which is the control qubit.
- Typo in the sentence "the identical parameteric gates are acted when the order of input nodes."
- Typo in the sentence "We now study the effect of width of the circuit increased"

Questions:
- It is not clear to me why there are instances of MILP that cannot be distinguished by GNNs, as in Figure 2. While the vertex degrees are the same, the connectivity is different, so shouldn't GNNs treat them differently? Perhaps I am missing something about how standard GNNs deal with this problem in the context of MILP.
- Why choose $R_{zz}$ over other two-qubit gates that commute with itself such as $R_{xx}$ or $R_{yy}$? This goes back to the weakness of the circuit construction not being well motivated.
- In the feature encoding layer, is there any reason why $R_x(c_i)$ and $R_x(u_i)$ as well as $R_x(l_i)$ and $R_x(\epsilon_i)$, are applied to different qubits?
- Out of curiosity, how the MILP instances are generated to be foldable or unfoldable? I suppose this requires something like solving the graph isomorphism problem.
- When predicting the solution vector, what is the actual representation of the classical information after reading out the qubits? For example, does a 2-qubit state for $v_1$ correspond to integers 0,1,2,3? Also, what happens when reading out a result that does not satisfy the constraints?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a class of quantum-based graph neural networks equivariant under permutations of the vertices of the graph. The authors argue that this class of neural networks are effective in solving mixed-integer linear programming (MILP) problems, and back up this intuition with numerics. They also check in their numerics the trainability of their introduced class of quantum neural networks.

### Strengths
The authors study the trainability of their model; due to its large symmetry group (permutation invariance), the authors believe the model is trainable (when there are few auxiliary qubits) and, indeed, demonstrate it empirically. The authors never state it, but I believe this is essentially due to the results of arXiv:2210.09974, which give trainability guarantees for permutation invariant quantum machine learning models.

### Weaknesses
I am more skeptical of the numerical results demonstrating a separation in expressive power between the EQGNN and the GNN the authors cite from (Chen et al., 2023b) (though admittedly I am not an expert on GNNs). The divergence of testing performance in Fig. 10 seems to me that the classical GNN is overfitting, potentially due to the order of magnitude difference in the numbers of parameters between the quantum and classical models. I highly recommend the authors perform supplemental numerics where these parameter counts are brought in line to control for this behavior. It is also unclear to me whether there is actually any theoretical quantum advantage when the quantum model has no auxiliary qubits as arXiv:2211.16998 gives efficient classical simulation algorithms for permutation-invariant quantum systems and machine learning models. This might limit the utility of the introduced quantum model to the case where there are many auxiliary qubits, which then runs into problematic training behavior as the authors point out.

A much more minor point, but there are also many typos: "and yielding" at the bottom of page 3, "expressivity power" in the abstract, "guarantee to distinguish" in the abstract, and "TorchQauntum" at the bottom of page 7 are some that I found.

### Questions
What are the connections between this work and previous work on permutation-invariant quantum machine learning models (cited above)? What explains the terrible generalization performance of the classical GNNs? The authors should perform additional numerics fixing the parameter counts of the classical and quantum models to control for this behavior.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
