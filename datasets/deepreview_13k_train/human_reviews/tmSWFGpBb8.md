# Learning the Complexity of Weakly Noisy Quantum States

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Quantifying the complexity of quantum states is a longstanding key problem in various subfields of science, ranging from quantum computing to the black-hole theory. The lower bound on quantum pure state complexity has been shown to grow linearly with system size [J. Haferkamp et al., 2022, *Nat. Phys.*]. However, extending this result to noisy circuit environments, which better reflect real quantum devices, remains an open challenge. In this paper, we explore the complexity of weakly noisy quantum states via the quantum learning method. We present an efficient learning algorithm, that leverages the classical shadow representation of target quantum states, to predict the circuit complexity of weakly noisy quantum states. Our algorithm is proved to be optimal in terms of sample complexity accompanied with polynomial classical processing time. Our result builds a bridge between the learning algorithm and quantum state complexity, meanwhile highlighting the power of learning algorithm in characterizing intrinsic properties of quantum states.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates a fundamental question in quantum state complexity: how to predict/learn the complexity of weakly noisy quantum states. The authors develop an efficient learning algorithm that:

1. Uses classical shadow representation of quantum states
2. Provides optimal sample complexity with polynomial classical processing time
3. Works specifically for weakly noisy states (noise strength O(1/n) and depth O(poly log n))

The main contribution is establishing an efficient algorithm for learning quantum state complexity in noisy environments.

### Strengths
- The algorithm is rigorously analyzed with provable guarantees on both sample and computational complexity.

- The work studies quantum state complexity in noisy environments which better reflect real quantum devices.

- The approach cleverly leverages classical shadows and intrinsic properties of quantum circuit architectures to make the learning problem tractable.

- The sample complexity is shown to be optimal with respect to circuit depth.

### Weaknesses
 - It is well known in quantum complexity theory that the circuit complexity of a quantum state cannot be efficiently learned [1, 2, 3]. For example, the existence of pseudorandom states that can be generated in polylog depth on 1D circuits [3] immediately implies that no polynomial-time quantum algorithm can distinguish between polylog circuit complexity (complexity defined in terms minimum circuit depth) and exponential circuit complexity. Hence, it is not possible to predict complexity of a state in polynomial processing time without first solving quantumly hard cryptographic problems. I find it very confusing that the authors claim to predict circuit complexity in polynomial time.

 - Despite the focus of practical importance (the presence of noise), the paper did not provide any numerical experiments to validate the theoretical claims (including both efficient sample and computational complexity). I think it is important for this work to have supporting numerical experiments for system size that scales to 50-100 qubits.

 - While the paper focuses on weakly noisy states, it's unclear how the approach would scale to more general noise models or stronger noise regimes. I think the work did not provide enough justification for the focus on weakly noisy states.

### Questions
Could the authors provide further clarification on how it is possible to predict the circuit complexity of a state in polynomial time? There are a plethora of existing results proving that circuit complexity is not efficiently learnable. Assuming the claims given in this work are correct, could the authors provide a detailed exposition for how this seemingly contradictory statements can be resolved?

Could the authors provide numerical simulations demonstrating their learning algorithm's performance on concrete examples of noisy quantum states? This would help validate the theoretical guarantees and provide intuition about the practical performance.

The paper focuses on weakly noisy states with specific noise parameters (O(1/n) strength and O(poly log n) depth). Could the authors comment on whether similar techniques could be extended to more general noise models or stronger noise regimes? If not, could the authors describe if stronger results are simply impossible for any learning algorithm?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a quantum learning algorithm to predict the complexity of weakly noisy quantum states. The authors introduce the concepts of Weakly Noisy Quantum State and Limited-Structured Complexity and prove that their algorithm achieves optimal sample complexity with respect to their definition of noisy circuit depth. They also provide a lower bound for sample complexity. This work also shows meaningful connections between learning algorithms and quantum state complexity.

### Strengths
The paper studies a fundamental problem of understanding the learning complexity of noisy quantum states, which has potential applications in various fields claimed for black-hole theory and condensed-matter physics. The authors propose a novel quantum learning algorithm that leverages the intrinsic structure of quantum circuit architectures to predict the complexity of weakly noisy quantum states. The theoretical analysis provides provable guarantees on the sample complexity and efficiency of the proposed algorithm.

### Weaknesses
- The setting of weakly noisy quantum states is not well-motivated, and it is unclear how the proposed learning approach can be feasible in practice. The accumulation of quantum noise on each quantum system can be significant, and the considered noise model may not be sufficiently practical or meaningful. Not sure about the the noise channel is assumed to be gate-independent.
- The paper is difficult to follow, with various parameters in the theorems that are not clearly explained (e.g., Theorem 4). The use of the same letter R to define both the noise numbers in the definition of Weakly Noisy Quantum States and the regrets in later sections adds to the confusion.
- The paper does not provide detailed examples or numerical experiments to support the proposed algorithm's effectiveness and practicality. This lack of empirical evidence makes the results less convincing.
- It is not very clear to me whether the main algorithms consider quantum noises.
- It is not convincing that the results are of a broad interest in the ICLR community.
- The results presented in the paper do not appear to be particularly surprising or groundbreaking in the field of quantum learning theory.

### Questions
- Could you provide a more compelling motivation for studying weakly noisy quantum states? How do they relate to real-world quantum systems, and what are the potential applications of your findings?
- Given that quantum noise can accumulate rapidly in depth significantly in each quantum system, how does your proposed learning approach remain feasible in practice? Why gate-independent noise channel? Please clarify the practicality of your noise model and its implications for the scalability of your method. Better to compare with an explicit circuit model example.
- Several parameters in the theorems, such as Theorem 4, are not clearly explained. Could you provide more context and explanations for these parameters to improve the readability of the paper?
- The use of the same letter R to define both the noise numbers in the definition of Weakly Noisy Quantum States and the regrets in later sections is confusing. Please consider using different notations for clarity and consistency throughout the paper.
- To support the effectiveness and practicality of your proposed algorithm, could you provide detailed examples that illustrate its workings and benefits?
- Do you assume quantum noises in the main algorithm 1?
- Numerical experiments on benchmark datasets or simulated quantum systems would strengthen the empirical evidence for your method. Could you include such experiments to demonstrate the performance of your algorithm in various settings?
- While your paper introduces a new quantum learning algorithm, it would be helpful to provide a more comprehensive comparison with existing methods in the field of quantum learning theory. Could you discuss how your approach differs from and improves upon prior work?
- Could you elaborate on how your work on learning the complexity of weakly noisy quantum states is relevant to the broader ICLR community?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a quantum learning algorithm that estimates the complexity of weakly noisy quantum states, unlike prior research focusing primarily on pure states, thereby connecting theoretical principles to practical scenarios observed in real-world quantum devices. The proposed algorithm is based on quantum circuit architecture (QCA) combined with classical shadow representation. It reaches near-optimal sample efficiency in the estimation of state complexity, which is theoretically analyzed in this paper to underscore its efficacy. The paper points out several promising research studies that may open up when the expressivity of QCA can be improved, and methodologies for direct complexity predictions in noisy quantum states are developed.

### Strengths
1. The paper confirms that the proposed approach can handle such complex quantum states even in noisy environments, validated through a robust theoretical framework based on theorems and proofs, including the sample complexity and the efficacy of Bayesian optimization in the noisy quantum environment.
2. The application of classical shadow representation in quantifying the complexity of weakly noisy quantum states is novel and crucial from a quantum perspective. This subsequently gives way to efficient quantum information processing classically, making the theoretical methods introduced more feasible.

### Weaknesses
1. The paper acknowledges that the proposed algorithm approximates the complexity of noisy quantum states and refers to further research on more direct prediction methods. However, it would benefit from an in-depth analysis of limitations, such as sensitivity on different noise models or how scaling issues may affect deployment to larger quantum systems. Specifically, the paper should explore how the approximation quality degrades with increasing noise strength, and whether the algorithm is more sensitive to coherent or incoherent noise. Furthermore, a discussion on the computational cost of the algorithm as the number of qubits increases is needed, including memory requirements and the scaling of the classical shadow representation.
2. The paper lacks a detailed discussion of the specific hardware requirements and the practical steps needed for real-world implementation. Details such as compatibility with existing quantum hardware, scalability in practical quantum systems, and specific technological constraints are not thoroughly explored. For instance, the paper should specify the required gate fidelity and coherence times for the quantum hardware, and discuss the challenges of implementing the required quantum circuits on different quantum computing platforms (e.g., superconducting, trapped ion, photonic). The paper also needs to address the practical limitations of preparing the classical shadows, including the number of measurements needed and the associated overhead.

### Questions
1. Could the authors elaborate on specific quantum hardware requirements for implementing the algorithm? Are there particular quantum systems where the algorithm's performance has been or can be practically tested?

2. How does the algorithm perform under different types of quantum noise models? Is the accuracy in the complexity predictions different between, e.g., local-depolarizing versus global-depolarizing channels?

The paper could be enhanced by considering the following suggestions:

- The paper should include a more detailed discussion of the computational and practical limitations of the algorithm (for example, stress-testing the algorithm under increased complexities and reporting on its degradation or stability performance.)
- Incorporating key proofs and insights from the appendices into the main body would enhance the paper's value, as some essential concepts, like the subroutine BMaxS, are only briefly mentioned in the main text.
- It would also be very useful if the manuscript provided a framework for empirical testing and validation of the algorithm, including benchmark selection and metrics of validation. This would help bridge the missing gap between theoretical research and practical applications and give a much stronger justification for the effectiveness of the algorithm in noisy quantum environments.

### Soundness
3

### Presentation
2

### Contribution
2
