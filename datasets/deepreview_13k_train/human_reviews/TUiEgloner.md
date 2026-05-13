# Adaptive Learning of Quantum Hamiltonians

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
The challenge of learning representations for quantum Hamiltonian systems resides at the intersection of quantum information and learning theory. Viewed through the lens of learning theory, this task can be regarded as the non-commutative counterpart to learning graphical models. In our research, we design and analyze adaptive learning algorithms, including the quantum iterative scaling algorithm (QIS) and gradient descent (GD), for the Hamiltonian inference problem using adaptive Gibbs state oracles. Our principal technical contribution centers on the thorough analysis of their convergence rates, involving the establishment of both lower and upper bounds on the spectrum of the Jacobian matrix for each iteration of these algorithms. Furthermore, we explore quasi-Newton methods to enhance the performance of both QIS and GD. Specifically, we propose the use of Anderson mixing and the L-BFGS method for QIS and GD, respectively. These quasi-Newton techniques exhibit remarkable efficiency gains, resulting in orders of magnitude improvements in performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the learning of quantum Hamiltonians using adaptive Gibbs state oracles. This paper's approach is based on quantum iterative scaling (QIS) and gradient descent (GD) with a more tailored analysis and closed-form formula for the
Jacobian.   The authors modified convergence rate analysis and studied heuristic algorithms for acceleration, including the quasi-Newton method. The claims have been supported by numerical experiments.

### Strengths
The main strength of the paper is in providing explicit Jacobian expressions for the adaptive algorithms used in Hamiltonian learning. Moreover, the convergence rate analysis derived in this paper is beneficial in understanding the Hamiltonian learning problem.

### Weaknesses
It seems that the paper's novelty is limited to some extent. Major results rely heavily on existing works such as Liang et al. (2004). Specifically, the main theorems in Section 4 are extensions of the analysis in the classical setting. It appears that the paper's results are restricted to the problem they study, and the contribution is only to provide an explicit formula for the Jacobian. The analysis, while technically sound, does not seem to offer significantly new insights into the fundamental challenges of quantum Hamiltonian learning beyond what is already known in the classical setting. The core techniques, such as the iterative scaling and gradient descent, are well-established, and the adaptation to the quantum domain, while non-trivial, does not introduce a fundamentally new approach. The explicit Jacobian expression, while useful, feels like a necessary step in applying existing methods rather than a major breakthrough.

### Questions
Can you further explain the main novelty of the analysis compared to that of the classical settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies quantum iterative scaling and gradient descent algorithms to learn the Hamiltonian of a quantum system by solving the maximum entropy problem or its dual. 
They assume the setting where one has access to the expectation values of the terms of the Hamiltonian in the Gibbs state, as well as an oracle to prepare a Gibbs state adaptively to prescribed values of the Hamiltonian parameters.
The main result is to compute the converge rate of the algorithms as a function of the number of parameters. They also discuss acceleration of the algorithms by quasi Newton methods, that are supported by experiments showing the improvements.

### Strengths
- Well written
- Rigorous convergence analysis
- Novel bound on the Hessian of the free energy
- Practical consideration on acceleration by quasi-Newton methods

### Weaknesses
 - Problem setting is not clearly motivated. While Hamiltonian learning is a central problem in quantum computing, it is not clear to me why one would prefer to look at the Hamiltonian inference problem where one has to prepare adaptively a Gibbs state and measure observables in it
- Preparing adaptively Gibbs states and measure observables in it is computationally hard - at least beyond some critical temperature, as discussed by the authors in the conclusions. See also the very recent work [https://arxiv.org/abs/2310.02243] for an efficient algorithm at all temperatures. It is then not clear whether this approach scales and is practical. The requirement of an adaptive Gibbs state preparation oracle is a significant hurdle, as it implies the ability to efficiently thermalize to a potentially very different Hamiltonian at each iteration, which is not generally feasible. This contrasts with typical Hamiltonian learning scenarios where one might have access to a fixed set of quantum states or measurements.
- I could not find details of the systems studied in the experiments. Specifically, the type of interactions (e.g., Ising, Heisenberg), the system size (number of qubits), and the specific parameters used in the random Hamiltonians are missing. This lack of detail makes it difficult to assess the practical relevance and reproducibility of the numerical results.
- Novelty is limited as it is an extension of the framework of [Anshu et al] to bound the spectrum of the Hessian

Minor:
- Page 1: I think that there is no $\times 1$ in the definition of $\alpha_j$ since $H_j$ is already acting on the whole Hilbert space
- Line 4, Algorithm 1: I think k should be m

### Questions
- Can you add more details on the motivation and benefits of the Hamiltonian inference problem?
- What is the system size you used in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a new problem of Hamiltonian inference. Here a learner would like to infer the coefficients of a local Hamiltonian. The oracle returns the expectation of any specific chosen product term of the Hamiltonian under the Gibbs state corresponding to a chosen Hamiltonian with similar geometry. The paper proposes two algorithms for this problem, namely the quantum iterative scaling and gradient descent, and proves their polynomial (in the number of the product terms of the Hamiltonian) convergence. Furthermore, the paper proposes two accelerations, based on quasi-Newton methods, to improve the convergence.

### Strengths
**significance:** The problem of Hamiltonian learning is fundamental in quantum learning. 

**originality:** As far as I know, the Hamiltonian inference problem formulation of this paper is completely new. Moreover, the main technical tool is a new 'quantum belief propagation' lemma that can be important for other applications.   

**quality:** The polynomial convergence of the proposed algorithm is good, as the number of product terms is itself polynomial in the number of qubits. These claims are supported by rigorous proofs. Finally, experiments clearly demonstrate the advantages of the proposed accelerations.

**clarity:**  The paper is written well overall. The ideas in the paper flow smoothly and are supported by good motivation. Additionally, the results presented in the paper are generally accompanied by thorough and informative comments or explanations.

### Weaknesses
The primary limitation of this paper is that the main algorithms are essentially specific instances of the quantum iterative scaling problem of Ji (2022) and gradient descent. While it's worth noting that their convergence analysis is not entirely straightforward, it relies on several pre-existing results, including Ostrowski's theorem and Anshu et al.'s (2021) lower bound on the Hessian $L$. Furthermore, the new 'quantum belief propagation' introduced in this paper ( cf. Lemma C.3) is similar to the original one, as can be seen by changing $\tanh\rightarrow \sinh$. The core issue is that the modifications, while technically necessary for the analysis, do not represent a significant conceptual leap beyond existing techniques. The analysis, while rigorous, largely leverages existing machinery rather than introducing fundamentally new analytical tools. The paper would be strengthened by a more in-depth discussion of the limitations of these algorithmic choices and a more thorough exploration of alternative approaches.

### Questions
Can you show a matching lower bound on adaptive algorithms for the Hamiltonian inference problem with the oracle you propose in the paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work builds on recent breakthroughs in learning of quantum gibbs states from measurement data. The authors apply new optimization methods to solve the max-entropy problem associated with this learning task. They also derive rigorous complexity bounds for these optimization methods. The main technical contribution is a modified version of the Quantum Belief Propagation technique that is used to upper bound the eigenvalues of the Hessian.

### Strengths
1.  Gives rigorous guarantees for the computational complexity of learning quantum Hamiltonains from solving the max entropy problem.

2. The new Quantum BP method in this work could be a useful alternative to the method introduced by Hastings. If the authors can find some use cases where this method gives better bounds then this would be a good addition to the quantum information literature

### Weaknesses
1. Oracle assumed is too strong and impractical. The oracle solves a very hard computational problem even in the classical setting, especially in the low temperature regime. The setting in this work is the quantum analogue of learning classical graphical models given an oracle that can always return the sufficient statistics given the energy function of a model. 

The main technical challenge that needs to be addressed in this field is the fact that there are no quantum versions of the pseudo-likelihood type methods that are used to learn classical Gibbs states. The existence of these methods in the quantum regime would bypass the need for these types of oracles. A very recent work (https://arxiv.org/abs/2310.02243) has shown that the computational complexity of solving this problem is polynomial in the size of the system, without assuming any strong oracles. This new method has much worse sample complexity, so a practical algorithm is still out of reach.

In general oracles are useful to establish relative complexity of two tasks, inference and learning in this case. But for learning Gibbs states, from classical results, we already know that inference is much harder than learning. So the bounds established in this work are only marginally interesting.

2. It is mostly using established techniques in optimization to solve a standard problem of matching sufficient statistics (essentially Maximum Likelihood).  Novelty of this work mainly comes from the techniques used to establish the bounds on Hessian.  The methods used to solve the problem it self are not new.

3. Overall the method is not very efficient. Theory gives an exponential worst case run-time (which is absorbed into the oracle) and the field of quantum computing is too nascent to provide any high quality data  to establish any practical claims regarding the algorithm.

### Questions
1. Are there useful cases of Gibbs state learning where some algorithm can implement the oracle used in this work without directly preparing the Gibbs states?

2. How does the complexity of this work compare to the high-temperature learning results of Haah et al. (https://arxiv.org/abs/2108.04842)?
The oracle used in the paper under review can possibly be implemented efficiently in this regime. But then the total complexity of the method proposed here must be compared with that of Haah et al.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
