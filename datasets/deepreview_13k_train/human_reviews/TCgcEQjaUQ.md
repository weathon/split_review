# Scalable Message Passing Neural Networks: No Need for Attention in Large Graph Representation Learning

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
We propose Scalable Message Passing Neural Networks (SMPNNs) and demonstrate that, by integrating standard convolutional message passing into a Pre-Layer Normalization Transformer-style block instead of attention, we can produce high-performing deep message-passing-based Graph Neural Networks (GNNs). This modification yields results competitive with the state-of-the-art in large graph transductive learning, particularly outperforming the best Graph Transformers in the literature, without requiring the otherwise computationally and memory-expensive attention mechanism. Our architecture not only scales to large graphs but also makes it possible to construct deep message-passing networks, unlike simple GNNs, which have traditionally been constrained to shallow architectures due to oversmoothing. Moreover, we provide a new theoretical analysis of oversmoothing based on universal approximation which we use to motivate SMPNNs. We show that in the context of graph convolutions, residual connections are necessary for maintaining the universal approximation properties of downstream learners and that removing them can lead to a loss of universality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to substitute the multi-head attention in graph transformers with pure message passing. The authors provide theoretical analysis to prove that combined with residual connection, graph transformers with pure message passing can achieve universal approximation and alleviate over-smoothing.

### Strengths
- The proposed method is simple.

- The paper focuses on over-smoothing, an important problem in graph learning.

- The paper provides both empirical and theoretical analyses.

### Weaknesses
- The contribution of this paper is weak. The main focus is replacing the attention module in the transformer with a message-passing module and using the residual connections to alleviate the over-smoothing problem. However, the use of residual connections to address over-smoothing has already been explored in DeepGCN[1], which this paper does not mention or compare. Additionally, the implementation of deep GNNs has been studied in several other works[1]-[4].

- The paper contains a substantial amount of repetitive descriptions of existing work, such as message-passing neural networks and GCN (Eq. 2/3 vs. Eq. 6). Additionally, the theorem introduced in Section 4.1 is neither utilized later in the paper nor a contribution of this work.

- The contributions of the paper also involve repetitive work, such as a) using residual connections to mitigate over-smoothing; b) based on reference [5], Theorem 4.4 is evidently valid.

- Empirical analysis lacks heterophilic benchmarks to validate the effectiveness of SMPNN on over-smoothing.

- In tab. 7, SMPNN achieves the best performance on ogbn-proteins with 12 layers. Does SMPNN require significantly more computational resources and parameters to achieve comparable or better performance to baseline models?



[1] DeepGCNs: Can GCNs Go as Deep as CNNs? ICCV'19

[2] Graph Convolutional Networks via Initial residual and Identity Mapping, ICML'20

[3] Training Graph Neural Networks with 1000 Layers, ICML'21

[4] Revisiting Heterophily For Graph Neural Networks, NeurIPS'22

[5] How Powerful are Graph Neural Networks? ICLR'19

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Scalable Message Passing Neural Networks (SMPNNs), a framework designed to scale traditional message-passing GNNs. By incorporating residual connections, it avoids the issue of oversmoothing. The method claims to work without the need for computationally and memory-intensive attention mechanisms.

### Strengths
The paper is well-written with a clear motivation. The methodology is easy to follow, and the experiment section is well-structured.The paper is well-written with a clear motivation. The methodology is easy to follow, and the experiment section is well-structured.

### Weaknesses
The experiments are not strong enough. For instance, all SMPNN variants should be included consistently across tables and figures in the section. The same applies to baselines, unless there are reasonable explanations for exclusions. Additionally, the distinctions among SMPNN variants and the strengths of SMPNN are not clear. For example, SMPNN uses significantly more GPU memory than SGFormer, yet the paper still claims that it does not use more memory than the baselines. Some presentation needs to modified, for example: FF notation needs to be written consistently with the rest of the paper.

### Questions
- See weaknesses.
- If SMPNN w/o FeedForward uses significantly less GPU memory and performs better in accuracy than SGFormer, why is it not considered the main variant?  
- The difference between Figure 2 and Figure 3 is unclear.  
- For the SMPNN variant with attention (detailed in the Appendix), how does it differ from GAT (Veličković et al., 2017)?
- A real-time per-epoch runtime analysis should be included alongside the big-O analysis in the paper.
- Could you clarify why SMPNN, which uses message passing, primarily compares against an attention-based baseline?

### Soundness
2

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
3

### Summary
This paper proposes Scalable Message Passing Neural Networks (SMPNNs), a deep, scalable GNN framework that omits attention in favor of local message-passing, achieving efficient performance on large graphs. It claims to outperform transformer-based models while avoiding issues like over-smoothing.

### Strengths
1. The paper provides solid theoretical support, particularly on residual connections and universal approximation, which strengthens the SMPNN design and its claims.

2. By replacing attention with scalable message-passing, SMPNN achieves efficient performance and good experiment results on large graphs, offering a notable advancement for scalable GNN applications.

### Weaknesses
1. In Section 3.2, the authors label their proposed block as a "transformer block." However, the SMPNN framework lacks any attention mechanism, which is a core component of transformers. Consequently, SMPNN functions more like a deep GCN with residual connections rather than a genuine transformer model. This categorization is misleading, as attention mechanisms fundamentally distinguish transformers by enhancing scalability and representation capacity in large graph models. Existing models such as GCNII [1], EGNN [2], and DeeperGCN [3] have already explored architectures with enhanced depth. Although these models improve scalability, they are still linear and inherently limited compared to transformers.

2. Table 1 mentions that the SMPNN has training time complexities comparable to other transformer-like models, such as GraphGPS and Exphormer. However, the experiments do not include comparisons with these transformer-based models, especially models with higher computational complexity, like Graphormer, that might showcase different trade-offs in performance versus scalability. While SMPNN is intended to scale to larger graphs, demonstrating performance across various data scales, especially small to medium datasets, would test its broader applicability.

3. SMPNN relies on local message-passing operations without incorporating global attention mechanisms, which may limit its ability to capture long-range dependencies effectively. For tasks where global context is essential, SMPNN's performance could be suboptimal compared to transformer-based models that use global attention mechanisms. A discussion on this limitation and potential strategies would strengthen the paper.

[1] Chen, Ming, et al. "Simple and deep graph convolutional networks." International conference on machine learning. PMLR, 2020.
[2] Zhou, Kaixiong, et al. "Dirichlet energy constrained learning for deep graph neural networks." Advances in Neural Information Processing Systems 34 (2021): 21834-21846.
[3] Li, Guohao, et al. "Deepergcn: All you need to train deeper gcns." arXiv preprint arXiv:2006.07739 (2020).

### Questions
same to weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a new Scalable Graph Convolution Network. The author develops a scalable message passing block which involves a residual connection that connects two parts. The first part is a GCN block, and the second part is a point-wise feed forward layer as in transformer. This architecture retains computation efficiency. Meanwhile, the author illustrates how their method solves the over smoothing problem. The original graph convolution is not a universal approximator. However, with a residual connection, the graph convolution can turn to a universal approximator. And the authors provide extensive experiment results to prove the efficiency of their method.

### Strengths
Pros: 

1: The motivation of this paper is clear. The author adapts the transformer architecture to address the scalability issue in Graph Neural Networks. 

2: The author presents both theoretical analysis and experimental results for their methods, offering a comprehensive approach. 

3: The authors provide extensive experiments on different dataset and relevant ablation study to prove the effectiveness of their method.

### Weaknesses
Cons: 

1: The SMPNN can maintain its performance but does not gain any advantages from a deeper network. What causes this? 

2: For larger graph datasets, the improvement from SMPNN is less pronounced. For example, on the ogbn-papers-100M dataset, the improvement is only 0.2%. Could this suggest that the model size is still inadequate? If we use a larger network for both SMPNN and Graph Transformer, SMPNN should experience less oversmoothing and demonstrate a more significant accuracy improvement.

### Questions
Please see weakness

### Soundness
3

### Presentation
3

### Contribution
3
