## Human Reviewer 1

### Summary
This paper studies causal structure learning from observational data, with an emphasis on scalability to high-dimensional settings. In particular, the authors decompose the overall structure learning problem into local subproblems, and develop an integration strategy based on a weighted voting mechanism with acyclicity enforcement. For the weighted voting mechanism, they give each edge $X -> Y$ a score $s(X \to Y)$, based both on the number of times that $X - Y$ occurs (with either orientation), and out of those times, what fraction of times it occurs in the orientation $X -> Y$. These weights are fed into a Greedy Feedback Arc Set (FAS) algorithm to (heuristically) maximize the total weight of included edges, while maintaining acyclicity, and the final graph is given by thresholding the GreedyFAS output.

Experimentally, the authors test on synthetic data and on the Sachs protein signaling dataset, with various recent causal discovery algorithms as base learners. In the synthetic experiments, they study both Erdos-Renyi and scale-free graphs, with both a naive parameter generation strategy as well as a normalized strategy. Using their method (with especially with weighted voting) tends to improve the performance of base learners across various metrics, such as false discovery rate (FDR), true positive rate (TPR), structural Hamming distance (SHD), and F1 score, and decreases computation time. They also offer a sensitivity analysis of one of their key parameters, $\lambda$, where larger $\lambda$ leads to denser graphs, obtaining smooth precision-recall curves.

### Strengths
**Originality and significance:** As the authors acknowledge, the idea of modular causal discovery is relatively well-studied, but existing algorithms are typically non-modular (i.e., they cannot use arbitrary base learners) or have other downsides (e.g. using a non-scalable algorithm for stitching together the subgraphs). The modularity of the proposed framework is nice, and the stitching algorithm is lightweight (though, by necessity, heuristic). Overall, the direction is a promising one for more scalable causal discovery.

**Quality and clarity:** The motivation and methodology is well-described, as well as the reason for particular methodological choices. The work is well-executed, with a good mix of theoretical results and empirical investigation.

### Weaknesses
**Details of causal structure learning:** Some details about causal discovery seem to be neglected or underemphasized. In particular, I noted two main issues:
1. **Introduction of unobserved confounding:** Taking a subset of nodes from a causal graph introduces unobserved confounding, even for Markov blankets. For example, take the graph with edge $X_1 \to X_2$, $X_1 \to X_3$, and for $k \in \\{1,2,\ldots,K \\}$, the edges $X_2 \to Y_k$ and $X_3 \to Y_k$. Then, for each $k$, the Markov blanket is $(X_2, X_3, Y_k)$, and the local graph will have an edge between $X_2$ and $X_3$. If $K$ is large, then there would be some edge between $X_2$ and $X_3$ in the final graph, even though that edge is not in the true graph. In particular, each base learner will *not* return the subgraph induced by ${V} \cup \text{MB}(V)$, but a supergraph of the induced graph. 
2. **Identifiability of orientations:** In the introduction, the authors state that "the true DAG can be recovered given sufficient data", but for only observational data, this is simply untrue without further assumptions (e.g. linearity + non-Gaussianity). It seems that their framework assumes every base learner returns a DAG, rather than a Markov equivalence class / essential graph. This should be discussed and emphasized, and is a limitation of their approach in settings where those further assumptions are unwarranted.

**Minor weaknesses**
3. I don't think Theorem 3.1 is worth stating as a theorem, it's immediately implied by the definition of the Markov blanket.
4. Theorem 3.2 assumes that the votes are independent, but in practice the subgraphs will not be independent if each subgraph is learned using the same dataset. They can be made independent by data partitioning, but this drastically reduces the sample size.

### Questions
1. How do you address the issue that taking subsets introduces unobserved confounding? (see Weakness 1)
2. How should these results be applied when the votes are not independent? (see Weakness 4)

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
The authors propose an efficient causal structure learning method (VISTA), which decomposes the global causal structure learning problem into local subgraphs based on Markov blankets and then integrates these subgraphs through a weighted voting mechanism. They also provide the theoretical analysis for the weighted voting and error bounds analysis for the proposed method. Experimental results demonstrate the effectiveness of VISTA.

### Strengths
1. The theoretical analysis is helpful, which supports the proposed idea.

2. The experimental comparisons are sufficient, verifying the effectiveness of VISTA.

### Weaknesses
1. The details of learning each subgraph are insufficient. Did the authors use the raw data, or the data consisting of the target variable and its Markov blanket?

2. In part 3 of Section 2, the authors state that “they either assume correct inputs at merging time, …, or perform essentially uncalibrated frequency-based stitching”. Could the authors provide specific examples of existing methods that fall into each of these two categories? In addition, how does the proposed method differ from the latter type, given that it also learns local subgraphs from data and integrates them via weighted voting? Fundamentally, isn’t the proposed approach also frequency-based in nature?

3. For Theorem 3.1, isn’t 𝐸 supposed to be the complete set of edges? Why is it stated that 𝐸 ⊆ 𝐸(𝐺’)? Moreover, it is unclear how 𝐺’ is derived. In other words, the construction of 𝐺[𝑋 \cup 𝑀𝐵(𝑋)] (for X \in V) is not properly defined in the proof. Consider the causal structure 𝐴→𝐵←𝐶 & 𝐴→D & D←𝐶. If we learn G[B \cup MB(B)] (i.e. G(B \cup {A,C})), is it learned solely from the data containing variables A, B and C? if so, it seems 𝐺’ cannot be correctly reconstructed. Could the authors clarify this? 

4. Figure 1 is useful as it illustrates the advantages of the proposed idea. However, there is one concern: the Markov blanket represents a subset of features, whereas other causal discovery methods output causal structure. Why, then, is it appropriate to compare them directly?

5. Regarding Section 3.1, which constitutes the core of the paper, the authors introduce NV as the native idea (or baseline) motivating their approach. However, this baseline appears to be a misleading aggregation strategy. In causal discovery, researchers would not typically take the NV idea as the natural voting point. Instead, a more common and intuitive approach is to perform edge-level frequency voting first, followed by direction-level voting. Therefore, from my perspective, I consider that it is not appropriate to present the proposed method as a remedy to the limitations of NV, as this comparison lacks persuasiveness.

### Questions
As noted in the Weaknesses, especially points 3 and 5.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces VISTA (Voting-based Integration of Subgraph Topologies for Acyclicity), a modular framework that decomposes the global causal structure learning problem into local subgraphs based on Markov Blankets. The global integration is achieved through a weighted voting mechanism that penalizes low-support edges via exponential decay, filters unreliable ones with an adaptive threshold, and ensures acyclicity using a Feedback Arc Set algorithm.

### Strengths
1.	Decomposes global DAG learning into node-centered MB subgraphs; plug-and-play with any MB finder and local learner, without adding identifiability/distributional assumptions on bases.
2.	The aggregation strategy is efficient and edge-level, performing a one-pass weighted voting instead of relying on expensive global searches or solver-based optimization. It also comes with theoretical guarantees.
3.	Experiments demonstrate that VISTA remedies the typical performance drop of base learners, consistently improving performance over standalone baselines.

### Weaknesses
1. The goal of many causal discovery tasks is to learn the Markov blanket, yet this approach requires first learning the Markov blanket for each node — a process seems to be somewhat putting the cart before the horse. In general, the divide-and-conquer causal discovery techniques should try to avoid overly strong `divide ` tasks, for example, doing divide based on a learned rough skeleton or structure. For instance, we can first run the PC algorithm to construct a causal graph, then partition this graph and apply NOTEARS or DAG-GNN separately to each subgraph, and can yield better performance compared to directly applying the N./D. to the entire node set. But does this even make much sense?

2. The experiment is inadequately designed/conducted:

2.1 It should incorporate the extent to which Markov blanket learning performance influences causal discovery results.

2.2 It should incorporate constraint-based and causal functional model-based baselines, evaluated in terms of both time efficiency and accuracy performance.

2.3	It should incorporate other divide-and-conquer causal discovery methods, such as
Cai R, Zhang Z, Hao Z. SADA: A general framework to support robust causation discovery. International conference on machine learning. PMLR, 2013: 208-216.
Cai R, Zhang Z, Hao Z, et al. Sophisticated merging over random partitions: a scalable and robust causal discovery approach. IEEE Transactions on Neural Networks and Learning Systems, 2017, 29(8): 3623-3635.
Md. Musfiqur Rahman, Ayman Rasheed, Md. Mosaddek Khan, Mohammad Ali Javidian, Pooyan Jamshidi, and Md. Mamun-Or-Rashid. 2021. Accelerating Recursive Partition-Based Causal Structure Learning. Proceedings of the 20th International Conference on Autonomous Agents and MultiAgent Systems. 2021, 1028–1036.

2.4 The paper claims efficiency, yet the only real-data evaluation is on Sachs (11 variables, 856 samples), which makes it hard to demonstrate scalability. Moreover, there is no systematic runtime comparison. Thus, the efficiency claim is insufficiently supported.

2.5	The paper reports extensive synthetic results on ER/SF graphs (various n) but does not specify the data-generation pipeline — e.g., the SEM family (linear vs. nonlinear) and noise distributions. Please add a brief, self-contained description. This will make the experiments reproducible. Moreover, the causal discovery results are primarily affected by in-degree, not out-degree; thus, presenting only out-degree information adds little value to the analysis.

2.6	To strengthen the persuasiveness of the findings, visual divide-and-conquer should be performed on a classic dataset (e.g., ALARM or ANDES, see “bnlearn”).

### Questions
Please see Weaknesses*

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper introduces VISTA, a scalable "divide-and-conquer" framework for causal discovery. It learns local structures within node-specific Markov Blankets, aggregates them using a novel Weighted Voting scheme to suppress noise, and enforces a global acyclic structure. VISTA is theoretically grounded and experimentally validated to be faster and more accurate than baselines, substantially reducing the False Discovery Rate.

### Strengths
1. The proposed Weighted Voting aggregation mechanism is novel and elegantly designed, surpassing simple heuristic rules.

2. The experimental validation is comprehensive, systematically demonstrating the superiority of the method across multiple settings.

3. The method is supported by a solid theoretical foundation in addition to its outstanding empirical results.

### Weaknesses
1. The performance ceiling of the VISTA framework is largely constrained by the accuracy of the Markov Blanket identification in the initial step. If the MB estimation algorithm performs poorly under conditions of data sparsity or extremely high dimensionality, the associated true causal edges can never be recovered in subsequent steps. The paper's discussion on this limitation is somewhat insufficient. Although the framework is modular, a sensitivity analysis concerning its "weakest link" would strengthen the paper.

2. In a very dense graph, the Markov Blanket of a node could be very large. In such cases, the computational advantages of the "divide-and-conquer" approach may be significantly diminished. 

3. The paper provides a good comparison of Weighted Voting (WV) with Naive Voting (NV), where WV's superior performance is expected. However, the comparison with other voting-based ensemble methods is not sufficiently in-depth.

4. The final stage of the framework employs the GreedyFAS heuristic to ensure acyclicity. While efficient, heuristic methods can introduce new errors. The paper fails to provide an analysis that quantifies the potential negative impact of this heuristic step on the final results.

### Questions
1. Could you comment in more detail on the sensitivity of VISTA to errors in the initial Markov Blanket identification stage? For instance, what is the quantitative impact on the final structural accuracy if the recall of MB identification is low?

2. In the context of dense graphs, how do the performance and efficiency of VISTA compare to running a baseline algorithm directly on the full graph? Are there scenarios where the overhead of the divide-and-conquer strategy outweighs its benefits?

3. While the paper demonstrates the superiority of Weighted Voting over Naive Voting, could you elaborate on how WV compares to other established voting-based ensemble methods?

4. The GreedyFAS heuristic is used for cycle breaking in the post-processing step. Could you elaborate on the implications of choosing this approximation algorithm on the final output? What is the potential bias introduced compared to an optimal (though computationally expensive) cycle-breaking method?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3
