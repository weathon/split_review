# Grothendieck Graph Neural Networks Framework: An Algebraic Platform for Crafting Topology-Aware GNNs

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Due to the structural limitations of Graph Neural Networks (GNNs), particularly those relying on conventional neighborhoods, alternative aggregation strategies have been explored to enhance expressive power. This paper proposes a novel approach by generalizing the concept of neighborhoods through algebraic covers to overcome these limitations.
We introduce the Grothendieck Graph Neural Networks (GGNN) framework, providing an algebraic platform for systematically defining and refining diverse covers for graphs. The GGNN framework translates these covers into matrix representations, extending the scope of designing GNN models by incorporating desired message-passing strategies.
Based on the GGNN framework, we propose Sieve Neural Networks (SNN), a new GNN model that leverages the notion of sieves from category theory. SNN demonstrates competitive performance in experiments, particularly in differentiating between strongly regular graphs, and exemplifies the versatility of GGNN in generating novel architectures.
In conclusion, our work advances the design of GNNs by introducing algebraic structures that empower more expressive message-passing mechanisms, addressing the limitations of traditional neighborhood-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Grothendieck Graph Neural Networks(GGNN) framework, which systematically defines and refines diverse covers for graphs from an algebraic perspective. The framework uses matrix representations of covers and utilizes change-of-order mapping to enrich GNN operations. The authors further propose Sieve Neural Networks (SNN) based on the concept of sieves in category theory, and provide corresponding analysis. Experiments on SR and CSL datasets verifies the expressive power of SNN.

### Strengths
The GGNN framework can systematically define and refine diverse covers of graphs from an algebraic perspective, which is novel and offers plenty of design space. Overall, the paper is well presented. I checked with the proofs and have not found fatal mistakes.

### Weaknesses
 * Although the GGNN framework provides a general recipe for new GNNs, the authors only present one specific new GNN (i.e., SNN). The paper could benefit from more efforts elaborating on this.

* The theoretical analysis does not involve the connection with the WL hierarchy. What is the fine-grained expressivity of the proposed methods? The paper can also further benefit from more comparison and relationship with existing works, including isomorphism/homomorphism expressivity and other topology-aware GNNs.

* The experiments can be improved. (1) SR and CSL can only partially reflect expressivity in a very coarse manner. Can you conduct experiments on BREC[1], a more fine-grained expressivity benchmark? (2) TUdataset typically consists of very small and easy datasets, which is not convincing. Experiments on more common benchmarks (e.g., ZINC and QM9) are strongly encouraged.

### Questions
* Given that GGNN is a general framework, can you offer some examples of new GNN architectures other than SNN? Brief descriptions suffice.

* Can you elaborate on the expressivity compared with k-WL so that the results align with the experiments on SR and CSL?

* What is the scalability and performance of SNN in more large-scale real-world datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a framework that extends message-passing graph neural networks through generalizing the definition of neighborhood via algebraic representation of the covers of graphs. With the covers mapping into matrix representations, the framework is able to extend GNNs into new architectures, e.g., sieve neural networks, by leveraging relevant theories. Experiments are performed on datasets to verify the efficacy of the proposed approach.

### Strengths
1. The proposed framework seems to be a new concept inspired by generalizing conventional message passing with algebraic covers.

2. The algorithmic analysis on the method is detailed.

### Weaknesses
 1. The complexity of the proposed approach is O(n^4) which significantly limits the scalability towards larger graphs, see Q1.

 2. The experiment results are preliminary with part of those conveying vague information and part of those lacking important baselines, see Q2 and Q3.

 3. Missing discussions with more recent literatures, see Q4. The related works mentioned in this paper are earlier than 2023 with many missing.

 Minor:
 There are numerous inappropriate usages of citet and citep throughout the paper which hinders the readability.

### Questions
1. It would be helpful to provide the runtime of different approaches to give an idea on the scalability of the approach. In particular, runtime on different scales of the graphs would be appreciated. Since the model is of complexity O(n^4), I believe this is already a limitation which is even higher than some of the recent advanced approaches.

2. The SR (line 474) and CSL (line 485) of the experiments only convey vague information with no quantitative results presented.

3. The results in Table 1 are not quite convincing since the strong baselines are not included, such as [1]. The work has been cited and discussed in related works but not referred to in Table 1.

4. Missing related works, such as [2], [3], [4], [5].

[1] Feng et al. How Powerful are K-hop Message Passing Graph Neural Networks. NeurIPS'22.

[2] Zhang et al. Rethinking the Expressive Power of GNNs via Graph Biconnectivity. ICLR'23.

[3] Zhang et al. Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness. ICLR'24.

[4] Wijesinghe et al. A New Perspective on "How Graph Neural Networks Go Beyond Weisfeiler-Lehman?". ICLR'22.

[5] Zhao et al. A Practical, Progressively-Expressive GNN. NeurIPS'22.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents the Grothendieck Graph Neural Network framework, a approach that enhances GNNs by generalizing neighborhood structures using algebraic covers. Utilizing category theory and Grothendieck topologies, GGNN redefines graph covers, which are then converted into matrix representations to expand GNN architectural possibilities. The authors introduce the Sieve Neural Network within this framework, leveraging category theory to create sieve-based covers that support richer message-passing strategies. This model shows improved emperical performance.

### Strengths
This paper tries to design a new type of GNNs from the perspective of category theory. This is a novel and promising research direction. Empirical studies show improved performance of the new GNN.

### Weaknesses
The major weakness is perhaps the writing style and structure of this paper. I read the paper three times but still could not grasp what benefit the new GNN framework provides. In particular, the motivation/intuition is burried deep in lots of definitions, would be better to mention it clearly and early.
The construction of the framework is very complex and confusing and involves a lot of new terms and concepts that are not well explained. The new GNN has a very high complexity of $O(n^4)$ so I would expect the authors to justify this trade-off in complexity by benefits but couldn't find such discussion.
* The construction of GGNN involves a lot of newly introduced terms and concepts, but what benefit does it provide? How are the the directed subgraphs generated and how does such generatoin affect GGNN's power? Would be good to have specific sections with explanations of the benefits of GGNN and the process for generating directed subgraphs. Also a discussion on how different generation methods might impact GGNN's expressive power is better.
* The definition of directed subgraph is confusing. a gentle introduction of "acyclic" graph somewhere would be better. Adding it somewhere in preliminary would be nice.
* Thm 2.1.1 is trivial: Rep(D) is just a directed adjacency matrix. If the authors think this is important, please elaborate.
* I failed to find results of on SR and CSL datasets mentioned in Sec 3.4 except text description.
* Related work is limited and should be improved. There are many works try to enrich feature aggregation with alternative neighourhood definition e.g. [1], please consider compare with these works.
* wrong citation style used (I think author used \cite where it should be \citep), making a complex paper even harder to read

### Questions
* What (theoretical) superiority does GGNN gives us over other GNNs to justify the high complexity cost? Please be concrete.
* How are directed subgraphs chosen? Does the choice affect the power of GGNN?

### Soundness
2

### Presentation
1

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
This paper presents the Grothendieck Graph Neural Networks (GGNN) framework, an algebraic approach for constructing topology-aware Graph Neural Networks by generalizing neighborhood structures through algebraic covers. The GGNN framework introduces a novel approach to define high-order adjacency via directed subgraph and graph cover. Based on this, the authors propose the Sieve Neural Networks (SNN) model, leveraging the sieve concept from category theory to perform hihg-order message passing based on the derived matrix notation.

### Strengths
1. The GGNN framework creatively applies algebraic topology, offering a new paradigm for designing message-passing strategies that extend beyond conventional neighborhood-based approaches.

2. By using algebraic covers, GGNN can capture higher-order relationships in graphs, which enhances GNN expressiveness and aligns well with the intrinsic structure of graph data.

3. SNN demonstrates strong performance in experiments, particularly in distinguishing structurally complex graphs.

### Weaknesses
1. While GGNN introduces a novel approach for incorporating higher-order graph structural information into the message-passing framework, it does not include comparisons with other related methods, such as path-based GNNs[1-3] or substructure-based GNNs[4-5], and $K$-hop message passing GNNs[6-7], which also integrate higher-order structural information. It would strengthen the work to explain GGNN’s specific advantages over these methods, particularly concerning its expressive power. Specifically, the paper lacks a clear explanation of how the algebraic cover approach offers advantages over existing methods in terms of capturing complex graph structures. For example, it is unclear how GGNN's approach to defining neighborhoods via algebraic covers compares to methods that explicitly consider paths or subgraphs in terms of computational complexity and the ability to capture long-range dependencies.

2. The readability of the paper could be enhanced. For instance, including pseudo-code would provide a clearer procedural understanding of the GGNN method. Additionally, a figurative example demonstrating how SNN distinguishes strongly regular graphs where the 3-WL test fails would be beneficial for clarity. The current description of the method is abstract, making it difficult to grasp the practical implementation and the specific steps involved in the message-passing process. A concrete example would help illustrate how the algebraic cover is constructed and how it influences the message-passing mechanism.

3. Since the framework relies on concepts from category theory, it would benefit the readers if some background knowledge on this topic were provided to make the paper more self-contained. The paper assumes a level of familiarity with category theory that may not be common among the target audience. Providing a brief overview of the key concepts, such as sieves and monoids, would make the paper more accessible.

4. The experimental validation is primarily limited to TUDatasets. Including other datasets commonly used for GNN expressivity, such as OGB or QM9, would help assess the generalizability of GGNN across varied graph types. The current evaluation does not sufficiently demonstrate the robustness of the method across different types of graphs. The TUDatasets are relatively small and may not fully capture the challenges posed by larger, more complex graphs.

5. The results on the SR and CSL datasets are not shown in a tabular format.

### Questions
1. What is the advantages of GGNN and SNN over the existing methods in enhancing the expressive power of GNN in terms of distinguishing graph structures?

### Soundness
3

### Presentation
2

### Contribution
3
