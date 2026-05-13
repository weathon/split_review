# UMMAN: UNSUPERVISED MULTI-GRAPH MERGE ADVERSARIAL NETWORK FOR DISEASE PREDICTION BASED ON INTESTINAL FLORA

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
The abundance of intestinal flora is closely related to human diseases, but diseases are not caused by a single gut microbe. Instead, they result from the complex interplay of numerous microbial entities. This intricate and implicit connection among gut microbes poses a significant challenge for disease prediction using abundance information from OTU data. Recently, several methods have shown potential in predicting corresponding diseases. However, these methods fail to learn the inner association among gut microbes from different hosts, leading to unsatisfactory performance. In this paper, we present a novel architecture, \textbf{U}nsupervised \textbf{M}ulti-graph \textbf{M}erge \textbf{A}dversarial \textbf{N}etwork (UMMAN). UMMAN can obtain the embeddings of nodes in the Multi-Graph in an unsupervised scenario, so that it helps learn the multiplex association. Our method is the first to combine Graph Neural Network with the task of intestinal flora disease prediction. We employ complex relation-types to construct the Original-Graph and disrupt the relationships among nodes to generate corresponding Shuffled-Graph. We introduce the Node Feature Global Integration (NFGI) module to represent the global features of the graph. Furthermore, we design a joint loss comprising adversarial loss and hybrid attention loss to ensure that the real graph embedding aligns closely with the Original-Graph and diverges from the Shuffled-Graph. Comprehensive experiments on five classical OTU gut microbiome datasets demonstrate the effectiveness and stability of our method. (We will release our code soon.)

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new unsupervised graph neural network architecture called UMMAN for predicting diseases based on intestinal flora data. The key ideas are: 1) Construct multi-graph representations of the flora-host relationships using different similarity metrics. 2) Introduce an adversarial training scheme that makes the model embeddings agree with the true graph while disagreeing with a shuffled graph. 3) Propose a two-stage Node Feature Global Integration module to characterize both local node and global graph features. Experiments show state-of-the-art performance on multiple disease datasets compared to previous methods.

### Strengths
- Novel application of graph neural networks to microbiome disease prediction, allowing the model to learn relevant flora-host relationships.
- Interesting adversarial training approach with shuffled graphs as a regularization method.
- Thorough experiments demonstrating superior performance over existing techniques on multiple datasets.

### Weaknesses
- The proposed adversarial training scheme seems a bit ad-hoc. More analysis could be provided on why this particular approach is effective.
- Ablation studies only evaluate the contribution of individual components; would be good to see the ablation of a full adversarial training scheme.
- More discussion could be provided on the choice of graph construction methods.

### Questions
- How dependent is the performance on the specific graph construction techniques used? Have other graph representations been explored?
- Is the adversarial training approach specifically tailored for this problem setting, or does it represent a more general regularization technique?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study for a practical problem, the intestinal flora disease prediction task, which predict disease through abundance information of gut microbes.

The major challenge of this task is that there is a multiplex and implicit connection between gut microbes and hosts, which makes the task difficult if only using the abundance information. In light of this challenge, the authors propose a method UMMAN which combines graph neural network to help learn the association between gut microbes and hosts.

Original-Graphs, are constructed by using multiple relation-types, and then utilized to update the embedding of nodes through Graph Convolutional Networks. Attention mechanism is also introduced to update the embeddings of the corresponding nodes of the Multi-Graphs.

Then the relationship among nodes of the Original-Graph is destroyed to get the corresponding Shuffled-Graph, which will be used for adversarial learning to obtain the correlation among nodes more reliably. The authors design the adversarial control group, i.e., keep the position of the edges unchanged, and randomly disrupt the nodes to train part of the discriminator at the same time.

In addition, the authors introduce the Node Feature Global Integration (NFGI) to describe a more comprehensive embedding of the graph with node-level stage and graph-level stage.

### Strengths
The idea of introducing GNN for the intestinal flora disease prediction task by learning the inner association between gut microbes and hosts is new to the field.

### Weaknesses
1. Technical contribution is a bit marginal as both the applied model and the idea of contrast learning are somehow take-off-shelf.

2. The motivation for applying GNN needs to be clearly explained i.e. why the columns in the tabular dataset are transformed into the nodes on a graph? Specifically, it is not very clear why some microbes are considered to be more correlated with each other and that they should be connected by an edge on a graph. The paper only provides a simple claim that two nodes are considered to be connected if the distance between their embeddings is below a variable threshold. It would be better if the authors could provide more details to illustrate the motivation. Moreover, as introducing graph machine learning to the field is one of the main contributions, it would be better if the authors could provide more details and instructions on the embedding process. For example, what are the features taken into consideration, the abundance level, the microbes' class, or anything else?

3. The motivations of the proposed method (especially for Shffuled-Graph and NFGI) need to be clearly and explicitly explained. For example, it is not well motivated why we need to perturb the original graph by exchanging nodes.

For the claim that ‘basic CNNs can't beat the traditional machine learning algorithm in this case (OTU datasets that are extended to table types) because the basic CNN’s kernel cannot learn arbitrary transformed features, which is not suitable for OTU datasets,’ it would be better for the authors to provide more details about the logic chain and explain what is meant by "arbitrary transformed features" in the context of OTU datasets.
Similarly, it would be better to tell more about why exchanging the column order in the tabular dataset will not affect the final result.In the introduction, it is mentioned that 'The exchange of rows and columns of the datasets do not affect the results of pattern recognition.'The authors should explain why this property is not desired i.e., why the authors desire to affect the results of pattern recognition by exchanging the rows and columns of the datasets and how it motivated them to propose their method.

For the proposed Shuffled-Graph, the motivation should also be explicitly illustrated. E.g., why some microbes are considered to be more correlated with each other, and what is the benefit of perturbing this kind of correlation? Why the Shuffled-Graph generated by breaking the correlation among nodes can be used as the negative adversarial control group, and why does such an adversarial learning method work?  It would be better for the authors to add proper references or experiments to support the claim that such perturbation should work.
Moreover, for NFGI, why such a component is desired, and why do the authors design such a proposed graph-level stage instead of other graph-level operations such as pooling?

4. It would be better if the authors could provide more details of the proposed methods, especially those of core contributions. E.g., how the K bins are chosen and decided for the GLD in NFGI.

5. What is the 'true embedding', and how can it 'includes the complex and implicit relationship between gut microbes and hosts'?

### Questions
1. How the existing works conducted on the tabular data can be introduced in the Related Works with more details. E.g., what a typical tabular data look like? A figure with a few columns and rows from the tabular data should be enough

2. The motivations of any proposed method should be clearly and explicitly explained instead of just telling the reader how or what to do with the proposed method. Even some toy examples can provide a more comprehensive introduction for readers.

3. Some notations appear in the equations for the first time and are not mentioned in the text. It would be better if the authors could align them with the text, e.g., H(which should align with ‘global embedding obtained by NFGI’) in eq11 and P(which should align with ‘global embedding matrix of real graph’) in eq12.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper firstly proposes a framework to model the gut microbiota disease prediction as a graph-level prediction task. The idea is to formulate multi-graphs to represent the multiplex connection between gut microbes and hosts, then a novel (problem-specific) graph learning architecture named UMMAN is proposed to generate the graph embedding. In UMMAN, GCN is utilized within each multi-graph to generate node embeddings and a novel readout function NFGI is proposed to generate the graph embedding corresponds to the multi-graph, then the attention mechanism is applied among multi-graphs. UMMAN is trained in an unsupervised manner.

### Strengths
Recently, graph neural networks (GNNs) have achieved impressive performance in various bioinformatical applications including drug discovery [1,2], Protein-Protein Interaction prediction (PPI) [3], molecular design [4], etc. This paper extends the applicability of GNNs to gut microbiota disease prediction and proposes a relevant unsupervised GNN named UMMAN. Experimental results demonstrate that UMMAN can beat previous machine learning models in the field, making it a pertinent and valuable research topic. 

I would recommend the authors to add more discussion of the recent successes of GNNs in the context of bioinformatics in the introduction section to improve the manuscript.


[1] Wang, J.; Liu, X.; Shen, S.; Deng, L.; Liu, H. DeepDDS: deep graph neural network with attention mechanism to predict synergistic 601 drug combinations. Briefings in Bioinformatics 2022, 23, bbab390.

[2] Dong, Z.; Zhang, H.; Chen, Y.; Payne, P.R.O.; Li, F. Interpreting the Mechanism of Synergism for Drug Combinations Using Attention-Based Hierarchical Graph Pooling. Cancers 2023, 15, 4210. https://doi.org/10.3390/cancers15174210

[3] Zitnik, M., & Leskovec, J. (2017). Predicting multicellular function through multi-layer tissue networks. Bioinformatics, 33(14), 190-198.

[4] Olivecrona, M., Blaschke, T., Engkvist, O., & Chen, H. (2017). Molecular de-novo design through deep reinforcement learning. Journal of cheminformatics, 9(1), 48.

### Weaknesses
1. The presentation of the paper should be significantly improved. For instance,

   (1) In the last paragraph in page 5, 'On the wholethe function $\mathcal{G}$ denotes the embedding of the graph ...', delete 'the'.

   (2) In the same paragraph, 'Let {$x^{∗}_{j}$} _{j=1,2..,n} be the each center of the histogram bins', replace n with K (number of bins)

   (3) The description of 'Graph-Level stage' in NFGI is unclear. 

   (4) In function 11, $\mathcal{T}$ and $H^{(t)}$ are not clearly defined.

   (5) The definitions of Original-Graph and Shuffled-Graph is not very clear. It is better to provide formal definitions.

   (6) ...

2. The objective of the design of NFGI is unclear. Since the sum of node embeddings is a widely used graph-level readout function, both the node level stage/descriptor (NLD) and graph level stage/descriptor (GLD) are used to summarize extracted node embeddings to a graph-level vectorial representation. 

3. The experiment section is not very sound. Recent SOTA (state-of-the-art) expressive GNN baselines are not included. Since the gut microbiota disease prediction is studied as a graph prediction task, these powerful GNN baselines are necessary.

4. The paper concludes that the proposed UMMAN is stable. The experimental section does not support it.

### Questions
1. It is not clear why the unsupervised training is used. What's the advantage over supervised learning on the gut microbiota disease prediction?

2. Nodes in a graph can be randomly permuted, thus these there is no fixed order of nodes in a graph. Then what is the meanings of 'position of edges' and 'disrupt the nodes' in the sentence 'we design the adversarial control group, i.e., keep the position of the edges unchanged, randomly disrupt the nodes to train part of the discriminator'? Does that mean we keep the adjacency matrix yet permute the node order?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aim to obtain the embeddings of nodes in the multigraph under unsupervised situation, so that it helps learn the multiplex relationship. The experiments are mainly conduct on disease network.

### Strengths
1. It learns multiplex connection between intestinal flora and hosts to guide the prediction of diseases.

2. This work proposes Nnde feature global integration descriptor to represent the global embedding of a graph.

3. The experiments of this work is good, comparing to existing algorithms.

### Weaknesses
1. The technique contribution of this work is not very high as it mainly uses the GNN for disease network.

2. The work may not related to ICLR community, as we can see that  most of reference are from bioinformatics.

3. The baselines are old, and the code/dataset are not available.

### Questions
1. The technique contribution of this work is not very high as it mainly uses the GNN for disease network.

2. The work may not related to ICLR community, as we can see that  most of reference are from bioinformatics.

3. The baselines are old, and the code/dataset are not available.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
