# Learnable Stability-Aware Unstructured Grid Coarsening Using Graph Neural Networks for Accelerated Physics Simulations

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Efficient simulations of complex physical systems described by partial differential equations (PDE) require computational methods that can reduce the resource demands without sacrificing the accuracy. Traditionally, this is achieved by ``upscaling'' the simulation grids or by aggregating cells based on a priori information. Here, we introduce a novel framework based on graph neural networks (GNN) for learnable self-supervised differentiable coarsening of unstructured computational grids. We leverage graph-based representation of the physical system and offer a graph coarsening method which preserves the underlying physical properties together with the stability of the chosen numerical scheme. This is achieved by minimizing the error between the output of the simulations using coarsened and original graph. We demonstrate the approach on several example differential equations, modeling sub-surface flow and wave propagation. We demonstrate that the model exhibits ability to maintain high fidelity in simulation outputs even after 95\% reduction on the nodes, significantly reducing computational overhead. We also show that the model exhibits generalizability to unseen scenarios, thereby outperforming the baselines. Thus, the developed approach demonstrates the ability to accelerate simulation without comprising accuracy and hence has potential for accelerating physical simulations in various domains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work proposes a method for mesh coarsening, which may facilitate faster physical simulations. The coarsening is done using self-supervised GNN to apply to unseen settings. They also investigated the effect of stability loss, which enhances the stability of training and prediction, and a differentiable implicit solver for stable prediction. The numerical experiments suggest that the proposed method has a competitive performance with a baseline machine learning method.

### Strengths
* The work focuses on the mesh coarsening problem, which is relatively new to the community.
* The explanation of the method is clear and easy to follow.

### Weaknesses
 * The novelty of the method is limited. They claimed the differentiable implicit method is their novelty; however, PyTorch supports differentiable linear solvers ( https://pytorch.org/docs/stable/generated/torch.linalg.solve.html ). In addition, the community knows that there are implicit GNNs (e.g., [Gu et al. NeurIPS 2020 https://arxiv.org/abs/2009.06211 ]) that solve implicit problems.
* The experimental evaluation is weak. The authors state that mesh coarsening is a recent approach, and there are a limited number of existing methods, but there are actually a lot of works investigating mesh coarsening (e.g., [Pffaf et al. ICLR 2021 https://arxiv.org/abs/2010.03409 ] and [Alet et al. ICML 2019 https://arxiv.org/abs/1904.09019 ]). The authors must mention these existing works and evaluate them in the numerical experiments to show the superiority of the proposed method.
* The effectiveness of the proposed method is limited. The experimental results suggest that the method has almost the same accuracy and longer computation time for training. If the reviewer did not miss, there is no evaluation of the prediction time, which is one of the most essential metrics for the mesh coarsening task. In addition, there should be a comparison regarding the speed-accuracy tradeoff with classical numerical analysis methods with varying resolutions because a simple mesh coarsening may work for the problems considered in the paper.

### Questions
* What would be the potential pros and cons compared to the classical methods, e.g., adaptive mesh refinement? The mesh coarsening task would be interesting, but the reviewer is not sure if this direction is promising, given that we have plenty of optimized methods in the classical numerical analysis field.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Aiming at accelerating the numerical PDE solving-based simulation, the authors propose a method that utilizes graph neural networks to generate a coarsened mesh such that the solver can generate solutions quickly. The loss terms are designed such that the solution is stable and accurate. The proposed framework is applied to the cases of (simplified) wave propagation and (simplified) subsurface flow.

### Strengths
1. Automatic optimization of the grid, saving human efforts.
2. Designed loss term to soft-enforce stability of the simulation on the coarsened grid.
3. Results are comparable with recent methods based on global optimization.

### Weaknesses
A few issues can be observed, listed below in the order of importance:

1. Whilst the solution from the coarsened grid are accurate at the node points, the super-coarsened grid inevitably lead to another source error since quite a great proportion of applications would require the field solution rather than discrete points, which would necessitate interpolations from the solution points. Such error is largely ignored when the authors are trying to coarsen the grid as much as possible. In clear words, how much error would one observe when one is going to plot out the whole simulated pressure field by interpolating from the simulation results? It is easy to imagine that the grid in Fig. 8 would give a decent interpolated field, while the coarsened grid in Fig. 9 would probably not. The authors did not consider those errors in the proposed grid coarsening algorithm, which poses a significant limitation to its application.

2. The method is applied to very simple cases. As discussed by the authors themselves, applications in more complex scenarios would be great to have in the future.

### Questions
1. The largest question I have is that, since a graph neural network is already employed, why not further the effort and directly generate the solution with the graph neural network (by increasing the current one layer network to a slightly larger one)?
2. Table 1 & 2, it is reported that the method is actually slower and more memory intensive than the baseline, while results are comparable or only slightly better???

### Soundness
3

### Presentation
2

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
This paper proposes a Graph Neural Network (GNN) based approach for automated mesh coarsening for PDE solutions. The authors extend previous work on self-supervised coarsening of unstructured grids by introducing a learnable method that aims to generalize across different scenarios (eg, varying mesh resolutions and source/sink terms) without requiring new runtime optimization.

While the core idea of learnable mesh coarsening is interesting, and the authors claim to have benefits such as no need to redo optimization on the fly, there are several fundamental concerns:

1. Insufficient Performance Advantages
   - The method demonstrates worse accuracy compared to baseline in 1 out of 2 test cases; The authors should at least justify why this accuracy trade-off is acceptable in practical applications

2. Limited Generalization Capabilities
   - Experimental results show significant performance deterioration when:
     a. Applied to meshes of different resolutions
     b. Tested with additional source terms
   - This contradicts the paper's central claim of improved generalization ability

3. Limited Computational Efficiency Improvement
   - The time comparison between the proposed method and baseline approaches shows very limited advantages (eg, from 22s to 5s, both are at similar magnitudes)
   - Let along the training cost ahead of time, which makes the gain even more questionable.

Overall:
I recommend rejection of this paper. There are some additional minor suggestions on the clarity of writing, if the authors would like to improve their manuscript. But without experiments proving significant benefits, I would not consider chaning my decision.

### Strengths
- An interesting trial to extend an on-the-fly optimization problem to be learned by GNN; so that it can save time in the future deployments.

### Weaknesses
1. Insufficient Performance Advantages
   - The method demonstrates worse accuracy compared to baseline in 1 out of 2 test cases; The authors should at least justify why this accuracy trade-off is acceptable in practical applications. The accuracy degradation is particularly concerning given that the baseline method is already a well-established approach for mesh optimization. The paper needs to provide a more in-depth analysis of the scenarios where the proposed method is preferable, even with the observed accuracy loss. A clear justification for accepting this trade-off, perhaps in terms of computational cost or other practical benefits, is missing.

2. Limited Generalization Capabilities
   - Experimental results show significant performance deterioration when:
     a. Applied to meshes of different resolutions
     b. Tested with additional source terms
   - This contradicts the paper's central claim of improved generalization ability. Specifically, the performance drop when applied to different mesh resolutions indicates that the learned coarsening strategy is highly sensitive to the input mesh structure. This limits the practical applicability of the method, as it would require retraining for each new mesh resolution. Similarly, the performance degradation with additional source terms suggests that the model is not robust to changes in the underlying PDE problem, further undermining the claim of improved generalization.

3. Limited Computational Efficiency Improvement
   - The time comparison between the proposed method and baseline approaches shows very limited advantages (eg, from 22s to 5s, both are at similar magnitudes)
   - Let along the training cost ahead of time, which makes the gain even more questionable. The reported speedup, while present, is not substantial enough to justify the added complexity of training a GNN. The training overhead, which is not negligible, further diminishes the overall efficiency gains. The authors need to provide a more detailed analysis of the computational cost, including the training time and the inference time, to demonstrate the practical benefits of their method.

### Questions
Other minor questions on clarity and writing (authors should add these details to their manuscript in addition to answering here):
- How does the GNN decides which nodes to keep in corsened mesh? Top-K?
- Once coarsened nodes are obtained, how to get the new mesh? The current method only mentions triangular mesh, what is your proposal to adapt in these cases where the mesh is 3D or no longer simplex?
- How many timesteps do you keep the gradients, 1, eg only calculating the gradients for stepping from n to n+1, or multi-step; if multi-step, how many?
- You mentioned implicit method can improve results. But where are the results to support this claim?
- The simulation is required to be differentiable. This easily achieved in explicit scheme, but challenging to general PDEs solution schemes, eg, WENO for nonlinear advection terms. What is your proposal to these extensions?
- In sec 3.3., you mentioned Sij is learnable by NN. What is the NN that outputs Sij? as Sij depends on the topology, ie the graph G, it should be output via some GNN strucutre? Otherwise it's not possible to extend to other mesh structure.
- Page 5, you mentioned stability loss (1st appearence of that term in main text) without simply introducing its meaning, which hinder the reading flow of readers.
- Can you mentioned the method to deal with cases when sensor locations do not align with the grid points? Do you use Barycentric interpolants?
- Eq. 9 does not seem to be connected with Eq. 8 as the former actually regularize the number of coarsened nodes, n, it seems to have nothing to do with eg CFL or criteria for stability. Consider improving the writing here.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose a novel framework that leverages graph neural networks (GNNs) to facilitate a self-supervised learnable coarsening process. This GNN-based approach creates a generalizable coarsening strategy. This adaptability allows it to function across different simulation setups without requiring grid-specific re-optimization.

### Strengths
The introduction of a self-supervised GNN-based coarsening framework represents a significant advancement over traditional methods that require specific optimizations for each grid.

### Weaknesses
There are missing implementation details. See questions.

It would be beneficial to see a comparison of the proposed clustering method with baseline clustering techniques. The current evaluation lacks a direct comparison of the cluster quality, which is a crucial aspect of the method's performance. Without this comparison, it's difficult to assess the effectiveness of the adaptive clustering approach.

The evaluation would be strengthened by including comparisons with additional reduced-order modeling baselines. The current evaluation does not sufficiently benchmark the method against state-of-the-art reduced-order modeling techniques, making it hard to gauge its relative performance and advantages.

### Questions
1. Are alternative remeshing strategies, such as Delaunay triangulation, considered, and if so, how do their performances compare?
2. Is your proposed method adaptable to non-fixed mesh topology systems, such as Lagrangian systems like the Deforming Plate model discussed in MeshGraphNets[1]? 
3. Can you illustrate the meaning of colorbar in Figure 8 of Appendix A?
4. What is the input quantities of the GCN for each task?
5. It would be better if the authors could compare the clusters generated by the proposed method with the clusters of baselines.
6. It would strengthen the evaluation of your method to include comparisons with additional reduced-order modeling baselines, such as UPT[2] and Transolver[3].

[1] Learning Mesh-Based Simulation with Graph Networks.

[2] Universal Physics Transformers: A Framework For Efficiently Scaling Neural Operators.

[3] Transolver: A Fast Transformer Solver for PDEs on General Geometries.

### Soundness
3

### Presentation
3

### Contribution
3
