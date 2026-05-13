# FIMP: Foundation Model-Informed Message Passing for Graph Neural Networks

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
Foundation models have achieved remarkable success across many domains, relying on pretraining over vast amounts of data. Graph-structured data often lacks the same scale as unstructured data, making the development of graph foundation models challenging. In this work, we propose Foundation-Informed Message Passing (FIMP), a Graph Neural Network (GNN) message-passing framework that repurposes existing pretrained non-textual foundation models for graph-based tasks. We show that the self-attention layers of foundation models can effectively be leveraged on graphs to perform cross-node attention-based message-passing. Our model is evaluated across diverse domains on image networks, single-cell RNA sequencing, and fMRI brain activity recordings in finetuned and zero-shot settings. FIMP outperforms strong baselines, demonstrating that it can effectively leverage state-of-the-art foundation models in graph tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce Foundation-Informed Message Passing (FIMP), a novel message-passing framework designed to leverage pretrained non-textual foundation models for graph neural networks (GNNs). 
Unlike existing GNNs, which utilize a single embedding for nodes, FIMP represents nodes as sequences of feature tokens. 
This enables cross-node attention-based message-passing using the self-attention layers from pretrained models. 
The proposed method is evaluated on tasks across image networks, spatial transcriptomics, and fMRI brain activity recordings, showing significant improvements over baseline GNNs. 
Additionally, FIMP demonstrates zero-shot capabilities on image classification tasks using pretrained ViT.

### Strengths
I think it seems like the authors are trying hard to emphasize how FIMP is fundamentally different from existing attention-based GNNs like GATs and graph transformers. The statement with boldface might indicate that they have faced challenges in communicating the novelty of their work or distinguishing it from prior approaches in earlier submissions.
**However, in my opinion, this research is both timely and important because it aligns well with the current era of foundation models dominating various domains like NLP, computer vision, and even biomedicine.**
Existing foundation models excel with unstructured data (like text and images), but applying them directly to graph-structured data is challenging. 
FIMP addresses this gap by allowing foundation models pretrained on unstructured data to be repurposed for graph-based tasks through its innovative tokenization and message-passing approach.
The authors provide comprehensive evaluations across diverse datasets, demonstrating that FIMP outperforms existing GNN models like GCN, GraphSAGE, and GATs. Notably, FIMP with pretrained models (e.g., scGPT and BrainLM) achieves the best results in gene expression prediction and brain activity reconstruction.
The zero-shot embedding experiments on the Mapillary image dataset highlight FIMP's ability to leverage pretrained foundation models without additional training, which is a significant advantage in scenarios where labeled graph data is scarce.

### Weaknesses
- While I acknowledge the novelty and potential impact of the research direction taken in this work, I must also express some concerns. The proposed module, despite its creative approach (direction), appears somewhat simplistic in its current form. It would benefit greatly from a deeper theoretical analysis to clarify why the architecture is effective and how it fundamentally differs from existing methods. This would not only strengthen the authors’ claims but also provide a clearer understanding of the model’s underlying principles.



- I noticed that while the paper benchmarks against various GNNs, it does not include comparisons with several main baselines (non-foundation models) that are well-established within each specific domain. Is there a particular reason why these comparisons were omitted? Including these baselines would provide a more comprehensive evaluation and help validate the effectiveness of FIMP beyond the GNN-specific context.


- I would like to address the reporting of experimental results. The performance metrics are averaged over five runs, but it is unclear if this number of repetitions is statistically sufficient to ensure robust conclusions, especially given the variability in results. For example, in the Mouse Embryo cell type classification task, the reported standard deviations appear quite significant. Increasing the number of runs or providing a justification for why five is adequate would enhance the reliability of the reported outcomes.


- (minor) Additionally, regarding the reference to Graph Transformer Networks (GTNs) on line 803, I believe there might be a mischaracterization of the original work by Yun et al. (2019). The GTNs discussed in that paper are not graph transformers in the sense typically understood in this context. Instead, they are better described as a graph-adapted version of Spatial Transformer Networks [1]. As stated by Yun et al.:
> Yun et al. (2019): "GTNs can be viewed as a graph analogue of Spatial Transformer Networks which explicitly learn spatial transformations of input images or features."

[1] M. Jaderberg, K. Simonyan, A. Zisserman, et al. Spatial transformer networks. In Advances in neural information processing systems, pages 2017–2025, 2015.

### Questions
please see the above section.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper incorporates pre-trained LM for cross-node message creation for a non-textual graph neural network. To this end, it tokenizes each node's content into a sequence and employs self-attention between sequences from pairs of nodes. Evaluations on genomics, brain, and street-view images demonstrate its effectiveness.

### Strengths
1. The writing and organization are good. The presentation is easy to follow.2. 
2. The proposed methods can be applied to many fields. 
3. Experimental evaluations from different fields demonstrate its effectiveness.

### Weaknesses
1. The novelty is very limited. The proposed method is the extension of attention in GAT to non-textual node content. This aims at jointly considering source and target nodes for message passing. However, this is not novel.
2. The proposed method lacks clear motivation. It is direct for non-textual node content. Thus, the significance is weak. It is not clear why the cross-node attention can improve the performance. 
3. The evaluations are not convincing. Only the GNN baselines are compared. Besides, it is not clear how the node attribute is constructed for GNNs. How about using the embedding from LM as the node’s attribute?
4. Figure 3 lacks a description in the main body.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a message-passing framework that leverages pretrained non-textual foundation models for graph-based tasks. The proposed method, FIMP, aligns node tokenization in Graph Neural Networks with tokenization schemes used by foundation models, allowing for more granular feature-level interactions during message passing. The authors demonstrate FIMP's effectiveness across diverse domains, including image networks, single-cell RNA sequencing, and fMRI brain activity recordings, showing improvements over strong baselines and highlighting the potential of repurposing non-textual foundation models for graph tasks.

### Strengths
1. The expression is very fluent. Readers can easily understand the content of the work.

1. The study of graph foundation models and large graph models is very meaningful.

1. The paper demostrates FIMP outperforms traditonal GNN models on image networks, single-cell RNA sequencing, and fMRI brain activity recordings. FIMP can effectively leverage SOTA foundation models in graph tasks.

### Weaknesses
1. The algorithm proposed in this paper appears to be incremental. Although the paper discusses the differences from works like GAT, in essence, it merely transforms node features from vectors($x_v \in \mathbb{R}^d$) to matrices($x_v \in \mathbb{R}^{f \times d}$). This transformation, while allowing for feature-level attention, doesn't fundamentally alter the message-passing paradigm. The core mechanism remains aggregating and transforming node features, similar to existing GNNs, but with increased computational complexity due to the matrix representation.

2. The current experiments are limited to image networks, single-cell RNA sequencing, and fMRI brain activity. It is unclear whether this method is effective in other domains, especially traditional graph datasets. The paper lacks a clear justification for why these specific domains were chosen, and it's not evident that the proposed method would generalize well to other graph structures with different characteristics. The absence of experiments on standard graph benchmarks like OGB is a significant gap, making it difficult to assess the method's broader applicability.

3. As shown in Table 1, the gene expression prediction results on the mouse hippocampus and human heart spatial transcriptomics datasets, FIMP + scGPT performs much better than FIMP-base and FIMP + ViT. This indicates that to unleash the potential of the FIMP algorithm, a suitable and powerful foundation model is needed. However, in many scenarios, there may not be powerful foundation models available. Pretraining a suitable foundation model from scratch is also expensive and challenging. This dependence on task-specific and powerful foundation models limits the practical application of FIMP, especially in domains where such models are not readily available or are computationally prohibitive to train.

### Questions
The practical application of traditional GNNs is hampered by a significant computational burden. As shown in Figure 6, the time cost of FIMP is twice that of traditional GNNs. This concerns me about the practical value of FIMP. I would like to see a comparison of F1-Score and consumed time between FIMP + ViT and the ViT model alone on image classification dataset. I also hope to see the training time expenditure of FIMP on larger graph datasets.

In summary, if the authors can address my concerns, I would be open to increase my score.

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
4

### Summary
The paper introduces FIMP, a framework that adapts pretrained non-textual foundation models for graph-based tasks. FIMP repurposes existing pretrained non-textual foundation models for message-passing on graphs. FIMP is evaluated across diverse domains, such as image classification, spatial transcriptomics, and fMRI brain activity recordings, utilizing state-of-the-art foundation models like ViTs, scGPT, and BrainLM. It demonstrates competitive performance in a zero-shot setting for embedding image networks, achieving notable results without task-specific retraining.

### Strengths
1. The concept of leveraging pretrained foundation models for message passing in GNNs is innovative. This approach shows how pretrained knowledge can inform finer-grained interactions in graph structures.
2. The suggested method achieves improvements over the discussed baselines.

### Weaknesses
1. The paper is not easy to follow, with several concepts and sections lacking clarity (see questions below).
2. While the idea of integrating pretrained foundation models with MPNNs is interesting, the proposed approach is overly simplistic (a straightforward approach -- if I understood correctly –- see questions below). Simplicity in methodology is not inherently problematic in my opinion; however, the combination of simplicity with a lack of a clear motivation for addressing the problem raises concerns — see Weakness 4 for further details.
3. The experimental results are not entirely convincing, as the baselines used for comparison (e.g., GCN, GAT) are somewhat outdated. It would strengthen the paper to include comparisons with more recent state-of-the-art graph learning (e.g.,  GRIT [1]) methods that could offer a more rigorous benchmark for evaluating FIMP's performance.
4. In my opinion, the paper lacks sufficient motivation. The tasks presented appear to be crafted primarily to emphasize FIMP’s strengths, rather than addressing meaningful, real-world applications. If I understand correctly, the authors construct a graph from publicly available datasets (e.g., the Mapillary image dataset). For example, line 173 states: “images form a geographical proximity graph.” However, this implies that the method is evaluated exclusively on datasets where the graphs were constructed by the authors, and these graphs are not publicly accessible.
To strengthen the paper, the authors can either (1) provide a compelling rationale for how such a setting could arise naturally in real-world scenarios, or (2) identify and utilize publicly available datasets that align with their setup.

### Questions
1. Lines 191-193: "By aligning the tokenization in FIMP with the tokenization scheme of pretrained foundation models, we reduce distribution shift in token representation when applying these models to graph-structured data." Does this mean that you are directly adopting the tokenization strategy of the pretrained foundation model? Clarification on how closely you follow the original tokenization would be helpful.
2. In Algorithm 1, which of the weights are learned from scratch, and which are (possibly) borrowed from the pretrained foundation model? A clearer distinction between learned and reused weights would improve understanding.
3. How does FIMP-base specifically leverage the knowledge embedded in a foundation model? From what I understand, given lines 251-253: “In its base formulation, cross-attention message passing can be done with a simple cross-attention mechanism which is learned from scratch during training. We denote this base version of our architecture as FIMP-base in our experiments.”, the knowledge transfer in this case occurs primarily through the tokenization process. 
4. On the FIMP versions that rely on a foundation model’s weights in the cross attention, It seems unclear how effective using the pretrained weights of a foundation model would be, given that cross-node attention differs from what the foundation model encountered during training (e.g., ViTs typically see only single images per training step). Could you elaborate on how the cross-node attention mechanism adapts to this discrepancy? Or did it just appear to work well in practice?

**References**:

[1] Graph Inductive Biases in Transformers without Message Passing. Ma et. al. 2023

### Soundness
3

### Presentation
2

### Contribution
2
