# Weighted Point Cloud Embedding for Multimodal Contrastive Learning Toward Optimal Similarity Metric

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
In typical multimodal contrastive learning, such as CLIP, encoders produce one point in the latent representation space for each input.
However, one-point representation has difficulty in capturing the relationship and the similarity structure of a huge amount of instances in the real world.
For richer classes of the similarity, we propose the use of weighted point clouds, namely, sets of pairs of weight and vector, as representations of instances.
In this work, we theoretically show the benefit of our proposed method through a new understanding of the contrastive loss of CLIP, which we call symmetric InfoNCE.
We clarify that the optimal similarity that minimizes symmetric InfoNCE is the pointwise mutual information, and show an upper bound of excess risk on downstream classification tasks of representations that achieve the optimal similarity.
In addition, we show that our proposed similarity based on weighted point clouds consistently achieves the optimal similarity.
To verify the effectiveness of our proposed method, we demonstrate pretraining of text-image representation models and classification tasks on common benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new understanding of the symmetric contrastive loss InfoNCE of CLIP, and clarify the point-wise mutual information is the optimal similarity that minimizes symmetric InfoNCE., then gives an upper bound of excess risk on downstream classification tasks of representations when the optimal similarity is achieved. Then, the paper proposes similarity based on weighted point clouds to consistently achieves the point-wise mutual information and the corresponding implementation of the proposed similarity.

### Strengths
1. The paper starts from a new understanding of contrastive loss, and proposes similarity measure that approximates the optimal formulation, which is theoretically well-founded.

2. The paper combines theory with practice and has demonstrated the effectiveness of the proposed similarity through experiments.

### Weaknesses
1. The innovation is limited. Some core concepts of the paper, such as suboptimality decomposition, are referenced from existing work.

2. The role of weighted point cloud seems to be overstated. The paper did not use concepts related to point clouds, such as neighborhoods, connectivity. Only the “weight” is used in the weighted similarity aggregation. The method essentially uses weighted sums of feature vectors, which is a common technique in representation learning, and the connection to point clouds is tenuous.

3. Some concepts or expressions need further clarification. For example, 1. What exactly does the similarity structure (line 41) mean? The notion of a 'similarity structure' is not clearly defined, and it's unclear how it relates to the proposed method or the theoretical analysis. 2. Why is the rank of G greater than d+1, there exists a certain error of the approximation of G? (lines 309-310) The explanation of why a higher rank of G leads to approximation errors is not sufficiently detailed, and the connection to the proposed method is not clear. 3. The assumption C.2 seems strong, can you provide a specific explanation based on practical examples? The assumption C.2, involving the existence of low-dimensional latent variables and continuous bijective decoders, needs further justification and examples to demonstrate its practical relevance. 4. The equation 3 has empty before ||, which seems a typo.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors presented an analysis of the contrastive loss of CLIP that gave insight on the optimal similarity measure for this loss. Furthermore, inspired by their analysis of the optimal loss, the authors proposed a new similarity measure that achives optimal similarity values, with reasonable computational cost.

### Strengths
The paper presents an alternative to the inner-product similarity through the use of weighted sums of kernel function evaluations. As such, the method benefits from the kernel trick: whereas the simple inner-product similarity may require a high-dimensionality in feature space, the use of kernels reduces the dimensionality of the feature space and shortens the amount of calculations required. Conversely, the method allows for greater performance in downstream tasks for the same amount of computation, by approsimating more closely the (theoretical) optimal similarity measure.

### Weaknesses
1. Inner-product similarity analysis

     A key point in the argument for the superiority of the authors' method over the standard similarity measure of CLIP is given in section 5.1, regarding the approximation error between the inner-product similarity matrix and the optimal similarity matrix $G$. There is an assumption that the number of samples $N$ is greater than the dimensionality $d$ of the feature space, thus the rank of the inner-product similarity matrix is smaller than the rank of $G$, implying the existence of approximation error. However, it is not clear from the paper that the approximation error is indeed deleterious, since the effective rank of $G$ could be substantially smaller than $N$ - and the effectiveness of CLIP suggests that this may indeed be the case. The argument hinges on the assumption that the full rank of $G$ is necessary for optimal performance, but this is not rigorously justified. It is possible that a lower-rank approximation of $G$, achievable through the inner-product, captures the essential structure of the similarity space. Furthermore, the authors' method relies on a combination of linear and non-linear kernels, and the ablation study shows that the linear-only kernel achieves comparable performance, particularly in zero-shot classification, suggesting that the non-linear component may not be as critical as claimed, and that the rank deficiency of the inner-product may not be the primary limiting factor.

2. Need for linear-only and nonlinear-only results

     The hyperparameter options for $(\alpha_1, \alpha_2)$ do not include a linear only $(1, 0)$ and nonlinear-only $(0,1)$ option. Given the ablation results, such choices were desirable.

### Questions
It would be interesting to have an analysis of:

- The effective rank of $G$ to clarify whether the stated deficiency of inner-product similarity is substantial. For instance, an analysis of the singular values of $G$ could be of value, since it would directly relate the rank disparity to the L2 error.

- The effectiveness of linear-only kernels in addition to the experiments already in place.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes to replace the point-wise contrastive loss of CLIP with a dense contrastive loss calculated by using the contrastive loss on top of the average pair-wise similarity between dense features (the features prior to the final pooling layer of encoders). The authors show that this leads to better results (using the same evaluation as CLIP). The method is rigorously motivated by analyzing excess risk relative to the optimal downstream classifier head.

### Strengths
(1) The introduction is especially well-written. I appreciated the motivation that many-to-many correspondences are not adequately represented by a single CLIP embedding.

(2) The theory is nice (but Eq. 3 has typos).

### Weaknesses
(1) It is unclear how this method differs from dense contrastive loses. (For example: https://openaccess.thecvf.com/content/CVPR2021/papers/Wang_Dense_Contrastive_Learning_for_Self-Supervised_Visual_Pre-Training_CVPR_2021_paper.pdf)

(2) Computational cost. The contrastive loss is already quite computationally expensive (square of mini-batch size if not using global hard negative mining). Now we multiply that cost by the square of number of feature vectors.

(3) Practically speaking (not considering the theory), there is not much innovation in this paper. Similarity metrics over pairs of sets of features are well-established. For example: ColBERT (https://arxiv.org/pdf/2004.12832). The extension from a pure NLP setting to image-text is straightforward.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3
