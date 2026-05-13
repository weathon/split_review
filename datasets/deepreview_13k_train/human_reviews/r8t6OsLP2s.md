# Discovering Message Passing Hierarchies for Mesh-Based Physics Simulation

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Graph neural networks have emerged as a powerful tool for large-scale mesh-based physics simulation.
Existing approaches primarily employ hierarchical, multi-scale message passing to capture long-range dependencies within the graph. 
However, these graph hierarchies are typically fixed and manually designed, which do not adapt to the evolving dynamics present in complex physical systems.
In this paper, we introduce a novel neural network named DHMP, which learns \textbf{D}ynamic \textbf{H}ierarchies for \textbf{M}essage \textbf{P}assing networks through a differentiable node selection method.
The key component is the \textit{anisotropic} message passing mechanism, which operates at both intra-level and inter-level interactions.
Unlike existing methods, it first 
supports directionally non-uniform aggregation of dynamic features between adjacent nodes within each graph hierarchy.
Second, it determines node selection probabilities for the next hierarchy according to different physical contexts, thereby creating more flexible message shortcuts for learning remote node relations.
Our experiments demonstrate the effectiveness of DHMP, achieving $22.7\%$ improvement on average compared to recent fixed-hierarchy message passing networks across five classic physics simulation datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an anisotropic hierarchical message passing technique together with dynamic coarser graph construction for such a hierarchy implementation. The authors claim better simulation quality for a range of test cases.

### Strengths
* new implementation of attention-based and hierarchical message passing in GNNs
* learnable hierarchy
* generalization and ablation studies

### Weaknesses
 * The proposed approach of anisotropic message passing differs only in small implementation details from graph attention and cannot be considered really novel
* In Table 2 the results from cited works are far from the ones reported in them. If one looks at the reported results in the MGN paper [33] Tobias Pfaff, Meire Fortunato, Alvaro Sanchez-Gonzalez, and Peter Battaglia. Learning mesh-based simulation with graph networks. In International Conference on Learning Representations, 2021, these results will be better than here. 

also the paper is not structured well, the authors main contributions are not written separately

### Questions
Why there is a huge difference in Table 2 for MGN model results in your paper and in the original paper? (probably also for another cited works)?

### Soundness
2

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
4

### Summary
The paper proposes two improvements to hierarchical GNN-based neural physics simulator surrogates. The first improvement is an anisotropic message passing mechanism which replaces sum aggregation with a weighted softmax aggregation. The second improvement is a differentiable node selection mechanism to learn long-range dependencies.

### Strengths
- The method is well motivated, presented in a clear way with nice visualizations and a comprehensive analysis of each proposed improvement.
- An extensive evaluation is provided with additional out-of-distribution evaluations, which are interesting to see.

### Weaknesses
 - While Figure 5 provides nice insights into high error regions, Figure 3 suggests that the model also assigns lots of nodes towards relatively uninformative regions. In the bottom right of the bottom left image of Figure, one can see a region that is densely populated with graph nodes, even though the flow is almost laminar in that region. A similar behavior can be observed in the bottom left region of the bottom right image of Figure 3. Figure 5 shows that the model tends to assign more nodes to challenging regions, but Figure 3 also suggests that lots of nodes are assigned to easy/uninformative regions. 

 - The number of hierarchies seems like an important hyperparameter, considering that the paper proposes to learn hierarchies instead of using static ones. A discussion how this hyperparameter is selected (e.g. based on problem size) and implications of unfavorable choices of this hyperparameter (e.g. via an ablation study) would strengthen the paper.

 - MGN reports vastly different performance of their method for the considered benchmarks, often outperforming DHMP. For example, DHMP reports 0.414 RMSE-1 for DHMP on the Airfoil dataset while MGN reports 0.314 for MGN (where the submitted paper reports 0.7738 for MGN).

### Questions
- Is there an intuition for why it seems (as shown in Figure 3) that also uninformative regions get lots of graph nodes assigned? 
- How would the distribution of nodes look over the whole dataset or a single simulation trajectory? E.g. are most nodes assigned to the region where turbulent flow happens instead of laminar flow?
- How is the number of hierarchy selected? Based on a validation set or based on the problem size/difficulty?
- What is the difference between the considered benchmarking settings and the benchmarks conducted in MGN? Why are the MGN paper results sometimes better than DHMP?

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
3

### Summary
Summary: The paper presents a new approach to learning to simulate physical systems using Graph Neural Networks (GNNs). Traditional GNNs rely on fixed, manually designed hierarchies / meshes, which fail to adapt to the evolving dynamics in physical simulations. The authors propose the Dynamic Hierarchical Message Passing (DHMP) model, which introduces dynamic, context-aware and data-driven hierarchies.

Key innovations of DHMP include:
* Anisotropic Message Passing: Facilitates direction-specific message propagation, allowing better representation of physical processes.
* Differentiable Node Selection: This component allows for learning adaptable, multi-scale graph structures that evolve over time.

DHMP outperforms existing methods, achieving an average of 22.7% improvement in five classic physics simulation datasets. It effectively models both local and long-range dependencies in time-varying, mesh-based systems.

### Strengths
The Dynamic Hierarchical Message Passing (DHMP) model adapts its graph structure dynamically, effectively captures long-range dependencies and handles unseen mesh structures, making it a strong solution for complex physics simulations.

### Weaknesses
Some potential limitations:

* Novelty of multi-scale graph neural networks by differentiable node selection: This work "Multiresolution equivariant graph variational autoencoder" by Truong Son Hy and Risi Kondor (https://iopscience.iop.org/article/10.1088/2632-2153/acc0d8) has already proposed a similar idea using Gumbel-Softmax for node sampling to construct an adaptive hierarchy.

* Increased Complexity: Theoretically, the dynamic adaptation of hierarchies and anisotropic message passing introduces additional computational overhead, making it more complex and potentially slower than fixed-hierarchy models. Could you please analyse the time complexity and the space complexity of your model and compare with other baselines? In the Appendix, Table 13 includes comparison with other baselines in terms of training cost, inference time and number of parameters that suggest the computational overhead of this work is not significant.

* Stability of Differentiable Node Selection (DiffSELECT): This learning mechanism might face instability challenges during training, especially in highly dynamic or chaotic systems, which could lead to less reliable performance in certain scenarios. The key component / function is the Gumbel-Softmax in the node sampling / selection (see Equation 6 in Section 3.3). However, the Gumbel-Softmax is sensitive with its temperature hyper-parameter \tau (see PyTorch instruction: https://pytorch.org/docs/stable/generated/torch.nn.functional.gumbel_softmax.html). How can you select the temperature hyper-parameter? Is it the same for every scenario?

It would be great if the authors can try on some turbulence datasets to showcase the stability of method.

* Limitation in Generalization: While DHMP performs well on some specific physics simulation datasets, its generalization to other domains or non-mesh-based applications may require further modification or tuning, limiting its broader applicability. Do you have any plan to apply your model into other domains or non-mesh-based applications? 

I suggest the authors to check PDEBench benchmark: https://arxiv.org/abs/2210.07182

### Questions
I would like the authors to address the potential limitations that I have listed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel multigrid method to coarsen and refine meshes dynamically, depending on the physics at the current time step. They also improve the usual sum aggregation in Message Passing by computing importance weights between each pair of nodes. They demonstrate their method on 4 usual physics datasets and a new one with adaptative re-meshing.

### Strengths
- a novel multigrid method based on Gumbel-Softmax sampling with only very few modifications to the graph net block (an extra probability output). The use of $K$-hop edges is also interesting. 
- a new AMP layer that replaces the usual sum as the aggregation method in the node update with a weighted sum.
- good results improvements on meaningful and standard benchmarks
- a clever usage of the previously defined important to improve on the fine mesh interpolation method

### Weaknesses
 - Important training details such as the number of training steps and the precise learning rate schedule are missing. At the moment, results from MeshGraphNet reproduced in the paper are much higher than in the original paper [1]. In my opinion, this hurts the paper a lot for two reasons: Was MGN (and the other models as well) simply undertrained to make the comparison with the new method better? If every model was actually properly trained for the right amount of steps, what would the comparisons look like now? 
- missing a comparison with [2] that seems to follow a similar strategy with attention based on both the nodes updates, and the node selection during the coarsening stage
- l202-3-4: I think that statement is wrong. GAT networks for example do use edge features during the attention computation. Similarly, even with absolute node positions in the node features, why would an attention based method not be able to compute the differences between those coordinates?

### Questions
- l69-78: Can a parallel be made with [3] where each hop gets processed by a different MLP?
- l74/75: Where is this computational efficiency demonstrated?
- About the AMP layers: I am not sure I understand what improvements you gain in comparison to computing attention. 
For the sake of clarity, I'll assume all functions are learnable parameters and let 
  - $(v_i,v_j,e_{ij}) = \varepsilon_{ij}$
  - $\hat e_{ij} = W_1 \varepsilon_{ij}$
  - $\alpha_{ij} = \sigma (W_2 \varepsilon_{ij})$

With your current formulation, you have: $\sum \alpha_{ij} \hat e_{ij} = \sum \sigma (W_2 \varepsilon_{ij}) W_1 \varepsilon_{ij}$. This is very similar to an unscaled dot-product, but presented as a novelty. Can you specify why you chose to use such a method?
- What's the increase in computational complexity when using AMP instead of a regular GraphNetBlock? 
- l213: How long does it take to construct such edges? What's the impact on the memory? 
- Appendix Section D2 : You compare performances but not training/inference time and vRAM usage for the different $K$-values. It would be very interesting to add those. 

**Changes**

- l108: You should specify that this feature propagation is related to the edge's length, not their number per se.
- l115: "However..." : issue with the sentence
- l152: "where..." : issue with the sentence
- Section 4: You define the number of layers for MGN but not the architecture details for the other models. 
- Table 2: It might be worth it to put in \emph or with another strategy the second best result. 
- l761: the inflow velocity varies as well
- table 7 l791: There's a typo for the noise used in the Airfoil Dataset
- l807: there's a typo for $n$ the node type

**Additional comments**

- Figure 1, I am unsure about the usefulness of the gradient arrows. 
- Section 5 could benefit from presenting [4]

[1] : Learning Mesh-Based Simulation with Graph Networks

[2] : Multi-Grid Graph Neural Networks with Self-Attention for Computational Mechanics

[3] : How Powerful are K-hop Message Passing Graph Neural Networks

[4] : GraphCast: Learning skillful medium-range global weather forecasting

### Soundness
3

### Presentation
3

### Contribution
2
