# SE3Set: Harnessing equivariant hypergraph neural networks for molecular representation learning

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
In this paper, we develop SE3Set, an SE(3) equivariant hypergraph neural network architecture tailored for advanced molecular representation learning. Hypergraphs are not merely an extension of traditional graphs; they are pivotal for modeling high-order relationships, a capability that conventional equivariant graph-based methods lack due to their inherent limitations in representing intricate many-body interactions. To achieve this, we first construct hypergraphs via proposing a new fragmentation method that considers both chemical and three-dimensional spatial information of molecular system. We then design SE3Set, which incorporates equivariance into the hypergragh neural network. This ensures that the learned molecular representations are invariant to spatial transformations, thereby providing robustness essential for accurate prediction of molecular properties. SE3Set has shown performance on par with state-of-the-art (SOTA) models for small molecule datasets like QM9 and MD17. It excels on the MD22 dataset, achieving a notable improvement of approximately 20\% in accuracy across all molecules, which highlights the prevalence of complex many-body interactions in larger molecules. This exceptional performance of SE3Set across diverse molecular structures underscores its transformative potential in computational chemistry, offering a route to more accurate and physically nuanced modeling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces SE3Set, an SE(3)-equivariant hypergraph neural network designed for molecular representation learning. The main contributions include: a novel fragmentation method that combines 2D chemical and 3D spatial information, a hypergraph neural network architecture that captures many-body interactions, and integration of SE(3) equivariance within the hypergraph framework. The method shows comparable performance to SOTA on small molecule datasets (QM9, MD17) and claims ~20% improvement on larger molecules in MD22.

### Strengths
1. The combination of hypergraph neural networks with SE(3) equivariance is novel and provides a theoretically sound approach to handling molecular symmetries.

2. The fragmentation method is well-designed, offering both explicit and implicit overlap schemes while preserving chemical intuition through maintaining functional groups and rings.

3. The implementation is thoroughly documented with detailed algorithms, parameters, and clear pseudocode for reproducibility.

4. The ablation studies are comprehensive, examining both fragmentation parameters and model components with clear justification.

### Weaknesses
1. The paper omits a comparison with recent relevant work, particularly EquiformerV2, which could provide important context for the method's effectiveness.

2. The computational efficiency analysis is inadequate, lacking detailed benchmarks of training time, memory usage, and scaling properties compared to baseline methods.

3. The complexity analysis in Appendix H needs more rigor and real-world benchmarking data to support the theoretical claims.

4. The method cannot handle certain molecule types in MD22 (like the Buckyball catcher), limiting its applicability to complex molecular systems.

5. The selection of hyperparameters, particularly cutoff values, appears arbitrary without clear guidelines for practitioners.

### Questions
1. Could you explain why certain molecules in MD22 (like the Buckyball catcher) cannot be handled by your fragmentation method? What modifications would be needed to support these structures?

2. The paper shows improved performance with increased fragment size (lower $c_w$), but this comes with higher computational cost. How do you recommend practitioners balance this trade-off?

3. The improvement on MD22 is attributed to better capturing of many-body interactions. Can you provide additional evidence or analysis to support this claim?

4. How does the method scale with system size? Could you provide complexity analysis for both time and memory usage as a function of number of atoms and fragments?

5. Have you considered extending the method to handle periodic systems or crystal structures? What modifications would be required?

### Soundness
3

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
4

### Summary
This work focuses on the task of learning molecular representations from 3D molecular structures and proposes a new model called SE3Set. Basically, SE3Set uses hypergraphs constructed based on a fragmentation strategy to represent many-body interactions and then develops an SE(3)-equivariant network to learn from the hypergraph. It’s an extension of hypergraph neural network (which was proposed for graphs without 3D information) and tensor product-based equivariant models.

SE3Set’s performance is demonstrated on several widely used benchmarks for molecular representation learning, including QM9, MD17, and MD22. It shows that SE3Set performs better than existing models on the large molecule benchmark MD22.

### Strengths
1. It is intuitively convincing to consider many-body interactions for molecular representation learning. SE3Set applies the idea of fragmentation to construct the many-body interactions of interest. This is a promising approach.

2. It is valuable to incorporate SE(3) equivariance into the hypergraph framework. In addition, the update rules (E2V and V2E) proposed in this work are very natural, compared to the existing AllSet framework for hypergraphs without 3D information.

3. The manuscript is well organized and easy to follow. I enjoy reading this work.

### Weaknesses
1. The experiment results are not so strong and comprehensive. 
- On three benchmarks, SE3Set shows notable improvements on MD22 but performs quite similarly to many existing methods on QM9 and MD17. I understand that it is claimed that SE3Set is more effective on large molecules where many-body interactions are more important. To support this claim well, experiments on more large molecule benchmarks should be provided. 

- SE3Set operates on hypergraphs and such hypergraphs are constructed based on overlapped fragments, which might bring memory and computation overhead. However, there is no analysis on the complexity of SE3Set and the experimental comparison in terms of memory and running time is also missing.

2. The ablation studies are not convincing, thus cannot support the main claim strongly. SE3Set’s performance is mainly demonstrated on MD22 but the ablation on fragmentation and E2V architecture is performed on one selected task on QM9. This is somewhat contradictory to the main claim that SE3Set (and the associated fragmentation strategy) is more effective for large molecule settings.

### Questions
As detailed in the weaknesses section, I highly recommend enriching the experiments and ablation studies of this work to make the main claim more convincing.

### Soundness
3

### Presentation
3

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
This paper proposes a novel molecular fragmentation method, which is applied to hypergraph neural networks. The design of the attention mechanism within the network ensures the equivariance of the hypergraph neural network.

### Strengths
1. The writing and structure of the paper are well-organized, making it easy to read.  
2. The downstream experiments and ablation studies are thorough and comprehensive.

### Weaknesses
1. I find the innovation in this paper somewhat limited. While many previous works have focused on the design of hypergraph structures and ensuring equivariance, the main contribution of the authors appears to be the proposal of a new fragmentation method. However, compared to existing fragmentation methods, the improvements introduced in this paper seem modest, and the differences primarily lie in the specific tasks each method is suited for, with each having its own strengths.
2. The paper’s performance on the QM9 and MD17 datasets is relatively unimpressive. While it emphasizes strong results on the MD22 dataset, the mediocre performance on the two datasets related to dynamic properties raises concerns about the practical applicability and generalizability of the proposed method, as real-world drug design tasks are closely related to these datasets. Additionally, given the emphasis on the method’s effectiveness for macromolecular data where interaction is crucial, I am curious about its performance on the LBA dataset.

### Questions
1. Could you introduce some chemical processes that can be effectively represented through hypergraph modeling? Which molecular processes can be better explained using hypergraphs? It seems that the paper primarily integrates the concept of functional groups into the hypergraph framework as a form of innovation.
2. Please further elaborate on the differences and advantages of the subgraph decomposition method proposed in this paper compared to previous classical methods, such as BRICS and first-principles-based subgraphs.

### Soundness
3

### Presentation
3

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
This paper proposes a new method, SE3SET, which combines Equivariant Graph Neural Networks (GNNs), HGNN, and attention mechanism to predict molecular properties. This approach shows improvements in related benchmarks.

### Strengths
a. This paper is well-written.
b. The experimental results are impressive.
c. The method is detailed and should be reproducible.

### Weaknesses
a. Some sections lack sufficient evidence. For example, in Section 4.1, fundamental principles should be supported with appropriate references or validated through an ablation study.
b. Some images could be adjusted for clarity. For instance, in Figure 2, it would improve readability if submodules were directly linked to the main model with arrows or other visual indicators.
c. The motivation behind this article is unclear, and it’s difficult to understand why the proposed method is uniquely suited to the related tasks. The introduction and related work sections mention that HGNN has been used in various graph neural network studies, yet they don’t explain the limitations of these works or how this study addresses these issues.

### Questions
a. How can the correctness of the four fundamental principles of fragment splitting be validated? Are there any citations?
b. What is the primary motivation of this paper? EGNN, attention mechanisms, and HGNN have already proved their effectiveness in previous works. Why are these three methods chosen together? Is there a specific reason for this combination?

### Soundness
3

### Presentation
3

### Contribution
2
