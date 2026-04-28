# On the Completeness of Invariant Geometric Deep Learning Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Invariant models, one important class of geometric deep learning models, are capable of generating meaningful geometric representations by leveraging informative geometric features in point clouds. These models are characterized by their simplicity, good experimental results and computational efficiency. However, their theoretical expressive power still remains unclear, restricting a deeper understanding of the potential of such models. In this work, we concentrate on characterizing the theoretical expressiveness of a wide range of invariant models. We first rigorously bound the expressiveness of the most classic invariant model, message-passing neural networks incorporating distance (DisGNN), restricting its unidentifiable cases to be only highly symmetric point clouds. We then show that GeoNGNN, the geometric counterpart of one of the simplest subgraph graph neural networks (subgraph GNNs), can effectively break these corner cases' symmetry and thus achieve E(3)-completeness. By leveraging GeoNGNN as a theoretical tool, we further prove that: 1) most subgraph GNNs developed in traditional graph learning can be seamlessly extended to geometric scenarios with E(3)-completeness; 2) DimeNet, GemNet and SphereNet, three well-established invariant models, are also all capable of achieving E(3)-completeness. Our theoretical results fill the gap in the theoretical power of invariant models, contributing to a rigorous and comprehensive understanding of their capabilities. We also empirically evaluated GeoNGNN, the simplest model within the large E(3)-complete family we established, which achieves competitive results to models relying on high-order invariant/equivariant representations on molecule-relevant tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the geometric completeness of a significant class of geometric deep learning models: invariant neural networks. These networks leverage invariant features to impose strong inductive biases on spatial information, yet their theoretical expressive power remains somewhat unclear. This study aims to bridge that gap, enhancing both our theoretical understanding and practical application of these models.

The authors first demonstrate that incorporating distance into message-passing neural networks (like DisGNN) allows for the identification of asymmetric point clouds but struggles with highly symmetric ones. They then investigate geometric extensions of subgraph-based GNNs and prove that these models, specifically GeoNGNN, can successfully distinguish symmetric point clouds, achieving E(3)-completeness.

### Strengths
- The paper attempts to address a crucial problem that enhances our understanding of the potential of invariant neural networks and can guide future model design.
- Investigating the geometric counterparts of subgraph GNNs is a novel contribution.
- The results extend beyond specific cases, such as asymmetric point clouds, broadening our understanding of how these models perform on symmetric point clouds as well.

### Weaknesses
 - The paper lacks clarity and structure in some areas. The detailed explanation of NGNN, which serves as the backbone of their main contribution, the GeoNGNN framework, is left in the appendix. I recommend the authors integrate key aspects of NGNN, such as its core equations or an architectural diagram, into the main text. Additionally, including a comparison with the original DisGNN would be helpful—highlighting the differences and explaining what enables NGNN (intuitively) to overcome the limitations of DisGNN. This would give readers a clearer understanding of how the proposed approach builds on previous work and addresses specific challenges without disrupting the flow. Instead, a brief overview of NGNN, along with key formulas and a comparison with GNN, could benefit the flow of the whole paper.

 - The results are primarily constrained to cases with global connectivity, which is often impractical in real-world applications due to the significant computational costs. Several studies [1], [2], [3], [4] have explored scenarios where the graph is not fully connected, underscoring the need to evaluate the performance of invariant neural networks in sparse graph settings. In practice, invariant neural networks tend to perform worse than equivariant ones in these cases. While the authors have left these cases in the future direction, it would greatly strengthen the paper if they could extend their analysis to sparse graphs or at least discuss how their completeness results may vary with different levels of graph sparsity. Providing theoretical bounds on performance degradation as connectivity decreases would also be valuable.

 - The experimental results, while showing some improvement, are relatively marginal, which limits the empirical impact of the work. I suspect this might be due to the sparsity of the graphs used in practical applications. The authors should aim to demonstrate the significance of their approach by clarifying in which specific cases their method outperforms existing methods. Providing examples or scenarios where GeoNGNN has a clear advantage would strengthen the empirical contributions.

### Questions
Please address the concerns I raised in the weaknesses section. Additionally, I recommend revising the introduction to better reflect the paper's contributions. In my view, the primary contribution is the proposal of the geometric counterpart of NGNN and the proof that this approach effectively resolves the limitation of DisGNN in identifying **symmetric point clouds when the graphs are even fully connected**. 
The authors should also consider relevant experiments in this direction to emphasize the novelty and significance of this work.

### Soundness
2

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper offers the following contributions:
1) Introduces and defines the notion of "Identify" for invariant GNNs, positioned between distinguishability and completeness.
2) Provides a characterization for the incompleteness of DisGNN
3) Proposes GeoNGNN to ensure indentification of the cases where DisGNN is incomplete
4) Demonstrates that several established invariant GNNs are capable of completeness

### Strengths
The paper introduces a novel conceptual framework for understanding the efficacy of certain invariant architectures. This is further supported through theoretical analysis and empirical studies. Additionally, it proposes a framework for the development of future architectures extending the impact and significance of the work.

### Weaknesses
The paper lacks sufficient empirical evidence to support its theoretical analysis, significantly reducing the overall significance and impact of the work. The selected real world experiments emphasize datasets which lack conformers or nearly isomorphic point clouds. Furthermore, the main text does not provide adequate evidence to demonstrate the advantages of GeoNGNN over the existing complete invariant architectures.

Additionally, the excessive use of bold text and the absence of a clear outline in the introduction make it challenging to follow and clearly understand the contributions of the paper.

The theoretical claims regarding the expressiveness of GeoNGNN in sparse settings rely heavily on a single example (C.2), and it remains unclear how this generalizes to more complex scenarios. The paper claims that relaxing the fully-connected condition leads to better expressiveness, but this is not rigorously demonstrated with varied sparsity patterns. The analysis lacks a systematic exploration of how different levels of sparsity affect the performance and distinguishing capabilities of GeoNGNN compared to DisGNN. Furthermore, the paper does not provide a clear explanation of how the local subgraph patterns captured by GeoNGNN translate to improved performance in practical applications, especially when compared to simpler, complete invariant architectures.

Finally, the paper does not adequately address the limitations of using datasets like QM9, which primarily consists of non-symmetric structures, to evaluate the distinguishing capabilities of invariant GNNs. The proportion of indistinguishable cases within the symmetric subset of QM9 is not analyzed, which is crucial for validating the theoretical claims. The noise study on QM9 does not clarify how the applied scaling coefficient interacts with the reported error of 0.1Å, making it difficult to assess the practical implications of the results. The study of ModelNet40 also lacks clarity, particularly regarding the sampling method and its impact on preserving symmetries. The paper does not provide a rigorous evaluation of the performance of GeoNGNN on datasets with nearly isomorphic point clouds, which is a key focus of the theoretical analysis. The construction and relevance of the synthetic dataset are also not clearly explained, making it difficult to understand the significance of the results.

### Questions
1) The excessive use of bold text and the absence of a clear outline make the paper’s contributions difficult to discern. Could the authors consider restructuring the introduction for better clarity?

2) I find that the statements in the section **Theoretical Characterization vs Practical Use** rely on the example C.2. How increasing the sparsity beyond this simple example is understudied despite the authors strong claims that relaxing the fully-connected condition leads to better expressiveness of GeoNGNN compared to DisGNN.

3) There is no supporting evidence for GeoNGNN over existing architectures in the primary paper. Additionally, there is no comparative analysis involving node feature information generated by a complete invariant function. Could the authors address this gap?

4) A significant portion of the QM9 dataset consists of non-symmetric structures. What are the proportions of indistinguishable data restricted to the subset of QM9 that includes only symmetric structures?

5) In the QM9 noise study, the significant reduction in non-distinguishable point clouds occurs near what appears to be the level of reported error in the QM9 dataset. Given the reported error of 0.1Å, how is this error rescaled based on the applied scaling coefficient? 

6) Distinguishing structures on QM9, which lacks conformers, does not seem to be as important as datasets which contain conformers or very nearly isomorphic point clouds.The most compelling analysis appears to come from the study of MD17 but with mixed results. GeoNGNN appears to do particularly well on Benzene which is highly symmetric. How does Benzene behave under the noise tolerance study?

7) Typically, ModelNet40 is sampled to avoid handling large point clouds. It is unclear from the text whether the entire mesh or a sampled version is used. If sampled uniformly, there is no guarantee that the symmetries are preserved. Could the authors clarify this in the text?

8) The selection of ModelNet40 does not seem to rigorously test the theoretical claims of the paper, which focus on nearly isomorphic point clouds. Could the authors provide more rigorous testing on datasets that better align with their theoretical focus?

9) It is unclear from the text and appendix what each structure in the synthetic dataset represents, how these structures were constructed, and why they are significant. Could the authors provide more detailed explanations on the construction and relevance of these synthetic structures?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors of the paper prove that certain families of models are not only
invariant with respect to the Euclidian group and permutation group, but also
that classes of models distinguish the orbits of $\mathbb{R}^3$ under the
action of $E(3)$. An extended analysis of the expressivity of DisGNN is
provided and it is shown that this network architecture is nearly $E(3)$
complete. As a last contribution an analysis is provided for various families
of neural networks and conditions are provided under which they are
$E(3)$-complete. The   theoretical   results   are   verified   by experiments
on  the QM9  dataset  and  a synthetic  dataset  with designed edge cases.

### Strengths
The authors have provided both extensive proofs as well as extensive analysis
to their claims. Overall the presentation and intend is clear and definitions
are well-thought out and the authors provide a good heuristic insight with each
introduced theorem and definition which is nice. The extensive analysis of both
DisGNN and GeoNGNN shows that the work is of good quality and looks to be of
good quality to the reviewer. All theorems come with extensive proofs and with
a intuition which is helpful for the non-mathmatical audience. The quality of
the content, such as originality and potential impact, is harder to asses since
the reviewer is not familiar expressivity research.

### Weaknesses
To the reader it seems that some of the definitions are somewhat convolved and
some simplification and clarity in the definitions might improve reading. Some
of the definitions, while they might be customary in the machine learning
literature, are somewhat unfortunately choses from a mathematical perspective.
Completeness of a space in the mathematical sense implies that each Cauchy
sequence has a limit within that space. A second example is the use of the term
isomorphism. While not wrong, a better phrasing is to say that the two point
cloud lie in the same orbit with respect to the action of the Euclidian group
acting on the tensor product of copies of $\mathbb{R}^3$. The current phrasing
might be better if is more in line with terminology used in machine learning.

### Questions
- How does this method for expressivity generalize to different types of architectures? To the reviewer it seems that this method for showing is very specific and would be difficult to generalize to other types of equivariant architectures acting on point clouds.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the expressiveness power of message-passing neural networks incorporating pairwise distance between graph nodes, showing the near E(3)-completeness. Furthermore, the authors study the subgraph graph neural networks, which can achieve E(3)-completeness. Therefore, it is possible to make DimeNet, GemNet, and SphereNet to achieve E(3)-completeness.

### Strengths
The paper symmetrically studies the problem of E(3)-completeness geometric graph neural networks.

### Weaknesses
The work is based on global connectivity assumption, and this assumption significantly limits this work. Specifically, the reliance on a fully connected graph structure for theoretical analysis neglects the sparsity that is inherent in many real-world molecular systems. This assumption makes the theoretical results less applicable to practical scenarios where long-range interactions are often negligible or computationally prohibitive. Also, the experimental results seem to be quite weak. The experiments primarily serve to validate the theoretical claims, but they lack a comprehensive evaluation against state-of-the-art methods on diverse datasets. The reported performance gains are not substantial enough to demonstrate the practical significance of the proposed approach.

### Questions
I have two questions.

1. Do you have any insight on achieving E(3)-completeness for frame-based approaches?

2. Can you comment on achieving E(3)-completeness by using node features beyond pairwise distances, e.g., dihedral angles?

### Soundness
2

### Presentation
3

### Contribution
2
