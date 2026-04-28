# Image Clustering via the Principle of Rate Reduction in the Age of Pretrained Models

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 8, 3, 8, 5

## Abstract
The advent of large pre-trained models has brought about a paradigm shift in both visual representation learning and natural language processing. However, clustering unlabeled images, as a fundamental and classic machine learning problem, still lacks an effective solution, particularly for large-scale datasets. In this paper, we propose a novel image clustering pipeline that leverages the powerful feature representation of large pre-trained models such as CLIP and cluster images effectively and efficiently at scale. We first developed a novel algorithm to estimate the number of clusters in a given dataset. We then show that the pre-trained features are significantly more structured by further optimizing the rate reduction objective. The resulting features may significantly improve the clustering accuracy, e.g., from 57\% to  66\% on ImageNet-1k. Furthermore, by leveraging CLIP's multimodality bridge between image and text, we develop a simple yet effective self-labeling algorithm that produces meaningful captions for the clusters. Through extensive experiments, we show that our pipeline works well on standard datasets such as CIFAR-10, CIFAR-100, and ImageNet-1k. It also extends to datasets that are not curated for clustering, such as LAION-Aesthetics and WikiArts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the image clustering problem in the age of large pre-trained models. Specifically, this paper develops a method to determine the cluster number in a given dataset. Then, this paper validates that the features from large pretrained models, such as CLIP, help achive better custering accuracy than the traditional feature pre-training. Moreover, this paper also develops a self-labeling method to produce text labels for the clusters. Experiments on many image datasets, including ImageNet-1k, demonstrate the effectiveness of the proposed method.

### Strengths
- This paper achieves state-of-the-art results on many image datasets, including ImageNet-1k.

### Weaknesses
Three main technique contributions are developed in this paper, including a method to determine the cluster number, a validation that the features from CLIP push the limits of image clustering, and a self-labeling method to annotate the text-labels for the clusters. I have three concerns about these three technique contributions:

- This paper seems did not discuss the existing methods to determine the cluster number and the difference among them. Do all the existing clustering methods not discuss how to determine the cluster number? Specifically, the paper does not address the well-known challenge of selecting the optimal number of clusters, a critical step in any clustering algorithm. Methods like the elbow method, silhouette analysis, or gap statistics are not mentioned or compared against. This omission makes it unclear how the proposed method's cluster number determination compares to established techniques, and if it offers any advantages or novel insights.
- The proposed clustering method is a simple combination between CLIP features and MLC optimization method. I realize it is meaningful to validate the superiority of CLIP features in image clustering, but the technique contribution itself is kind of subtle. The core of the clustering method appears to be a straightforward application of CLIP features within an existing MLC framework. While demonstrating the effectiveness of CLIP features is valuable, the paper does not introduce significant algorithmic innovations in the clustering process itself. The method seems to rely heavily on the pre-trained CLIP model, and the contribution of the clustering algorithm is not clearly articulated, raising questions about its novelty beyond leveraging existing models.
- A self-labeling method to annotate the text-labels for the clusters in *Algorithm 2* simply uses a cosine similarity metric to determine which texts are the closest ones given text candidates, which is a very simple solution. It does not meet my expectations that the proposed self-labeling method strongly relies on the pre-define text candidates. What if the text candidates are not given?

### Questions
See the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a novel method that leverages the rate reduction principle to learn to do image clustering using pretrained models. A technique for automatically select the optimal number of clusters is also proposed based on the same principle. Finally, a self-labeling mechism is proposed to label the clusters with semantic labels.
Experiments show that the proposed method achieves a good performance, as well as give a good estimation of the optimal number of clusters.

### Strengths
1. This paper provides an alternative way of performing image clustering, which seems to be performing well and could be of interesting for the community.
2. The method enables automatic estimation of the optimal number of clusters in a dataset, from the result the method seems to perform pretty well.

### Weaknesses
1. The main experiments are done on somewhat small datasets like CIFAR, or coarse grained dataset like COCO, the paper would be stronger if it could include finer-grained dataset for clustering like iNaturalist.

### Questions
1. I would be interesting in how the method perform on fine-grained datasets.
2. It would be better if the paper could include results of using other variant of CLIP models, such OpenCLIP.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission introduces a new image clustering pipeline named CPP, which leverages large pre-trained models like CLIP to efficiently and effectively cluster images, particularly on large-scale datasets. The authors propose to estimate the optimal number of clusters in a dataset and optimize the rate reduction objective using pre-trained features, resulting in a notable improvement in clustering accuracy (e.g., from 57% to 66% on ImageNet-1k). Furthermore, by utilizing CLIP's multimodal capabilities, a simple yet effective self-labeling algorithm is developed to generate meaningful text labels for the clusters. The pipeline demonstrates state-of-the-art performance across various standard datasets including CIFAR-10, CIFAR-100, and ImageNet-1k, and extends its applicability to datasets without predefined labels like LAION-Aesthetics and WikiArts.

### Strengths
1. **Leveraging Large Pre-trained Models**: The integration of the powerful image encoder from CLIP into the clustering framework MLC significantly enhances the pipeline’s ability to process and analyze images, leading to state-of-the-art clustering performance on various datasets.

2. **Improvement in Clustering Accuracy**: Through the optimization of the rate reduction objective using pre-trained features, the pipeline achieves a noticeable improvement in clustering accuracy, as demonstrated on ImageNet-1k.

3. **Self-Labeling Algorithm**: The pipeline includes a simple yet effective self-labeling algorithm that leverages CLIP’s vision-text capabilities, resulting in semantically meaningful clusters that are comprehensible to humans.

### Weaknesses
1. **Limited Innovation in Methodology**: The core of the proposed method appears to be the utilization of CLIP features for initializing the clustering process, but the algorithmic novelty beyond this initialization is not clearly established. The optimization process itself seems to rely on standard techniques, and the paper does not sufficiently articulate how the specific combination of pre-trained features and the chosen optimization objective leads to a fundamentally new approach to clustering.
2. **Concerns about Stability and Sensitivity**: As depicted in Fig.4, the model selection process exhibits a flat region around the optimal point, which raises concerns about the algorithm's stability and its sensitivity to perturbations. Small changes in hyperparameters or the choice of network architecture could potentially lead to significant variations in performance, making the method less reliable in practice. The lack of a more robust selection mechanism is a notable weakness.
3. **Potential Information Leakage**: The use of CLIP, pre-trained on a massive dataset, introduces a significant risk of information leakage, especially when evaluating on datasets like CIFAR and ImageNet, which are likely to have been seen by CLIP during its training. This potential leakage could bias the quantitative results, making it difficult to assess the true generalization capability of the proposed method. The paper does not adequately address this concern, nor does it provide an analysis of how this might affect the reported performance.
4. **Lack of Adequate Metrics for Text Labeling**: While the automated text annotation aspect of the pipeline is interesting, the paper lacks a robust evaluation of the quality of the generated text labels. The absence of appropriate metrics makes it difficult to validate the semantic meaningfulness of the clusters, and the paper does not provide a clear methodology for assessing the quality of the generated labels.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a unified approach for integrating feature learning with clustering processes. Its novel method for selecting the optimal number of clusters enhances the practicality of KNN and similar clustering methods for large-scale data, even when using computationally intensive models like CLIP. Additionally, it achieves state-of-the-art results on various datasets.

### Strengths
1- SOTA results
2- I find that enhancing KNN methods – whether by improving their scalability, representation, or explainability – is valuable. 
3- Good visual analysis Fig 3 and 4.

### Weaknesses
1- The paper's flow is somewhat challenging to follow.
2- The acronym MLC is initially mentioned in the contributions section without prior definition, leading to initial confusion, though its relation to previous works becomes clearer later in the paper.
3- While the method appears to be a practical extension of MLC, its level of novelty and contribution to the field is not distinctly evident.

### Questions
1- The complexity added by Equation 4 to the optimization process isn't clear. Is it possible for there to be multiple optimal values for K?
2- Could a simpler method, like the elbow method, be used to determine K?
3- A brief explanation of what "more-structured representation" means in the context of related works would be helpful.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a new image clustering workflow that leverages the powerful feature representation capabilities of large pretrained models (like CLIP) to effectively and efficiently perform image clustering. It first develop a new algorithm to estimate the number of clusters in a given dataset. Through extensive experiments, the paper demonstrate that the workflow performs well on standard datasets.

### Strengths
1. Novel image clustering pipeline: The paper proposes a novel image clustering pipeline that leverages the powerful feature representation of large pre-trained models such as CLIP and cluster images effectively and efficiently at scale. The paper also develops a new algorithm to estimate the number of clusters in a given dataset, and a simple yet effective self-labeling algorithm that generates meaningful text labels for clusters.
2. State-of-the-art performance: The paper demonstrates that the proposed pipeline achieves state-of-the-art clustering performance on standard datasets such as CIFAR-10, CIFAR-100, and ImageNet-1k. The paper also shows that the pipeline works well on datasets without predefined labels, such as WikiArt

### Weaknesses
1. Dependence on pre-trained models: The paper heavily relies on the pre-trained models such as CLIP to provide the initial feature representation and the text candidates for labeling. The paper does not explore how the choice of pre-trained models affects the clustering performance or the quality of labels. The paper also does not consider the potential biases or limitations of the pre-trained models, such as their data sources, or domains. Specifically, the reliance on CLIP's text embeddings for cluster labeling might introduce biases inherent in CLIP's training data, potentially leading to skewed or inaccurate cluster descriptions. A more thorough investigation into the impact of different pre-trained models, including those trained on more diverse datasets, is needed to assess the robustness of the proposed approach.
2. Limited evaluation and comparison: The paper also does not report enough ablation studies or sensitivity analysis to show the impact of different components or hyperparameters of the pipeline. For example, the paper does not provide sufficient details on how the number of clusters is estimated, and how sensitive the clustering performance is to the parameters of the proposed algorithm. Furthermore, the comparison with other clustering methods is not entirely fair, as the proposed method uses a large pre-trained backbone (ViT-L) while most other methods use much smaller backbones, like ResNet-18/34. This difference in backbone size makes it difficult to isolate the contribution of the proposed clustering algorithm from the feature representation power of the backbone.

### Questions
How does the choice of pre-trained models affect the clustering performance or the quality of labels?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
