# Topological data analysis on noisy quantum computers

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Topological data analysis (TDA) is a powerful technique for extracting complex and valuable shape-related summaries of high-dimensional data. However, the computational demands of
classical algorithms for computing TDA are exorbitant, and quickly become impractical for high-order characteristics. Quantum computers offer the potential of achieving significant speedup for certain computational problems.
Indeed, TDA has been purported to be one such problem, yet, quantum computing algorithms proposed for the problem, such as the
original Quantum TDA (QTDA)  formulation by Lloyd, Garnerone and Zanardi, require currently unavailable fault-tolerance.   
In this study, we present \NQTDA, a \emph{fully implemented end-to-end} quantum machine learning algorithm needing only a short circuit-depth, that is applicable to high-dimensional classical data, and with provable asymptotic speedup for certain classes of problems. The algorithm neither suffers from the data-loading problem nor does it need to store the input data on the quantum computer explicitly. The algorithm was successfully executed on quantum computing devices, as well as on noisy quantum simulators, applied to small datasets. Preliminary empirical results suggest that the algorithm is robust to noise.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Finding any application of NISQ (noisy intermediate-scale quantum) technology has been challenging, let alone in machine learning problems. Furthermore, most NISQ algorithms are heuristics in nature and do not come with rigorous guarantees. The authors propose a new NISQ algorithm for topological data analysis (TDA) with a rigorous performance guarantee for solving TDA efficiently (no classical algorithms can solve TDA efficiently due to complexity-theoretic hardness), does not suffer from data loading problems (many previous quantum algorithms only obtain advantage when one neglects the cost in data loading), and is robust to noise.

### Strengths
Understanding potential applications of NISQ is a very important question in the entire field of quantum computing. The work provides a significant step toward obtaining an end-to-end application of NISQ by proposing a NISQ algorithm for topological data analysis.

Topological data analysis is only efficient classically for low-order Betti numbers. Calculating high-order Betti numbers is known to be hard on a classical computer assuming widely believed complexity-theoretic conjectures. Hence, there are quantum advantages in calculating high-order Betti numbers.

While quantum algorithms for TDA have been known and have been subject to extensive studies in the past few years, existing quantum algorithms require deep quantum circuits, making them challenging to run on NISQ computers. The work proposes an algorithm NISQ-TDA that uses significantly shallower quantum circuits, making the algorithm suitable for the current quantum technology.

The authors experimentally tested the proposed NISQ-TDA algorithm on a 12-qubit trapped-ion quantum computer and showed promising results that the proposed NISQ algorithm is robust to realistic device noise.

### Weaknesses
A minor weakness of this work is that the proposed algorithm is not strictly applicable to NISQ devices. NISQ devices can only implement an O(log n)-depth quantum circuit before the measurement outcomes become random noise. While the work provided a significant improvement in the circuit depth, the circuit depth is still O(n).

A theorem analyzing the amount of local depolarizing noise on each gate that can be tolerated by the proposed NISQ-TDA algorithm is missing in the current writeup (the physical experiments do show that the proposed algorithm is promising). It is crucial to understand the noise scaling with respect to the number of qubits, as a fixed noise level per qubit will likely lead to an overall error that grows rapidly with system size. This is a critical point, as the practical utility of the algorithm depends on its ability to tolerate noise, and the current analysis does not provide a clear picture of this.

### Questions
Could the authors analyze the amount of local depolarizing noise on each gate that NISQ-TDA can tolerate? I suspect that the algorithm cannot tolerate a constant amount of noise per qubit (which is how people typically think of NISQ). However, understanding the noise level can still be very useful (e.g., noisy random quantum circuit sampling requires 1/n noise to have exponential quantum advantage).

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents NISQ-TDA, a new quantum algorithm for topological data analysis (TDA) that is readily implemented on near-term noisy quantum devices. This work avoids an unrealistic data input model by constructing an explicit (and shallow) quantum circuit for data-loading. The two major steps in the circuit construction are (1) representing the full boundary operator as a Fermionic boundary operator that allows efficient Pauli decompositions, and (2) projection onto problem-specific simplices using a quantum rejection sampling technique. Notably, the explicit circuit construction of the combinatorial Laplacian operator does not require accessing stored quantum data. 

To estimate the Betti number (defined as the rank of the kernel space of the boundary operator), the authors adopt a stochastic rank estimation method. First, the rank estimation problem is recast into a trace estimation problem through a spectral mapping function $h(\cdot)$, which can be constructed using a truncated Chebyshev series. Then, by employing a stochastic trace estimation method due to Hutchinson, the Betti number is estimated by summing over finitely many the Chebyshev moments. 

NISQ-TDA has been tested on both noisy numerical simulators and trapped-ion quantum devices (Quantiuum). Numerical results suggest good robustness against machine noise.

### Strengths
The Quantum TDA problem was first studied by Lloyd et al. (2016), in which an efficient quantum algorithm was proposed. The algorithm in Lloyd et al. requires a fault-tolerant quantum computer to run Grover's algorithm and digital Hamiltonian simulation (for QPE). This paper appears to propose a new quantum algorithm that does not rely on a fault-tolerant quantum computer with potential superpolynomial speedups compared to classical. 

Empirically, this paper presents both resource analysis (Fig 1A) and real-machine results (Fig 1B-D). Also, a noisy simulation suggests this algorithm is robust to machine noise. The numerical evidence strongly implies that this algorithm could be useful for NISQ devices, justifying the claim by the authors. Potential applications to ML, AI, neuroscience, and cosmology are discussed.

Overall, this paper is well-written and the plots are easy to follow.

### Weaknesses
I feel the technical discussion in Section 3 (especially the projection to a simplicial order) is a bit hard to follow. The description of the projection operators $P_{\Gamma}$ and $P_k$ lacks sufficient detail for a reader to readily implement them. For example, it's unclear how the quantum rejection sampling is explicitly realized in terms of quantum gates. A concrete example, showing the explicit circuit construction for a simple case (e.g., a 2-simplex), would significantly improve the clarity. Also, it would be beneficial to discuss more on the actual resources (gate counts, # of measurements, etc.) spent on the Quantinuum hardware. The current discussion is too high-level and lacks specific details about the hardware implementation. For instance, what is the specific gate sequence used to implement the Pauli operators, and how are the measurements performed to estimate the probabilities in Fig 1B-D?

### Questions
1. Theorem 1 gives a rigorous sample complexity of NISQ-TDA and the total time complexity is $O(\frac{n\log(1/\epsilon)}{\sqrt{\delta} \epsilon^2 \zeta_k^{2\log(1/\epsilon)/\sqrt{\delta}}})$. This time complexity looks exponentially better than the best-known classical result. However, this result is not directly comparable with the complexity of Quantum TDA ($O(n^5/(\delta_k \sqrt{\zeta_k}))$) (of course, the QTDA requires stronger quantum computers). Is it possible that NISQ-TDA can outperform the fault-tolerant QTDA in a certain parameter regime?

2. The circuit depth of NISQ-TDA heavily depends on the Chebyshev truncation number. What is the exact dependence of the Chebyshev truncation number in terms of the input data set (or the projection operator)? Does the resource analysis (Fig 1A) treat the Chebyshev truncation number as a parameter depending on the number of vertices, or it is fixed as a constant?

3. In Fig 1B-D, how many shots were used on the hardware to estimate the probability? 

4. In Fig 2A, the error seems huge for intermediate-size problems even with moderate machine noise (e.g., (0.001, 0.01) for 1- and 2-qubit gate error). To solve practical problems in the application domains, is there any way to further suppress/mitigate the machine noise for NISQ-TDA?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a hybrid classical-quantum algorithm for solving the problem of topological data analysis. More specifically, they consider the problem of estimating the Betti numbers for a simplicial complex. They propose an algorithm that is NISQ-friendly yet still yields speedup over the best-known classical algorithms. Moreover, the algorithm is fully implemented on an existing ion trap device, showing good agreement with simulated results as well as robustness to noise.

### Strengths
- This is a very interesting work that proposes to solve a problem that is hard for classical computers, accessible to quantum speedup, and is practically useful. 
- The end-to-end implementation on NISQ devices is quite amazing and the close match with noiseless simulation is also surprising.
- One particularly interesting aspect of this work is how they avoid the data-loading issue which is typical for many proposed quantum algorithms for machine learning. The projections by mid-circuit measurements appears to be an important step and I wonder if other quantum algorithms can benefit from this.

### Weaknesses
For real quantum advantage, the input data must satisfy several conditions listed at the end of Section 3. The advantage for solving the problem of deciding whether a simplicial complex has exponentially many holes seems less clear and perhaps less practical. It would be great to know if the algorithm still provides speedup for real-world instances. Specifically, the requirement that the input simplicial complex must have a number of holes that scales exponentially with the number of vertices is a strong constraint. It is not clear how often such complexes arise in practical applications of topological data analysis. Furthermore, even if such complexes do exist, the problem of determining whether a given complex satisfies this condition is likely to be computationally hard in itself, potentially negating any speedup gained from the quantum algorithm. The paper should discuss the practical implications of this constraint in more detail, perhaps by providing examples of real-world datasets that could satisfy it, or by discussing the kinds of data transformations that might be needed to make the algorithm applicable.

### Questions
- I am a bit confused by Figure 1B, C, and D. What exactly are the bars representing? I assume it shows the probabilities of obtaining results corresponding to vertices, edges, triangles, etc., but is it the case that several are omitted for the cube and square?
- I wonder if there is any intuitive, high-level reasoning for what kind of problem structure is being leveraged here that enables quantum speedup.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a quantum algorithm for topological data analysis (TDA), which is a technique for extracting shape-related features of high-dimensional data. The proposed algorithm NISQ-TDA uses a quantum rejection sampling technique to project onto the data-defined simplicial complex, and a stochastic rank estimation method to estimate the Betti numbers, which are signature values that describe the shape of the data. The paper provides theoretical and empirical analyses of the algorithm, showing that it has error guarantees, short circuit depth, noise resiliency, and potential speedup over classical algorithms for certain classes of problems.

### Strengths
1. The writing of the paper is clear and well-structured. The paper proposes a quantum algorithm for TDA called NISQ-TDA, which is a technique for extracting shape-related features of high-dimensional data. NISQ-TDA, is designed to work on noisy intermediate-scale quantum devices, which are the current and near-term quantum computers that have limited resources and error rates.

2. The paper presents one of the first quantum machine learning algorithms with short depth and potential significant speedup under certain assumptions. The proposed algorithm neither suffers from the data-loading problem nor does it likely require fault-tolerant coherence for even mid-size datasets.

3. The paper presents results from implementing the entire algorithm on real quantum hardware and noisy simulations, illustrating noise-resiliency at realistic noise-levels. The paper also discusses possible applications of NISQ-TDA for scientific machine learning and AI tasks.

### Weaknesses
1. The reviewer has a basic understanding of quantum computing, but not familiar with TDA. The paper does not provide sufficient background and related work on quantum computing, TDA and QTDA. It assumes that the reader is familiar with these topics and does not cite relevant literature or explain the key concepts and notations. Specifically, the paper lacks a clear explanation of the simplicial complex construction from the input data, which is fundamental to TDA. Furthermore, the quantum rejection sampling technique used for projection onto the simplicial complex is not sufficiently elaborated, making it difficult to assess its correctness and efficiency. The paper also does not adequately discuss the existing quantum algorithms for TDA, such as those based on quantum walks or adiabatic quantum computation, and how NISQ-TDA compares to them in terms of resource requirements and performance.

2. The paper does not provide any empirical evidence of the quantum advantage or noise-resiliency of the NISQ-TDA algorithm. It only shows some preliminary results on small datasets and noisy simulations, without any statistical analysis or comparison with baselines. The experiments lack a detailed description of the quantum hardware used, including the number of qubits, connectivity, and gate fidelities. The paper also does not specify the noise model used in the simulations, which is important for evaluating the algorithm's robustness. Moreover, the results are presented without any statistical significance analysis, making it hard to determine if the observed performance is due to the algorithm or random fluctuations. The absence of comparison with classical algorithms or other QTDA algorithms further limits the evaluation of the proposed method.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
