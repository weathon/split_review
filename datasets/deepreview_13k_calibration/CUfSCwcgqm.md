# Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through Efficient Communication Channel

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Graph Neural Networks (GNNs) have been widely adopted for drug discovery with molecular graphs. Nevertheless, current GNNs mainly excel in leveraging short-range interactions (SRI) but struggle to capture long-range interactions (LRI), both of which are crucial for determining molecular properties. To tackle this issue, we propose a method to abstract the collective information of atomic groups into a few \textit{Neural Atoms} by implicitly projecting the atoms of a molecular.
Specifically, we explicitly exchange the information among neural atoms and project them back to the atoms’ representations as an enhancement. With this mechanism, neural atoms establish the communication channels among distant nodes, effectively reducing the interaction scope of arbitrary node pairs into a single hop. 
To provide an inspection of our method from a physical perspective, we reveal its connection to the traditional LRI calculation method, Ewald Summation. The Neural Atom can enhance GNNs to capture LRI by approximating the potential LRI of the molecular.
We conduct extensive experiments on four long-range graph benchmarks, covering graph-level and link-level tasks on molecular graphs. We achieve up to a 27.32\% and 38.27\% improvement in the 2D and 3D scenarios, respectively.
Empirically, our method can be equipped with an arbitrary GNN to help capture LRI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors address a crucial challenge in drug discovery using Graph Neural Networks (GNNs) - the difficulty in capturing both short-range interactions (SRI) and long-range interactions (LRI) within molecular graphs. While current GNNs excel at modeling SRI, they struggle with LRI, essential for determining molecular properties. To overcome this limitation, the authors propose a novel approach. They introduce "Neural Atoms," abstract representations that amalgamate information from atomic groups within a molecule. By exchanging information among these neural atoms and projecting them back to atoms’ representations, they establish effective communication channels among distant nodes, reducing the interaction scope of node pairs to a single hop. The method's efficacy is validated through extensive experiments on three long-range graph benchmarks, demonstrating its ability to enhance any GNN in capturing LRI, a crucial step forward in molecular graph analysis for drug discovery. Additionally, the paper provides a physical perspective, establishing a connection between this method and the traditional LRI calculation method, Ewald Summation.

====================

During rebuttal, the authors provided more experimental results and more detailed discussions on several aspects. Therefore, I increase my rating.

### Strengths
- The problem of capturing long-range interactions in molecular graphs is interesting and important.

- The paper is generally well-written and almost clear everywhere.

- Experiments conducted on several datasets, to some extent, show the effectiveness of the proposed method in both graph-level and link-level tasks.

### Weaknesses
 - The novelty of the proposed method is limited. For example, from the perspective of general graph machine learning, supernodes have been widely used which are the same as the concept of neural atoms. While the authors claim differences in interaction and projection, the core idea of using abstract nodes to represent groups of atoms is not new. The use of multiple supernodes, each representing a subgraph or community, has also been explored in prior work, further diminishing the novelty of this specific approach.

- Some claims are controversial: in the Introduction, the authors claimed the disadvantages of transformers, especially the self-attention mechanism, but the way to project atom representations to neural atom representations in the proposed method still uses multi-head attention. This inconsistency undermines the argument against transformers. Additionally, the running time experiments do not clearly show the computational advantages of the proposed method over transformers, which contradicts the initial claim that Graph Transformers (GTs) are more computationally expensive than GNNs. The use of multi-head attention in the projection step likely contributes to this lack of clear advantage.

- There are some limitations in the experimental studies including:

1.  Experiments have been conducted on only three relatively small-size benchmark datasets. These datasets, while relevant, do not fully capture the complexity of real-world molecular graphs. The absence of larger and more recent benchmarks like OC20 and OE62 limits the generalizability of the findings.
2.  Representative SOTA methods have not been compared, for instance [1]. The lack of comparison with state-of-the-art methods specifically designed for long-range interactions, such as Ewald-based message passing, makes it difficult to assess the true contribution of this method.

### Questions
- From the comparison of the running time, there are no clear advantages of the proposed method compared to the transformers which conflicts with the claim in the Introduction (GTs are more computationally expensive than GNNs). What are the reasons? The multi-head attention used in step 1?

- What will be the performance on larger datasets? Can the proposed method beat more recent SOTA such as [1]?

[1] Ewald-based Long-Range Message Passing for Molecular Graphs, ICML 2023

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a technique called Neural Atom that tries to abstract a cluster of nodes into a single node and subsequently leverage these condensed nodes for exchanging information that may not be achievable within the original molecule graphs. The authors validate the effectiveness of these proposed techniques through comprehensive experimentation conducted on three distinct datasets and employing various GNNs.

### Strengths
- The authors have made commendable efforts to clarify how their proposed algorithm works by providing theoretical explanations, which is commendable. 
- They have also used real-world case studies to show how their method functions in practice.

### Weaknesses
 - The incorporation of virtual atoms is not a novel concept, as it has previously been applied graph research as early as 2017 [r1, r2, r3]. It would be beneficial for the authors to engage in a discussion regarding how their proposed techniques differ from these referenced works. Furthermore, it is worth noting that there is a concurrent study that outlines a similar pipeline [r4]. Given the potential significance of this similarity, it would be valuable to include a discussion of this related work.

- The proposed approach has the potential to be employed across various types of graphs, as the concept of "virtual atoms" could be (and already have been) utilized  in other datasets like the OGB benchmarks. However, the authors did not explore this possibility in their work.
- The quality of writing in the paper seems to get worse as you read further, especially in Section 4. There are a lot of grammar mistakes in Section 4.2. Additionally, there are some terms like "ratio" in Table 4 and "varying proportion" in the last paragraph on page 7 that are introduced without prior explanation. This gives the impression that the paper was completed hastily.

### Questions
I have a couple of questions about Figure 5. Can atoms within the same neural atoms share information? If so, I'm wondering whether information exchange between atoms from different neural atoms is actually more than between atoms within the same neural atoms.
 
I am open to adjust my scores after the discussion with the authors.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary:
This paper proposes a method called "Neural Atoms" to help graph neural networks (GNNs) better capture long-range interactions in molecular graphs. The key ideas can be understood as: (i) introduce a small set of "neural atoms" that group together subsets of the original atoms in the molecule. This reduces long interaction paths to a single hop between neural atoms. (ii) use attention mechanisms to learn how to group atoms into neural atoms; and to exchange information between the neural atoms. (iii) enhance the atom representations by mixing in information from the neural atoms, allowing GNNs to capture long-range interactions. 

Overall, the paper seems to formalize the concept of neural atoms as virtual atoms that represent clusters of real atoms. In concept, this resembles similar to DiffPool (Ying et al., 2018 reference in the paper). however their implementation and purpose can be differently understood.

### Strengths
Strengths:  
(a) simple and architecture-agnostic method that can enhance any GNN.  
(b) reduces long-range interactions to single hop, avoiding path explosion issue.  
(c) outperforms baselines on molecular graph tasks needing long-range modeling.  
(d) visualizations show neural atoms learn meaningful groupings aligned with interactions.

### Weaknesses
Weaknesses:    
(a) does not utilize 3D coordinate information available for some molecules.   
(b) mainly considers intra-molecular, not inter-molecular interactions.   
(c) hyperparameter tuning needed for number of neural atoms, as the problem with pooling operation known earlier in graph learning literature.   
(d) lacks strong theory on optimal atom groupings.

### Questions
Questions:   
(a) How are the neural atom groupings initialized? Are they randomly assigned?   
(b) is there a theoretical justification for why this approach models long-range interactions well?  
(c) could 3D coordinate data be incorporated to better model distance-dependent interactions?   
(d) how does this approach scale to very large molecular graphs?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
