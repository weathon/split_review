# Rethinking the symmetry-preserving circuits for constrained variational quantum algorithms

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 6, 5

## Abstract
With the arrival of the Noisy Intermediate-Scale Quantum (NISQ) era, Variational Quantum Algorithms (VQAs) have emerged as popular approaches to obtain possible quantum advantage in the relatively near future. In particular, how to effectively incorporate the common symmetries in physical systems as hard constraints in VQAs remains a critical and open question. In this paper, we revisit the Hamming Weight (HW) preserving ansatz and establish the links from ansatz to various symmetries and constraints, which both enlarges the usage of HW preserving ansatz and provides a coherent solution for constrained VQAs. Meanwhile, we utilize the quantum optimal control theory and quantum overparameterization theory to analyze the capability and expressivity of HW preserving ansatz and verify these theoretical results on unitary approximation problem. We conduct detailed numerical experiments on two well-studied symmetry-preserving problems, namely ground state energy estimation and feature selection in machine learning. The superior performance demonstrates the efficiency and supremacy of the proposed HW preserving ansatz on constrained VQAs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work discusses incorporating symmetries as hard constraints in ansatz design for Variational
Quantum Algorithms (VQAs). In particular, the authors revisit the Hamming Weight (HW) preserving ansatz. By adopting Dynamical Lie Algebra (DLA) as a quantum optimal control theory and over-parameterization theory based on the maximum rank of quantum Fisher information matrix, one can quantify (and further ensure) the expressivity and capability of the proposed symmetry-preserving ansatz. These theoretical guarantees are verified on the unitary approximation problem. Moreover, the authors can demonstrate better performance on ground-state energy estimation ( need to preserve electron number) and feature selection as a constrained QUBO problem (preserve number of features), both using VQE.

### Strengths
A novel idea to use Dynamical Lie Algebra and over-parameterization theory for Parametrized Quantum Circuit (PQC) to design symmetry-preserving VQA ansatz.
Very clear explanation of the theoretical tools used.
The authors conduct extensive numerical studies showing positive results.
A bottom-up approach to guide quantum circuit design compared to the previous top-down approach [1]. The latter uses a different sampling-based definition of expressivity and entanglement capability to guide general-purpose circuit design, but actual task performance could vary a lot.
Hard constraints are more favorable than soft constraints in some industrial use cases, where solution validity and robustness are priorities.
[1] Sim, Sukin, Peter D. Johnson, and Alán Aspuru‐Guzik. "Expressibility and entangling capability of parameterized quantum circuits for hybrid quantum‐classical algorithms." *Advanced Quantum Technologies* 2.12 (2019): 1900070.

### Weaknesses
Regarding the literature review, it is not clear to me why the authors chose to categorize some previous work based on XY-mixer QAOA [1-2] as soft constraints. Their circuit is composed of a problem Hamiltonian layer (ZZ gates) and a mixer layer, both preserving the Hamming weight instead of adding a penalty to the cost function.
One of my biggest concerns is when we run this framework on NISQ hardware or noisy simulation. A bit-flip (X) error would suddenly break the Hamming distance. Will this be a big problem or not? It will be better to see more results along this consideration.
Need more discussion on the trainability of the proposed ansatz and Barren Plateau (BP) phenomenon. It makes intuitive sense to think of better trainability compared to HEA since it is only exploring a constrained subspace. The optimization problem should be easier. Previous work [3] showed that a compound layer consisting of FBS gates could lead to a gradient decay only polynomially. Will the same conclusion hold for this work?
Some numerical experiment details don't make sense to me. For example, why did the authors choose the penalty weight in Eq. 16 as \alpha = [0.5, 1, 5, 10]. To my best knowledge, people usually set this empirical parameter to a much larger value like 100.

### Questions
Can you explain why you use gate infidelity as the performance metric for the unitary approximation problem but plot Success Probability in Fig. 2? I guess the authors are converting infidelity of 1e-5 as log10(1e-5)/log10(1e-10)=0.5. Please make it clear in the paper.
It would be nice if the author could discuss connections of their HW preserving VQE with XY-mixer QAOA or other constrained QAOA. And maybe apply the theoretical tools used here to improve those work?
What is the basis set used in ground-state energy estimation (such as STO-3G) to discretize the computation space?
I believe the second test case, feature selection, is not a typical benchmark for VQAs. Is this a classically hard problem? Can you say more about why choose this test case?

Some Typos:
--Right below Lemma 4.1. "Ramakrishna et al. (1995) has shown that if the dimension of DLA" instead of "Ramakrishna et al. (1995) has shown that if the dimension of the dimension of DLA"
The y-axis in Fig. 3 and Fig. 7 should be in logarithmic scale
Right below Appendix B.1. 'qubit'

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Different families of Hamming weight (HW) preserving quantum circuits are examined in the context of general variational algorithms. A theoretical framework is developed for understanding when a given circuit family is sufficiently expressive to generate arbitrary symmetric transformations, and these various circuit families are experimentally compared against each other and against different baseline models in a variety of problems.

### Strengths
* The paper includes a large number of results of both a theoretical and experimental nature, that should be useful for someone wanting to use HW-preserving quantum circuits. Overall, this will likely encourage the use of these type of symmetric circuits in the context of more general classes of variational problems than they have been used in the past.

* The experimental tasks are well chosen, with the unitary approximation, ground state energy estimation, and feature selection problems being representative of problems from quantum computing, quantum chemistry, and machine learning. The baseline methods used for comparison seem to be well chosen, and to the best of my knowledge are representative of the methods actually used in these various subject areas.

* The paper is well-written, both in terms of its overall structure and its writing. Given the amount of material presented, this is critical for being able to understand the paper's results. The appendices are quite helpful for providing background and additional detail about the results.

### Weaknesses
 * The premise of the paper is a bit atypical for conference submissions, in that it isn't "selling" a new model or method developed by the authors. Rather, the goal of the paper seems to be improving the community's understanding regarding the expressivity and performance of HW-preserving circuits in general. I think this is a valuable contribution, but I could see other reviewers pointing to a lack of novelty due to this unorthodox aim.

* There is a lot of material that is packed into a limited space, and while I found the presentation to help a lot with this, the results still take some time to digest and understand in detail.

* Figure 4 compares a large number of different circuit ansatzes, but many of these overlap with each other and are barely visible (e.g. the RBS-full points). It would helpful to revise this figure to permit easier viewing of all of the baseline results, for example by varying the colors, size, and/or ordering of the plot markers.

### Questions
I don't have any particular questions for the authors.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies ansatz for variational quantum algorithms with the requirement that they preserve Hamming weight. They test the expressibility for the task of unitary approximation, where they show that the expressibility of these ansatz is the same as predicted (in terms of the number of parameters needed). In addition, experiments demonstrate the effectiveness of their approach on two different tasks: ground state preparation and feature selection.

### Strengths
- This paper nicely summarizes and makes clear the idea of using Hamming weight (or in physics terminology, excitation) preserving ansatz for variational quantum algorithms. The numerical results verify the accuracy of the theory, which characterizes the expressibility of these ansatz.
- The experiments are nice, showing a modest improvement over existing methods.

### Weaknesses
 - Typos: "relative" should be "relatively" throughout
- Typo: In Figure 2, "Haar measurement" should be "Haar measure"
- Typo: "Hartree-Fork"
- Based on common gate sets of real machines, I feel the BS gate is quite artificial. It might make more sense to use parameterized $XX$ rotations with single-qubit $Z$ rotations. If the intention is to perform VQAs on near-term machines, then one might want to use more native instructions than the decompositions shown in Fig 5 and Fig 6. Specifically, the use of CNOT gates in the BS gate decomposition appears unnecessarily complex, given that direct two-qubit interactions are often available on hardware.
- Related to the above point, the decomposition of the BS gate is addressed as a possible limitation. I am pretty sure a better decomposition is possible using $XX$, $YY$ and $ZZ$ rotations. The provided decomposition using CNOTs and single-qubit rotations is not ideal for many architectures, and exploring alternative decompositions could significantly improve the practical applicability of the proposed ansatz.
- I think this idea of preserving the Hamming weight is not very new, and the theoretical results are not very surprising to me. For this reason, I feel the contribution of this work is not so large, although the proposed ansatz appear to perform better than existing ones.

### Questions
- In Equation 8, should the maximization be over $M$ such that $M\geq M_c$?
- Where does the construction for the BS gate come from?
- Throughout this paper, it is stated that this is a "revisiting" of the Hamming weight preserving ansatz. What is the status of the previous work using these ansatz, and what are the specific improvements made in this paper compared to previous proposals?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors review the known Hamming Weight (HW) preserving ansatz and discuss how it fits into the dynamical Lie algebra framework of (Larocca et al., 2023). The authors give an elementary gate set that they show generates all HW preserving gates (i.e., that gives "full controllability"). The authors then perform numerics demonstrating the practical utility of the HW preserving ansatz.

### Strengths
The authors give a nice review on the HW preserving ansatz and link it to the well-known line of results discussing when quantum machine learning (QML) models are trainable by examining their controllability. The authors also describe a set of gates to parameterize the HW preserving ansatz in a controllable way.

### Weaknesses
Most of the paper is review. For instance, arXiv:2303.16585 (which the authors cite) already demonstrates that the HW preserving ansatz is efficiently trainable. Though never explicitly linked to (Larocca et al., 2023) in arXiv:2303.16585, the intuition that the trainability comes from the large symmetry of the ansatz is stated and described: see, e.g., their Figure 3. The numerical experiments, while demonstrating the practical utility of the HW preserving ansatz, largely replicate the type of analysis already performed in prior work, just in a different context. The core contribution of the paper, which is linking the trainability of the HW preserving ansatz to subspace controllability, is not sufficiently novel given that the trainability of this ansatz was already established. The authors' analysis of the trainability of the HW preserving ansatz, while potentially providing a tighter bound, does not introduce a fundamentally new perspective or result. The specific advantage of using the HW preserving ansatz for constrained VQAs, as opposed to the finance problems considered in arXiv:2303.16585, is not clearly articulated beyond the claim that it is more suitable, without a detailed explanation of why this is the case.

### Questions
What are some advantages to directly linking trainability to subspace controllability given the trainability of the HW preserving ansatz was already known?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
