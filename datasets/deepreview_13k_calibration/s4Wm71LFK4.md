# What Are Good Positional Encodings for Directed Graphs?

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 8, 5, 6, 5

## Abstract
Positional encodings (PEs) are essential for building powerful and expressive graph neural networks and graph transformers, as they effectively capture the relative spatial relationships between nodes. Although extensive research has been devoted to PEs in undirected graphs, PEs for directed graphs remain relatively unexplored. This work seeks to address this gap. We first introduce the notion of \emph{Walk Profile}, a generalization of walk-counting sequences for directed graphs. A walk profile encompasses numerous structural features crucial for directed graph-relevant applications, such as program analysis and circuit performance prediction. We identify the limitations of existing PE methods in representing walk profiles and propose a novel \emph{Multi-q Magnetic Laplacian PE}, which extends the Magnetic Laplacian eigenvector-based PE by incorporating multiple potential factors. The new PE can provably express walk profiles. Furthermore, we generalize prior basis-invariant neural networks to enable the stable use of the new PE in the complex domain. Our numerical experiments validate the expressiveness of the proposed PEs and demonstrate their effectiveness in solving sorting network satisfiability and performing well on general circuit benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose (i) the notion of walk profile in a directed graph for counting bidirectional walks with given numbers of forward and backward edges between two nodes and (ii) a novel positional encoding (PE) which can provably reconstruct the walk profiles of the directed graph. This PE is a direct extension of Magnetic Laplacian PE (Mag-PE) to multiple phase shift parameters q (potentials): the position of a graph node is represented by concatenating Mag-PEs for the different parameters. 

In particular, they prove that in order to reconstruct walk profiles of some length L between any two nodes, just over half of this length is the number of potentials needed in their Multi-q Mag-PE. They also identify that expressing walk profiles is robust to the choice of the q values. Additionally, they generalize their PE, using ideas from previous stable PE frameworks, towards node-stable and edge-stable representations. 

In the experimental section, Multi-q Mag-PE is benchmarked against Laplacian, SVD and Mag-PE in predicting node pair distances and and classifying synthetic graphs; their PE is also coupled with backbone models to predict properties of real word circuits and its robustness explored. In most cases, Multi-q Mag-PE demonstrates a consistent performance gain over comparison baselines with up to x3 execution overhead (due basically to processing/training for more q's).

### Strengths
- This paper has an exemplary organization with clean definitions and explanation of fundamental developments and a balanced experimental section.

- Both the notion of the walk profile and the generalization of Mag-PE to multiple q's are well motivated and simple to reason about.

- It is important that the paper provides a provable connection of Multi-q Mag-PE (which is a latent representation) to something which is more "tangible": path type counters (i.e. walk profile) (Theorem 4.2).

### Weaknesses
 - Runtime overhead, although quantified within the x3 envelope in Section 5.4, is a disadvantage in the approach. The combination of SPE and standard Mag-PE could strike a good balance (but then the "which q value" question will be raised). Also depending on the number of q's, runtime overhead would vary. On this front, having a rule of thumb to adopt for the cardinality of q's (i.e. Q) for a given task/dataset combination, would be very useful to have.

- The explanation of why SVD-PE is insufficient for capturing bidirectional walk profiles could be more detailed. While the authors mention that SVD-PE captures alternating walks, the connection to the limitations in expressing general bidirectional patterns is not fully elaborated. Specifically, it is not clear how the inability to directly compute $[A^2]_{u,v}$ via SVD-PE lookup translates to a practical limitation in capturing general walk profiles. The argument would benefit from a more concrete example illustrating this deficiency.

- The justification for Equation (2) being produced "by definition" is insufficient. A more detailed explanation of how the phase accumulation along paths leads to the specific form of the equation is needed. The connection between the number of forward/backward edges and the resulting phase is not immediately obvious and requires further clarification.

- While the robustness to the choice of q's is empirically observed, a deeper theoretical explanation would be beneficial. The linear system argument is a good starting point, but it does not fully explain why the performance is not significantly affected by different choices of q, especially when considering the potential for generalization issues. The observation that random q's are not always optimal on real-world datasets suggests that the choice of q's is not entirely arbitrary and warrants further investigation. The tuning of the range of q's, similar to tuning the single q value in standard Mag-PE, should be discussed in more detail.

### Questions
- What is the intuition behind needing the PE of another, third node (w) in addition to the SVD-PEs of u, v nodes when discussing the shortcomings of SVD-PE? Actually SVD seems to be a good choice for compactly expressing powers of special structures like (A * A^T) or its transpose; powers of A are not the only matrices to use in the presence of both forward and backward links/edges. 

- Could you provide a more detailed justification of how Equation (2) is produced? (currently: "By the definition" (line 260)).

- A practical issue with Mag-PE is what q to choose. In Multi-q Mag-PE the choice of q's does not seem to be a critical factor in performance outputs (e.g. discrete Fourier transform based vs randomly sampled). Is there a justification for this empirically observed robustness? Or again, some care choosing q's should be exercised, but now on the range from which to select q's? For example for the case of random graphs q's are in (0, 1/2) range but for sorting network (satisfiability tasks) q's lie in a much "slimmer" range (defined as a function of the number nodes and edges)?

- What is the role of m in Equations (3), (4) (also consider balancing paretheses in these: minor, unbalanced "{" instead of "(" appear in them)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new positional encoding for node representation in directed graphs with provably better expressive power and stability. The paper starts by discussing Magnetic Laplacians with potential $q$, and introduces the concept of *walk profiles*, the number of walks of lengths $l$ given $l - k$ backwards passes of an edge, a more informative descriptor of directed graphs than the standard adjacency powers could provide. It then shows how a Magnetic Laplacian fails to predict walk profiles. Given this, the paper then proposes a simple extension, Multi-q Magnetic Laplacian Positional Encodings, and shows that this extension, with $Q$ distinct q values selected from the range $[0, \frac{1}{4})$ can predict walk profiles of length $L$ of nearly double $Q$ (Precisely, $Q = \lceil \frac{L}{2}\rceil + 1$). The paper then studies the stability of complex positional encodings returned with multiple Qs and proposes an invariant encoding mechanism (SPE) to circumvent the increasing ambiguity of complex eigenvectors and eigenvalues. 

Empirically, the paper conducts extensive experimentation, both on real-world and synthetic baselines. In synthetic settings, the paper proposes a setting in which models must predict (normalized) walk profiles and other structural properties (shortest path, longest path) over directed graphs. In these experiments, Multi-q Magnetic Laplacian PE with SPE clearly demonstrates superior performance, even with respect to the same model with other encoding choices than SPE (such as SignNet). Moreover, the paper reports ablation results on the selection of $q$ values, showing that multiple $q$ values are indeed necessary for performance, and that even only using the best $q$ cannot reproduce the best results. A robustness study is also reported, highlighting that performance is robust to choices of $q$, and even improves slightly with random (distinct) $q$ values. In terms of real-world experiments, the paper conducts an extensive experimental study on a suite of directed graph benchmarks, demonstrating strong performance improvements with Multi-q Magnetic Laplacian PE across several baseline models. Finally, the paper discusses runtime for pre-processing, training and inference using their approach, and shows that while $q$ does lead to increased runtimes, these increases are palatable.

### Strengths
- The theoretical arguments made by the paper are sound and well-thought: The definition and accompanying figures for walk profiles are very helpful, and are very well connected to real-world settings. Moreover, the proof sketch for showing how Multi-q Magnetic Laplacian can recover walk profiles in Theorem 4.2 appears sound. Overall, the flow of argumentation in this paper is smooth, balanced, and easy to follow, with all pre-requisite results presented in good time.
- The experimental analysis is compelling and extensive. I especially appreciate the synthetic results and the targeted study of structural graph property predictions, which in my opinion really emphasizes the contribution of the paper's approach. These findings are also further supported by ablation and robustness analysis, and comprehensive details in the appendix. Real-world experiments are also strong and convincing. All in all, the empirical analysis ties very nicely with the theoretical results, and corroborates its results nicely.

### Weaknesses
 - One aspect of this work that could be improved is to include baselines and datasets used in previous work, such as OGBG-code, NA and BN (as used, e.g., in Thost et al). The current results are quite strong, but I imagine that the message would be even more compelling if your findings also apply to more specialized models, and produce results on the corresponding datasets to glean more interesting insights, e.g., can these PEs even improve specialized directed GNN models? 

In general, I find that this is a serious work with good presentation, extensive experimentation, and a strong take-away message. I therefore support this paper for publication.

### Questions
No questions.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper attempts to determine good positional encodings for directed graphs. To quantify this, the authors first introduce the graph-topological concept of “walk profilesˮ, which count how many paths there are between all two nodes with a varying relaxation $k$ of how many edges can be oriented in the “wrong wayˮ. Then, they show that a normal Laplacian PE cannot capture all of these walk profiles, while their extended Magnetic Laplacian, $L$-MagPE, can capture all such walks up to length $\frac{L}{2} +1$.

### Strengths
- The paper is presented adequately, and is easy to read.
- The interest in being able to express the walk profiles is nicely motivated in the introduction.
- Walk profiles are introduced as a way of counting walks which is more comprehensive than simple shortest path distances, which can be trivial in directed graphs.
- The authors show empirically that their method is superior when simple models are used on simple tasks. They also show that theoretically their PE is more expressive with respect to walk profiles.

### Weaknesses
 - As the authors have discussed it in Section 4.3, the main limitation is the extra compute-time with larger $L$, induced namely by the calculation of large and numerous eigendecompositions. As shown in Section 5.4, the cost seems to grow linearly.
- While it is described informally why walk profiles can be of interest, there is no theoretical justification of their use. Moreover, there are no connections to existing measures of modelsʼ expressivity (e.g., $k$-WL[1]).
- It is not clear whether the authors have attempted any other methods to provide information about walk profiles. It is also not discussed whether other PEs [2, 3] also lack this ability to capture walk profiles.
- In the experiments, while there is a fair share of ablations, standard GNN models can be added.
- In the experimental section, it seems that the biggest gain was in the Experiment 5.1, where very simple models are used. As soon as the task gets more complex, a stronger model is invoked (SAT), and there the gains are much less evident if present at all.

Overall, the paper also does not adequately answer the question it sets in its title. While the paper propose a positional encoding specific for directed graphs (and discusses its properties), it does not answer the question of what makes good positional encodings for directed graphs (and where the expressiveness is located compared to many potential alternatives).

### Questions
1. Have you tried reducing the cost when calculating higher terms? Or is it a fundamental limitation of the method?

2. Why are walk profiles are of interest? Of course, they might be explicitly such for some tasks, but can graph transformers (such as SAT) not learn them some other way using other positional embeddings?

3. Have you tried other simple models on the datasets, potentially with no positional encodings just to see how they perform as baselines?

4. For the experiment in Section 5.1, have you tried larger graphs?

5. Do you know whether walk profiles are related in any way to $1$-WL or beyond for measuring expressivity?

6. How could the proposed approach be located within existing PEs in terms of expressiveness? The proposed approach may be better (as argued) in terms of capturing walk profiles, but other PEs (or their variations on directed graphs) may have other strengths.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the need for improved positional encodings (PEs) specifically designed for directed graphs. The authors introduce Multi-q Magnetic Laplacian PE, an enhancement of the Magnetic Laplacian PE that incorporates multiple potential values (q) to better capture directed graph structure. This Multi-q Mag-PE method is proposed to address limitations in existing PEs for directed graphs by generalizing walk-counting sequences into a walk profile. The paper provides theoretical support for Multi-q Mag-PE's effectiveness and evaluates it on multiple tasks, where it is shown to outperform traditional single-q PEs and other established methods.

### Strengths
1.	Multi-q Mag-PE is a unique extension within the domain of GNN, specifically targeting the gap in encoding methods for directed graphs.

2.	The paper establishes theoretical backing for Multi-q Mag-PE's ability to capture bidirectional walks and to accurately express walk profiles. This is an advancement over prior methods that fall short in representing such details in directed graphs.

3.	Through extensive experiments across synthetic and real-world datasets, the paper demonstrates that Multi-q Mag-PE can outperform existing PEs, validating its effectiveness for both complex and directed graph tasks.

### Weaknesses
1.	Although theoretically the Multi-q Mag-PE should allow near-perfect reconstruction of the walk profile, practical RMSE results are not close to zero. This discrepancy, acknowledged by the authors, indicates limitations in applying the theoretical model to real-world scenarios. Specifically, the optimization process for learning the mapping from the Multi-q Mag-PE to the walk profile appears to be a bottleneck. The paper does not provide sufficient analysis on the optimization landscape, which could be highly non-convex, leading to suboptimal solutions and the observed non-zero RMSE.

2.	The Multi-q approach significantly increases computational demands due to multiple eigenvalue decompositions, which could challenge its scalability to larger graphs, especially those with millions of nodes or edges. Although the authors attempt to address this with runtime experiments and discuss potential optimizations, questions about the approach's feasibility for large-scale real-world applications remain. The paper lacks a detailed analysis of the computational complexity as a function of the number of q values and graph size, making it difficult to assess the practical applicability of the method for large graphs.

3.	The motivation for introducing the walk profile is not so clear. To be specific, heuristic definitions or possible theoretical explanations are needed to illustrate its effectiveness. While the paper mentions that walk profiles capture directed motifs, it does not provide a rigorous justification for why this representation is superior to other possible encodings. A more detailed explanation of the theoretical properties of walk profiles, and how they relate to the structural characteristics of directed graphs, is needed.

4.	The improvements shown in real-world tasks were less pronounced than those on synthetic datasets, potentially due to the controlled nature of synthetic datasets, which may not represent the broader spectrum of real-world graph structures. The paper does not provide sufficient analysis of the differences between synthetic and real-world datasets, nor does it discuss the potential reasons for the performance gap. This makes it difficult to assess the generalizability of the proposed method.

### Questions
1.	Given that the computational complexity of directly using the walk profile is potentially manageable, could you elaborate further on why it wasn’t directly computed as features? Additionally, would an ablation of such a direct computation provide insight into how Multi-q PE compares in practical tasks?

2.	Would it be possible to apply this model to larger graphs by selectively reducing the number of q values?

3.	Have you considered validating the proposed method on a wider range of GNN or transformer backbone models? This could help generalize the results and illustrate broader applicability across different architectures.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel positional encoding (PE) to enhance both message-passing GNNs and graph transformers, specifically, over directed graphs. Essentially, it extends the Magnetic Laplacian eigenvector-based PE by incorporating multiple potential factors. The evaluation is rather detailed containing both general performance comparisons and more elaborate analysis.

(Please note: I did not check all theoretical details)

### Strengths
- The research is well motivated in the first sections of the paper
- The theory is well-explained
- It is nice that the approach is considered with both MPNNs and transformers
- Also, the authors mention that this is the first work to propose the usage of complex PEs in a stable way. But I don't have the expertise to judge the relevance of this.

### Weaknesses
 - The paper is rather densely written
- Table 3 (which contains the more important, real-world data) is hard to parse and the differences seem oftentimes marginal (e.g., considering standard deviation)
- Another suitable baseline on the DAG data would be DAG transformer [1]
- There is a recent paper [2], which considers other realistic datasets, and maybe should be considered as competitor and be compared to 

### Questions
- Sec. 5.4: what is the size of the data here?

### Soundness
3

### Presentation
2

### Contribution
3
