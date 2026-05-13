# Beyond Circuit Connections: A Non-Message Passing Graph Transformer Approach for Quantum Error Mitigation

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Despite the progress in quantum computing, one major bottleneck against the practical utility is its susceptibility to noise, which frequently occurs in current quantum systems. Existing quantum error mitigation (QEM) methods either lack generality to noise and circuit types or fail to capture the global dependencies of entire systems in addition to circuit structure. In this work, we first propose a unique circuit-to-graph encoding scheme with qubit-wise noisy measurement aggregated. Then, we introduce GTraQEM, a non-message passing graph transformer designed to effectively mitigate errors in expected circuit measurement outcomes. GTraQEM are equipped with a quantum-specific positional encoding, a structure matrix as attention bias guiding nonlocal aggregation, and a virtual quantum-representative node to further grasp graph representations, which guarantees to model the long-range entanglement. Experimental evaluations demonstrate that GTraQEM outperforms state-of-the-art QEM methods on both random and structured quantum circuits across noise types and scales among diverse settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors put forward a new graph-transformer method for quantum error mitigation. By not using message passing, the approach has the potential to better capture the long-range correlations created by quantum circuits.

### Strengths
Strengths:
   - It is a nice application of graph transformers. While it’s pretty straightforward, their approach works better than other GNN-based quantum error mitigation methods that I’ve seen.
   - Pretty good results on simulated data. While a lot of the error bars overlap, the new method regularly outperforms competitors on many of the toy error models.

### Weaknesses
REVISION: Many of my concerns have been addressed.

Weaknesses:
   - Lots of misleading or slightly incorrect claims in the background section. See below.
   - Simulations leave a fair bit to be desired. In particular, they don’t use any error models with coherent errors, which are particularly pernicious kinds of errors because they’re effects depend intimately on the unitary implemented by a quantum circuit (e.g., coherent errors can cancel). The IBM fake providers use an error model that models gate errors as a depolarizing channel followed by thermal relaxation (T1 decoherence). Their incoherence-only error model only features depolarizing noise, which is probably the easiest to mitigate
   - No head-to-head comparisons on experimental data: They ran 50-qubit circuits on IBM Brisbane but then didn’t compare their new approach to other methods (if they did, I’m sorry! I missed it in the paper).

Miscellaneous remarks:
   - The circuit-to-DAG encoding (or a very similar encoding) used in this paper was used earlier in this paper: “QuEst: Graph Transformer for Quantum Circuit Reliability Estimation.” You should cite it.

Here’s a list of the misleading claims in the paper: 
   - “Quantum Error Correction (QEC) (Calderbank & Shor, 1996; Gottesman, 1997; Terhal, 2015) first offers a theoretical solution by fully correcting quantum errors at the hardware level, but its implementation demands impractically qubit overheads and complex operations (Cai et al., 2023).” I don’t think that QEC corrects errors at the hardware level. Most QEC protocols (e.g., quantum error correcting codes) require syndrome data to be extracted and then processed by a classical co-processor. The quantum state is then adaptively updated (at least when running a circuit that uses a universal gate set) in response to the results of the syndrome data analysis. I’d change this statement to better reflect how QEC works.
     I also don’t think it’s fair to say that QEC is “impractical.” Large-scale fault-tolerant quantum computation is certainly currently infeasible, but lots of teams are working on making it a reality! I’d re-phrase this to say that large-scale fault-tolerance quantum computation is currently well beyond the capabilities of our experimental hardware. 
   - “ Overall, QEM provides a feasible approach to enable imperfect quantum systems to produce reliable outcomes (Kandala et al., 2019; Bravyi et al., 2022; Cai et al., 2023), which is crucial for achieving practical quantum supremacy over classical supercomputers (Daley et al., 2022; Kim et al., 2023).” So, most quantum error mitigation methods also have an exponential-in-the-qubit-count overhead. So it’s not clear if they’ll offer a path to quantum computational supremacy. Past works, such as in the Kim et. Al. Paper, have only shown hints at quantum advantage, which is a much weaker claim. This sentence should be rewritten to reflect this.
   - “ Machine learning-based QEM methods have recently been developed, offering greater generality across various settings.” This claim is questionable and requires citations. 
   - “ Bell nonlocality (Bell, 1964; Brunner et al., 2014) demonstrates that entangled particles exhibit correlations where the measurement outcome of one particle instantaneously influences that of another, regardless of the distance between them.” This is not an accurate description of Bell nonlocality. Entanglement does not allow particles to influence each other at a distance. No information is transmitted. Instead Bell nonlocality allows for measurement distributions with non-classical correlations. 
   - “ We introduce a data augmentation technique that constructs training data by composing circuits with their inverse circuits.” Composing circuits with their inverses in order to (ideally) create the identity circuit is not a new idea. It underpins almost all randomized benchmarking algorithms (Clifford RB, Magann et. Al.). You should at least mention this.
   - Section 2.2 gives a very non-standard overview of the noise sources in quantum computers. For instance, I’ve never heard anyone use the term “real quantum device errors” before. I would re-write the section to first talk about Markovian vs. non-Markovian errors, then step through the differences between the kinds of Markovian errors a device can experience: incoherent/stochastic errors, coherent errors, and “other errors” like amplitude damping (see “A Taxonomy of Small Markovian Errors”). N.B. I’m pretty sure that all quantum error channels also have a Kraus decomposition (this is not clear from your claim in A.7.1 when you state that incoherent errors have a Kraus decomposition).

### Questions
Why are there no comparisons to other techniques in the 50-qubit data?

What was the total wall clock time spent running each error mitigation method in your simulations?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel approach, GTraQEM, for quantum error mitigation. This method is based on a graph transformer that employs multi-head attention mechanisms and a learnable Quantum Circuit-Representative node instead of traditional message-passing. The authors claim that this model captures both the circuit structure and its intrinsic nonlocality, which are limitations in existing learning-based or ML-based QEM methods. Experimental results demonstrate that GTraQEM outperforms ML-based approaches on both random quantum circuits and Trotterized circuits.

### Strengths
1. GTraQEM introduces a unique non-message-passing graph transformer approach and a circuit-to-graph encoding scheme for quantum error mitigation.
2. The authors present a data augmentation technique, called circuit inverse composition, which reduces dependency on ideal expectation values in the training data.
3. The paper demonstrates GTraQEM’s error mitigation performance compared to learning- or ML-based approaches on both random and structured quantum circuits across various noise types.

### Weaknesses
1. While the authors compare GTraQEM with learning- or ML-based QEM approaches, showing many promising results, classical QEM methods such as Probabilistic Error Cancellation, Symmetry Constraints, and Purity Constraints are not included in the experimental comparisons or discussed anywhere in the paper.
2. The authors clearly demonstrate that GTraQEM can achieve better performance in noise calibration compared to learning- or ML-based QEM methods. However, they do not compare the overheads of these methods, which is crucial for evaluating QEM methods.
3. I am concerned about the scalability of GTraQEM due to its reliance on edge features that require expectation measurements. As quantum circuits grow in size and complexity, the need for extensive measurements could result in significant resource demands, potentially limiting the applicability of GTraQEM for larger quantum systems or more complex circuits.
4. Typo: [Czarnik, 2021a] and [Czarnik, 2021b] refer to the same paper.

### Questions
My questions address the weaknesses of the paper:
1. Why did you choose not to include classical QEM methods such as Probabilistic Error Cancellation, Symmetry Constraints, and Purity Constraints in your experimental comparisons?
2. Can you provide experimental or theoretical comparison of the overhead associated with GTraQEM compared to other QEM methods?
3. How do you plan to address potential scalability issues related to the need for expectation measurements in GTraQEM as circuit sizes and complexities increase?
4. Could you explain why there is only ZNE compared in the no idea EV cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a novel quantum error mitigation (QEM) method, GTraQEM, which uses a machine-learning approach. GTraQEM encodes the quantum circuit into a graph, then uses a non-message-passing graph transformer to construct a QEM mitigator. The effect is proved by 1) numerical simulations using a quantum circuit simulator; 2) IBM's quantum computer, and the authors compares GTraQEM with many other existing QEM approaches.

QEM is a popular way to handle the quantum error in near-term quantum computers which are subject to noise, before a practical quantum error correction can be realized.  ML-based QEM is of great importance in the NISQ era because of its practicality in the experiment.

### Strengths
1. The technique used in this paper is novel, and the results are good. Inputting the circuit structure into the graph transformer to construct ML-based QEM is intuitive, which is also proved to be effective via numerical evidence.
2. This paper uses a practical test case (transverse-field Ising model), which is considered to be one of the most possible applications of quantum computers in NISQ-era.

### Weaknesses
1. Unclear experiment settings.

The experiment settings used in this paper are not clearly stated in the experiment section. This highly weakens the paper's conclusion. Because QEM is an area that is mainly based on experimental/numerical evidence, it is vital to clarify the methods and the settings when the authors do not provide any codes.

In my opinion, the results shown in the figures and tables are not that convincing for me. For example, In Fig. 3, the results show that ZNE does not have any effect in all experiments. This clearly contradicts with the famous known results such as [Nature volume 618, pages500–505 (2023)], which also applies the transverse-field Ising model and trotterisation. 

2. The paper writing needs to be strengthened. For example, the 15-qubit circuits experiment in Table 2 seem to be confusing. Why do we need this?

3. Figure 3 is unclear. I can hardly recognize the color.

4. There are many typos. For example, 6 qubit should be 6-qubit (in Fig. 3), and the 
broken sentence in line 408.

5. The limitations of the proposed approach should be discussed, including the extra cost caused by the acquisition of the training set, and the cost of the training process.

### Questions
A few concerning points are listed as follows, and I hope the authors can clarify these before I change my mind about this paper's decision.

1. The original data/code generated by this paper should be provided to improve reproducibility. Also, there should be an explanation about why ZNE does not have any effect in Fig. 3 and Table 1.

2. The y-axis in Fig. 4 is the absolute error of EV. However, panel (f) implies there is some distribution over 2.0. In fact, it should be always in the range [0,2] (considering the observable should be within [-1,1]). 

3. Whether the type of the circuit matter in GTraQEM? How is the generalizability of the method?

4. As this paper uses an IBM's quantum computer (Brisbane), it is recommended to articulate the hardware's physical parameters to improve the soundness, e.g. the topology (including the 50 used qubits), the coherence time, the single-qubit and two-qubit fidelities during the experiment.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a learning-based quantum error mitigation method by leveraging quantum-specific positional encoding and a structure information matrix for transformer to suppress the noise when estimate the expectation value.

### Strengths
this work exploits circuit topology in learning-based QEM empowered by multi-head attention and provides comprehensive experiments and shows the out-performance.

### Weaknesses
1. since it does not provide the related codes, the reproducibility is unknown.
2. while this work applies the various exist techniques to enhance the QEM which may be interesting for the community of quantum computation, it does not propose some novel structure or interesting theoretical findings which have widely applications.

### Questions
1. what does Fig.2. want to express? It is unclear the inverse quantum circuit used in here.
2. In Fig1. does the model use DAG with learnable node(QCR Node) to construct parametrized structure matrix? does the output of GTraQEM module concatenates with $x_{QCR}^L$ to form the input of the regression module? and how to construct $x_{QCR}^{L}$ ?
3. what's the sample complexity of such learning-base QEM model?

### Soundness
3

### Presentation
2

### Contribution
3
