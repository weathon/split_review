# ER-AAE: A quantum state preparation approach based on entropy reduction

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Amplitude encoding of classical vectors serves as a cornerstone for numerous quantum machine learning algorithms in real-world applications. Nevertheless, achieving exact amplitude encoding for general vectors needs an exponential number of gates, which negates the potential quantum advantages. To address the challenge of large gate number in the state preparation phase, we propose an approximate amplitude encoding algorithm based on entropy reduction (ER-AAE) within the classical framework. Given a target vector, the ER-AAE algorithm generates a sequence of gates, comprising single-qubit rotations and CZ gates, that approximates the amplitude encoding of the target vector. The structure of encoding circuits in ER-AAE is built inductively using a greedy search strategy that maximally reduces the linear entropy. We further prove that the state produced by ER-AAE approximates to the target state with the infidelity bounded by the linear entropy of intermediate states. Experimental results, including state preparations on random quantum circuit states, random vectors, MNIST digits, and CIFAR-10 images, validate our method. Specifically, real-world data reveals a noteworthy trend where linear entropy decays significantly faster compared to random vectors. Furthermore, the ER-AAE algorithm surpasses the best existing encoding techniques, achieving lower error with an equivalent or fewer number of CNOT or CZ gates.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes approximate amplitude encoding of classical information into quantum states. The proposed method allows to leverage the precision of the encoding with the number of the gates and thus can be adapted based on requirements. The encoding is minimized based on linear entropy reduction, calculated as entanglement reduction, by adding one gate at the time from exhaustively searching the set of available gates for the one that minimizes the linear entropy the most. The results looks promising as on the MNIST and CIFAR the proposed method seems to outperform the other approaches that are used for comparison.

### Strengths
- The proposed approach based on the entanglement minimization is interesting and novel.

### Weaknesses
 - The main advantage is also a weakness. While the approximate method allows to encode the states at a lesser precision with a smaller amount of gates, it can also lead to a higher cost when encoding for 100% accurate representation. This is a significant limitation because, while the method aims to reduce gate count for approximate encoding, it does not guarantee an advantage over exact methods when high precision is required. The method's performance is also highly dependent on the dataset's structure and the initial state's entanglement. If the data representation is unstructured and highly entangled, the linear entropy decay might be slow, thus requiring more gates to achieve the desired precision. This variability in performance across different datasets makes it difficult to predict the method's effectiveness in new, unseen scenarios.

### Questions
Is the entropy decay same for all datasets? If not how will this method be affected if for different datasets the decay will be different?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose a new method for finding quantum circuits to prepare a target quantum state. The proposed algorithm starts with a target state and iteratively finds the best parametrized two qubit operations one can apply to the state. The aim to to construct such a circuit that minimizes a sum of subsystem linear entropies. The authors test their algorithm using classical simulations and show that this can be used to encode elements from various machine learning datasets into a quantum circuit with good accuracy and favorable performance.

### Strengths
This addresses an important problem at the intersection of machine learning and quantum computing, i.e. how to prepare quantum states that effectively encode large datasets. The paper is very clearly written and the arguments of the authors are easy to follow.

### Weaknesses
There are general questions/concerns I have about the paper.
1. Could the authors clarify the setting of Algorithm 1? Is this intended as a quantum algorithm or is it meant to be simulated on a classical computer?  In other words, does the algorithm require any quantum resources?

2. In QML literature, the notion of a QRAM is often used to circumvent the data loading problem[3]. Conceptually, should I think of AR-EEE as a candidate algorithm for a QRAM? Or is it independent of the QRAM idea all together?

3. In Proposition 2, the state $| \phi \rangle$ is defined but not used anywhere in the statement. 

4. If a large enough C is used, is the algorithm always guaranteed to find a $v_c$ that is a product state? Will it find such a $v_c$ for a large enough C if the assume that the greedy search and the angle optimizations used in the algorithm  never get stuck in local minima?

5. Do the authors have any intuition on why the algorithm performs poorly on random vectors in Fig 2 (a)? Is this due to limited expressivity of the variational circuit used in this procedure?

6. The authors claim that states that AR-EEE encodes well are those with low entanglement. Could the authors clarify what type of entanglement structure is favorable for AR-EEE? For states with low entanglement, is AR-EEE favorable to the naive approach of preparing a tensor network (with a large enough bond dimension similar to how C was increased in the experiments here) and then preparing that directly using a quantum circuit [1] [2]? For 2D images, it is possible that the specific low-entanglement structure can be captured by a PEPS. 

7. Many QML algorithms require coherent access to a dataset in superposition [3]. While the numerical demonstration here deal with single elements from CIFAR and MNIST. Do the favorable properties, like low entanglement, shown by single images imply that these superposition states can also be prepared easily?

### Questions
There are general questions/concerns I have about the paper. 
1. Could the authors clarify the setting of Algorithm 1? Is this intended as a quantum algorithm or is it meant to be simulated on a classical computer?  In other words, does the algorithm require any quantum resources?

2. In QML literature, the notion of a QRAM is often used to circumvent the data loading problem[3]. Conceptually, should I think of AR-EEE as a candidate algorithm for a QRAM? Or is it independent of the QRAM idea all together?

3. In Proposition 2, the state $| \phi \rangle$ is defined but not used anywhere in the statement. 

4. If a large enough C is used, is the algorithm always guaranteed to find a $v_c$ that is a product state? Will it find such a $v_c$ for a large enough C if the assume that the greedy search and the angle optimizations used in the algorithm  never get stuck in local minima?

5. Do the authors have any intuition on why the algorithm performs poorly on random vectors in Fig 2 (a)? Is this due to limited expressivity of the variational circuit used in this procedure? 

6. The authors claim that states that AR-EEE encodes well are those with low entanglement. Could the authors clarify what type of entanglement structure is favorable for AR-EEE? For states with low entanglement, is AR-EEE favorable to the naive approach of preparing a tensor network (with a large enough bond dimension similar to how C was increased in the experiments here) and then preparing that directly using a quantum circuit [1] [2]? For 2D images, it is possible that the specific low-entanglement structure can be captured by a PEPS. 

7. Many QML algorithms require coherent access to a dataset in superposition [3]. While the numerical demonstration here deal with single elements from CIFAR and MNIST. Do the favorable properties, like low entanglement, shown by single images imply that these superposition states can also be prepared easily?

[1] Schön, Christian, et al. "Sequential generation of entangled multiqubit states." Physical review letters 95.11 (2005): 110503.
[2] https://arxiv.org/abs/1104.1410
[3] Biamonte, Jacob, et al. "Quantum machine learning." Nature 549.7671 (2017): 195-202.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors introduce and numerically test a method for approximately preparing target quantum states, with an eye toward using this approach for implementing an amplitude encoding scheme for quantum machine learning. To achieve this, the authors "work backwards:" given copies of the state, the algorithm applies two-qubit gates in sequence, choosing at each step the gate which minimizes the linear entropy of the state. After this procedure is repeated a number of times, the algorithm then optimizes the fidelity with the all-zero state over single-qubit rotations. The resulting approximate state preparation circuit is then the adjoint of this circuit applied to the all-zero state.

### Strengths
Amplitude encoding is an important building block in many quantum machine learning algorithms, and understanding when it can be approximately performed using quantum circuits of low gate complexity (relative to the Hilbert space dimension) is important for understanding when these algorithms are efficient in practice.

### Weaknesses
The suggested algorithm not only requires a greedy optimization over the two-qubit gates, but also performs an optimization of the fidelity over single-qubit gates; both of these optimization procedures can lead to poor optima due to the local nature of the searches. The numerical experiments are also not fully described, leaving in question the relative merits of the authors' introduced method with previous existing methods (see Questions).

The proposed technique is also not the most novel; other quantum algorithms (such as ADAPT-VQE, Nat. Commun. 10, 3007; Overlap-ADAPT-VQE, Commun. Phys. 6, 192) use a greedy method to choose gates to apply in approximate state preparation. The main distinction is that here, the authors use a different loss for each optimization step---the linear entropy rather than, e.g., the fidelity. However, the authors give little motivation as to why this choice of loss is preferable. Furthermore, while the authors now compare to ADAPT-VQE, it is not clear that the comparison is entirely fair. The authors' method uses a fixed gate structure (CZ gates), while ADAPT-VQE uses a more general gate set, and thus the comparison may be more reflective of the gate set choice than the optimization method itself. It is also unclear if the ADAPT-VQE method was optimized over the same number of parameters as the authors' method, or if the optimization was performed with the same computational budget.

### Questions
More discussion on the performed numerics is needed to fully understand the implications of this work. For instance, for the numerics in Figure 3, how were the models "normalized" to have equivalent computational costs? I.e., were they normalized to have identical final quantum circuit depths, or was the computational cost for performing the optimization normalized to be identical, or was the number of free parameters normalized to be identical? I ask because the authors' construction uses 6 parameters for each two-qubit unitary, and the authors numerically consider unitaries up to depth 100. This is 600 parameters for a state in a Hilbert space dimension of (in the case of the MNIST data set) 1024, and thus the authors' method parameterizes a significant fraction of the full Hilbert space; I would thus expect a similarly parameterized hardware-efficient ansatz to perform similarly well to the authors' methods.

Another question is: how do these methods compare to similar greedy-state-preparation methods, such as ADAPT-VQE, where the only difference in methods is the choice of loss function? This sort of experiment would more clearly delineate what advantages the authors' methods have over preexisting methods.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on the amplitude encoding problem, which is one of the most significant subroutines in the context of quantum machine learning. The authors argue that general amplitude encoding (in the worst-case scenario) may require exponentially large quantum gates. In this paper, the authors introduce an Entropy Reduction AAE method to address this problem. The ER-AAE algorithm utilizes variational principles and greedy search strategies to reduce linear entropy and ultimately produce a quantum circuit. The authors numerically benchmark their method on several popular classical datasets.

### Strengths
From a high-level perspective, this paper is well-written, clearly introducing the research background on the amplitude encoding methods and applications, meanwhile presenting their results clearly. Meanwhile, the authors have put effort into the numerical simulation section, where they benchmark the proposed method across several datasets.

### Weaknesses
My main concern is about the problem setup, as outlined on Page 2 and detailed in Algorithm 1. If my understanding is correct, the authors assume that many copies of the target quantum state $|v\rangle$ are provided. Using these prepared copies of $|v\rangle$, Alg. 1  aims to find a set of quantum gates $G_1,\cdots,G_C$ (and W) to approximately prepare $|v\rangle$. The main question is: if $v$ originates from a classical dataset, where do these quantum states $|v\rangle$ come from? And if many copies of $|v\rangle$ are already available, why not use these quantum states directly to implement machine learning tasks? This setup is very different from the results in [J. Iaconis et al., npj Quantum Information, 2024], which first encode classical data into an MPS (Matrix Product State) and then transform the MPS into a quantum circuit using methods such as those proposed by [Shi-Ju Ran, Phys. Rev. A, 2020]. From this perspective, the problem statement (specifically, the requirement of Algorithm 1) seems quite strange to me. Specifically, my main concern can be summarized by:
(1) Whether they assume access to prepared quantum states or just classical data vectors
(2) If quantum states are assumed, how these are obtained from classical data
(3) How the proposed method compares to directly using prepared quantum states, in terms of efficiency and practicality for machine learning tasks

My other concern is that the proposed algorithm requires a $2^N$-sized input ($v_{target}$), and all the involved operations $Gv_i$ seem to require exponentially large classical running time. As a result, the algorithm is not efficient. Furthermore, even if the linear entropy can be computed exactly using classical methods, this still requires exponentially large running time. From my understanding, this algorithm is still designed with quantum devices in mind. Finally, while the authors claim that their method is efficient, they do not address the scenario where the target amplitudes satisfy the area law. In this case, the MPS method would be highly efficient, and the quantum state preparation would also be efficient. It is unclear whether the proposed method can achieve similar efficiency when the data points follow the area law.

### Questions
1. A detailed explanation of how they evaluate linear entropy in practice
2. An analysis or estimate of the number of copies of $|v\rangle$ required to achieve a given precision in the entropy estimation
3. A discussion of how the sample complexity affects the overall efficiency of their method
4. As claimed by authors, after finding quantum gates $G_1,\cdots,G_C$, the quantum state $|v\rangle$ is mapped to a tensor-product state $|v_c\rangle$. In Eq. 5, authors mentioned that the trace distance ($L_{infid}$) can be used to train the circuit $V(\theta)$. However, it is known that the global observable may result in serious barren plateaus phenomenons [M. Cerezo et al., Nat Commun 12, 1791 (2021).] Whether this phenomenon may dramatically affect the algorithm efficiency, leading the proposed method is not scalable?
5. In proposition 2, the quantum state $|\phi\rangle$ looks like a single-qubit state. What is the relationship between $|\phi\rangle$ and Eq. 8?

### Soundness
3

### Presentation
3

### Contribution
2
