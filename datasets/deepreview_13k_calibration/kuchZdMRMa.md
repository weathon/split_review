# Topological Data Analysis on Graphs: Euler characteristics, Persistent Homology, or Spectrum?

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 5, 3, 3

## Abstract
Graph neural networks (GNNs) are limited by the Weisfeiler-Leman (WL) hierarchy and cannot compute graph properties such as cycles. Topological descriptors (TDs) such as the Euler characteristics (EC), persistent homology (PH), and Laplacian spectrums have thus been employed to enhance the GNNs. However, despite empirical successes,  the theoretical underpinnings of these TDs remain largely underexplored. We bridge this gap with a rigorous characterization of TDs focusing on three key aspects: expressivity (representational power), stability (robustness to data perturbations), and computation (implementation cost). We evaluate the expressivity of different TDs, and design a novel scheme $\operatorname{RePHINE}^{Spec}$ that is strictly more expressive. We also propose new metrics to assess the stability of the state-of-the-art RePHINE method and the newly proposed $\operatorname{RePHINE}^{Spec}$ method. To address computational costs, we introduce and analyze weaker variants for several descriptors. TDs find significant applications in molecular contexts, so we also explore new filtration functions on the molecular graphs. Finally, we formalize the properties of filtration functions derived from graph products. Overall, this work lays the foundation for the principled design and analysis of new TDs that can be tailored to specific applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents new topological descriptors, especially RePHINE and RePHINESpec, designed to enhance the capabilities of GNNs by enhancing how well they capture complex graph features like cycles. By analyzing expressivity, stability, and computational efficiency, the authors compare various descriptors and explore practical applications, including insights for molecular graphs.

### Strengths
1. The paper covers a range of topological descriptors and presents a detailed comparison of their expressivity, stability, and computational expenses.
2. The paper considers applications in molecular graphs, offering insights that could benefit chemistry and drug discovery.

### Weaknesses
1. The definitions and theoretical explanations are dense and without sufficient explanations. This can be very difficult to follow for people with limited background.
2. The focus is primarily on color-based filtrations. Expanding the discussion to include other kinds of filtrations, would give a more comprehensive perspective.
3. . While the paper presents more expressive descriptors like RePHINESpec, it doesn’t address the computational cost, particularly in large graphs or real-time applications.

### Questions
1. The paper’s applications are primarily molecular. Can this be expanded to other fields that use GNNs, such as social network analysis?
2. How does the use of topological descriptors like RePHINESpec compare with traditional GNN methods, particularly in tasks that do not require high expressivity?
3. The paper proposes several filtrations for molecular graphs. What criteria were used to select these?
4. What is the STABILITY OF REPHINE DIAGRAMS? explanation is missing. Can the authors provide practical examples where stability significantly impacts application outcomes?
5. How sensitive are the proposed descriptors (especially RePHINESpec) to variations in parameters such as filtration type or depth?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a rigorous theoretical analysis of different topological descriptors (TDs) used to enhance graph neural networks (GNNs), focusing on Euler characteristics (EC), persistent homology (PH), and Laplacian spectrums. The authors examine these TDs through three key lenses: expressivity (representational power), stability (robustness to perturbations), and computational efficiency. They introduce a novel descriptor called RePHINE_Spec that combines spectral features with RePHINE and prove it is strictly more expressive than existing methods. They also propose a new metric to assess the stability of RePHINE and analyze weaker variants of several descriptors to address computational costs. The work includes theoretical results about filtrations on graph products and applications to molecular graphs.

### Strengths
The paper's primary strength lies in its comprehensive theoretical treatment of topological descriptors, providing rigorous proofs and clear characterizations of their properties. The authors make several significant theoretical contributions, including proving the equivalence of EC and max EC diagrams, establishing stability bounds for RePHINE, and characterizing filtrations on graph products. The work is well-structured, building from fundamental concepts to more complex settings. The paper also introduces useful variants of existing methods that maintain expressivity while reducing computational costs.

### Weaknesses
The paper is heavily theoretical and could benefit from more empirical validation of the proposed methods, particularly RePHINE_Spec. While the theoretical advantages are well-established, there is limited discussion of practical implementation challenges or computational benchmarks comparing the different methods. The analysis of computational complexity, especially for RePHINE_Spec, remains abstract, lacking concrete details on how the additional spectral information impacts runtime and memory usage in practice. The paper also does not address potential limitations of the proposed methods when applied to very large graphs, where the computation of topological descriptors can become prohibitively expensive.

### Questions
- How does the computational complexity of RePHINE_Spec compare to existing methods in practice, and what are the memory requirements for storing the additional spectral information?
- Can the authors provide empirical evidence that the improved expressivity of RePHINE_Spec translates to better performance on real-world tasks?
- Could the theoretical framework developed in this paper be extended to handle dynamic or temporal graphs where the topology evolves over time?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors analyse three topological descriptors Persistent Homology, Euler Characteristic and Laplacian Spectrum from expressivity, computation and stability standpoint. The authors also introduce weaker but computationally more feasible topological descriptors. They show that $RePHINE^{spec}$ is among the most expressive topological descriptors. Further, they show that $RePHINE$ diagrams are stable and discuss how the analysis would generalize for product of graphs.

### Strengths
I like the problem that the authors are attempting to solve, which is to have a comprehensive guide about which topological descriptor to use on what kind of data/tasks. I feel that solving this problem would really help TDA in ML community.

### Weaknesses
Last line of the first paragraph “the theoretical foundations of TDs remain rather elusive.” This statement, as it reads, is incorrect. All the topological descriptors have a rich theory backing them. What the authors, perhaps, want to say is the expressivity analysis of TDs is rather elusive.

Definition 1: $f_e(c,c’) = f_e(c,c’)$ -> $f_e(c,c’) = f_e(c’,c)$

Most of the comparisons in Theorem 1 seem fairly obvious from the definitions. 

I don’t understand the point of stating Theorem 2 separately. Isn’t it already stated in Theorem 1 that $EC$ and $EC^m$ have the same expressive power?

The flow seems to be lacking from Section 4 onwards. I don’t quite get the motivation behind the product of graphs and death-time filtrations. 

Section 5 seems something new, although I am not sure about its applicability as such. 

I didn’t quite understand the overall point being made by Section 7. 

In Definition 8, what does $h_1 ~ h_2$ mean?

Line 491: Bond Coloring Representation -> Bond Counting Representation?

Overall, I think that the paper needs significant revisions before it is ready for acceptance.

### Questions
The stability section just talks about the stability of $RePHINE$ diagrams, which is a straightforward extension of the stability of persistence diagrams. What about the stability of $RePHINE^{spec}$? Can that be characterized as well? What about the stability of EC?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper seeks to systematically study and provide advice (in the form of new contributions) on three topological descriptors for graph neural networks in terms of expressivity, stability, and computational cost.

### Strengths
The paper seeks to rigorously study and provide a convincing basis for the role of topology in graph neural networks, which I agree with the authors is not yet convincing.  I think the paper does a good job at outlining the challenges of topological methods in computational settings, especially in deep learning and graph neural networks.

### Weaknesses
Some of the main conclusions and findings of the paper are not that surprising, such as the Euler characteristic being strictly less expressive than persistent homology.  This is in quite fact obvious, given that the (persistent) Euler characteristic is an alternating sum of Betti numbers, while persistent homology by construction contains more information.  Overall, while I agree with the need for an unbiased and rigorous study of the effectiveness of topological methods in graph neural networks and I believe that this part of the study was carried out well, I am still not convinced by the place that topology has in graph neural networks and I am not convinced by the new contributions proposed in the paper, which in some cases, I see as straightforward extensions of existing methods.  Perhaps it is an artifact of needing to "sell" the new contribution.  I almost feel like the paper would have been stronger as a rigorous computational survey paper, systematically studying the strengths and limitations of topological methods, with a presentation of straightforward/obvious ways to fix the limitations.

The paper is also not very well written.  I am missing the traditional summarized bullet point list clearly listing all contributions of the work.



### Questions
- Do you mean Euler characteristic or persistent Euler characteristic?  Definition 5 is the static version, but a persistent version is cited with Turner et al. being the reference.
- Overall, I find the presentation of the topological descriptors studied confusing; it is not very clear to me whether the persistent version is being studied for the three types or the static ones, although the title of the paper and the introduction seems to emphasize persistent versions of all descriptors.  Why are persistent versions studied in particular and not static ones?
- Should the authors choose to study static topological descriptors as well, I would be interested in what can be said about the Hodge Laplacian?  The kernel is known to encode geometric information about the homology of simplicial complexes (and therefore graphs as a lower dimensional special case); other eigenspaces do the same for graphs.  However, for the persistent version (which appears to be the one studied in this paper – again, not always clear...), only the kernel has been studied.
- What can be said in addition to expressivity?  What about interpretability of topological methods?  For this point, I admit that my rating of "soundness" might be somewhat unfair, as I think this paper would be stronger as a review/experimental study paper (as mentioned in the "weaknesses" section) and I would be open to raising my score for this criterion.  Although it may be (substantially) more work, I still feel like it is a plausible question since in some instances, interpretability and expressivity can be seen as related, especially in considering topological notions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper establishes several results on topological descriptors on graph representation learning.

### Strengths
The paper studies three topological descriptors—Euler Characteristics, Persistent Homology, and Laplacian Spectra—from various perspectives and compares their features and effectiveness.

### Weaknesses
I found the paper difficult to follow due to a lack of cohesion among the presented results. The paper includes multiple, somewhat incremental findings that are loosely grouped under a single theme but lack a clear, unifying narrative. Each topic examined by the authors requires a much deeper, individual analysis; however, the paper only provides limited advancements in each area. Moreover, these results appear largely unrelated to one another, creating an impression of a collection of disjointed findings rather than a focused contribution to the field of topological descriptors in graph representation learning. I will address some points in more detail below.

1.  **Expressivity of PH or TD**: The expressivity of persistent homology (PH) or topological descriptors (TD) is difficult to define without specifying the space of filtration functions. Without this specification, one could theoretically achieve any level of distinguishing power between graphs by selecting suitable filtration functions (or colorings). Therefore, the current results lack meaning from a machine learning perspective, as they do not offer a robust comparison to graph neural network (GNN) expressivity. The paper needs to explicitly define the space of filtration functions considered and justify why these choices are relevant for graph representation learning. Without a clear definition of the filtration function space, the expressivity results are not comparable to existing GNN expressivity results.

2.  **Stability**: The stability result presented here is incremental, as it mainly builds upon foundational work by Cohen-Steiner (2006). There is limited novel contribution to the understanding of stability in this context. The paper should more clearly articulate the specific challenges in extending existing stability results to the proposed RePHINE framework. It is not sufficient to simply state that the result is an extension; the paper should highlight the technical hurdles overcome and the novel insights gained. The stability result should also be more thoroughly analyzed, for example, by considering the implications of different choices of metrics for measuring the distance between persistence diagrams.

3.  **Product of Graphs**: The purpose of this section is unclear, as it does not seem connected to the main theme of the paper. The motivation for ML and relevance to the other sections should be clarified. The paper needs to provide a clear explanation of why graph products are relevant to the study of topological descriptors in graph representation learning. The connection to machine learning should be made explicit, perhaps by discussing how graph products arise in real-world datasets or how they can be used to improve the performance of GNNs. The results in this section should be more clearly linked to the other sections of the paper.

4.  **Death-time Filtration**: The relevance of this section to the other sections is also unclear. Its connection to the overall analysis needs to be better justified. The authors derive several new notions and make comparisons between them. However, the motivation is again unclear. The paper should clearly explain the motivation behind exploring death-time filtrations and how they relate to the standard birth-time filtrations used in persistent homology. The authors should also provide a more detailed analysis of the properties of death-time filtrations and their potential advantages or disadvantages compared to birth-time filtrations. The connection to the overall analysis needs to be better justified, perhaps by showing how death-time filtrations can be used to address specific limitations of birth-time filtrations.

5.  **Molecular Graphs**: Since this is an ML venue, I would expect experimental validation. Some experiments demonstrating the utility of the discussed approaches on molecular graphs would be valuable to illustrate practical implications.

**In summary**, the paper discusses several interesting topics; however, it lacks focus and depth. I recommend narrowing the scope to one or two of these topics, accompanied by a much deeper analysis, with clearly defined goals and statements. This approach would lead to a more substantial and coherent contribution.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
