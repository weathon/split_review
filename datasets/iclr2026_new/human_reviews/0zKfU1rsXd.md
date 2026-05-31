## Human Reviewer 1

### Summary
AQER relates approximate-state-loading error to entanglement entropy S and derives corresponding information-theoretic bounds

### Strengths
1.	Provides information-theoretic bounds that relate approximation error directly to a locally measurable entanglement proxy, guiding circuit construction for state preparation.
2.	Consistently outperforms MPS, HEC and AQCE at equal two-qubit gate budgets on both classical and quantum data sets.

### Weaknesses
1.	Theorem 3.1 is general, but the evaluated states appear to be low- or modestly entangled; tougher, higher-entanglement regimes are not covered.
2.	No scaling analysis of gradient variance with qubit number; trainability claim remains heuristic.
3.	The paper claims code availability but does not provide the anonymous GitHub link in the main text, which could hinder reproducibility efforts.

### Questions
1.	Could 2-D random circuits or critical 2-D spin systems be included to probe performance when entanglement is less easily reduced?
2.	Could the authors provide gradient-magnitude statistics across N=10–50 qubits?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper introduces a unified framework for analyzing the accuracy of approximate quantum loaders (AQLs), by bounding the achievable infidelity in terms of an entanglement measure S (the sum of single-qubit Rényi-2 entropies after applying the inverse loader to the target state). Building on this, the authors propose AQER, a data loader that constructs an encoding circuit by first reducing the target state’s entanglement, then applying single-qubit product-state corrections with closed-form parameters, and finally refining all parameters jointly. Experiments on classical datasets (MNIST, CIFAR-10, SST-2) and quantum datasets (random quantum circuits and Ising model ground states) reaching up to 50 qubits, show lower infidelity than MPS-, HEC-, and AQCE-based baselines for the same or fewer two-qubit gates.

### Strengths
- The paper presents a clear, useful bound for all AQLs, formulated in terms of the entanglement measure S.


- The AQER algorithm is intentionally designed to minimize the S, which the theory connects directly to infidelity.


- Once target states are available, training AQER relies only on local measurements.


- Experiments provide encouraging evidence that supports the paper’s central claims

### Weaknesses
Although the above strength, I do not think the current version of the paper matches the ICLR criteria for the following reason:

- My main concern is the computational cost required to reach low infidelity in the general case. The theoretical bound in the paper is meaningful only in the limit S goes to 0. For target states with moderate or high entanglement, achieving a small S requires deeper circuits U, and it is unclear whether this can still be done with circuits of polynomial size.


- Also, the upper bound is stated in terms of the existence of a product state with certain properties. This does not guarantee that a generic product-state ansatz will satisfy the same bound in practice.

- Another concern I have is that computing the entanglement measure requires access to the target state. For quantum data, this may be possible if multiple copies of the state are available, though the number of required copies is not made explicit. For classical data, however, one must first classically construct the full target state, which is not tractable at large numbers of qubits. In fact, the classical-data experiments in the paper are limited to around 10 qubits.


- Even for quantum states, as far as I understand, the simulations proposed in the paper rely on tensor-network methods, which inherently assume limited entanglement. This suggests that highly entangled quantum data are effectively out of scope for the demonstrated results.


- Finally, it is not clear that the optimization described in Eq. (2) can be solved in polynomial time.

### Questions
- Can the authors specify what happens, in terms of the algorithm’s computational complexity, if the target states have a high level of entanglement?


- Can the authors provide theoretical guarantees that the optimization step in Eq. (2) is efficient?


- How is the method applicable to high-dimensional classical data that require a large number of qubits?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper introduces AQER, a novel three-stage algorithm for approximate quantum loading (AQL). The core idea is to construct a quantum circuit by greedily minimizing an entanglement measure, the sum of single-qubit Renyi-2 entropies. The authors provide a theoretical bound linking this measure to the final approximation error and demonstrate through extensive simulations on classical and quantum datasets that AQER outperforms several existing methods in both accuracy and gate efficiency.

### Strengths
The paper's primary strength is Theorem 3.1, which establishes a formal information-theoretic bound between the approximation infidelity and the proposed measure. This provides a solid theoretical justification for the algorithm's design, moving beyond purely heuristic approaches.

The entanglement-reduction-guided strategy for building the circuit is a novel and intelligent heuristic. It offers a structured method for ansatz construction that aims to position the optimization in a favorable region, which is a key challenge in variational algorithms.

The authors have conducted extensive and compelling numerical experiments across a diverse set of benchmarks, including classical data and quantum many-body states up to 50 qubits. The consistent and significant performance gains shown in Table 1 strongly support the practical effectiveness and scalability of the proposed method.

### Weaknesses
1. The paper compellingly argues that AQER mitigates barren plateaus in the final optimization. However, a critical discussion or numerical experiment is missing on the optimization landscape. The algorithm's success hinges on this greedy step being efficient. The paper would be significantly strengthened by a discussion of why the local structure of this cost function makes the optimization in Step I tractable.

2. The experimental comparison relies heavily on the two-qubit gate count, which is a good but incomplete metric. To make a fairer and more robust assessment of AQER's scalability, I suggest the authors consider the gate depth, the number of trainable parameters, measurement overhead, and training cost.

3. The study is performed under ideal, noise-free conditions. Given that the practical utility of any near-term algorithm depends on its noise resilience, the paper would be substantially more impactful with a discussion on this aspect. For instance, how might hardware noise affect the measurement of entanglement and the subsequent greedy circuit construction? Even a qualitative discussion or a small-scale simulation under a simple noise model would add significant value.

### Questions
See weakness

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a structured method for synthesizing circuits for quantum state preparation, with a primary focus on loading classical data onto a quantum computer as quantum states (e.g., encoding a classical vector into a quantum vector). The core insight behind the proposed method, AQER, is supported by a theoretical upper bound on the best-case infidelity (over initial product states), expressed in terms of the sum of single-qubit entanglement entropies of the target state evolved under a circuit.

Building on this insight, the method proceeds in three stages:
- Circuit search to reduce the entanglement of the target state.
- Approximation of the resulting low-entanglement state by a product state.
- Parameter refinement to optimize performance.

The authors perform simulation-based benchmarks on both classical and quantum data-loading tasks, demonstrating that their method consistently outperforms existing approaches.

### Strengths
- The approach is grounded in a clear and well-motivated theoretical insight, which lends credibility to the method and provides a room for future extensions. Given that quantum state preparation is, in general, an infeasible problem in terms of computational complexity, it is reasonable that the paper does not pursue purely theoretical guarantees.

- Numerical benchmarks across multiple datasets demonstrate consistent performance improvements over prior methods.

### Weaknesses
- Since the target hardware setting is the NISQ regime, the lack of experiments on real quantum devices, or even simulations under realistic noise models (e.g., depolarizing noise), makes it difficult to assess how the proposed method would perform in practice. This limitation is particularly relevant given that several prior works in this area include evaluations on real hardware.

### Questions
Can the theoretical characterization of infidelity be extended to general noise models, where the unitary evolution is replaced by a generic quantum channel (CPTP map)?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3