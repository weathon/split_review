# Deep Orthogonal Hypersphere Compression for Anomaly Detection

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Many well-known and effective anomaly detection methods assume that a reasonable decision boundary has a hypersphere shape, which however is difficult to obtain in practice and is not sufficiently compact, especially when the data are in high-dimensional spaces. In this paper, we first propose a novel deep anomaly detection model that improves the original hypersphere learning through an orthogonal projection layer, which ensures that the training data distribution is consistent with the hypersphere hypothesis, thereby increasing the true positive rate and decreasing the false negative rate. Moreover, we propose a bi-hypersphere compression method to obtain a hyperspherical shell that yields a more compact decision region than a hyperball, which is demonstrated theoretically and numerically.  The proposed methods are not confined to common datasets such as image and tabular data, but are also extended to a more challenging but promising scenario, graph-level anomaly detection, which learns graph representation with maximum mutual information between the substructure and global structure features while exploring orthogonal single- or bi-hypersphere anomaly decision boundaries. The numerical and visualization results on benchmark datasets demonstrate the superiority of our methods in comparison to many baselines and state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces an innovative approach to anomaly detection, enhancing traditional hypersphere learning with an orthogonal projection layer. This improves accuracy and reduces false negatives. The paper also introduces a more compact decision region, a "hyperspherical shell," and extends the methods to graph-level anomaly detection. The experimental results demonstrate the effectiveness of these methods in comparison to existing approaches. The contributions include enhanced anomaly detection techniques, particularly beneficial for high-dimensional and graph-based data.

### Strengths
The paper stands out in the following aspects:
1.	Originality: The paper presents a problem that may lead to suboptimal performance in the field of anomaly detection and provides a solution, offering a novel approach to enhance the performance of anomaly detection algorithms.
2.	Quality: The research is of high quality, marked by a well-structured approach, rigorous validation, and superior performance compared to existing methods. The use of benchmark datasets adds to the credibility.
3.	Clarity: The paper is well written, ensuring clear communication of the research. It offers a logical flow.
4.	Significance: The paper addresses a novel anomaly detection issue, offering potential improvements for high-dimensional and graph-based data. The practical applicability and broad relevance make it highly valuable.

### Weaknesses
1.	This article mentions the concept of hyperspheres but doesn't provide a more rigorous theoretical explanation for why standard hyperspheres are superior to boundaries formed by ellipsoids. Adding mathematical proofs or a deeper theoretical foundation would strengthen the paper. Specifically, the paper should elaborate on the limitations of using a hypersphere as a decision boundary when the underlying data distribution, after transformation by a neural network, might be better represented by an ellipsoid. The assumption that data will conform to a hyperspherical shape in the latent space needs more justification, especially given that neural network transformations can introduce complex correlations and non-uniform variances across dimensions. A discussion on how the proposed orthogonal projection mitigates this issue would be beneficial.
2.	High-dimensional data and large datasets pose scalability challenges. The paper could address the scalability of the proposed methods and discuss their efficiency and computational requirements in dealing with big data. The analysis should include a discussion of the computational cost associated with the singular value decomposition (SVD), especially as the dimensionality of the input data and the size of the dataset increase. Furthermore, the paper should explore potential optimizations or approximations to the SVD to make the method more practical for large-scale applications. A more detailed analysis of the memory requirements for storing the projection matrices and intermediate results would also be valuable.

### Questions
1. The proof of Proposition 2 in section C of supplementary materials should be make more clear.

2. In equation 3, how to guarantee the projected embeddings is orthogonal via  singular value decomposition?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of unsupervised anomaly detection. The authors proposed a deep orthogonal hypersphere compression method, which has two variants. The authors also provided theoretical analysis. The experiments on images, tabular data, and graphs showed that the proposed methods are more effective than the competitors.

### Strengths
* The motivations and technique details of the proposed methods are clearly illustrated. The visualizations (e.g. Figures 1-4, 12 and 13) are very impressive.
* The ideas especially the two concentric hyperspheres for anomaly detection are novel and interesting. They provide new insights into anomaly detection.
* The theoretical analysis such as Propositions 1, 2, and 3 make the paper solid.
* The experiments are extensive. There are image datasets (e.g. CIFAR10), tabular datasets, and six graph datasets.
* More importantly, in the experiments, the proposed methods significantly outperformed state-of-the-art anomaly detection methods such as DROCC (2020), PLAD (2022), and GLocalKD (2022) and OCGTL (2022).

### Weaknesses
A minor weakness is that some points haven’t been sufficiently explained. Please refer to my questions.

1. Figure 2 shows that the orthogonal projection improves the performance of anomaly detection. What is the fundamental reason? I suggest the authors provide further analysis as well as some references if possible. 
2. A typo or grammar issue in the first paragraph of Section 2.1.2: ‘cannot be avoided by solving equation 1’, it is not an equation. It is an optimization problem.
3. Does Proposition 2 mean the distance (to the original or hypersphere center) based anomaly score in high-dimensional space are not reliable? If yes, the authors may add a few words to the last paragraph in Section 2.2.1 to provide a hint or motivation for the new anomaly score defined by (9).
4. Given Proposition 2, in the high-dimensional space, the normal data are already far away from the origin. Why do we need to further push them to the outer hypersphere, namely, performing the hypersphere compression to reduce the thickness of the shell?
5. Are $r_{max}$ and $r_{min}$ fixed or adjusted adaptively?
6. In Proposition 3, when $r_{min}=r_{max}$, $\kappa$ is infinity. Does this still make sense?
7. What make graph anomaly detection special compared to image and tabular data anomaly detection? 
8. In Section 3.1, the authors mentioned a comparison method FCDD, but Table 2 doesn’t include the corresponding result.
9. In Appendix K, the authors showed the results of imbalanced experiments of graph data. Does it mean the results on graph data in the main paper are from balanced experiments? What is the difference between these two settings?

### Questions
1. Figure 2 shows that the orthogonal projection improves the performance of anomaly detection. What is the fundamental reason? I suggest the authors provide further analysis as well as some references if possible. 
2. A typo or grammar issue in the first paragraph of Section 2.1.2: ‘cannot be avoided by solving equation 1’, it is not an equation. It is an optimization problem.
3. Does Proposition 2 mean the distance (to the original or hypersphere center) based anomaly score in high-dimensional space are not reliable? If yes, the authors may add a few words to the last paragraph in Section 2.2.1 to provide a hint or motivation for the new anomaly score defined by (9).
4. Given Proposition 2, in the high-dimensional space, the normal data are already far away from the origin. Why do we need to further push them to the outer hypersphere, namely, performing the hypersphere compression to reduce the thickness of the shell?
5. Are $r_{max}$ and $r_{min}$ fixed or adjusted adaptively?
6. In Proposition 3, when $r_{min}=r_{max}$, $\kappa$ is infinity. Does this still make sense?
7. What make graph anomaly detection special compared to image and tabular data anomaly detection? 
8. In Section 3.1, the authors mentioned a comparison method FCDD, but Table 2 doesn’t include the corresponding result.
9. In Appendix K, the authors showed the results of imbalanced experiments of graph data. Does it mean the results on graph data in the main paper are from balanced experiments? What is the difference between these two settings?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study centers on hypersphere-based anomaly detection challenges, presenting the orthogonal projection layer as an enhancement for deep SVDD. Additionally, the authors introduce the concept of bi-hypersphere anomaly detection. The effectiveness of these proposed modules is rigorously validated through a series of comprehensive experiments and insightful visualizations. Furthermore, the application of the two algorithms is extended to address graph-level anomaly detection, showcasing their versatility and potential impact in various contexts.

### Strengths
+ The paper's content is grounded in sound research, with a particularly innovative contribution in the form of the bi-hypersphere concept.

+ The research is substantiated by a comprehensive and diverse set of experiments, encompassing three distinct data types. The visualizations effectively convey the superiority of the proposed method.

+ The visualization results pertaining to anomaly detection are distinctive and intuitive, enhancing the paper's overall quality. The improvement over the previous baselines is remarkable.

### Weaknesses
 - Why can the orthogonal projection layer ensure a standard hypersphere?

- The occurrence of the "soap bubble phenomenon" needs further clarification. Does it mean incompletely optimized?

- We know that Deep SVDD compels normal data close to the center of the decision boundary, why do anomalies appear within this decision boundary? What are the main differences and similarities between normal data and these anomaly data?

- Authors claimed that DO2HSC is to control training data to be more compact. I think the complete optimization of DOHSC can also reach this target, so what advantages does DO2HSC have about data compactness?

- Some details need to be double-checked, such as the bolding of three results in Table 13, Class 1 of MUTAG result, while the caption specifies marking only the best two results.

### Questions
See Strengths and Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper suggests a new technique of hypersphere learning via a particular decision boundary to tackle the problem of Anomaly Detection. The boundary in this case is an orthogonal projection layer and the training data distribution is aligned with this geometry, a fact that encourages the correct prediction. The suggested methods seem to be ubiquitous in the data modalities, with emphasis on the graph data, and this is supported by numerical experiments.

### Strengths
- The paper is well written and the propositions seem sound.

- The paper solves the optimization problem (1) and this choice seems novel. The existing literature presented the following restrictions: (i) the decision surface inferred is not a standard hypersphere but at times a hyperellipsoid, leading to insufficient accuracy, (ii) the 'regular' data are located far from the hypersphere center, thus spoiling the normality of the predicted region and allowing anomalous data to fall into the sphere, (iii) the hypersphere is shows high sparsity leading to misclassification of the anomalous points.
The paper suggests (i) DOHC that employs an orthogonal projection layer that limits the evaluation errors, and (ii) DO2HSC that faces the second issue above using two co-centered hyperspheres. 
The use of a regularization term in the objective function (1) avoids the correlation of the features and the problem of different variances. 

- The authors provide extensive experiments in three different cases of datasets. Each case contains several datasets. The comparison to SOTA methods seems superior for the DOHSC and DO2HSC proposed model. 

- The proposed architecture is applicable in graph data based on the optimization of (16) function.

### Weaknesses
Minimal weaknesses. 
A weakness that can be pointed out is the use of one class in total for the anomaly detection problem, but this is clarified by the authors.
Good paper overall.

### Questions
- Can the authors offer some details about the averaging of scores (table 1)? Did they conduct repeatedly the same experiment like in tables 2,3?
- In the tabular data-based experiments, can the authors say why they chose F1 and not AUC ROC again, like in the graph data? 
- For the visualization of the data, the paper pictures it 'by setting the projection dimension to 3'. Thus, was any further processing of the output applied? E.g. a dimensionality reduction technique? If yes, the AUC ROC score after this outcome may have changed from the table 3 score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
