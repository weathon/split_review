# Curriculum GNN-LLM Alignment for Text-Attributed Graphs

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Aligning Graph Neural Networks (GNNs) and Large Language Models (LLMs) benefits in leveraging both textual and structural knowledge for Text-attributed Graphs (TAGs) learning, which has attracted an increasing amount of attention in the research community. Most existing literature assumes a uniformly identical level of learning difficulties across texts and structures in TAGs, however, we discover the $\textit{text-structure imbalance}$ problem in real-world TAGs, $\textit{i.e.}$, nodes exhibit various levels of difficulties when learning different textual and structural information. Existing works ignoring these different difficulties may result in under-optimized GNNs and LLMs with over-reliance on either simplistic text or structure, thus failing to conduct node classifications that involve simultaneously learning complex text and structural information for nodes in TAGs. To address this problem, we propose a novel Curriculum GNN-LLM Alignment ($\textbf{CurGL}$) method, which strategically balances the learning difficulties of textual and structural information on a node-by-node basis to enhance the alignment between GNNs and LLMs. Specifically, we first propose a text-structure difficulty measurer to estimate the learning difficulty of both text and structure in a node-wise manner. Then, we propose a class-based node selection strategy to balance the training process via gradually scheduling more nodes. Finally, we propose the curriculum co-play alignment by iteratively promoting useful information from GNNs and LLMs, to progressively enhance both components with balanced textual and structural information. Extensive experiments on real-world datasets demonstrate that our proposed $\textbf{CurGL}$ method is able to outperform state-of-the-art GraphLLM, curriculum learning, as well as GNN baselines. To the best of our knowledge, this is the first study of curriculum alignment on TAGs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces curriculum GNN-LLM alignment to tackle the text-structure imbalance problem in learning on text-attributed graphs. It proposes a node-wise difficulty measurer, a class-based node selection strategy, and a curriculum co-play alignment to balance and enhance learning between GNNs and LLMs. Extensive experiments show CurGL outperforms selective existing models on the classic node classification task across five well-known datasets.

### Strengths
- The motivation to balance the role of LLMs and GNNs in a fine-grained sample-wise manner for TAG learning is straightforward and convincing.
- Writing is clear and easy to follow. Pseudo code is present to assist better understanding of the mechanisms designed.

### Weaknesses
 - Novelty. The E-M training between LLMs and GNNs has been explored by a handful of pioneer works, e.g., SimTEG and GELM. The proposed CurGL enhances such framework by adding additional strategies for balancing the LLM and the GNN.
- Unclear and potentially unfair experimental setting for baseline llm-as-predictor models. Is is unclear that how are the llm-as-predictor models testified, especially in Table 1. Is is based on a zero-shot manner as in Glbench, or are they also trained with the same training set? In terms of training, is it training-from-scratch or fine-tuning?
- Lack of discussion of a very relevant work, GraphGPT: Graph Instruction Tuning for Large Language Models.
- The proposed CurGL relies heavily on the availability of training data, and shows poor potential in transferring learning and zero-shot generalisation. Although it leverages an LLM for textual-based learning, the design of node-wise difficulty measurer and class-based selection strategy requires high-quality labels for the model to learn and converge. While it is quite reasonable for a graph learning model, the trained CurGL cannot be adapted to unseen data (unlike LLaGA, OFA and others), making its potential application quite narrow.
- Can CurGL generalise beyond node classification, to link prediction or graph classification?

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a method called Curriculum GNN-LLM Alignment designed for Text-Attributed Graphs (TAGs). The goal is to address the text-structure imbalance problem in TAGs, where nodes have varying levels of difficulty in learning textual and structural information. The CurGL approach progressively balances these difficulties through three key modules.

### Strengths
1.	The integration of node difficulty into node classification is clearly motivated and engaging.
2.	The presentation is well-organized, and the ablation study clearly demonstrates the impact of each technique.

### Weaknesses
1.	My primary concern is whether this method is effective for heterophilic graphs, as the proposed difficulty measurer seems tailored to homophilous graphs.

2.	The class-based node selection assumes balanced class sampling within each subgraph. However, this assumption may be problematic for highly imbalanced datasets, potentially leading to biased or suboptimal node selection.

3.	Related to the above, it’s unclear how the authors handle edges between selected nodes in the class-based node selection. In each subgraph, nodes from different classes are sampled proportionally, which does not guarantee connectivity among them.

4.	Another major concern is computational overhead. This method involves additional steps beyond GLEM, which already has considerable running time[1]. Efficiency analysis is essential and appears missing from the experimental section.

5.	The performance appears insufficiently strong; for instance, the results on Arxiv are weaker than those of methods like LEADING[2]. Larger datasets, such as ogbn-products and ogbn-papers100M should also be included.

6.	The paper’s claim of using LLMs seems overstated, as small language models are used. To solve this obvious mismatch and align claims with experiments , it would be more appropriate to use models like LLAMA or GPT.

7.	It is unclear if this approach generalizes to tasks beyond node classification, such as link prediction and graph classification. Focusing solely on node classification may limit the overall contribution.

8.	I am curious why GLEM achieves strong performance on Cora and Pubmed, which have very few labels. The results seem inconsistent with findings from existing works[1].

9.	Similar to GLEM, this method relies heavily on the quality of pseudo-labels. Although an ablation study is provided, it does not fully address potential issues that could arise with low labeling ratios.

### Questions
1. How does the implementation achieve sampling of simpler nodes first?
2. Are the pretrained language models in the third block in Table 1 fine-tuned with labels?

### Soundness
1

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
This paper tackles the text-structure imbalance problem in representation learning on text-attributed graphs. The authors propose a curriculum GNN-LLM alignment method to balance the learning difficulties of textual and structural information.

### Strengths
The paper is clearly written and easy to follow.

The proposed method demonstrates improved performance.

### Weaknesses
The novelty of this paper is incremental. It is evident that the ideas of difficulty measurement and curriculum learning are borrowed from existing works, such as [1,2]. Additionally, using loss as a measure of learning difficulty is a well-adopted approach.

The authors emphasize the text-structure imbalance problem, i.e., the learning difficulties of different nodes vary depending on textual attributes and topological structures. However, they provide only an intuitive example in figure 1 to illustrate this issue, without presenting real experimental results to substantiate the existence of this problem.

In Table 1, it is unusual that SOTA methods perform worse than the baseline GCN. An explanation for this unexpected phenomenon is needed.

What is the computational efficiency of the proposed model? Calculating node difficulty involves computing shortest paths between nodes, which increases computational complexity and may limit the model’s applicability to large-scale datasets.

The integration of curriculum learning into the training stage is unclear. According to Algorithm 2, the training process appears closely similar to that of the existing method [2].

The mathematical representation of equations and loss functions lacks clarity. For example:

   a. In Eq. (1), what does "MLP" represent? Is it a large language model or a multi-layer perceptron?  
   b. What is the relationship between $\hat{y}$ and $f_\theta(S)$? Are they equal?  
   c. In Eq. (6), there is no $y_v$. What does $1$ represent? Is it a column vector or a scalar? Additionally, if $D_t$ is larger, does this imply that the loss is also larger?

### Questions
Does selecting nodes with lower difficulty improve classification accuracy on nodes with higher difficulty?

### Soundness
3

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
3

### Summary
This paper presents CurGL, a curriculum-based alignment method for Text-Attributed Graphs that introduces a text-structure difficulty measurer, a class-based node selection strategy, and curriculum co-play alignment to iteratively enhance Graph Neural Networks and Large Language Models. The experiments demonstrate the superiority of the method.

### Strengths
- The writing is fluent and easily comprehensible.
- It is one of the earliest works to apply Curriculum Learning in the field of TAGs.
- The authors propose a class-based hard node selection strategy and a text-structure difficulty measurer, which serve as an inspiration for the community.

### Weaknesses
 - There is a lack of explanation and mathematical proof as to why the EM algorithm is used instead of updating the model parameters of LLM and GNN simultaneously.
- The experiments in this work are insufficient, as they only include node classification experiments without covering graph classification or link prediction. Additionally, I have some concerns about the current experimental results, see below.
- The selection of the \(\lambda\) and \(\alpha\) values lacks sufficient justification. The optimal values seem to vary significantly between datasets (Cora and Citeseer in Figure 4), suggesting a potential sensitivity to dataset characteristics that is not well addressed. The paper does not provide a clear methodology for determining these hyperparameters, which could limit the practical applicability of the method.
- In section 4.4, the observed decrease in accuracy of pseudo-labeled nodes selected by CurGL as the number of steps increases is concerning. While the authors provide an explanation, it is not clear if this decrease indicates a fundamental limitation of the method or a potential issue with the selection process. The paper should explore this phenomenon more deeply and discuss its implications.
- In Section 4.5, the opposite trends exhibited by the LLM and GNN components across different datasets are not adequately explained. The paper should provide a more detailed analysis of why the performance of these components varies so differently across datasets, and what this suggests about the method's robustness and generalizability.
- In the main results, it is surprising that a simple GCN outperforms models like TAPE and ENGINE. This raises questions about the effectiveness of the proposed method compared to simpler baselines and the overall experimental setup.

### Questions
1. Could the authors provide more insights into the selection of the $\lambda$ and $\alpha$ values? For different datasets (Cora and Citeseer in Figure 4), they seem to require different values.
2. In section 4.4, why does the accuracy of pseudo-labeled nodes selected by CurGL decrease as the number of steps increases?
3. In Section 4.5, why do both of the two components, LLM and GNN, exhibit opposite trends across different datasets?
4. In the main results, it seems that a simple GCN outperforms models like TAPE and ENGINE.

### Soundness
1

### Presentation
3

### Contribution
2
