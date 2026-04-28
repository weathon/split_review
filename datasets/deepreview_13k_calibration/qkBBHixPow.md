# PIORF: Physics-Informed Ollivier-Ricci Flow for Long–Range Interactions in Mesh Graph Neural Networks

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Recently, data-driven simulators based on graph neural networks have gained attention in modeling physical systems on unstructured meshes. However, they struggle with long-range dependencies in fluid flows, particularly in refined mesh regions. This challenge, known as the 'over-squashing' problem, hinders information propagation. While existing graph rewiring methods address this issue to some extent, they only consider graph topology, overlooking the underlying physical phenomena. We propose Physics-Informed Ollivier--Ricci Flow (PIORF), a novel rewiring method that combines physical correlations with graph topology. PIORF uses Ollivier--Ricci curvature (ORC) to identify bottleneck regions and connects these areas with nodes in high-velocity gradient nodes, enabling long-range interactions and mitigating over-squashing. Our approach is computationally efficient in rewiring edges and can scale to larger simulations. Experimental results on 3 fluid dynamics benchmark datasets show that PIORF consistently outperforms baseline models and existing rewiring methods, achieving up to 26.2\% improvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors propose Physics-Informed Ollivier–Ricci Flow (PIORF) which builds on the Ollivier–Ricci Flow. This innovative rewiring method integrates physical correlations with graph topology to address the over-squashing problem, which traditional approaches often overlook by focusing solely on graph topology without considering underlying physical phenomena. The proposed method is designed with the following 3 goals: 1) physical context, 2) efficiency, 3) accuracy. Furthermore, authors extend the ORC to node-level curvature, which is the core of the RIOFR. Experimental results on 3 fluid dynamics benchmark datasets show that PIORF consistently outperforms baseline models and existing rewiring methods.

### Strengths
1. The authors introduce a novel Ollivier–Ricci Flow, termed PIORF, to address the over-squashing problem that neglects physical phenomena.

2. The authors extend the ORC to node-level curvature.

3. The effectiveness of the method is validated through experimental verification.

### Weaknesses
1. There is a lack of sufficient theoretical analysis compared with former works.

2. The paper does not provide a clear explanation for how the added edges address the underlying physical phenomena. The connection between adding edges based on velocity differences and the mitigation of over-squashing is not well-established.

3. The legends in the figures are not clear. Furthermore, the meaning of the colors used in the figures is not explained, making it difficult to interpret the results, especially in figures 1, 4, 7, 8, 9, 10 and 11.

4. The authors claim that the degree of a node is negatively correlated with curvature, which contradicts the existing theory that a fully connected graph does not have over-squashing (maximum curvature). The paper does not adequately clarify whether this discrepancy arises from specific conditions discussed in the context of fluid dynamics. The correlation between node degree and curvature is not sufficiently justified.

5. The computational efficiency is demonstrated only through experimental illustrations of efficiency gains, with no accompanying theoretical analysis. The paper lacks a formal analysis of the time complexity of the proposed method compared to existing approaches.

### Questions
1(W1). Inadequate theory compared to previous work(BORF)[1]. And authors complain that 'BORF works in batches and calculates the curvature with a minimum and maximum in each batch. Then, connections are added to the set with the minimum edge value to uniformly weaken the graph bottleneck. To save computation time, BORF does not recalculate the graph curvature within each batch, but rather reuses the already computed optimal transfer plan between sets to determine which edges should be added.', but there is no indication in this paper that there is an increase in efficiency compared to BORF

2(W1). The addition of edges also changes the topology, which may lead to negative consequences that are not addressed in the paper.

3(W1). Computational efficiency is demonstrated only through experimental illustrations of efficiency gains, with no accompanying theoretical analysis.

4(W1). Contrary to the existing theory. Topping's work [2] suggests that a fully connected graph does not have over-squashing (maximum curvature). However, as shown in Figure 3(a), the authors claim that the degree of a node is negatively correlated with curvature. These two theories are clearly contradictory. The authors should clarify whether this discrepancy arises from specific conditions discussed in the context of fluid dynamics. The degree may not be correlated to the level of curvature.

5(W2). There is no clear rationale for why adding edges between $s$ and $r$ would address the underlying physical phenomena. The authors only provide some intuitive insights from physics and experimental simulations, but these edges could potentially have a negative impact.

6(W3). Legends should be provided, and the meanings of the colors should be clarified to help readers better understand the impact of color changes in the figures (Figure 1, 4, 7, 8, 9,10 11).

[1] Khang Nguyen, Nong Minh Hieu, Vinh Duc Nguyen, Nhat Ho, Stanley Osher, and Tan Minh Nguyen. Revisiting over-smoothing and over-squashing using ollivier-ricci curvature. In In- ternational Conference on Machine Learning, pp. 25956–25979. PMLR, 2023

[2] Jake Topping, Francesco Di Giovanni, Benjamin Paul Chamberlain, Xiaowen Dong, an Michael M Bronstein. Understanding over-squashing and bottlenecks on graphs via curvature. arXiv preprint arXiv:2111.14522, 2021

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a novel graph rewiring method when using GNNs to solve PDEs. The basic idea is to combine regions based on both graph topology (Ollivier-Ricci curvature (ORC)) and physical features defined on each graph node (e.g. velocity). The proposed method first identifies bottleneck regions, i.e., with low ORC at the nodes, and then connects them with nodes having a maximum difference in physical properties. It seems that the first step identifies well-connected graph clusters typically far away on the graph and then connects them through basically one or two other nodes, namely the one(s) having the lowest and/or highest chosen physical feature. This way, information can propagate quickly between distant regions. The presented experiments seem promising.

### Strengths
- Combining topological and physical features. ORC seems meaningful for identifying clusters. Combining it with the physical features also makes sense, as these are quantities of interest.
- Performance on the presented benchmarks is good.
- Overall, the manuscript is well written and has many ablations/baselines.

### Weaknesses
 - **W1: Why ORC?** I get the point of wanting to connect clusters (according to the used library for computing the ORC, low ORC reveals "bridges within clusters": https://pypi.org/project/GraphRicciCurvature/), but I'm not convinced that this is the best way. Note that I don't say that it is not the right way, I just say that there is no discussion of alternatives. 
- **W2: Why not node degree?** If the ORC and the degree of a node are strongly correlated, there should not be much difference between using the degree of a node versus a low ORC. I strongly recommend ablating this design choice (**Ablation 1**). If both perform comparably, there is no reason to use ORC, as the degree of a node is a much simpler concept. Thus, Occam's razor would favor it, and talking about adaptation by other researchers, one would not have to use a separate library to compute curvatures.
- **W3: 6.4 Ablations.** I was not expecting this amount of ablations regarding the second half of your algorithm (lines 5-6 of Algorithm 1, physical features), but I was definitely expecting more ablations regarding the first part (lines 3-4 of Algorithm 1, ORC). In particular, how about randomly picking $S$ nodes instead of the current lines 5-6 of the algorithm relying on the ORC (**Ablation 2**)? This would show the importance of using physical features for rewiring, which seems to be a major part of the approach.
- **W4: Simplest baseline.** I appreciate your effort in the model comparison part! However, I'm missing the simplest possible rewiring technique: randomly pick the same number of bidirectional edges as you use ($S$ if I'm not missing something), and see how this model performs (**Ablation 3**). From what I know, the chosen baselines (DIGL, SDRF, etc.) are designed for very different downstream tasks, and I'm not surprised that they underperform.

I'll be more than happy to increase my score upon adding the suggested Ablations 1-3.

**Minor/Typos:**
- L. 376: "changes" -> "change"?
- L. 425: "boxe" -> "boxes"?
- L. 462:  "PIORF maintains the lowest computation time in all datasets and edge counts." Is this true? The orange FoSR line is nearly identical; by the way, it is also pretty hard to see the orange line, probably even impossible if I print the manuscript on paper -> please think of a better visualization (e.g. log y-axis?). Please fix the whole paragraph regarding which approach is "the fastest", as there seem to be two of them.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an enhancement in mesh-based graph network simulators by addressing the over-squashing problem using a novel physics-informed rewiring approach. Notably, the method is able to scale to large scale fluid simulations due to the controlled complexity in performing rewiring. Experimentally, the proposed approach achieves notable improvement over existing mesh-based graph networks across three benchmarks, showcasing its efficacy.

### Strengths
1. The paper is well written and the proposed approach is easy to follow.

2. The motivation is very clear with an elegant solution based on ORC.

3. The discussions on the improved efficiency of the proposed approach over existing rewiring methods should be appreciated.

4. Experiments are thorough and the results are well presented.

### Weaknesses
These are some minor weaknesses which do not substantially hurt the paper but would be good to add more discussions.

1. The proposed approach is mainly developed upon mesh-based representations. Adding more discussions to whether this could be generalized to ubiquitous graph network simulators (e.g., with particle representations or rigid bodies) would enhance the contribution.

2. Some metrics are not clear to readers, e.g., Pressure, Density. It would be helpful to provide some explanations on the actual physical interpretation of these quantities, in the context of the considered simulation environments.

3. All datasets seem to be artificial and adding more experiments (if applicable) on some real-world datasets would significantly enhance the paper.

### Questions
Q1. Is the approach also applicable to particle-based simulations? e.g., [1].

Q2. Could the approach be combined with other physical inductive biases like equivariance [2], [3], [4]? It would be interesting to have some of these discussions in the paper or as related literature.

Q3. Could the approach be applied together with constraint-aware graph simulators like [5]?

Q4. Are there any real-world dataset on which the model can be evaluated? Practitioners would be more exciting to see how the method performs in actual real-world scenarios.

[1] Li et al. Learning particle dynamics for manipulating rigid bodies, deformable objects, and fluids.

[2] Satorras et al. E(n)-equivariant Graph Neural Networks.

[3] Huang et al. Equivariant Graph Mechanics Networks with Constraints.

[4] Han et al. Learning Physical Dynamics with Subequivariant Graph Neural Networks.

[5] Rubanova et al. Constraint-based graph network simulator.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a method called PIORF that enhances long-range interactions in mesh graph neural networks for fluid dynamics simulations. It uses Ollivier–Ricci curvature (ORC) to identify bottleneck regions in the graph and connects these areas with nodes having high velocity gradients. The authors evaluate PIORF on three fluid dynamics datasets and choose multiple backbone GNNs to demonstrate its effectiveness. The results show that PIORF outperforms existing graph rewiring methods in fluid simulation.

### Strengths
1. The paper studies the over-squashing problem in fluid simulation.
2. The proposed methods consider both the graph topology and physical quantity.
3. The authors conduct experiments on various backbones.

### Weaknesses
I appreciate the authors' effort in exploring the over-squashing problem in fluid dynamic learning. However, multiple issues are still underexplored from my point of view. The details are as follows:

1. Most graph rewriting methods study the classification problem in graphs like citation networks and social networks. The significance of over-squashing in fluid simulation is underexplored.  Whether and how does it affect learning performance? One observation that raises such a question is that in Table 1, existing graph rewriting methods enhance errors in most cases, indicating that over-squashing might not be the key issue in learning fluid dynamics.

2. For the method, connecting the nodes with the highest velocity gradient is straightforward. How does the author avoid connecting nodes with low influence but high-velocity gradients?

3. What is the ratio of negative ORC? Do you consider it to determine the pooling ratio?

4. The authors do not provide time complexity.

5. From Table 4, Random and Only Removal also significantly reduces model errors. Do they alleviate the over-squashing problem?

### Questions
Overall, my concerns are as follows:

1. Whether over-squashing exist in or significantly affect fluid dynamic learning?
2. How does PIORF alleviate over-squashing? more insights into model designs.
3. Does the performance improvement result from that PIORF alleviate over-squashing?

### Soundness
2

### Presentation
3

### Contribution
2
