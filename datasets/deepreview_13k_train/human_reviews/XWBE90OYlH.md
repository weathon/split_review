# Graph Neural Networks for Edge Signals: Orientation Equivariance and Invariance

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Many applications in traffic, civil engineering, or electrical engineering revolve around edge-level signals. Such signals can be categorized as inherently directed, for example, the water flow in a pipe network, and undirected, like the diameter of a pipe. Topological methods model edge signals with inherent direction by representing them relative to a so-called \emph{orientation} assigned to each edge. 
These approaches can neither model undirected edge signals nor distinguish if an edge itself is directed or undirected. We address these shortcomings by (i) revising the notion of \emph{orientation equivariance} to enable edge direction-aware topological models, (ii) proposing \textit{orientation invariance} as an additional requirement to describe signals without inherent direction, and (iii) developing \model, an architecture composed of novel direction-aware edge-level graph shift operators, that provably fulfills the aforementioned desiderata. It is the first general-purpose topological GNN for edge-level signals that can model directed and undirected signals while distinguishing between directed and undirected edges. A comprehensive evaluation shows that \model outperforms prior work in edge-level tasks, for example, improving in RMSE on flow simulation tasks by up to \ourimprovement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper distinguishes between orientation invariant (i.e. those with fixed sign regardless of orientation) and equivariant (those that change sign depending on orientation) features. It highlights the importance of being able to model both types of features in a graph learning scenario and proposes a new model that is able to do so.

### Strengths
The paper is well-written, bringing across the main point nicely. The theoretical claims are sound and the proofs seem correct.

### Weaknesses
The main idea of the paper brings little novelty. Both invariant and equivariant edge features have been explored previously - just not together. The performance gain could well be attributed to a more complex model.
The theoretical contributions are very simple. Essentially Theorem 4.1 follows by design.

### Questions
- How many trainable parameters do the models use respectively?
- How sensitive to hyperparameters is your proposed model?

### Soundness
4

### Presentation
4

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
This paper focuses on dealing with edge values on graphs that can only be defined up to an orientation assigned to that edge. Such values flip their sign if the orientation direction of that edge is changed. Conversely, there are edge values that are scalars and do not require an orientation to be defined. Functions that aggregate and update edge values can be either equivariant (the predicted value changes with orientation) or invariant (the predicted value remains the same) to changing the orientation of edges. The authors propose GNN model that at each layer takes in as input orientation-aware equivariant and invariant edge values and outputs updated orientation-aware equivariant and invariant edge values. The authors use a clever design to ensure that the model keeps the equivariant and invariant edge values consistent across the layers. They also introduce a principled way to aggregate across equivariant and invariant edge values. Finally, they extend they approach to graphs with directed edges by using a magnetic Laplacian. Directed edges always have a well defined orientation given by the edge direction. The magnetic Laplacian incorporates a complex phase shift to values of directed edges during the aggregation step. The authors use synthetic data and some real world data sets that their proposed method outperform existing methods on graphs with orientation-aware edge values.

### Strengths
This reviewer generally liked the paper. The reviewer was not aware of the problem of graphs whose edge can take on both orientation-aware equivariant and invariant values. However, the author's real world data sets seem convincing and not too contrived. It seems like there is a problem here to solve. The way the authors construct their framework, for example how the equivariant and invariant graph Laplacians are constructed using boundary operators and stitched together, is clever and principled. There is no argument that the proposed GNN respects the symmetries of the problem when it comes to equivariance and invariance of edge values with respect to edge orientations. The empirical evidence is also strong. It seems that respecting the symmetries does help with performance. Finally, the authors do a reasonable job with their ablation studies to highlight where the improvements form their method is coming from.

### Weaknesses
A minor weakness is potentially the nuanced nature of this problem. To this reviewer the problem of applying GNNs to graphs with mixed undirected and directed edges and edge values on undirected edges that can be both equivariant and invariant to their orientation could be viewed as too much of a niche problem and perhaps not enough of a significant advance for the field of learning of graphs more broadly. Therefore, this paper may lack broad interest at ICLR.

The main weakness of the proposed method is the use of magnetic Laplacian and phase shifts in the complex plane to account for directed edges. Although magnetic Laplacian is a reasonable way to aggregate information across neighboring nodes in a directed graph, it is not the most general way to do so and has limited expressivity. The reason for this is simple. The phase used to weigh features across directed edges can result in information loss when the complex features are aggregated at each node. For example, a phase angle of q aggregated with a phase angle of -q results in real value that is indistinguishable from a value aggregated from undirected edges. Similarly if q = 1/2 then 4 hops along directed edges will result in a purely real value indistinguishable from messages aggregated from undirected edges. Similarly, after multiple hops where the edge values may become complex, it will not be possible to determine whether a complex value arriving at a node came from a real value propagated along a directed edge or a complex edge value sent along an undirected edge. Therefore, the use of a phase shift and complex numbers is not the most general way to aggregated information in directed graphs and results in loss of information and thereby lower expressivity of GNNs.

Arguably, the most general way to do aggregation of features of neighboring nodes in a directed graph is proposed by Rossi et al. There, the features from neighbors connected by outgoing edges is aggregated separately from that of neighbors connected by incoming edges. This can be easily extended to include undirected edges as a separate category. During the update step the aggregated features of outgoing and incoming neighbors are concatenated alongside the self feature of the node. The authors should consider such a scheme and construct their boundary operator this way (a vector now that separately aggregates features from outgoing and incoming directed edges and undirected edges). The Laplacian operator can be constructed using this boundary operator and the same constraints applied to ensure that equivariance and invariance requirements are kept. Given how principled the author's approach has been to respecting the symmetries with respect to edge orientation, it would be interesting to see if the most principled way to incorporate edge directions will further improve the performance of their model.

### Questions
Please see comment above regarding weaknesses. Can the authors comment on whether it is possible to do away with magnetic Laplacian and construct their method using the most general framework for aggregating information in directed graphs from Rossi et al.? If so, can the authors implement this approach and do an empirical comparison to their current approach 
using the magnetic Laplacian?

To address this reviewer's concern about the niche nature of the problem tackled in the paper, could the authors elaborate on the broader applications of their work? What sort of real world problems can be solved using the proposed approach? Are there more general implications of the proposed approach for solving related problems?

### Soundness
2

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
3

### Summary
The author proposes a novel model that decouples direction and orientation. The framework explicitly models equivariant/invariant orientation constraints for undirected and directed edges in graphs via different types of Laplacians. The model is comprehensively evaluated across a wide range of tasks and datasets, and outperforms prior works by a large margin.

### Strengths
The paper defines a clear problem to solve, and the solution is well-motivated. Specifically, decoupling direction from orientation and differentiating directed equivariant edge signals in different scenarios make the work unique compared to prior works. I believe the setup for controlling edges’ signals can be set as a new standard for the field. The theoretical analysis is also comprehensive and sheds light on the design choice. The experiments are also well-designed. They cover different tasks related to directed graphs with no parallel edges. The proposed novel set of benchmarks, which includes 3 synthetic datasets and 5 real-world datasets with 3 different tasks, is a significant contribution to the field.

### Weaknesses
One weakness of the paper is on the presentation side. The paper, even displays a lot of figures, to demonstrate different concepts, is still vague in many arguments. Please refer to the Questions section for detailed concerns. Another problem is model comparison. I think the paper will be more comprehensive if the model is compared with the more recent relevant work such as [1].  The next problem is the scalability problem. It seems to me that the novel way of different Laplacian constructions is a fairly computationally expensive process due to the unconventional way of defining incidence matrices. The benchmark itself also only contains small graphs, so it is unclear if the model can scale. Also, the method itself seems to not work on directed multigraphs. Intuition for using Magnetic Laplacian isn’t clear to me; do we really need to introduce complex phase shift to represent directed edges, or can we just pick an arbitrary value and separate undirected and directed Laplacian? Also please refer to question 5 for my concern.

### Questions
1. On line 200-203, the authors state that “We restrict our novel constraints to undirected edges by requiring equivariance/invariance among direction-consistent orientations only. This allows representing the direction of directed edges through their orientation which, consequentially, must not be arbitrary.” Could you please explain the meaning behind this statement in a simpler term? If I understand correctly, orientation is generated arbitrarily for undirected edges, and direction-consistency only matters for directed edges. Also why does the representation of undirected edges allow representing the direction of directed edges?
2. Figure 2 should be explained more instead of just stating that the representations are indistinguishable for models that are orientation-equivariant for directed edges.
3. What is the time complexity to form the incidence and laplacian matrices in the paper?
4. I don’t think $\mathbf{B}_{\text{inv}}$ should be claimed to be a novel Laplacian as it is already standard definition in many works.
5. How sensitive the model is with respect to the hyperparameter $q$? It seems to me that if an edge has $k$ incoming edge messages such that $kq=2\pi m$ where $m$ is a natural number, the information regarding direction will be wiped out (assuming edge features are the same across edges).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper seeks to extend equivariant machine learning to signals (functions) defined on the vertices of a graph, including signals which are inherently directed (as well as undirected signals). It aims to produce representations which are either invariant or equivariant to changes in edge direction as appropriate, which is non-trivial since standard methods require a boundary operator which chooses an arbitrary edge direction. 

It achieves its goals by formulating the notion of direction consistent orientations and uses this notation to formulate joint orientation equivariance / invariance and then applying several distinct convolution operations (with various generalized magnetic Laplacians ) together with a fusion module and showcases its numerical effectiveness on real and synthetic data sets including data sets from traffic, which was one of the motivating applications.

Overall: I am rating this paper a six, but would have rated this paper a seven if that were an option.

### Strengths
The tasks are well motivated by realworld scenarios – figure 2 is quite nice!

The proposed network is an elegant solution for achieving the desired properties

Experiments are well sought out and feature a thorough ablation

### Weaknesses
The use of separate equivariant/invariant Laplacians L_equ, L_{inv-> equ}, etc is quite interesting. However, it is unclear how the proposed model compares to other networks defined in these Laplacians. Could one instead construct a ChebNet style architecture as was done in (Zhang et al 2021) with the magnetic Laplacian

I am unsure if the baselines adequately capture the current SotA


Minor:

Many equations, e.g., (6) and (7) are missing punctuation marks. (This does not affect my score but should be fixed)

The notation B^H is used without definition. I understand that this is the Hermitian transpose, but it should still be defined. (This does not affect my score but should be fixed)

Capitilization in the references e.g., ``laplacian” vs ``Laplacian”, should be fixed (This does not affect my score but should be fixed)

### Questions
The condition that \sigma_{equ}(-x)=-\simga_{\equ}(x) (line 242) seems stange. Are there common activation functions that satisfy this?

Why is there multiplication by the Laplacians in (2) and (3)? Based on standard GCNs it seems that left multiplication by low-pass filters (I-L/2) would be more natural?

Can this framework be extended to settings where there are both edge signals and node-signals?

Similarly, can it be extended to signed and directed graphs? The reference Zhang et al (2021), which the authors take setting from was extended to this setting in subsequent work ``MSGNN: A Spectral Graph Neural Network Based on a Novel Magnetic Signed Laplacian” (He et al.)

### Soundness
4

### Presentation
4

### Contribution
4
