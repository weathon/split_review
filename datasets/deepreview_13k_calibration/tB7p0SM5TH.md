# GraSP: Simple yet Effective Graph Similarity Predictions

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Graph similarity computation (GSC) is considered one of the essential operations because of its wide range of applications in various fields. Graph Edit Distance (GED) and Maximum Common Subgraph (MCS) are the most popular graph similarity metrics. However, calculating exact GED and MCS is a complex task that falls under the category of NP-hard problems. Consequently, state-of-the-art methodologies learn data-driven models leveraging graph neural networks (GNNs) for estimating GED and MCS values. A perceived limitation of these approaches includes reliance on computationally expensive cross-graph node-level interaction components but to little avail. Instead of building up complicated components, we aim to make the complicated simple and present GraSP, a simple yet highly effective approach for GSC.  In particular, to achieve higher expressiveness,  we design techniques to enhance node features via positional encoding, employ a graph neural network backbone with a gating mechanism and residual connections, and develop a multi-scale pooling technique to generate meaningful representations. We theoretically prove that our method is more expressive and passes 1-WL test performance capabilities. Notably, GraSP is versatile in accurately predicting GED and MCS metrics. In extensive experiments against numerous competitors on real-world datasets, we demonstrate the superiority of GraSP over prior arts regarding effectiveness and efficiency. The source code is available at https://anonymous.4open.science/r/GraSP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method for approximating graph similarity scores, leveraging random walk method for position encoding, RWPE, and multi-scale pooling. The overall method GRASP shows superior performance compared to exiting methods over four datasets and two graph similarity/distance metrics.

### Strengths
1. The method is well-motivated with the observation that cross-graph node-level interaction is costly, and the proposed method is relatively simple with great inference time reduction.
2. The paper is well written and easy to follow.

### Weaknesses
1. It would be interesting to know what would be the alternative to the proposed combination of summation and attention pooling, e.g. what if a simple non-learning combination is used, i.e. $\alpha * z_{sum} + (1 - \alpha) * z_{att}$ where $\alpha$ is a hyperaprameter scalar. This will further highlight the importance of learnable combination of the two pooling methods.

2. The overall novelty is limited, given the adoption of random walk positional encoding and combination of existing graph pooling are not firstly proposed in this paper.

### Questions
1. Why the time complexity for computing the random walk positional encoding can be omitted? For each new graph pair, the inference time should include such positional encoding, since at inference time, the graph pair can be new and thus unseen by the model. Unless the authors assume a database-like setting, such overhead cannot be omitted.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed GRASP, a method that leverages Graph Neural Networks to approximate Graph Distance/Similarity metrics, namely:
1. Graph Edit Distance (GED) and 
2. Maximum Common Subgraph (MCS) 

whose exact computations are NP-Hard. The authors enhanced node features using positional encoding and learned an embedding for graph using RGGC layers and multi-scale pooling. These embeddings are used to estimate GED/MCS. The authors demonstrated better efficacy and efficiency of their model compared to baselines.

### Strengths
1. The paper focuses on predicting graph similarity/distance metrics which is a very important problem. The organization of the paper is good and easy to follow. 
2. The authors used positional encoding to enhance node features which also aided in passing the 1-WL test.
3. The ablation study is good which covered most of the design choices the authors made.

### Weaknesses
 1. The authors presented MSE on predicted similarity scores (obtained by exponentiating a normalized version of GED) instead of predicted GED. Given the task is to predict GED, results should be reported on GED itself and not its transformation to a similarity metric that distorts the true errors. While some previous works such as SIMGNN have also followed the same methodology of reporting results on exponentiated similarity instead of true GED, there is no justification for this transformation. The use of an exponentiated similarity score obscures the actual error in GED prediction, particularly for larger distances where the exponential function will compress the error, making it difficult to assess the true performance of the model in predicting larger GED values. This transformation also makes it difficult to compare with traditional methods that directly predict GED.

 2. The statistics of the data used for training, validation, and inference are not provided in the paper, which are important to understand the quality of results. The lack of information regarding the distribution of graph sizes, the range of GED values, and the number of samples in each split makes it difficult to assess the robustness and generalizability of the proposed method. This information is crucial for understanding the experimental setup and for reproducing the results.

 3. The MSE scores of baselines reported in the paper do not align with the existing literature. For example, GREED outperforms other baselines such as H2MN, SIMGNN in the literature but it is not reflected in this paper. What is the source of this discrepancy? Were all methods trained on error over GED or over the similarity score. The authors need to release the version of code they used benchmarking the baselines and the exact loss function so that reproducibility and any source of discrepancy can be properly analyzed. The discrepancy in reported baseline performance raises concerns about the experimental setup and the comparability of results. It is essential to ensure that all baselines are implemented and trained correctly to provide a fair comparison.

 4. Experiments are not extensive.
 * The heat maps are provided for the AIDS700nef dataset where graphs are of small sizes. Heatmaps on datasets with larger graphs such as PTC give a better idea of the performance of Grasp and those need to be included.
 * It is not clear how Grasp generalizes for unseen graph sizes. Given that generating ground truth for graphs with larger sizes is expensive, it is interesting to see how Grasp performs when training is done with smaller graphs and testing is done on larger unseen graphs. This aspect needs to be compared with other state-of-the-art baselines such as GREED and H2MN.

 5. The estimated GED didn’t include costs for relabeling of edges. The authors didn’t mention how to extend this work to include edge substitution costs.

 6. The novelty of GRASP is limited apart from using positional encoding. Grasp tackles the issue of cross-graph interactions, although it's important to recognize that Greed had already addressed this limitation before Grasp.

### Questions
1. It's unclear whether the reported MSE scores for GRASP are a result of the loss computed using the GED or similarity scores (obtained after normalization of GED). The code, specifically Line 170 in src/trainer.py, appears to calculate the loss using GED/Similarity score based on the command line parameters. A consistent methodology is required across all datasets and baselines. Hence, this needs to be clarified.

2. Are the baseline models trained to output GED scores or similarity scores (obtained after normalization of GED)? Models such as GREED are trained to output GED, training them to output similarity scores might affect the performance.

3. How is the Neural Tensor Network (NTN) affecting the performance of the method? Have you considered using only L2-Norm to predict GED, which will preserve the metric property as well? This analysis is not included in the ablation study.

4. What are the statistics of train-validation-test sets?

5. How does the accuracy vary with query size and GED on datasets with larger graphs?

6. What are the RMSE scores of GRASP and other baselines on GED?

### Soundness
1 poor

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach, GRASP, for predicting graph similarity, specifically focusing on GED and MCS metrics. GRASP deviates from the trend of incorporating complex mechanisms by introducing a simplified model that utilizes positional encoding and RGGC to enhance the expressiveness and efficiency of graph neural networks. The authors claim theoretical superiority over the 1-WL test, a widely recognized method for graph isomorphism.

### Strengths
S1: The authors innovatively incorporate positional encoding within GNN framework, a commendable step that advances the GNN's ability to capture nuanced structural information. This ingenuity potentially sets a new precedent for subsequent research in graph similarity assessment.\
S2: The methodology introduced in this paper demonstrates notable efficiency. \
S3: The experimental results seem to be promising.

### Weaknesses
W1: The presentation of the content, particularly in Section 3, lacks clarity and cohesiveness, making it challenging for readers to follow and understand the proposed methodology. 
W2: The paper posits inefficiency in contemporary cross-graph interaction techniques as a primary catalyst for the development of GRASP. However, the narrative lacks a coherent demonstration of how GRASP mitigates these inefficiencies. The empirical section, intended to validate the method's enhanced efficiency, does not decisively support this assertion. Specifically, the performance metrics juxtaposed with existing strategies such as GREED and ERIC suggest comparable efficiencies, an outcome that muddles the purported superiority of GRASP in this domain. The authors should consider a more nuanced exposition of the method's unique efficiencies, supplemented by robust experimental evidence, to substantiate claims of its advancement over current practices. 
W3: The authors assert that prevailing cross-graph interaction modules contribute significantly to computational overheads. However, the delineation of how their proposed GRASP framework, which ostensibly employs similar cross-graph interactions via NTN, innovates upon or diverges from traditional methodologies is ambiguous. This lack of clarity muddles the reader's understanding of any novel contributions the paper might be making in this specific aspect of the framework. It is imperative for the authors to elucidate the nuanced operational differences, if any, introduced by GRASP that ameliorate the time-costly nature of cross-graph interactions, distinctly setting their approach apart from conventional ones. This clarification could significantly enhance the perceived value and ingenuity of their methodology.

### Questions
Q1: Numerous methods exist to enhance the expressiveness of GNNs. What motivated your decision to exclusively focus on positional encoding in your approach? \
Q2: What is the rationale behind using RGGC as a backbone? Furthermore, can you explain how the gating mechanism contributes to the effectiveness of your task? \
Q3: On page 4 of your paper, you note that "both of the above pooling methods have some drawbacks." Can you offer more specific evidence or instances that highlight these limitations? \
Q4: Could you delve into the key differences between GED and MCS, explaining the importance of considering MCS when many related studies concentrate primarily on GED?
Q5: What sets NTN apart from existing methods of cross-graph interaction, and why is NTN a suitable option for your proposed approach? \
Q6: How does GRASP tackle the issue of efficiency, and what factors make it an efficient solution?

### Soundness
4 excellent

### Presentation
1 poor

### Contribution
2 fair
