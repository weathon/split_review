# Limitations of measure-first protocols in quantum machine learning

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
In recent times, there have been major developments in two distinct yet connected domains of quantum information. On the one hand, substantial progress has been made in so-called randomized measurement protocols. Here, a number of properties of unknown quantum states can be deduced from surprisingly few measurement outcomes, using schemes such as classical shadows. On the other hand, significant progress has been made in quantum machine learning. For example, exponential advantages have been proven when the data consists of quantum states and quantum algorithms can coherently measure multiple copies of input states. In this work, we aim to understand the implications and limitations of combining randomized measurement protocols with quantum machine learning, although the implications are broader. Specifically, we investigate quantum machine learning algorithms that, when dealing with quantum data, can either process it entirely using quantum methods or measure the input data through a fixed measurement scheme and utilize the resulting classical information. We prove limitations for quantum machine learning algorithms that use fixed measurement schemes on the input quantum states.
Our results have several implications. From the perspective of randomized measurement procedures, we show limitations of measure-first protocols in the average case, improving on the state-of-the-art which only focuses on worst-case scenarios. Additionally, previous lower bounds were only known for physically unrealizable states. We improve upon this by employing quantum pseudorandom functions to prove that a learning separation also exists when dealing with physically realizable states, which may be encountered in experiments. From a machine learning perspective, our results are crucial for defining a physically meaningful task that shows fully quantum machine learning processing is not only more efficient but also necessary for solving certain problems. The tasks at hand are also realistic, as the algorithms and proven separations hold when working with efficiently preparable states and remain robust in the presence of measurement and preparation errors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors design a quantum machine learning task that exhibits a sample and time complexity separation between two classes of quantum algorithms acting on input training data consisting of quantum data and classical labels with the goal of producing a classical description of a quantum circuit that can then be deployed on unseen quantum data to produce samples from a distribution related to the training data. The main difference between the two classes of quantum algorithms is that the more powerful class is allowed to process the input quantum-classical training data in "one go", while the weaker class is hamstrung to first turn the quantum data into classical data, one training data-point at a time, without looking at the classical labels before being allowed to process this now-classical data together with the classical labels through a quantum algorithm to produce a classical description of the deployment quantum circuit. At deployment time, the weaker class is then further forced to measure the unseen quantum data before feeding it into the quantum circuit produced at the end of the training phase.

Unsurprisingly, there is a complexity separation between the fully quantum algorithm and the hamstrung quantum algorithm which seems to essentially be a restatement of the intractability of the Hidden Matching Communication problem. Finally, the authors claim to extend the complexity separation to efficiently preparable training data sets by using pseudo-random functions.

### Strengths
Originality: The authors venture to create a quantum machine learning task with average-case complexity separations between measurement-first and fully-quantum quantum algorithms.
Quality: The authors seem to know the techniques of the sub-field well (including those related to POVMs, HM problem, Yao's principle, QPRFs, ...), as well as other related work (including classical shadows, shadow tomography, ...)
Clarity: The authors do try to provide both diagrammatic, high-level and low-level explanations.
Significance: The authors do aim to produce a significant result by hoping to shed light on the role of information loss due to measurement when performing quantum machine learning in the average-case setting with realistic training data.

### Weaknesses
### weaknesses:
 Unfortunately, the high aims and strong potential of the "Strengths" section, seem not to be met. I believe this is mainly due to the overly restrictive setting of the weakened class of "measurement-first" quantum algorithms. The most confusing and vague constraint is: "that the measurement strategy cannot depend on the specific target concept". Looking at Definition 5 and 7 for clarity this seems to be the following constraint on the hamstrung class:

Training:
Quantum data + classical labels -----[Point-wise measurement]------> M(Quantum data) + classical labels = Classical data + classical labels ----[Quantum Algorithm]----> Classical description of Quantum circuit

Deployment:
Quantum data -----[Point-wise measurement]------> M(Quantum data) = Classical data ----[Quantum Algorithm given by circuit above]----> Sample

Therefore it seems that the main difference between the two classes is that the weaker one actually only operates on classical data during both training and deployment while the stronger one is allowed to operate on quantum data. This is a difference between data capacity and not really about a separation between interesting algorithmic classes. The imposed restrictions on the measurement-first (MF) protocol appear to artificially limit its capabilities, particularly in how the measurement strategy is constrained during the training phase. By forcing the MF protocol to convert quantum data into classical data point-wise without considering the classical labels, the protocol is essentially reduced to operating on classical data throughout both training and deployment. This raises concerns about whether the observed separation is a genuine reflection of algorithmic differences or simply a consequence of the MF protocol's limited access to quantum information.

Secondly, there does seem to be quite a few unclear statements or mistakes:

* Lines 157-159 is unclear
* Lines 205-210 claims a significant difference between this work and Jerbi et al.'s, but given the above characterization it is not clear that this is the case.
* Line 229 introduces f', why the prime?
* \pi_x is not anywhere clearly connected to \Lamda_x
* z and x are used inconsistently/confusingly in multiple places
* Eq (3) and Eq (5): the training data should not include x, perhaps g_i(x) is somehow meant (however see below)?
* Eq (3) and Eq (5): (y, b) ~ \pi_x and not (x,y,b)
* Line 285: perhaps \Tilde{\pi}_x should be \Tilde{\pi}_{T_x} since the x dependence is surely only through T_x
* Eq (8): how can x appear as an unbound function variable on the LHS and as a bound variable on the RHS?
* Line 370: the use of Aaronson et al. is the very heart of the whole paper, yet this is not reproduced anywhere in the paper
* Line 434: please remind me what non-uniform means in this context.
* Eq (9): the notation of dot and unfilled function brackets is not defined/explained.
* Lines 475-480: is unclear, especially given that there are supposed to be different random functions for each data-point.
* Eq (11): if g_i(x) is of size n+1, doesn't this change the learning problem in unclear-ways, not least because the dimensions no longer match (2n + 1 != 2n + 2)
* Eq (29): \pi_x(f) -> \pi_x(f^{(k)})
* Line 787: is query access -> has query access

### Questions
* How can my following perceived weakness from above be remedied:
"This is a difference between data and not really about a separation between interesting algorithmic classes."
* Is my understanding correct that the essence of the separation between the two classes boils down to the inability to compress the unseen quantum data during deployment time? What would happen if the measurement restriction during training were modified to allow the measurements to depend on the labels? Or if we must keep them blind of the labels, joint measurements across all data-points were allowed?
* Line 289: Why is the "more general" case not studied, when it is arguably much more interesting than the restrictions under consideration?
* Theorem 5: What are the assumptions of Yao's principle? Are they satisified?
* Line 810: How can Bob output 1 when y is in R_f(x) without knowledge of *f*?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates a fundamental question in quantum machine learning (QML): whether quantum advantages can persist when quantum data is first measured and converted to classical information before processing. The authors establish a formal separation between two types of QML protocols:

1. "Measure-first" protocols: Those that first measure quantum states using a fixed measurement strategy (though possibly complex and coherent) before processing

2. "Fully-quantum" protocols: Those that can process quantum states coherently and maintain quantum data throughout the entire learning & deployment process

The main contribution is proving that there exists a learning task involving quantum measurements where measure-first protocols provably require exponentially more data than fully-quantum protocols, even when restricted to efficiently preparable quantum states. This is shown by constructing a specific learning problem based on the Hidden Matching problem and quantum pseudorandom states.

### Strengths
- The paper addresses a fundamental question about the nature of quantum advantages in machine learning and provides concrete evidence that some quantum tasks inherently require maintaining quantum states throughout processing.

- The proofs are rigorous and combine multiple techniques from quantum computing, cryptography, and communication complexity.

- Unlike previous work, the separation holds even for average-case performance (not just worst-case), efficiently preparable quantum states (not just arbitrary states), and scenarios with experimental noise and errors.

### Weaknesses
 - While the paper discusses robustness to noise theoretically, no numerical simulations or experimental results are provided to demonstrate the practicality of the proposed protocols. Specifically, the theoretical analysis does not address the practical challenges of implementing the required quantum measurements and state preparations with realistic noise models. The paper would benefit from a more detailed discussion on how the theoretical noise robustness translates to practical scenarios, including specific noise parameters and their impact on the observed separation.

- While the separation is proven rigorously, it relies on a somewhat artificial learning task constructed specifically to demonstrate the separation. The learning problem based on the Hidden Matching problem and quantum pseudorandom states, while theoretically sound, lacks direct connection to real-world quantum machine learning applications. It would be valuable to explore if similar separations can be established for more natural learning problems, such as those involving classification or regression tasks with quantum data.

- The paper focuses on a specific type of quantum learning problem involving Hidden Matching. The analysis does not provide a clear understanding of how broadly these limitations of measure-first protocols apply to other quantum learning scenarios, particularly those involving different types of quantum data or learning objectives. It remains unclear whether the observed exponential separation is a general phenomenon or specific to the chosen problem.

### Questions
Given the theoretical claims regarding noise robustness for the separations established in this work, could the authors add a numerical experiment showcasing the separation under noisy settings? For example, it would be beneficial to simulate your protocols with realistic noise models for near-term quantum devices. It would also be useful to see how the separation between measure-first and fully-quantum protocols changes as noise increases.

The main result (Theorem 1) is stated in terms of an existence statement. Could the author provide a more concrete description regarding the task that lead to the separation between "measurement-first" vs "fully quantum" methods?

Do the authors consider the separation to hold in many natural learning problems that people are actively working on? Could the authors comment on whether the community should consider most problems to be addressable using measurement-first protocols? If not, could the authors comment on what families of problems one should expect fully-quantum protocols to be much more powerful than measurement-first protocols? Providing a few concrete examples of widely-studied quantum machine learning problems where they expect their results might be relevant would also be useful in this context.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In the paper entitled "Limitations of Measure-First Protocols in Quantum Machine Learning," the authors constructed a learning task based on quantum phase states, which provides a separation between the full quantum protocol and classical-shadow-based protocols in terms of sample complexity. From my understanding, the construction is fundamentally based on the fact that $FBQP/qpoly\neq FBQP/poly$, while the authors claimed that they successfully achieved the worst-to-average case reduction. In summary, this work theoretically studied the differences between two popular quantum machine learning paradigms, which advances our understanding of quantum models to some extent.

### Strengths
1. This paper clearly demonstrates its main results and the comparison to related work.
2. The authors rigorously proved the separation of sample and running time by implementing a polynomial reduction to the Hidden Matching problem, which provides new insights in the field of quantum machine learning.

### Weaknesses
Here are some weaknesses and questions on this paper.
1. Is the proved separation just an instance of $FBQP/qpoly \neq FBQP/poly$ [S. Aaronson et al., 2023], where $FBQP/poly$ represents classical shadow-based algorithms (including measure multiple states by Bell measurement).
2. The worst-to-average reduction seems very natural; if my understanding is correct: the classical shadow methods may fail for every $x$ (as shown in Eq.~7), due to the fact that $FBQP/qpoly \neq FBQP/poly$.
3. The main contribution of this paper relies on the Theorem~2. I know the proof idea is there, but the proof details in the Appendix B is not very easy to follow.

### Questions
1. It would be helpful to provide the explicit construction of U_x (also the learned measurement operator).
2. The problem is quite artificial (alghough Y. Liu et al. Nat. Phy. 2021 is still an artifical construction); it would be perfect if the phase states can be substituted to other more practical quantum state (such as ground state or thermal state of a physical system).

### Soundness
4

### Presentation
3

### Contribution
4
