# Biologically Plausible Brain Graph Transformer

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
State-of-the-art brain graph analysis methods fail to fully encode the small-world architecture of brain graphs (accompanied by the presence of hubs and functional modules), and therefore lack biological plausibility to some extent. This limitation hinders their ability to accurately represent the brain's structural and functional properties, thereby restricting the effectiveness of machine learning models in tasks such as brain disorder detection. In this work, we propose a novel Biologically Plausible Brain Graph Transformer (BioBGT) that encodes the small-world architecture inherent in brain graphs. Specifically, we present a network entanglement-based node importance encoding technique that captures the structural importance of nodes in global information propagation during brain graph communication, highlighting the biological properties of the brain structure. Furthermore, we introduce a functional module-aware self-attention to preserve the functional segregation and integration characteristics of brain graphs in the learned representations. Experimental results on three benchmark datasets demonstrate that BioBGT outperforms state-of-the-art models, enhancing biologically plausible brain graph representations for various brain graph analytical tasks

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a brain graph representation learning framework aimed at enhancing biological plausibility, with a focus on capturing the small-world architecture of brain networks. Specifically, the authors propose a novel framework called BioBGT, which emphasizes node importance encoding and functional module encoding. The framework consists of two key components; 1) Network entanglement-based node importance encoding, which captures the significance of nodes in the process of information propagation, and 2) Functional module-aware self-attention, which generates node representations that reflect both the functional segregation and integration properties of brain networks. The experimental results demonstrate the effectiveness of this design and its superior performance in brain disease detection tasks.

### Strengths
- As emphasized by the authors, their method highlights the biological properties of the brain structure via biological plausibility.
- Overall, the presentations are clear and easy to understand their framework and results.
- The experiments are well-structured with multiple brain datasets, and the proposed model demonstrates strong performance in most cases.

### Weaknesses
 - The authors propose three main methods: network entanglement-based node importance encoding to reflect the different importance of each node like the hub node, community contrastive strategy-based functional module extractor and an updated self-attention mechanism for functional module-aware self-attention mechanism. However, I couldn’t find much difference from the original works of each methods the authors mentioned they were inspired by. On top of that, the equation 6 and its proof in the appendix needs to be double checked (shouldn’t log2(Z_i Z) be log2(Z_i/Z)?).

- As shown in [1] and the proof in the appendix, the two equations appear identical. However, due to an error in the calculations within the proof, the resulting expressions differ. Therefore, in Eq. (6) of Theorem 1, the second term should be log_2(Z_i/Z) instead of log)_2(Z_iZ). Additionally, while defining the hub characteristics in the brain through node entanglement (NE) seems reasonable, it is difficult to identify significant novelty compared to previous studies.

- Even though the authors provided citations on the quantum entanglement methods, it would be very helpful for the readers to have more details on the definition and why they need to be utilized to quantify the structural information.

- The term “with their biological plausibility preserved” seems to be misleading in Line 345, since the classification performance alone does not directly demonstrate the effect of the biological plausibility, which is never dealt until much later in section 4.4.

- Tables 1 and 2 suggest that the baselines were not compared fairly. Their high standard deviations undermine the credibility of the experimental results.

### Questions
- Contributions and novelty need to be clarified as well as the questions raised in the Weakness.

- As seen in [2] and Eq. (9), the self-attention formulations are nearly identical. However, the proposed method claims to enhance functional module encoding by making the exponential kernel trainable. The explanation regarding the benefits of learning the kernel seems insufficient. Could you elaborate on the advantages of this approach? Additionally, the experiments only compare the proposed method with the self-attention mechanism from Eq. (2). A more thorough discussion of the differences between the proposed approach and the method presented in [2] would strengthen the analysis. 

- Why did the authors use 50 randomly selected nodes to validate the biological plausibility in node importance encoding? The number of nodes of the brain networks doesn’t seem to be too large. Also, are the results consistent across all datasets?

- In Figure 5, the authors present the average self-attention scores as a heatmap. However, in the results of the proposed BioBGT, the block-like color patterns corresponding to functional modules do not consistently appear across all ROIs. Could you explain the reason for this discrepancy? (For example, between ROIs 40 and 60, the block-like regions with high values are not observed.) Also, I think the caption should be more informative for the figure. 

- Moreover,  the biological plausibility in functional module-aware self-attention seems to be ``plausible'' as in its block-like patterns, but do they comply with the neuroscientific prior knowledge? Adding analysis on which functional module match each block may help the biological plausibility of your method.

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
This paper proposes BioBGT, a framework that incorporates node importance encoding and community-aware Graph Transformer for learning the network representation of the brain. 
Strengths of this work include that 1) the proposed method is motivated by incorporating prior knowledge of the brain, and 2) it shows clear improvement over the presented baselines.
Some concerns and suggestions are outlined in the `Questions` section.

### Strengths
- Motivation to incorporate prior knowledge of the brain into the framework
- The proposed method shows clear improvement over the presented baselines

### Weaknesses
 - The authors’ emphasis on biological plausibility is weakly supported both theoretically and experimentally.
- The baseline model performance in the experiments is generally lower than expected, so verification may be necessary.

### Questions
### Major concerns
- The biological properties of the brain graph are very complex and not much known yet. Strong assumptions and statements about "biologically plausible" properties can be generally toned down throughout the manuscript.
- The proposed methodology does not seem to significantly incorporate the biological property of the human brain as the authors claim, given that the theoretical and empirical findings are not very supportive. Specifically:
  - 1) In Section 4.4, using PCC values (which seem to reflect the average functional connectivity strength across the nodes) as a representative measure of biological plausibility is logically tenuous. Even if we assume that the PCC value is representative of biological plausibility, the quantitative similarity between NE values and PCC values has not been studied. 
  - 2) The BioBGT output demonstrated in Figure 5 (c) does not seem to represent a biologically plausible network, which deviates from the modular patterns of brain functional connectivity.
- Section 4.5 focuses more on generalizability across datasets than on comparing the scale of the model parameter size, data, and computation. Please consider revising the possibly misleading term 'scalability' to 'generalizability'.
- The generalizability of BioBGT to non-biological networks shown in Section 4.5 seems to contradict the authors' emphasis on the strength of the BioBGT, that it introduces 'biological' property of the human brain to the framework. Please revise the logical consistency of Section 4.5 since it reads as if any network that contain hubs and modules are considered 'biological'.
- Merging Tables 1, 2, and 6 and reducing the number of presented metrics (e.g., AUC and ACC) would improve the readability of the results.
- Ablation studies seem to show redundant node importance ablations with various graph metrics. Please consider reducing the number of node importance ablations and merging the result with FM-Attn ablation results. 
- In Eq. (7), please elaborate on the rationale for incorporating node importance through addition rather than multiplication or concatenation. 



### Minor concerns
- Clarification needed on “high correlation” (line 054): please clarify if this refers to the correlation of temporal changes.
- The category "Brain Graph Learning Models" can be revised to "Message-Passing Neural Networks (MPNNs)" or "Graph Neural Networks (GNNs)". GAT is classified as a Graph Transformer, but it is more often considered as a GNN. Please consider re-categorizing the model.
- Please consider adding more recent Graph Transformer-based studies on functional connectivity as baseline methods.


### Recommendation
Given the above concerns, especially the weakness of the experimental results in supporting the authors' claim, I initially recommend reject of the paper.


### Recommendation after rebuttal
Given the authors' response to the concerns, I recommend weak reject of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The Biologically Plausible Brain Graph Transformer (BioBGT) is introduced here as a graph transformer specifically aimed at creating brain graph representations rooted in biological principles. Unlike prior models that allow representations to form without these constraints, BioBGT uses the concept of network entanglement - borrowed from quantum computing - to more accurately assess node importance than traditional centrality metrics. Furthermore, the authors implement a community contrastive training method, enabling node representations to account for network communities. These two contributions are aligned with core characteristics of fMRI-based graphs, underscoring their relevance for neuroimaging-focused models.


_____________________
EDIT (after rebuttal period): I appreciate the answers and discussions that the authors had with me and the other reviewers. Based on all this I'm increasing the score from 6 to 8 (accept), as well as increasing the contribution score from 3 to 4. There are still some small weaknesses that I've mentioned in this discussion and that is why I do not increase the score of this paper to the maximum value. I thank the authors for the insightful discussions and the time taken to address my concerns.

### Strengths
I found this paper compelling and I believe it has strong potential for ICLR. The writing is clear and well-organized, making it highly readable. The paper’s originality lies in its combination of concepts from another field, applied thoughtfully to the fMRI domain, with evidence that this approach yields positive outcomes. In this sense, the results in tables 1 and 2 are quite impressive, while those in Table 6, though somewhat less robust, still demonstrate solid performance.

The authors leverage three widely recognized neuroimaging datasets and employ two different parcellation methods. I feel the choice of baseline models is appropriate for the study’s goals, with an exception that I will provide in the next section. The quick experiments in Section 4.5 are noteworthy, showing that the model can achieve comparable performance on non-neuroimaging datasets with similar underlying motivations.

### Weaknesses
1. No experiment is conducted with a smaller parcellation. The results using the ADNI dataset - where a smaller parcellation was used - are not as strong, which in my opinion are an indication that a smaller number of ROIs could impact the performance of this method. Given the focus on community structure and node importance of this work, I think it would have been important to understand whether the size of the parcellations are an important factor in this models performance.
2. Even though the ablation study makes a good job in comparing different alternatives to the node importance encoding by comparing other centrality measures, there is no ablation study for the community contrastive strategy. 
3. The work lacks comparison with more "traditional" ML models like random forests or SVM. In a few fMRI works/papers that I have seen in the past, and also based on my experience with these datasets, I typically see is that more "traditional" models achieve similar or even better performance than deep learning when trained on the upper-triangle of the correlation matrices (which has been historically widely explored in the connectomics field). In this sense, for a conference like ICLR, I find the lack of comparisons with traditional ML models in this specific context a weakness of this paper.
4. This work has an entire section (4.4) focused on the biological plausibility of its model, but these results do not discuss whether these modules correspond to any known brain structure or medical knowledge. Furthermore, it is not clear how these different modules contribute to the final classification, and thus it is not clear how plausible and good these representations are.

### Questions
I will be happy to revise my final score if the authors tackle the weaknesses I have identified. Furthermore, I have the following questions, more or less in the order they appear in the paper:
1. Equation 7 mentions "learnable embedding vectors", but I do not see those in the equation. Can the authors specify this better?
2. Did the authors try other contrastive loss functions beyond the one in equation 8?
3. How did the authors calculate the F1/sensitivity/specificity scores for the ADNI dataset, where we have 3 classification labels?
4. In Conclusion, the authors argue that they "managed to keep the number of parameters comparable to other models". Where is this shown in the paper?

### Soundness
3

### Presentation
4

### Contribution
4
