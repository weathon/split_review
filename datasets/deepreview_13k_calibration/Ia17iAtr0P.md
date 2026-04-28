# Physics-constrained Graph Symbolic Regression

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 8, 3

## Abstract
As data-driven scientific discovery increasingly demands explainable over ‘black-box’ machine learning (ML) methods, Symbolic Regression (SR) that derives analytical expressions can help identify key functional dependencies in complex systems. However, traditional SR methods often suffer from (a) inefficient exploration due to their inability to compress the search space of equivalent expressions, and (b) non-physical solutions that violate fundamental physics constraints. We here introduce a symmetric invariant representation of candidate analytical expressions using a Symbolic Graph (SG), on which the Symbolic Graph Neural Network (SGNN) encodes operators, symmetries,   constraints and constant fitting knowledge. We further develop reinforcement learning (RL) algorithms with Monte-Carlo Tree Search (MCTS) on our SGNN for SR. Such a physics-constrained graph symbolic regression (PCGSR) method effectively compresses the search space for efficient SR. Experiments on synthetic and real-world scientific datasets demonstrate the efficiency and accuracy of our PCGSR in discovering underlying expressions and adhering to physical laws, yielding physically meaningful solutions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a symbolic regression method “PCGSR” that improves the symbolic expression search space with a better representation (“symbolic graph”) and imposes constraints to yield physical solutions. Experiments on two SR benchmarks validate the approach of using the symbolic graph representation (with deep RL + MCTS) and experiments on predicting copper lattice energies validate the efficacy of imposing domain knowledge constraints.

### Strengths
1. Demonstrates the utility of a good representation (“symbolic graph”) and, to a lesser extent, neural guidance (deep RL + MCTS), in searching for a good symbolic expression.
2. Shows a potentially interesting application (copper lattice energy prediction), though I have reservations regarding the practical interest of this application (see Weakness 3 below).

### Weaknesses
1. The method does not fully implement what the method is claimed to implement. In particular, despite physics constraints being the second main selling point of the paper (and in the title of the paper), no systematic way of doing that was given. No physics constraints were imposed in the experiments on the AI-Feynman and Nguyen benchmarks. On the copper crystal benchmark, the only constraints are either very specific to the experiment in question ($f(r) \to \infty$ as $r \to 0^+$), or just reimplement something that already exists (correct dimensions, from AI-Feynman). (By the way, I do not consider trivial mathematical constraints mentioned in the paper like “argument of log is positive” or “energy function must output a scalar” to be “physics constraints”. These are just basic conditions that need to be met for SR to even be possible at all.) See also question 2 below for my doubts on the use of the term “physics constraints” the way the paper used it.
2. Furthermore, incorporating domain knowledge as constraints has already been explored in many ways in the literature. See, for example, a brief review given in Section 1.2 of Fox et al. 2024 [1].
3. The copper crystal benchmark shows PCGSR’s ability to find a formula for the energy of 32 copper atoms in a lattice, after being trained on DFT data from 32 copper atoms in a lattice. Such a formula is not of much practical use since it does not apply to anything other than 32 copper atoms in a lattice, so the experiment is not a good demonstration of the practical applicability of PCGSR. (By contrast, actual computational chemistry methods such as DFT are applicable to materials/molecules in general.) Although the paper does show results of transferability to a copper lattice compressed volumetrically by 50%, this compressed lattice is not something that can physically exist in the real world and is thus not of practical interest either. An experiment that would better showcase PCGSR would be to train on data from a non-trivial class of materials/molecules to discover 1 formula that accurately describes all of them.
4. Another main selling point of the paper is that it addresses the issue where previous methods do not search efficiently because of semantically equivalent expression trees. However, this issue has already been addressed in the literature in many ways—see the brief review given in the introduction section of Huynh et al. 2016 [2].
5. Another main selling point of the paper is its use of neural-guided search (deep RL + MCTS). This idea is also not new. See, e.g., Landajuela et al. 2021 [3].
6. The results in Table 1 are not particularly strong given that PCGSR does not outperform SPL or NGGP with great statistical significance ($1.3\sigma$ and $1.0\sigma$, respectively).

### Questions
1. The introduction of deep RL with the SGNN feels quite costly to me. What do the tradeoffs look like for the accuracy gains from the SGNN vs. the extra computational costs incurred? Or are these costs balanced out by the gains from the extra guidance from the SGNN in the later parts of the training? Table 2 shows # of evaluations as a cost metric, but that doesn’t take into account the forward and backward passes of the SGNN, so I wonder what the wall-clock time looks like with vs. without the SGNN?
2. The paper frequently mentions that the SGNN encodes physics constraints, but what people typically think of as “physics constraints” are a lot more involved than the ones considered. For example, I think of time/spatial symmetry and conservation of energy/momentum etc. Do you have a systematic way to incorporate constraints likes these in PCGSR?
3. It would be nice to contextualize the results in Table 3. What is the typical MAE in DFT calculations? What is typically the accuracy needed for an energy calculation to be practically useful?
4. What do the costs look like in Table 1 (e.g. # evaluations, wall-clock time)? Although the max # evaluations (500k) and the time limit (24hrs) were the same for all methods compared, it could be that, on easy tasks, PCGSR takes longer than the baselines. It would be helpful to see a breakdown over cost, e.g., the recovery rate when the time limit is 2, 4, 6, 12, 24 hours.

Corrections:
1. Abstract line 1: “explainable” -> “explainability”
2. Line 118: $f \subset Q$ – I don’t think “$f$ is a subset of $Q$” is the intended meaning here?
3. Lines 230 & 239: “We” -> “we”. Line 321: “we” -> “We”
4. Lines 421–424 (about Pauli’s exclusion principle): There’s a misunderstanding of Pauli’s exclusion principle here. The phenomenon described in lines 421–424 is just electrostatic repulsion (Coulomb’s law) and has nothing to do with Pauli’s exclusion principle. Pauli’s exclusion principle states that two fermions cannot be in the same quantum state. As an example, electrons in an atom cannot occupy the same quantum state; as a result, because each electron has two spin states, every atomic orbital can hold at most two electrons, resulting in the structure that we see in the periodic table (2 elements in row 1, 8 elements in row 2, etc.).

Suggestions:
1. Given my criticisms of the paper, the following reworked story would be more convincing to me: "We show that using a graph neural network to predict next actions in neural-guided MCTS outperforms previous approaches to neural-guided search for SR." That's it--nothing about the symbolic graph (Weakness 4) or physics constraints (Weaknesses 1-3).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
•	This paper introduces a new method for Symbolic Regression, termed Graph Symbolic Regression (SGN). The authors propose using a Graph Neural Network (GNN) to represent mathematical expressions as expression graphs (EGs), addressing inefficiencies in traditional symbolic regression by reducing the search space through symmetry and permutation invariances.
•	The authors also incorporate unit-consistency constraints to ensure that resulting expressions are physically meaningful.
•	The method is benchmarked against existing methods using both synthetic datasets and real-world applications.

### Strengths
•	By leveraging symmetry and permutation invariances, the proposed GSR method effectively compresses the search space, enabling more efficient exploration of possible expressions.
•	The inclusion of unit-consistency constraints ensures that the expressions produced are physically meaningful.
•	The method is evaluated across diverse datasets and outperforms several existing symbolic regression methods.
•	The application on the DFT dataset is both significant and engaging.

### Weaknesses
 •	The two main components, permutation invariances and unit-consistency constraints, are conceptually unrelated and could potentially be split into separate papers, each addressing a distinct methodological contribution.
•	The proposed permutation invariances appear to apply only to addition, multiplication, and power operators. How would this method handle trigonometric operators, for instance, with cases like ( \sin(x + \pi/2) = \cos(x) )? Furthermore, it's unclear if the method can handle more complex equivalencies, such as those involving the distributive property (e.g., a*(b+c) = a*b + a*c), which are also common in mathematical expressions.
•	Although Figure 2 is clear, it’s unclear how Equation 2 aids the simulation step in MCTS, or how it relates to Equation 6 in the appendix. Specifically, the connection between the prior probabilities (P) produced by the SGNN and their use in guiding the MCTS search is not well-explained. The role of the predicted reward 'r' in the MCTS simulation also needs further clarification, particularly how it influences the selection of nodes during the tree traversal.
•	Previous work, including the original DSR paper, has implemented constraints to eliminate infeasible equations, and some other studies already utilize unit constraints to filter out physically meaningless equations. How does Section 3.4 offer a novel approach here? The description lacks a clear explanation of how the proposed method differs from existing constraint-based approaches, making it difficult to assess the novelty of this contribution.

### Questions
•	Could you clarify the third point in the Weaknesses?
•	Could you also elaborate on the rationale behind the SGNN objective (Equation 5)?
•	A recent paper, Scaling Up Unbiased Search-based Symbolic Regression (IJCAI2024), also proposes graph representations to replace tree structures. Could you compare SGN’s approach with theirs?
•	The literature review on constraint-based methods could be strengthened. The claimed difference between your work and "Deep Symbolic Regression for Physics Guided by Units Constraints: Toward the Automated Discovery of Physical Laws" requires clarification. For example, they use a design constraint to exclude infeasible next-step tokens without using a penalty, which contrasts with your summary.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a symmetric invariant data structure, the Symbolic Graph, replacing expression trees in symbolic regressions. It also develops a GNN to encode physics constraints and guide the MCTS algorithm. Numerical experiments on two benchmarks and one synthetic dataset show the performance improvement of the proposed method.

### Strengths
1. The presentation, visualization, and the design of real-world experiments.
2. The idea of handling symmetric invariance by a new data structure.

### Weaknesses
1. The necessity of GNN. It seems that the proposed symbolic graph(SG) can be viewed as a tree with more branches and special nodes (e.g. summation, directed minus). If this is true, then the SG (with trivial modifications) can also be processed by existing non-graph neural networks designed for expression trees. The ablation study shows that the proposed PCGSR achieves higher recovery rates than MCTS-Tree, but only by 1.25%. This improvement appears marginal, especially since MCTS-1 also outperforms PCGSR by 1.25%. Furthermore, while PCGSR reduces the number of evaluations of MCTS-* by about 25%~30%, which speeds up training, this speedup might be insignificant in practice, given that multi-processing is typically applied in the search. It is unclear if MCTS-* can achieve comparable efficiency to PCGSR with a 30% or 50% increase in CPU cores, and potentially without GPU usage in some cases (MCTS-1, MCTS-Tree-1).
2. The necessity of physics-constrained NN. It seems that the NN is self-trained to learn the physics constraints from hand-crafted rules. But If the rules are simple and explicit, then one can bypass the self-training and directly encode the rules into the MCTS process. If the rules are complex or unknown, then how to train the network to learn them? The physics-constrained NN appears to be an interpolation of pre-defined rules to alleviate reward sparsity, which benefits efficiency. However, the numerical experiments do not strongly support this statement.

### Questions
1. Why were the NNGP and SPL baselines not compared in the real-world experiment (Table 3)?

### Soundness
2

### Presentation
3

### Contribution
2
