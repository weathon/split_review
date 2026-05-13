# Improving Graph Generation with Flow Matching and Optimal Transport

- Decision: Reject
- Scores: 8, 6, 6, 1

## Abstract
Generating molecular graphs is crucial in drug design and discovery but remains challenging due to the complex interdependencies between nodes and edges. While diffusion models have demonstrated their potentiality in molecular graph design, they often suffer from unstable training and inefficient sampling. To enhance generation performance and training stability, we propose GGFlow, a discrete flow matching generative model incorporating optimal transport for molecular graphs and it incorporates an edge-augmented graph transformer to enable the direct communications among chemical bounds. Additionally, GGFlow introduces a novel goal-guided generation framework to control the generative trajectory of our model, aiming to design novel molecular structures with the desired properties. GGFlow demonstrates superior performance on both unconditional and conditional molecule generation tasks, outperforming existing baselines and underscoring its effectiveness and potential for wider application.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces GGFlow, a novel generative model aimed at improving the generation of graph-structured data. The author proposed a discrete flow matching framework combined with optimal transport (OT) and an edge-augmented graph transformer. It is the first discrete flow matching generative model with optimal transport for graph data. Additionally, GGFlow introduces a novel goal-guided generation
framework to control the generative trajectory of our model towards desired properties. The experiments show that GGFlow achieves state-of-the-art results in both unconditional and conditional graph and molecule generation tasks.

### Strengths
1. This paper is well-written and easy to read.
2. The authors introduced the first discrete flow matching generative model tailored for graph data, leveraging optimal transport for improved efficiency and stability.
3. The performance of the proposed method is quite promising.

### Weaknesses
This paper introduces a novel technique that combines discrete flow matching with optimal transport to enhance the efficiency of graph generation. While innovative, borrowing flow matching concepts from diffusion models used in image generation, several aspects could be further clarified:

1. Reward Function Definition: The method relies on a well-defined reward function, which is critical in reinforcement learning (RL) algorithms. However, the paper lacks a discussion on how the choice of reward function impacts the algorithm's performance and outcome. Specifically, the paper does not explore the sensitivity of the model to different reward functions, nor does it provide a rationale for selecting the specific reward function used, beyond its alignment with the evaluation metric. This leaves open questions about the robustness of the approach to different reward formulations.

2. Stability Claims: Although the authors assert that this approach offers greater stability in training and sampling, the experimental results do not provide direct comparisons with other diffusion-based generation algorithms to substantiate this claim. The paper does not include a detailed analysis of the training dynamics, such as convergence rates or variance in loss, compared to other methods. Furthermore, the sampling stability is only indirectly assessed through confidence intervals, which may not fully capture the nuances of sampling behavior.

3. Optimal Transport Justification: The use of optimal transport is presented as an improvement over other flow-matching techniques, yet there is no theoretical evidence provided to explain why optimal transport is preferable in this context. A rationale for this choice would strengthen the paper. The paper lacks a discussion on the specific properties of optimal transport that make it suitable for graph data, or why it would be superior to other coupling strategies in the flow matching framework. A more in-depth analysis of the theoretical underpinnings of this choice is needed.

### Questions
Although the performance is promising, the optimal transport is quite time-consuming. It is better to provide the complexity analysis or train/inference time compared with other methods.

### Soundness
3

### Presentation
3

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
This work introduces a discrete flow matching model for graph generation that uses optimal transport and edge-augmented graph transformer. The authors also introduce RL-based conditional graph generation. The proposed approach yields stable training and improves sampling efficiency.

### Strengths
- The discrete flow matching for graph generation seems to be novel, although there is existing work on flow matching framework for graph generation.

- The edge-augmented graph transformer seems to be an improvement of the previous graph transformer architecture.

- The motivation for using optimal transport to improve sampling efficiency for graph generation is reasonable but lacks experimental results.

### Weaknesses
 - CatFlow (Eijkelboom et al., 2024) is a graph generation method based on variational flow matching, which is highly related to this work. Although there is a comparison in Appendix B.3, there should be an experimental comparison and explanation of why GGFlow is better.

- Experiments for generic graph generation should use larger datasets like Planar or SBM instead of Ego-small and Community-small datasets which consist of very small graphs. Additionally, validity metrics such as V.U.N. (valid, unique, and novel) should also be used to evaluate models as MMDs are not a reliable metric, especially for small graphs. In particular, for the Grid dataset, the validity metric should be used to show that the generative model can actually produce a grid structure.

- Ablation study should be also conducted using datasets where validity or similar metrics can be measured, e.g., Planar or SBM datasets.  Relying only on MMD does not give much information on how the performance is improved.

- Comparison on molecule graph generation is not fair. It is not clear whether the new graph transformer architecture or the flow matching framework provides the performance improvement. In order to show this, there should be an ablation study on using the same architecture.

- The ablation study on sampling efficiency improvement based on optimal transport is not clear. Which experiments support this claim? Figure 3 only shows that GGFlow outperforms DiGress or GDSS, not the OT ablation.

### Questions
Please address the weakness above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes a discrete flow matching generative model incorporating optimal transport for graph structures with improved training stablility and efficient sampling compared with diffusion model. It achieves outstanding performance on both unconditional and conditional molecule graph generation tasks.

### Strengths
1. Clear illustration of graph flow matching method.
2. Strong performance on generation tasks. Clear ablation study.

### Weaknesses
1. Incomplete ablation study. Ablation of OF and GraphEvo is only conducted on one synthetic datasets.
2. Training stablility, as one of the benefits this work claims, is not compared in experiments.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces GGFlow, a graph generative model based on discrete flow matching and optimal transport. GGFlow aims to improve upon current graph generation methods, particularly diffusion-based models, by addressing two challenges: training stability and sampling efficiency. Additionally, GGFlow introduces a goal-guided generation framework using reinforcement learning, enabling conditional generation.

GGFlow generates graphs by transforming an initial noise distribution to a target data distribution through a smooth probability path, defined by a probability velocity field. This approach  the complexities associated with stochastic processes as in diffusion models.
To reduce the variance in training and sampling, GGFlow incorporates optimal transport to construct the joint distribution of the source and target graphs. The model integrates an edge-augmented transformer architecture (GraphEvo), which uses a triangle attention mechanism.

Using reinforcement learning, GGFlow can guide the graph generation process to meet predefined objectives, allowing for conditional generation where desired properties are targeted directly. 
GGFlow demonstrates high performance on small graph generation tasks. 

The article evaluates the model on synthetic and real-world datasets of small graphs, demonstrating effectiveness of the method. The experimental section includes an ablation study to assess the impact of both GraphEvo and Optimal Transport on model performance.

### Strengths
The paper is well-written and thoroughly documented. The appendix provides useful additional insights.

The proposed model introduces a novel graph generative approach based on discrete flow matching, which is a novel approach for graph generation. 

The method demonstrates competitive generative performance on small graph datasets, showing its effectiveness and relevance.

These are concise but significant strengths.

### Weaknesses
Weaknesses after rebuttal:

### 1. OT is Not Permutation-Invariant

One of the claimed main contributions of the paper is the use of Optimal Transport (OT) for graphs. However, the OT employed is not permutation-invariant, making it an OT on adjacency matrices under specific permutations, rather than on graphs.

The OT relies on the Hamming distance, which aggregates element-wise differences between adjacency (and annotation) matrices. This element-wise computation is dependent on node ordering, meaning that permuting one matrix changes the distance: \( H(G_0, G_1) \neq H(G_0, \pi G_1) \). The authors acknowledge that the Hamming distance is not invariant to arbitrary permutations, but they argue that their method only requires invariance under identical permutations, which is insufficient for true permutation invariance of graphs.

While the lack of permutation invariance would not be a problem if directly acknowledged, the paper obscures this limitation, and some formulations are misleading. The core issue is that the method operates on a specific representation of the graph (an adjacency matrix with a fixed node ordering) rather than the graph itself, which is a fundamental limitation of the approach.

---

### 2. Misleading Claims

Theorem 1 states: "the optimal transport map exhibits invariance under identical permutations." While this is technically true, it is misleading because it implies that the OT is invariant under all permutations, which is not the case. Specifically, if one matrix is permuted independently, the Hamming distance is not preserved: \( H(G_0, G_1) \neq H(G_0, \pi G_1) \). The authors' argument that their method only requires invariance under identical permutations does not address the core issue that the OT is not operating on the graph structure itself, but rather on a specific matrix representation.

This leads to other misleading claims:

- Lines 54–55: "The model preserves graph sparsity and permutation invariance, which is essential for realistic graph generation."  
  - This is true without OT but incorrect with OT.  The permutation invariance is only true for identical permutations of the coupled graphs, not for arbitrary permutations of individual graphs.

- Line 272: "Graphs are invariant to random node permutations, and GGFlow preserves this property."  
  - Similarly, this is true without OT but incorrect with OT. The method does not preserve permutation invariance in the general sense.

- Lines 275–277: "Since the source and target distributions are permutation invariant, the independent coupling also exhibits this invariance. Our optimal transport map, derived from Equation 7, similarly demonstrates invariance to identical permutations."  
  - The use of "similarly" is misleading, as "invariance to identical permutations" is fundamentally different from true permutation invariance. The optimal transport map is not invariant to arbitrary permutations of the input graphs.

The paper does not address how this non-invariant OT relates to truly invariant graph distances, leaving a significant gap in the discussion. The method's reliance on a fixed node ordering undermines the claim of operating on graphs directly.

---

### 3. Inconsistent Results and Interpretation

The authors claim that OT improves generative performance. However, the ablation study (Table 4) shows the model without OT performing better on 3 out of 8 metrics. With metrics being close and no standard deviations provided, there is no evidence of a significant effect of OT. The authors have not provided a compelling argument that OT is significantly improving the performance of the model.

Additionally, in the enzyme dataset, the paper reports MMD distances between generated and test sets that outperform the MMD between training and test sets. The explanation provided is incorrect, as MMD, being a distance between distributions, does not directly depend on sample size. The fact that the generated distribution is closer to the test set than the training set is highly unusual and raises concerns about the validity of the experimental setup or the interpretation of the results. The authors' explanation does not address this issue.

---

### Summary

The paper's claims around OT, permutation invariance, and the effectiveness of OT lack clarity and accuracy. Furthermore, the experimental results do not convincingly support the proposed benefits of OT. These issues should be addressed to ensure transparency and scientific rigor. The core issue is that the method operates on a specific representation of the graph (an adjacency matrix with a fixed node ordering) rather than the graph itself, which is a fundamental limitation of the approach.



___ Version before rebuttal ____

The paper raise some concerns:
- Some claims in the paper are misleading.
- Some results are questionable (generated graph distribution measured closer to the test set than the training set distribution?)


**Theorem 1 Validity**

The claim in Theorem 1 is problematic because the proof relies on the invariance of the Hamming distance under arbitrary permutations. However, the proof should show that the distance is invariant to independent permutations, i.e., $H(G^0, G^1) = H(\pi^0G^0, \pi^1G^1)$ instead of identical permutations (as exposed in appendix C.4: $H(G^0, G^1) = H(\pi G^0, \pi G^1)$). Therefore, the invariance does not hold. Consequently, if this assumption is indeed incorrect, then the Optimal Transport (OT) mechanism does not operate directly on graphs, but rather on specific graph representations, undermining a key contribution of the paper.

If Theorem 1 indeed fails, this calls into question the effectiveness of OT as applied in this context, and a significant part of the article should be reviewed.

**Experiments**

The experimental section has several limitations, and addressing these would significantly strengthen the work's impact. The main experimental limitations are as follows:

- Small Datasets: Except for the 'grid' dataset, which is a peculiar synthetic dataset, the model has only been tested on small graphs (up to 64 nodes for Planar, which is only reported in the appendix, and up to 38 nodes for Zinc). Testing on larger datasets such as SBM, Enzymes, Ego, or Proteins would improve the evaluation.

- Overfitting Concerns on Small Datasets: Evaluations on larger datasets are especially important given that generic datasets, often containing few instances, can easily be overfit. For instance, the lower novelty and uniqueness score on Ego-Small suggests some degree of overfitting on that dataset.

- Incomplete Ablation Study: While the model introduces several additional components, a more systematic ablation study on multiple dataset would clarify each element’s contribution. Moreover, a comparison between discrete flow matching and discrete diffusion would highlight the advantages of the flow matching framework. To ensure fairness, it would be beneficial to use a discrete diffusion model with identical architecture, extra features, and hyperparameters as a baseline. For molecular generation, presenting results without additional molecular features (which are not used in most baseline models and has been improved significantly the molecular metrics) would also be insightful.

- Scalability: While scalability is briefly mentioned as model limitation in the conclusion, it would be beneficial to include indicators of this issue in the experimental section. For instance, reporting generation times would provide insight about the model scalability.

**Lack of Novelty/Originality**

The paper represents an application of discrete flow matching to graph generation. This type of approach was expected; indeed, another paper submitted paper proposes a similar contribution (https://openreview.net/forum?id=ZGRRC514rI). 

**Missing Explicit References in Method Presentation**

Section 3 would benefit from more explicit references to foundational works. For instance, it would be useful to specify which discrete flow matching frameworks, as cited in Section 2, the authors drew inspiration from and how GGFlow differs from these.

**Minor Comments**

Line 51: This sentence lacks a main verb.

Line 44: Could you clarify the instability issues encountered in training diffusion models or provide relevant references?

### Questions
My evaluation relies primarily on the accuracy of Theorem 1 and the experimental design. The current rating assumes that Theorem 1 is incorrect. Naturally, if further clarification or evidence proves this theorem valid the rating would be significantly revised.
Similarly, clarification and/or improvement to the experimental section would change my evaluation.

### Soundness
1

### Presentation
2

### Contribution
2
