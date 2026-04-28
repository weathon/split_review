# PATTERN MATCHING-BASED OUT-OF-DISTRIBUTION DETECTION FOR MULTI-LABEL NODE CLASSIFICATION

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Graph neural networks (GNNs) have achieved dominant performance in various prediction tasks on graphs. When deploying GNNs in the real world, estimating the possibility of out-of-distribution (OOD) testing samples becomes a crucial safety concern. Although some research has investigated the graph OOD detection problem, most have concentrated on single-label classification scenarios, aspecific case of the more general multi-label classification, which has broader applications, such as in social networks where nodes can represent users with multiple interests or attributes. In this paper, we first introduce and define the multi-label graph OOD detection problem and propose a simple yet effective pattern matching-based OOD detection method to address it. In particular, our method utilizes feature pattern matching and label pattern matching to obtain two matching scores. By incorporating topological structure adjustment, we ultimately derive confidence scores, serving as indicators of the likelihood that a test sample is an OOD instances. We conduct extensive comparisons with existing OOD detection methods in the context of multi-label graphs. The results show that our method achieves an impressive 7.61% reduction in FPR95 compared to the leading baselines, setting a new state-of-the-art. Furthermore, our approach can servas a benchmark for OOD detection on multi-label graphs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on detecting OOD in graph multi-label classification problems. It defines the problem, and proposes a method to quantify feature pattern matching and label pattern matching, utilizing label propagation to derive the final confidence score for OOD. Empirical evaluations on five real-world datasets demonstrate that the proposed method achieves better average accuracy compared to selected baselines.

### Strengths
Strengths:
1. The paper studies OOD in a practical setting, which could lead to potential real-world application and inspire further research and development in the field.

2. The proposed method is straightforward and easily understandable.

3. Ablation studies are included to analyze the contribution of different components of the proposed method.

### Weaknesses
Weaknesses:
1. The paper lacks details on the normalization of two scores in Equation 11.  Additionally, the equal weighting of these scores seems arbitrary and might need further investigation into alternative weighting schemes or a data-driven approach to determine optimal weights. Specifically, the paper does not discuss the impact of different normalization techniques (e.g., min-max scaling, robust scaling) on the final OOD detection performance. The choice of Z-score normalization, while common, needs justification, especially given the potential for skewed score distributions. Furthermore, the equal weighting of feature and label pattern matching scores is a significant limitation. Without a clear rationale, it's difficult to ascertain whether both scores contribute equally to the final OOD detection performance or if one score dominates the other, potentially masking important signals.

2. Figure 3 in the paper lacks explicit details about its origin. It is unclear whether the figure is based on specific data analysis or merely serves as a random illustration. This lack of clarity is particularly crucial because the figure is used to explain the design choice of "sum logits" in the absence of theoretical analysis. The paper should clarify whether the figure represents an average trend across multiple datasets or a specific instance. If it is a specific instance, it's important to show that the trend is consistent across different datasets. The lack of statistical significance for the observed trend further weakens the justification for the "sum logits" approach.

3. Though the experimental results show the proposed method achieves a better score on average, it is suggested to provide further analysis to explain why it performs worse in certain domains within the DBLP dataset. In addition, the paper lacks a theoretical foundation to support the effectiveness of the proposed method. The paper should delve deeper into the characteristics of the DBLP dataset that cause the performance drop in certain domains. For example, are there specific label co-occurrences or feature distributions in those domains that make OOD detection more challenging? A theoretical analysis, even if heuristic-based, could provide insights into why the proposed method works and its limitations.

4. The major concern is the limited novelty of the proposed method. Feature pattern matching and label pattern matching have been widely adopted in previous works like NAC and (Hendrycks et al., 2022). And label propagation is also common in handling graph data to refine pseudo labels or predicted scores. The proposed method appears to be a direct combination of existing methods in multi-label classification OOD and graph mining, with limited novel contributions. The paper needs to clearly articulate how the combination of these existing techniques leads to a novel approach for graph multi-label OOD detection. The paper should also demonstrate that the proposed method is not simply a trivial combination of existing techniques but rather a new approach with unique advantages.

### Questions
See Weaknesses

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
3

### Summary
Multi-label classification on graphs is an important task. This paper studies the multi-label graph OOD detection problem and proposes a simple yet effective pattern matching-based OOD detection method. Experimental results show that the method proposed in this paper is good.

### Strengths
1. This paper is easy to follow.
2. Multi-label classification on graphs is an important issue. 
3. Improvement in experiments seems good.

### Weaknesses
1. The method proposed in this paper lacks necessary theoretical analysis.

2. The idea of confidence score is not novel, as it has been widely used in works related to OOD and class imbalance.

3. I noticed that the authors cited the work of Zhao et al.[1], but they did not use the relevant new datasets in the experimental section.

4. The ablation experiments show it is very sensitive to hyperparameters, especially regarding label propagation.

5. No time complexity or runtime comparison. No pseudo-code and no data statistics.

### Questions
Can you provide the experimental results related to the PCG, HumLoc, and EukLoc datasets [1] ?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of out-of-distribution (OOD) detection for graph neural networks (GNNs) in multi-label classification tasks. The authors propose a novel, pattern matching-based method that combines feature and label pattern matching to produce two matching scores. These scores are further refined with topological structure adjustments to derive confidence scores, indicating the likelihood of a test sample being an OOD instance.

### Strengths
1. The multi-label classification on graph OOD detection is important and interesting.
2. The research problem is challenging.
3. The method is supported by theoretical analysis, which strengthens the validity of the approach.
4. The proposed method demonstrates promising results across multiple datasets, including a real-world application, highlighting its practical effectiveness and versatility.

### Weaknesses
1. The connection between pattern matching and multi-label classification needs clearer illustration. Specifically, it would be helpful to explain how pattern matching contributes to or enhances the multi-label classification process and to outline the role it plays within the proposed framework. The current explanation lacks detail on how the feature and label pattern matching scores are integrated with the multi-label classification model's output. It is unclear if these scores are used to adjust the classification probabilities or if they act as independent indicators of OOD, and how the topological structure adjustments further refine these scores in the context of multi-label classification.

2. The scalability of the proposed method is not thoroughly explored, particularly for large-scale graphs where such an approach might be impractical. The paper does not provide a detailed analysis of the computational complexity of the pattern matching process, especially considering the potential need to compare each test sample against all training samples or a representative subset. Furthermore, the memory requirements for storing and processing the feature and label patterns for large graphs are not discussed, which is crucial for assessing the method's feasibility in real-world scenarios.

### Questions
same as in the Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This manuscript studies the OOD problem on multi-label graphs. The authors introduce feature pattern matching, label pattern matching, and label propagation via GNN and then conduct the multi-label OOD classification on nodes. Experimental results, as they reported, demonstrate the effectiveness of their solution.

### Strengths
S1: the technical solution seems to make sense. 

S2: Figure 1 is beautiful

### Weaknesses
W1: code not available

W2: I want to know the difference in MLNC OOD detection between graph and CV/NLP data. My main concern is that there seems no difficulty in applying the existing techniques on the graph. I wonder about the unique challenges of graph domains and how the authors solve them with their creative contributions. 

W3: It seems that this paper is not the first work to solve multi-label graph OOD detection. See this work: Evidence-Based Out-of-Distribution Detection on Multi-Label Graphs.

W4: I think the paper could be further polished. The language writing could be significantly improved. 

W5: It would be more solid if the proposed solutions could have some theoretical guarantee.

Overall, this manuscript may propose a self-contained solution to multi-label OOD problems on graph domains. Although I hate to say this, I am afraid I have to say (with full respect) that the novelty and contributions of this submission might be not strong enough for this conference. I think it might be further enhanced with some theoretical support, more convincing public code, and more clear paper writing 

Plus: Kindly note that when I say "more clear writing", I do not only hope the language issues could be improved (e.g. line 075-077) but I also think there are some logical points in the paper should be polished. For example, the authors use a large part of the content to say they use sigmoid instead of softmax for multi-label problems. Do the authors wish to treat this as their contribution? because I think it is such a simple and obvious thing. If the authors wish to claim this tiny change matters and is a significant technique contribution, maybe they can provide with in-depth theory analysis further. Many other places are looked like just for filling the page length but I don't know why they are necessary to be mentioned. The authors present some technique choices and different results (like Figure 3) but we need to know why.

### Questions
Q1: between ID and OOD nodes, there seem to be some middle cases, for example, ID nodes have labels $\{A, B, C\}$ with distribution $P_1(A, B, C)$, some other nodes have labels $\{A, B, C, D, E\}$ with a totally different distribution $P_2(A,B,C,D,E)$, and then the rest node have labels $\{D, E\}$ with the distribution $P_3(D,E)$. I wonder how to deal with $P_1$ and $P_2$.

Q2: refer to W2

Q3: refer to W5

### Soundness
3

### Presentation
2

### Contribution
3
