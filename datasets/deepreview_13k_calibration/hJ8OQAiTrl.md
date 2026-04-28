# Combining Structure and Text: Learning Representations for Reasoning on Graphs

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Effective reasoning on real-world graphs necessitates a thorough understanding and optimal utilization of structural information from graph structure and textual information corresponding to nodes and edges. Recent research has primarily focused on two paradigms: employing graph neural networks to capture structural features and utilizing language models to process textual information, respectively. While these approaches have shown impressive performance, integrating structural and textual information presents significant challenges. To be more specific, concurrently training graph neural networks and language models is particularly challenging, primarily due to the scale of real-world graphs. This paper introduces a novel framework, named CoST, tailored for graph reasoning tasks. The proposed optimization objective enables alternating training of the GNN and PLM, leading to the generation of effective text representations by the PLM model, thereby enhancing the reasoning capabilities of the GNN model. Empirical results demonstrate that CoST achieves state-of-the-art performance across representative benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript introduces CoST (Combining Structure and Text), an advanced framework for graph reasoning that synergistically integrates structural information from Graph Neural Networks (GNNs) with textual data from Pre-trained Language Models (PLMs). The framework employs a novel alternating training mechanism designed to enhance the reasoning capabilities of both GNNs and PLMs when applied to real-world graph datasets. CoST effectively addresses scalability issues and optimizes the learning process by incorporating a variational objective, thus enriching both structural and contextual representations of graph entities. Empirical evaluations demonstrate that CoST achieves state-of-the-art performance across several benchmark datasets, including both homogeneous and heterogeneous graph types.

### Strengths
1. The primary strength of this paper lies in its alternating training framework, which iteratively optimizes both GNNs and PLMs. Unlike conventional approaches that either jointly train both models or concatenate their outputs, CoST introduces a two-stage optimization strategy that allows each model to refine its representations based on the complementary output of the other.

2. The authors conduct extensive experiments on multiple graph reasoning benchmarks. CoST consistently outperforms state-of-the-art baselines. The empirical results show significant improvements, validating the model's effectiveness across diverse datasets and various graph topologies.

### Weaknesses
1. Limited LLM Backbone Evaluation: The paper only utilizes MiniLM as the LLM backbone for the PLM component. To demonstrate the broader applicability of the proposed framework, additional experiments using prominent LLMs, such as llama, should be conducted. This would help ascertain whether the alternating training approach and the integration mechanism are generalizable across different LLM architectures. Furthermore, the choice of MiniLM, while efficient, might not fully capture the complex semantic nuances that larger models could potentially leverage, thus limiting the performance ceiling of the proposed approach.

2. Complexity of Training Paradigm: The alternating training paradigm, while effective, introduces considerable complexity in both model implementation and hyperparameter tuning. The generation of pseudo-targets by GNNs, coupled with the alternating nature of updates between GNN and PLM, results in multiple hyperparameters, complicating reproducibility. The paper lacks a detailed sensitivity analysis of these hyperparameters, particularly regarding the learning rates for the GNN and PLM during each alternating phase, which could significantly impact convergence and final performance. The practical challenges of implementing and tuning this complex training regime are not sufficiently addressed.

3. Questions Regarding Pseudo-Target Method: The pseudo-target method is central to the alternating training paradigm in CoST, yet certain aspects remain under-explored. Specifically, why are particular pseudo-targets selected, and how does their quality influence the overall model performance? Are there explicit criteria guiding the selection of pseudo-targets, and how is their quality evaluated to ensure they are beneficial for PLM training? The paper does not provide a clear explanation of the sampling strategy for pseudo-targets, nor does it discuss the potential for noisy or misleading pseudo-targets to negatively impact the PLM's learning process. Clarifying these points would improve the understanding of how pseudo-targets contribute to model robustness and effectiveness.

### Questions
1. Why was MiniLM chosen as the LLM backbone? Could you experiment with other widely-used LLMs, such as llama, to demonstrate the generalizability of the approach?

2. Further Explanation of Pseudo Targets: The concept of using pseudo-targets from GNN predictions is innovative, yet it remains unclear how sensitive the model's performance is to the number of pseudo-targets chosen. Would varying the number of pseudo-targets significantly affect the model's performance? What criteria are used to select these pseudo-targets, and how is their quality assessed during training? Additional analysis on these questions could provide deeper insights into the robustness of the pseudo-target strategy.

3. Can you include a comparison with similar GNN+LLM works such as LinkGPT on additional benchmarks, as shown in Tables 3 and 4?

### Soundness
2

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
3

### Summary
This article proposes a new optimization method tailored for the combination of GNNs and PLMs. This work is motivated by an ICLR 2023 paer titled "GLEM - Learning on Large-scale Text-attributed Graphs via Variational Inference in ICLR 2023".
In this article, the authors conduct multiple sets of experiments on graph datasets from various domains, with the experimental conclusions validating the effectiveness of their new method in graph search-related problems.This new optimization method outperforms traditional graph structure (Struct)-based methods, PLM-based methods, and some mainstream methods combining GNNs and PLMs across four mainstream models.

### Strengths
This article is well written with clear presentation of the new optimization method, and their experiments are rigorous  with repeatability.

### Weaknesses
Overall, this paper may represent a significant algorithmic contribution, but it requires supplementing some theoretical details in the article:
- In the proof of Theorem 2.1 (Equation 13), the derivation of the last equality lacks detail. It requires a detailed elaboration on how the prefix $\mathbf{E}$ is added to the first term and why the second term lacks a $\mathcal{E}$ compared to the description in Theorem 2.1. Could you provide a step-by-step derivation of the last equality, specifically explaining the addition of the expectation operator to the first term and the absence of it in the second term? This would help clarify the mathematical reasoning behind Theorem 2.1.

### Questions
1. Supplementary figures are needed. Could you could include a flowchart or diagram that shows the step-by-step process of how a query is processed through the PLM and GNN components of the CoST framework? This would enhance the reader's understanding of the model's architecture and operation.
2. In Table 2 and Table 3, $H@1$ is only computed for the AmazonSports, AmazonClothing, MAGGeology, and MAGMath datasets, while $H@10$, $H@50$, $H@100$ are only computed for the CitationV8 and GoodReads datasets. Could you explain the rationale behind choosing these specific metrics for each dataset, and whether this choice affects the comparability of results across datasets?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to combine structure and text information for solving reasoning tasks on graphs. The authors propose CoST, a framework that employs graph neural networks (GNNs) to capture structural features and pretrained language models (PLMs) to capture textual features respectively. Since it is challenging to jointly optimize the GNN and PLM, the authors leverage the variational lower bound of the joint objective and optimize the GNN and PLM in a cyclical manner. The authors demonstrate the effectiveness of CoST on 9 datasets, including both homogeneous and heterogeneous graphs. CoST outperforms both GNN-based and LLM-based methods that only uses information from a single modality.

### Strengths
- This paper studies the problem of combining structure and text, which is a general and important problem in the community of graph representation learning.
- The proposed CoST has clear motivations from variational Bayesian perspective.
- CoST provides robust performance gain over a wide range of datasets and several base models. The empirical contribution is solid and likely to be applicable to other models and datasets.

### Weaknesses
 - The position and the contribution of this paper is not very clear. Combining structure and text has been widely studied in the context of text-attributed graphs (TAGs) [1, 2], and I don’t think the setting of this paper is a contribution given its similarity to TAGs. Regarding the proposed CoST, several papers have used the same idea of variational EM algorithm to optimize two models capturing two views of graphs [3, 4, 5]. There is scarcely any novelty for the proposed method.
- It is not very fair to compare CoST against GNN-based and LLM-based methods that only use features from one modality. Based on this comparison, we can only conclude that combining two modalities is effective, which is a known lesson in many machine learning domains. We can’t conclude that CoST is an advanced method for combining two modalities. The authors should compare CoST against some baselines (e.g. [1]) that fuse structural and textual information for graph reasoning.
- The abstract and introduction are not well written. The authors focused too much on the setting of combining structure and text, which is important but not a big challenge in the community. I recommend the authors to rethink the challenges in this setting and discuss more about how their method technically solves the challenges. The authors may also remove Figure 1, as it is not related to the challenges.

### Questions
- In Equation 3, how do you define the probability over an answer set $O_{(h, r)}$? Equation 1 & 2 only define the probability over a single answer.
- How to understand the meaning of the latent variable $H_{(h, r)}$? It looks like $V_{/O(h, r)}$ excludes the ground truth answers from all entities. How can you call it the candidate target node set for the query (h, r, ?)?
- Equation 10 should be log probabilities, not probabilities.
- Why do you omit $H_{(h, r)}$ in $p_\phi$ in the second line of Equation 10?
- Line 461 - 463: I understand CoST pretrained GNN only uses structural information. How do language models come up here?
- $t$ in Equation 12 doesn’t need to be bold.
- It’s a little bit complicated for CoST to use two optimization stages. Is there any reason for not using a mixed objective of pseudo labels and ground truth like in [5]?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a comprehensive framework that addresses the challenges associated with processing graph data by combining both structural attributes (the connections between nodes) and textual information (node labels or node descriptions). The paper aims to improve the performance of various graph-based reasoning tasks, including link prediction, node classification, and knowledge graph completion. These models are trained on large datasets to learn representations that can effectively distinguish between different nodes based on their structural position within the graph and their associated text features.

### Strengths
1. The paper is well-structured, making it accessible to both researchers and practitioners in the field. It provides clear explanations for complex concepts and algorithms, supported by illustrative examples that aid understanding.

2. The clarity of the paper is good. The authors use appropriate terminology throughout the document, making it accessible to researchers with a background in machine learning and graph theory.

### Weaknesses
1.  It would be beneficial to provide a detailed description of the experimental setup, including data preprocessing steps, model configurations, hyper-parameters tuning process, and any specific challenges encountered during implementation. 

2. The authors could include a more detailed discussion on model evaluation metrics that specifically address the integration of structure and text.

### Questions
How much do hyperparameters affect the method proposed in this work?

### Soundness
3

### Presentation
3

### Contribution
3
