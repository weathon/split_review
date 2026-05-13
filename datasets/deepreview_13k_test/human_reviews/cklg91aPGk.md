# Propagation Alone is Enough for Graph Contrastive Learning

- Decision: Reject
- Scores: 6, 5, 6, 3, 5

## Abstract
Graph contrastive learning has recently gained substantial attention, leading to the development of various methodologies. In this work, we reveal that a simple training-free propagation method PROP achieves competitive results over dedicatedly designed GCL methods across a diverse set of node classification benchmarks. We elucidate the underlying rationale for PROP’s effectiveness by drawing connections between the propagation operator and established unsupervised learning algorithms. To investigate the reasons for the suboptimal performance of GCL, we decouple the propagation and transformation phases of graph neural networks. Our findings indicate that existing GCL methods inadequately learns effective transformation weights while exhibiting potential for solid propagation learning. In light of these insights, we enhance PROP with learnable propagation, introducing a novel GCL method termed PROPGCL. The effectiveness of PROPGCL is demonstrated through comprehensive evaluations on node classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors investigate how the propagation and transformation components affect the Graph Contrastive Learning (GCL) methods. They first illustrate that simple uniform propagation can achieve competitive performance compared with GCL baselines through empirical experiments. Then, they further conduct experiments on how the propagation and transformation layers contribute to the GCL process. The results suggest that the GCL process could not help learn very meaningful transformation parameters but could be helpful in learning propagation hyper-parameters. Based on these observations, they further proposed a GCL framework named PROGCL, which adopts different training-free PROP as backbones. Specifically, they replace the encoder in GCL methods with propagation-only polynomial GNNs. The effectiveness of these methods are verified by empirical experiments.

### Strengths
1. Originality: The paper majorly investigates how the components in GCL methods work. The findings in this paper are quite novel. 

2. Quality: The paper seems to be quite sound. Empirical experiments support the conclusions of this paper well. 

3. Clarity: In general, the paper is well written. All the important points and observations are clearly presented. The paper is also well-organized such that different investigations are quite logically presented.

4. Significance: The outcomes from this paper could be significant as they could help provide some guidance on designing effective and efficient GCL methods.

### Weaknesses
1. The title and narrative in this paper have been talking about GCL in general. However, this paper is more about GCL for node classification tasks only. Will these conclusions in the paper hold true for other tasks, especially graph classification tasks? It would be better if the authors could conduct further investigations. If not, it might be better if the authors could narrow their scope to GCL for node classification tasks. 

2. It would be more convincing if the authors could conduct experiments on larger datasets in addition to the adopted ogbn-arxiv dataset.

### Questions
See the questions in the Weakness part.

### Soundness
3

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
5

### Summary
The paper investigates a training free, non-parametric method called PROP for graph contrastive learning. "PROP" is a method which aggregates node features within K-hop neighbors, without any trainable weights. After such a feature propagation phase, the aggregated node features are fed to a downstream classifier for evaluation on node classification / graph classification tasks. The paper claims that for unsupervised learning, only performing "PROP" is enough and is in fact comparable in performance to other learnable methods from literature that utilize sophisticated contrastive objectives. Given the strong performance of "PROP" and claim that propagation of features is sufficient for GCL, the authors further propose "PROPGCL" paradigm, where encoders of traditional GCL methods are replaced with trainable propagation only polynomial graph neural networks. The authors then experimentally show how "PROPGCL" provides performance gains compared to standard encoder choices in said traditional GCL methods.

### Strengths
1) Viewing polynomial GNNs (propagation) as performing graph contrastive learning sheds new light into our understanding of contrastive learning methods for graphs.

2) Interesting insight via experiments that show feature transformations are not necessary in certain conditions for effective graph contrastive learning.

3) The paper provides a comprehensive set of experiments, with detailed analysis.

### Weaknesses
1) While the experiments are well done, the main claim is not fully supported / backed up. For e.g., in the graph level tasks (Appendix A), the proposed paradigm of only "PROP" is inferior to other GCL focused methods from literature and performance is not comparable. So why is it effective only for node level tasks?

2) The heterophilic graph datasets chosen in the paper are known to be problematic, choosing recent heterophilic datasets (for e.g.., from https://arxiv.org/abs/2302.11640) will provide a more robust argument. IMO the chosen datasets for node level tasks are quite small and limited to meaningfully test GCL in a realistic setting. Investigating the proposed paradigm of "PROP" and "PROPGCL" on large scale graphs from OGB (Open graph benchmark) will provide a more convincing argument. 

3)  The novelty of the proposed paradigm of "PROP" is quite limited since it is well known to the community that feature aggregation is a powerful inductive bias that GNNs possess. In fact, many GCL methods commonly employ randomly initialized and untrained GNNs as a baseline [c.f. ADGCL (https://arxiv.org/pdf/2106.05819) See for e.g. RU-GIN.]. Moreover, on node level tasks in heterophilic datasets, it is well known that such feature aggregation property of GNNs is very important.

4) While the authors acknowledge that in cases where there are low quality node features (sparse / noisy / absent), propagation alone can be insufficient. This IMO is one of the biggest drawbacks of the proposed approach. Previous methods aim to deal with such cases.

5) There is very little discussions on the results in conclusion section to string together different experiments into a cohesive argument. IMO the readers will appreciate a concise explanation rather than digging through the appendix.

### Questions
1) While the authors cite the paper "A critical look at the evaluation of GNNs under heterophily: Are we really making progress?" Platonov e.t. al, ICLR 2023 (https://arxiv.org/abs/2302.11640) why are the newer datasets not chosen for heterophilic datasets ?

2) Why is PROPGCL not evaluated for graph level tasks.?

3) How is PROP setup for graph level tasks?. Are resulting node feature after feature aggregation pooled into a single feature for downstream classification?

------- 
I raise my score from 3-> 5, given that the authors have answered some of my questions and concerns.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on graph contrastive learning (GCL). The authors reveal that a simple training-free propagation method PROP can achieve competitive results over dedicatedly designed GCL methods.
To further study the underlying reasons, they decouple the propagation and transformation phases of graph neural networks in GCL and find that GCL inadequately learns effective transformation weights while exhibiting potential for solid propagation learning. Motivated by this, the authors proposed a novel GCL method termed PROPGCL which demonstrates its effectiveness on various datasets.

### Strengths
1. This paper is well motivated by detailed observation and conducts a thorough analysis.
2. The proposed method is well supported by theoretical findings and previous works. The findings refresh the customary viewpoints on designing GCL methods.
3. The proposed method is simple but shows outstanding performance compared to previous GCL and GSSL methods.

### Weaknesses
1. The proposed method is only verified on node-level tasks with strong feature-connection relationships (i.e., strong homophily and heterophily). No study on the more complicated scenario, for example:
   - complex relationship between node features and edges, e.g., partial multidimensional homophily (Block & Grund, 2014)
   - graph structures introduce extra information instead of hinting homophily/heterophily, e.g., superpixel datasets (CIFAR10, MNIST) in Dwivedi et al. (2022).

Without this, the work can only show that previous GCL methods cannot adequately learn feature transformation. However, it cannot demonstrate that learning feature transformation is unnecessary or harmful if we can manage to learn adequately. A further study on it might lead to a stronger statement on the proposed method.

2. There is no evaluation of the inductive setting, including the single-graph datasets (e.g., datasets in Hamilton et al. (2017))
  and multiple-graph datasets (i.e., a dataset containing multiple graphs, such as those in Dwivedi et al. (2022)).













----

- Block, P., & Grund, T. (2014). Multidimensional Homophily in Friendship Networks*. _Network Science_, _2_(2), 189–212. 
- Dwivedi, V. P., Joshi, C. K., Laurent, T., Bengio, Y., & Bresson, X. (2022). Benchmarking Graph Neural Networks. _Journal of Machine Learning Research_.
- Hamilton, W., Ying, Z., & Leskovec, J. (2017). Inductive Representation Learning on Large Graphs. _Adv. Neural Inf. Process. Syst._, _30_.

### Questions
1. Is $\mathbf{A}$ including self-loops? If not, $\mathbf{A}^K$ or $\hat{\mathbf{A}}$ might not include all $K$-hops neighboring nodes as described in the text.

2. Is it possible to extend the PROP-DGI to multiple graph settings, such as the datasets in Dwivedi et al. (2022)? Any specific reasons that PROP-DGI is only evaluated in transductive setting?



- Dwivedi, V. P., Joshi, C. K., Laurent, T., Bengio, Y., & Bresson, X. (2022). Benchmarking Graph Neural Networks. _Journal of Machine Learning Research_.

### Soundness
2

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
The paper claims that non-parametric propagation is a special form of GCL and outperforms many existing GCN and GCL methods. The authors observe that GCL can effectively learn optimal propagation parameters, leading them to propose PROPGCL, which focuses solely on learning the propagation coefficients.

### Strengths
- Adequate experiments.
- The paper is easy to follow.

### Weaknesses
- The authors claim the PROP is a special GCL because it has an alignment operation between the node and its neighbors. However, the GCL is aligned node with itself on another view, this is different. Moreover, the commonly used infoNCE also includes the comparison part of negative samples. Therefore, I can't entirely agree that PROP is a special GCL.

- The PROP without a transformation matrix means that can not transform the node feature from the feature space to the class space. How to make PROP to make the prediction?
- The PROP form has been proposed in many previous works, such as SGC, PMLP[1], etc. What is the difference between PROP and SGC?

- The details of the proposed method should be provided, such as PROP-GRACE.

[1] Graph Neural Networks are Inherently Good Generalizers: Insights by Bridging GNNs and MLPs

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper makes an interesting observation about graph contrastive learning models. While recent GCL methods have become increasingly complex with sophisticated architectures and designs, the authors demonstrate that simple feature propagation alone can achieve competitive performance. They introduce PROP, a training-free propagation method that simply propagates node features along the graph structure. Despite its simplicity, PROP achieves competitive or even superior performance compared to state-of-the-art GCL methods across various benchmarks, particularly on heterophilic graphs. The authors further deepen their investigation by analyzing existing GCL methods from a decoupling perspective, separating the propagation and transformation components. Their analysis reveals that GCL methods struggle to learn effective transformation weights (performing no better than random), while showing potential in learning propagation coefficients. Based on these insights, they propose PROPGCL, a simplified version that removes transformation layers and only learns propagation coefficients. PROPGCL not only maintains competitive performance but also offers computational advantages.

### Strengths
1. The paper effectively shows an interesting fact that simple propagation can work as well as complex GNN encoders in graph contrastive learning.  

2. The paper's key strength lies in its systematic experimental design, particularly in Section 5.2. Through well-designed ablation studies comparing fixed propagation coefficients, fixed transformation weights, and an all-one baseline, the authors convincingly show that GCL methods can learn good propagation coefficients but struggle with transformation weights.

3. The experimental evaluation is remarkably comprehensive, comparing against diverse GNN architectures including spectral-based models (ChebNetII), spatial-based methods (GCN, GAT), and polynomial variants (GPRGNN, BernNet). Their simple PROP method consistently matches or outperforms these sophisticated architectures, especially on heterophilic graphs. The authors then show that their PROPGCL variants can further improve upon PROP.

### Weaknesses
This paper has a few areas that could be strengthened, primarily in its theoretical analysis.

1. In Section 4.1, where the authors present propagation as a non-parametric learning approach, the theoretical foundation could be more rigorous. The claim that propagation corresponds to gradient descent on Dirichlet energy lacks rigorous mathematical proof, and the cited papers (Zhu et al., 2021a) don't very clearly support this interpretation. The connection between propagation and non-parametric unsupervised learning remains more of an intuitive argument than a mathematically grounded one.

2.  The claim "the propagation operator can also be understood as a special GCL method, where the positive samples are randomly drawn from neighboring nodes" lacks rigorous proof. The authors directly make this connection without formal mathematical justification, and do not explain how propagation's deterministic neighbor aggregation truly corresponds to random sampling of positive pairs in contrastive learning.

3. Theorem 4.1 shows propagation minimizes the alignment loss, this actually corresponds to a mode collapse scenario where all node representations become identical - a situation that contrastive learning typically aims to avoid.

### Questions
1. In Section 4.1, the notation \( x^{+} \) appears in the alignment loss equation. Could you clarify what \( x^{+} \) specifically represents in this context? Explicitly defining this and other notations throughout would enhance clarity and help readers follow your ideas more smoothly.

2. Suggestion: The paper currently presumes familiarity with the standard Graph Contrastive Learning (GCL) pipeline. Including a brief overview of the GCL pipeline in the main text would benefit readers who may not have a deep background in GCL.

3. Suggestion: The computational efficiency appears to be a major advantage of PROP/PROPGCL, but this important result is placed in the appendix instead of main context.

### Soundness
3

### Presentation
3

### Contribution
2
