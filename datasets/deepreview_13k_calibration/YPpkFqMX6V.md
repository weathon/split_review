# Hypergraph Neural Networks through the Lens of Message Passing: A Common Perspective to Homophily and Architecture Design

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Most of the current hypergraph learning methodologies and benchmarking datasets in the hypergraph realm are obtained by \emph{lifting} procedures from their graph analogs, leading to overshadowing specific characteristics of hypergraphs. This paper attempts to confront some pending questions in that regard:  
\textcolor{violet}{\textbf{Q1}} Can the concept of homophily play a crucial role in Hypergraph Neural Networks (HNNs)? \textcolor{teal}{\textbf{Q2}} Is there room for improving current HNN architectures by carefully addressing specific characteristics of higher-order networks? \textcolor{blue}{\textbf{Q3}} Do existing datasets provide a meaningful benchmark for HNNs? 
To address them, we first introduce a novel conceptualization of homophily in higher-order networks based on a Message Passing (MP) scheme, unifying both the analytical examination and modeling of higher-order networks. Further, we investigate some natural --yet mostly unexplored-- strategies for processing higher-order structures within HNNs (such as keeping hyperedge-dependent node representations, or performing node/hyperedge stochastic samplings), 
leading us to the most general MP formulation up to date --MultiSet--, as well as to an original architecture design --MultiSetMixer. 
Finally, we conduct an extensive set of experiments that contextualize our proposals and successfully provide insights about our inquiries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the hypergraph neural network (HGNN) and proposes several artifacts for developing the HGNN model on top of the homophily concept. In particular, the authors first introduce a novel definition of homophily based on the message-passing scheme. Afterward, they propose a new HGNN architecture, namely MultiSet, to take into account the hyperedge-dependent relations when representing the nodes in a hypergraph. Besides, the MultiSetMixer is devised to implement the layer learning process. In addition, a connectivity-based mini-batching strategy is proposed to handle large hypergraphs. Extensive experiments on benchmark datasets validate the proposed methods.

### Strengths
1. How to design an effective HGNN architecture plays a vital role in the graph learning community. The implications of this work could be significant for many downstream applications.
2. Extensive experiments are conducted to evaluate the proposed approach on many benchmark datasets and models.

### Weaknesses
1. The presentation and organization of this draft should be improved with many efforts to reach the standard of a top-tier conference like ICLR. For example, the contributions are not highlighted clearly in the introduction, and many background introductions can be found throughout this paper.

2. The technical challenges that motivate this study are unclear. In other words, the technical contributions of this work are limited since the proposed methods are mostly incremental.

### Questions
1. What are the evaluation metrics w.r.t. the reported experimental results in Tables 1-4?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a Unified Homophily Conceptualization and MultiSet Framework for Higher-Order Networks. Their method unifies the analytical frameworks of data and network architectures, providing a coherent lens for exploring intricate higher-order network structures and dynamics. They also introduce MultiSet, a pioneering message-passing framework that reimagines Hypergraph Neural Networks (HGNNs) by enabling hyperedge-dependent node representations. Additionally, they unveil a new architecture, the MultiSetMixer, which capitalizes on an innovative hyperedge sampling strategy.

### Strengths
S1. they clearly present their experimental details
S2. their method makes sense and is interesting.

### Weaknesses
W1. The concept of homophily for hypergraphs is previously discussed. (e.g. X Sun, et al. "Self-supervised Hypergraph Representation Learning for Sociological Analysis". TKDE.) It is recommended to include these works in your paper and discuss the differences.

W2. homophily is not a gold standard criterion in the graph learning area. Some network data are not isomorphic. The limitations and applicable situations should be discussed.

W3. In traditional dyadic graph neural networks, there are two branches. The 1st one is GCN-based methods, which take node features as input and aggregate information by topological structure. The 2nd one is Transformer-based methods, which take node features+position encoding as input and use self-attention to update node embeddings. The differences between hypergraphs and dyadic graphs are their topological structures (e.g. dyadic graphs contain pair-wise relations and hypergraphs have higher-order hyperedges). This difference makes sense when we design a hypergraph neural network by the 1st branch. I wonder what the significant contribution of hypergraphs will be if we design a hypergraph neural network by the 2nd branch.

W4. the experimental performance seems not that surprising. From my own experience, the message-passing pattern: "node to hyperedge and then hyperedge to node", is usually not better than directly aggregating nodes without hyperedge representations. For example, $X=\Theta X W$ where $\Theta$ is the hypergraph Laplacian matrix  Your MULTISET extension seems also to confirm my guess: you use multiset aggregating and it is very similar to aggregating nodes from a more fine-grained view (you split hyperedge representation more carefully compared with traditional simple hyperedge aggregating). Then I wondered what would happen if we completely removed the hyperedge representation in the network updating. It seems the residual connections play a crucial role in your "node to hyperedge and then hyperedge to node" message-passing flow, I wonder what would happen if you completely remove this component and compare your hypergraph structure with directly aggregating nodes without hyperedge representation.

W5. I admit that the new extension is helpful for message-passing-based methods. However, as more generalized data, hypergraphs should be more general than dyadic graphs. The hypergraph model should be more general than traditional dyadic graphs and it may be promising to achieve more general AI on graph domains. From this view, transformer-based methods are usually larger than message-passing-based methods. I wonder how to design a large hypergraph model with heavy parameters (like GPT in NLP) to achieve the "ChatGPT moment" in the graph area. It seems that the 2nd branch is more promising than the 1st branch because the 2nd branch can easily generate many large models while the 1st branch suffers from shallow layers. I suggest reconsidering the contribution of this work from a bigger picture: I wonder what the meaning of their extension, or how helpful their extension can contribute to achieving this AGI vision.

W6. The experimental work should be more extensive. For example, "Can the concept of homophily play a crucial role in HGNNs, similar to its significance in graph-based research? " Following this question proposed by the authors, the experimental section should clearly present the applicable situation and whether the homophily indeed contributes to the final performance and how much.

"Given that current HGNNs are predominantly extensions of GNN architectures adapted to the hypergraph domain, are these extended methodologies suitable, or should we explore new strategies tailored specifically for handling hypergraph-based data? " I didn't see the answer to your question. "Are the existing hypergraph benchmarking datasets truly meaningful and representative enough to draw robust and valid conclusions?" I didn't see your response to this question.

W7.  Following W4. I think the challenges, target problems, and the motivation of your new extended multiset structure, are not well formulated, and not clearly discussed.

### Questions
see W1-7

I would like to see the rebuttal to the questions mentioned in the above section “Paper Weakness”. I’m afraid that I might have not sufficient time to see a very long rebuttal. A concise and clear one would be good. 

The potential weakness won't prevent me from raising my final score. I just want to make clear whether my understanding is correct.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out that most current hypergraph learning methods and benchmarking datasets have been adapted from the graph domain, leading to the neglect of the hypergraph network foundation. The paper defines a new concept of homophily in hypergraphs using message passing and introduces a novel framework called MultiSet. Furthermore, it suggests a mini-batching method for hypergraph networks and conducts several experiments related to this approach. Finally, the paper conducts experiments involving changes of connectivity and provides a comprehensive analysis of various hypergraph models.

### Strengths
1. The paper points out the limitations of previous hypergraph research, emphasizing the need for new homophily and architecture in HGNN.
2. This paper analyzed hypergraph models through various experiments.

### Weaknesses
 1. The author proposed homophily that can be applied to non-uniform hypergraphs and provided an analysis by demonstrating the homophily distribution changes with levels in Cora-CA and 20Newsgroups datasets. However, there is a lack of explanation regarding how the changes in homophily with levels are related to the performance of HGNN models or the characteristics of those datasets. Furthermore, typical heterophily analysis involves showing the correlation between model accuracy and the homophily measure, which is missing here. It would be beneficial to see how the performance of traditional hypergraph neural network methods changes with respect to the proposed homophily score as the number of layers increases, similar to the analysis done in graph heterophily research.
2. The novelty of the MultiSet framework proposed in the paper is limited. This is because previous research, such as EDHNN2 [1] and HNN [2], has already explored the use of different representations for each hyperedge. While the authors claim that MultiSet provides a more general framework, the specific advantages over existing methods are not clearly articulated. The necessity of generalizing AllSet (or UNIGCN2) needs to be better justified. For example, it would be helpful to explain why AllSet does not fit certain problems or data and how MultiSet can address these limitations.
3. The MultiSetMixer shows only marginal improvements in performance compared to existing baseline models and, in some cases, even exhibits lower performance. However, the paper lacks an analysis of the reasons behind these performance variations. It would be beneficial to have a comparison between the performance of MultiSet and AllSet along with explanations.
4. The main focus and key contributions of the paper are not entirely clear. While the motivation section highlights the shortcomings of existing hypergraph research and emphasizes the need for new homophily measures, architecture, and benchmark datasets, the actual experiments seem to place more emphasis on the mini-batching method than on the newly proposed homophily or the MultiSet architecture.

### Questions
1. In the Supplementary Materials (Page 19, MMLP CB explanation), could you please elaborate on the meaning of "connectivity level"? I'm having some difficulty understanding the concept of "top-3 connectivity level.“
2. In step 2 of Mini-batching, it is mentioned that hyperedges are padded using a special padding token. What is this special padding token? Additionally, it is written that the padding condition is |e| > L, but shouldn't it be |e| < L?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper offers an approach to understanding homophily by examining node class distribution in hypergraph datasets, accompanied by the introduction of MultiSetMixer, a dedicated hypergraph neural network crafted for efficient learning on hypergraphs.

Message passing is the central element for grasping homophily and enhancing current hypergraph neural networks with the proposed MultiSetMixer model.

Experiments 
* demonstrate that the MultiSetMixer model performs favourably, 
* uncover insights about connectivity patterns in benchmark datasets, emphasising the influence of large hyperedge cardinalities on performance, and
*  identify common failure modes related to distribution shifts and message-passing mechanisms.

### Strengths
### Clarity
1. Through clear explanations and qualitative analysis through Figure 1, the paper elucidates homophily in real-world hypergraphs.
2. The design of MultiSetMixer's architecture is clearly explained, and Propositions 1, 2, and 3 enhance the clarity of the presentation.
3. The paper exhibits a well-organised structure, complemented by a comprehensive supplementary material that thoroughly covers all aspects of the research content.


$~$
### Originality
4. The paper introduces an original homophily concept based on message passing, breaking away from an existing assumption of a k-uniform hypergraph structure. 
5. MultiSetMixer extends the existing hypergraph neural network models (such as AllSet and UniGCN) by offering a broader scope and enabling hyperedge-dependent node representations.

### Weaknesses
### Quality
1. To enhance quality, the paper could provide a conceptual framework to describe how the proposed homophily measure integrates with MultiSetMixer to strengthen their mutual reliance on message passing. Specifically, the paper lacks a clear explanation of how the homophily measure, which is calculated based on node class distributions within hyperedges, directly influences the learning process of MultiSetMixer through its message-passing mechanism. The paper should clarify whether the homophily measure is used as a loss term, a regularizer, or a metric to evaluate the model's performance, and how this integration impacts the model's ability to learn meaningful node representations.
2. To bolster the paper's quality, exploring datasets like Walmart and Congress, characterised by lower homophily patterns as shown in prior studies [Wang et al., 2023], could broaden the analysis beyond the datasets examined in this work. The current selection of datasets might bias the results towards scenarios where homophily is already strong, potentially obscuring the model's performance in more challenging, heterophilic environments. Including datasets with varying degrees of homophily would provide a more comprehensive evaluation of the model's robustness and generalizability.

$~$ 
### Significance
3. The mini-batching sampling method is not compelling when the entire input hypergraph can be stored in memory, particularly given the moderate sizes of all datasets as indicated in Table 6. The paper does not provide a clear justification for using mini-batching when the entire dataset can fit into memory. This raises concerns about the computational overhead introduced by mini-batching, which might not be necessary and could potentially hinder the model's performance. A detailed explanation of the benefits of mini-batching, even for small datasets, is needed.
4. The importance of hyperedge-dependent node representations could be reinforced with more compelling experiments, such as exploring hyperedge-dependent node classes [Choe et al., 2023]. The current experiments do not fully exploit the potential of hyperedge-dependent node representations. The paper should explore scenarios where nodes have different labels depending on the hyperedge they belong to, which would provide a stronger justification for the proposed approach.

### Questions
1. Were there specific examples or illustrations that clarify the conceptual framework linking the homophily measure and MultiSetMixer through message passing, ensuring a deeper understanding of their interrelation?
2. Related to the previous question, is it the case that MultiSetMixer can (provably) handle datasets with a high degree of heterophily better than existing models such as AllSet and UniGCN(II)?
3. What challenges or limitations were encountered in exploring datasets like Walmart and Congress, known for their lower homophily, and how could these challenges be addressed to enhance the scope of the analysis in this work?
4. Were there any insights into the rationale behind using mini-batching sampling, especially for datasets that can be entirely stored in memory?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
