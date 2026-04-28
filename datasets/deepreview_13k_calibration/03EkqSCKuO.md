# Port-Hamiltonian Architectural Bias for Long-Range Propagation in Deep Graph Networks

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8

## Abstract
The dynamics of information diffusion within graphs is a critical open issue that heavily influences graph representation learning, especially when considering long-range propagation. This calls for principled approaches that control and regulate the degree of propagation and dissipation of information throughout the neural flow. Motivated by this, we introduce port-Hamiltonian Deep Graph Networks, a novel framework that models neural information flow in graphs by building on the laws of conservation of Hamiltonian dynamical systems. We reconcile under a single theoretical and practical framework both non-dissipative long-range propagation and non-conservative behaviors, introducing tools from mechanical systems to gauge the equilibrium between the two components. Our approach can be applied to general message-passing architectures, and it provides theoretical guarantees on information conservation in time. Empirical results prove the effectiveness of our port-Hamiltonian scheme in pushing simple graph convolutional architectures to state-of-the-art performance in long-range benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces port-Hamiltonian Deep Graph Networks (PH-DGN), a new framework for graph neural networks that addresses the challenge of long-range information propagation. The approach embeds message passing within a port-Hamiltonian dynamical system framework, where node states are split into position (q) and momentum (p) components coupled through skew-symmetric matrices. The Hamiltonian function incorporates graph structure through neighborhood aggregation functions, and the port-Hamiltonian extension introduces learnable dissipative components (internal dampening and external forces) that allow the network to balance conservative information preservation with task-dependent information modification. The authors provide theoretical analysis of the framework's properties, including bounds on sensitivity and gradient behavior, and demonstrate empirically that their method outperforms existing approaches on several tasks requiring long-range information propagation, including synthetic graph property prediction tasks and real-world molecular property prediction. The framework can incorporate different message passing schemes and provides improved efficiency compared to previous Hamiltonian-based graph neural networks, with experimental results showing that while the purely conservative version performs well, including the dissipative components often leads to better task performance.

### Strengths
Overall, the idea of using Hamilton's dynamics for GNN is attractive, though not entirely new. 
Nevertheless, the paper is solid and is more general than existing approaches. 
The improved efficiency over previous Hamiltonian GNN approaches and the practical benefits for long-range propagation make it a useful contribution to the field.
The experimental results are also interesting. 

1. Technical soundness:
- Clear theoretical analysis of conservation properties
- Explicit connection between Hamiltonian dynamics and message passing
- Thorough experimental validation

2. Practical value:
- More efficient than previous Hamiltonian GNN approaches
- Good performance on long-range tasks
- Can incorporate different message passing schemes

3. Clarity:
- Well-structured presentation
- Good balance of theory and empirics
- Clear comparisons to prior work

### Weaknesses
 1. Novelty is incremental:
- Builds on existing ideas (Hamiltonian GNNs, message passing)
- Main contribution is combining these effectively rather than fundamentally new concepts

2. Technical questions:
- The derivation of the discretization scheme could use more justification
- Some assumptions about the structure of $W$ and $V$ matrices for explicit updates feel restrictive
- Could better explain why port-Hamiltonian framework is more appropriate than simpler alternatives

3. Empirical:
- Some ablation studies could be stronger (e.g., analyzing impact of different dissipative terms)
- Could better justify hyperparameter choices

### Questions
1. While the paper shows good empirical performance, it's unclear what types of problems would theoretically benefit most from a port-Hamiltonian approach versus standard message passing. Could the authors provide analysis or insights about which properties of the underlying data generation process would suggest using their method?

2. The authors demonstrate that adding dissipative components often improves performance, but how does the balance between conservative (Hamiltonian) and dissipative parts relate to the nature of the task? It would be valuable to see an analysis of when pure conservation might be preferable to including dissipation, and how practitioners should choose this balance for new problems.

3. Given that the method is inspired by physical Hamiltonian systems, it's surprising that there are no experiments on problems with actual Hamiltonian dynamics (e.g., molecular dynamics simulations). Such experiments could help validate whether the method's conservation properties provide advantages for physically meaningful conservation laws, beyond just improving general information flow.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes PH-DGN, a new GNN based on the port-Hamiltonian system to develop GNN that can solve graph learning tasks that require long-range dependencies. Two variants of PH-DGN are proposed: a conservative PH-DGN based on the Hamiltonian system and a PH-DGN based on the port-Hamiltonian system by introducing learnable dissipative terms. 
The theoretical analyses show that the conservative PH-DGN is stable and energy-preserving as a dynamical system, and derive a lower bound for the sensitivity, implying the possibility of long-range interaction.
Numerical experiments show that the conservative PH-DGN is energy-preserving without gradient vanishing using synthesis datasets (Section 3.1) and that the long-range interaction can be achieved in graph learning tasks that require long-range interactions (Sections 3.2, 3.3). Also, the usefulness of two variants of PH-DGN is evaluated on long-range graph benchmarks of real datasets.

### Strengths
- The background knowledge of the port-Hamiltonian system is explained carefully, increasing accessibility for readers unfamiliar with this topic.
- For conservative PH-DGN, the ability of long-range interaction is theoretically shown by giving the lower bounds of sensitivity.
- The validity of the proposed methods for synthesis datasets is properly demonstrated.

### Weaknesses
 - As the title indicates, the theme of this paper is the relationship between GNN and long-range propagation based on the port-Hamiltonian system. However, no theoretical guarantees on long-range propagation are given for general PH-DGNs with dissipative components.
- The tables of experimental results could be clearer (in particular Tables 2 and 5).
- For $\mathrm{PH-GDN}_{\mathrm{C}}$, which has theoretical guarantees, the prediction performance on the real dataset (long-range graph benchmark) does not outperform existing methods, and hence its practical usefulness is limited.



### Questions
**Questions**

- l.161: What is the definition of anti-derivative of an activation function $\sigma$?
- l.223, l.228: Which norm is used in $\| \partial \mathbf{b}_u(T) / \partial \mathbf{b}_u(T-t) \|$? 
- l.259: *Therefore, [...]. , it holds the capability of PH-GDN to perform long-range propagation effectively*: the authors compare the upper bounds of sensitivity for the existing model (Theorem 2.3) and the proposed model (Theorem 2.4), then argue that since the latter is larger than the former, the proposed model is more effective in performing long-range propagation. However, it is difficult to claim so because there is the possibility that Theorem 2.4 only shows a looser bound than Theorem 2.3, which does not exclude the possibility that the upper bound does not properly reflect the sensitivity of the PH-GDN. It should be shown theoretically or experimentally that this upper bound adequately reflects the sensitivity of the PH-GDN.
- l.1129: I want to clarify the setup of the Graph Transfer Task: If I understand correctly, the feature vectors of all nodes are 1-dimensional and randomly sampled from $\mathrm{Unif}([0, 0.5))$. The target value is 0 for the source node and 1 for the target node. Assuming that this problem setup is correct, I need help understanding why this task is solvable because the model cannot distinguish source or target nodes from other nodes from feature vectors.


**Minor Comments**

- l.196: *non-dissipative (i.e., long-range)*: I think this is a slightly misleading expression. My understanding is that this paper uses non-dissipative in the sense of energy-perserving. Although non-dissipative implies long-range propagation (Theorem 2.3), they are not equivalent. In fact, this paper argues that non-dissipative PH-DGN performs better than conservative PH-DGN in predicting the LRGB dataset in some numerical experiments.
- l.436: The use of position encoding is only mentioned in the caption of Table 2 and should be explicitly stated in the text, specifically in the setup of Section 3.4.
- l.436: The correspondence between Table 2 and Table 5 needs to be clarified. For example, the method titled *MPNNs* in Table 2 is titled *re-evaluated* in Table 5. However, GCNII is not listed as *re-evaluated*, but as *MPNNs*. Furthermore, it is difficult to tell from the captions of Table 5 whether the authors test each listed method by themselves or is a citation of existing research. The reference should be indicated for each method in Table 5, for example, by adding a column such as *reference* to Table 5.
- l.443: *Overall, our port-Hamiltonian framework [...] shows great benefit [...] without requiring additional strategies such as global position encoding, global attention mechanism, or rewiring techniques [...].*: I suggest clarifying how the usefulness of each strategy is shown by comparing it with existing methods. More specifically:
  - The superiority of the proposed method over global position encoding is justified by the comparison with MPNN-based models using position encoding.    　　
  - The superiority over the global attention mechanism is by comparison with the Transformer-based method.
  - The superiority of rewiring methods by comparison with Drew.
- l.1153: The reference to Adam (Kingma & Ba, 2015) should be cited.
- l.1343: n. layers -> the number of layers
- l.1353: Table 6 claims that PH-DGN achieves both Hamiltonian conservation and Learnable driving forces. However, I think this is misleading because to achieve Hamiltonian conservation, the dissipative component must be removed, resulting in $\mathrm{PH-DGN}_{\mathrm{C}}$. It is not possible to achieve both characteristics at the same time in one architecture. Instead, two variants that achieve only one of the two are proposed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work provides a novel methodology for the incorporation of port-Hamiltonian dynamics in graph representation learning. The central model, called a port-Hamiltonian Deep Graph Network (PH-DGN), is introduced first in a purely conservative setting using only the Hamiltonian and no non-conservative terms. Several theorems are developed to show that this conservative case leads to long-range data propagation between graph nodes, where the graph dynamics exhibit no energy loss and gradients do not vanish as the backward sensitivity matrix is bounded below. Dissipitive forces are then added to the full port-Hamiltonian model, which are two additional networks that may be trained to capture non-conservative forces. Several experiments follow, including a showcase of energy conservation and sensitivity to empirically verify theoretical work, and a graph transfer problem and graph property prediction problem to compare performance on benchmark tasks against other graph models in settings which require long-range information propagation.

### Strengths
- There is very clear motivation to this work, and it builds nicely upon other references.
- The proposed port-Hamiltonian approach is an original and clever way to allow for non-conservative dynamics in a graph network while still maintaining long-range message passing.
- The theoretical results for the conservative case are strong, and the motivation and interpretation for these are presented nicely.
- The experimental setup is superb; the care taken to ensure ease of replication is applauded. Model details are presented very clearly and choices are explained well for each step of the setup.
- A strong suite of models are compared against, with many different competitors and different approaches. The consistently favorable results provide a great deal of strength to claims of the proposed method's performance.
- The appendices are comprehensive for both proofs and experimental setup, and made clear many of the questions I had on an initial read.

### Weaknesses
 - The majority of the theoretical results are developed for the conservative case. This makes sense in the context, as conservative long-range message passing is stated as a goal, but I would also be quite interested to see what could be proven for the fully general port-Hamiltonian case. Specifically, the current analysis provides a strong foundation for understanding energy conservation and gradient behavior in the absence of dissipative forces, but lacks a rigorous characterization of how these properties are affected when the full port-Hamiltonian dynamics are engaged. A more detailed theoretical treatment of the dissipative case would be valuable, perhaps exploring bounds on the sensitivity matrix or energy dissipation rates under different conditions.
- In the explanation of Theorem 2.3, the statement that "the final representation of each node retains its complete past" seems somewhat strong. While I understand that the BSM result shows the influence of the entire past history on the current state, this statement as written seems to imply something stronger, and perhaps could be made more clear. The theorem demonstrates that the backward sensitivity matrix is bounded, implying that past states influence the current state, but it does not necessarily mean that all past information is perfectly preserved or equally weighted. A more nuanced discussion of the information flow and potential information loss would be beneficial.
- The dissipitive force terms are added in some experiments to great success, but the explanations of their performance are more intuitive and are not supported by hard data in the paper. There may be a great opportunity here for visualization to support the intuitive claims. While the authors provide a plausible explanation that these forces act as adaptive filters, this is not rigorously demonstrated. It would be beneficial to include visualizations of the learned force fields, or perhaps analyze the frequency content of the node embeddings to show how the dissipative forces are filtering information. Without this, the claims remain somewhat speculative.

### Questions
- How would classical GCN aggregation interact with Theorem 2.4? Can the bound be easily extended for that case?
- In Section 3.1, you mention that the growing behavior can be controlled by regularizing the weight matrices or using normalized aggregation functions. Did you try this? How are the empirical results?
- Have you examined the interpretability of a trained PH-DGN? In particular, do the learned non-conservative forces make sense for the associated problem?

### Soundness
4

### Presentation
3

### Contribution
3
