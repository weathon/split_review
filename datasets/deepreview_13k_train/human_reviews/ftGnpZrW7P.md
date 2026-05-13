# Gramian Multimodal Representation Learning and Alignment

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Human perception integrates multiple modalities—such as vision, hearing, and language—into a unified understanding of the surrounding reality. While recent multimodal models have achieved significant progress by aligning pairs of modalities via contrastive learning, their solutions are unsuitable when scaling to multiple modalities. These models typically align each modality to a designated anchor without ensuring the alignment of all modalities with each other, leading to suboptimal performance in tasks requiring a joint understanding of multiple modalities. In this paper, we structurally rethink the pairwise conventional approach to multimodal learning and we present the novel Gramian Representation Alignment Measure (GRAM), which overcomes the above-mentioned limitations. GRAM learns and then aligns $n$ modalities directly in the higher-dimensional space in which modality embeddings lie by minimizing the Gramian volume of the $k$-dimensional parallelotope spanned by the modality vectors, ensuring the geometric alignment of all modalities simultaneously. GRAM can replace cosine similarity in any downstream method, holding for 2 to $n$ modality and providing more meaningful alignment with respect to previous similarity measures. The novel GRAM-based contrastive loss function enhances the alignment of multimodal models in the higher-dimensional embedding space, leading to new state-of-the-art performance in downstream tasks such as video-audio-text retrieval and audio-video classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript proposed a novel strategy for the multimodal representation alignment, providing more informative semantics for multiple modalities through geometric alignment. The proposed method leverages Gramian volume to replace the traditional cosine similarity to preserve rich semantic Relations between multiple modalities. Additionally, the authors proposed the GRAM-based contrastive loss to improve the alignment between each modality. Finally,  they also proved the Gramian volume can serve as quantitative metrics to measure the performance of multimodal alignment for downstream tasks.  The paper is well-organized and provide a novel insight of multimodal learning and alignemnt.

### Strengths
1. The paper demonstrates a novel method to better align heterogeneous modalities in higher-dimensional geometric spaces, which take the sematic relation between multiple modalities into consideration. 

2. It demonstrated that the proposed Gramian volume can be utlized as a novel metrics to evaluate the alignment performance of  the mulitmodal model. 

3. The performance of the model is outstanding than other state-of-the-art methods. 

4. The use of figures and tables in this paper to  illustrate the clear concepts and findings is effective.

### Weaknesses
1. The comparison on confusion matrices of cosine-based approach and proposed method should be exhibited in the former paper instead of in the supplementary materials. Also, in order to demonstrate the effectiveness of the proposed GRAM Multimodal Contrastive loss, it is important to conduct more ablation studies, comparing the vanilla contrastive loss. It is reasonable to conduct ablation studies including: (1) without proposed L_D2A and L_A2D, (2) without L_D2A, with L_A2D; (3) without L_A2D and with L_D2A; (4) without L_DAM .etc. on ActivityNet and VATEX  datasets. Also, it is more appropriate to exhibit the confusion matrix  in the supplimentary in the section 3.5 GRAM as Model Performance Metric to show the effectiveness of the proposed metrics. 

2. In the introduction, the author should more explicity explain the concept of anchor modality. If the author quote this concept from another articles, please cite the articles.  Additionally, it is more plausible to conduct more explicit mathematic conduction on  superiority of the Gramm Volum comparing to trainditonal cosine similarity in the supplimentary. In the Figure 4, it is also neccessary to implement T-SNE visualization using cosine similarity to mask the comparisons.

3. Since the article proposed a new metrics,  it is neccessary to evalute other the-state-of-the-arts Methods (VAST, LanguageBind and VideoPrism-b and so on)  using the proposed metrcis.  

4. In the table, the method's performances surpass the other the-state-of-the-art Methods significantly. In such case, the author should release the code link for the readers to validate after the publication or should provide anonymous link of the partial datasets in the table.

### Questions
1. The comparison on confusion matrices of cosine-based approach and proposed method should be exhibited in the former paper instead of in the supplementary materials. Also, in order to demonstrate the effectiveness of the proposed GRAM Multimodal Contrastive loss, it is important to conduct more ablation studies, comparing the vanilla contrastive loss. It is reasonable to conduct ablation studies including: (1) without proposed L_D2A and L_A2D, (2) without L_D2A, with L_A2D; (3) without L_A2D and with L_D2A; (4) without L_DAM .etc. on ActivityNet and VATEX  datasets. Also, it is more appropriate to exhibit the confusion matrix  in the supplimentary in the section 3.5 GRAM as Model Performance Metric to show the effectiveness of the proposed metrics. 

2. In the introduction, the author should more explicity explain the concept of anchor modality. If the author quote this concept from another articles, please cite the articles.  Additionally, it is more plausible to conduct more explicit mathematic conduction on  superiority of the Gramm Volum comparing to trainditonal cosine similarity in the supplimentary. In the Figure 4, it is also neccessary to implement T-SNE visualization using cosine similarity to mask the comparisons.

3. Since the article proposed a new metrics,  it is neccessary to evalute other the-state-of-the-arts Methods (VAST, LanguageBind and VideoPrism-b and so on)  using the proposed metrcis.  

4. In the table, the method's performances surpass the other the-state-of-the-art Methods significantly. In such case, the author should release the code link for the readers to validate after the publication or should provide anonymous link of the partial datasets in the table.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses limitations in conventional pairwise contrastive learning methods used for multimodal data integration, where alignment is typically achieved by mapping multiple modalities to a single anchor (e.g., image or text). These methods often fail to ensure semantic consistency among non-anchor modalities. The authors introduce a novel measure, the Gramian Representation Alignment Measure (GRAM), which utilizes the volume of a parallelotope formed by modality vectors in a higher-dimensional space to achieve a holistic alignment across modalities. The GRAM-based approach not only improves semantic alignment but also enhances performance on various multimodal tasks.

### Strengths
1、Innovative Methodology: The introduction of GRAM as a higher-dimensional geometric measure provides a new approach to aligning multiple modalities simultaneously, addressing the limitations of traditional pairwise methods.


2、Strong Empirical Results: The paper demonstrates substantial performance gains across multiple multimodal benchmarks, including video-audio-text retrieval and classification tasks, showcasing the effectiveness of the GRAM-based approach.

### Weaknesses
1. Does the volume complexity of GRAM computation increase significantly as the number of modalities increases? Especially in high dimensional space, does this calculation affect the real-time performance and scalability of the model? Has any consideration been given to approximate or optimize computations to reduce the computational burden?

2.GRAM is based on the volume of k-dimensional parallel polyhedra built from multimodal vectors as the alignment metric. For sparse or dense distributions in high-dimensional Spaces, does this volume still accurately reflect the semantic relations between modalities? Is there an experimental analysis to verify the robustness of this approach under different data distributions?

3.The paper mentions GRAM as an alternative to the traditional cosine similarity, but does this new alignment measure introduce instability or optimization difficulties during the actual training process? Have ablation experiments been performed to investigate the effect of GRAM on the convergence speed and stability of the model? In addition, are the effects of different learning rates and regularization strategies on model performance taken into account?

4.Does GRAM still provide a significant advantage in simple modal alignment tasks, or does its performance gain mostly manifest in complex multimodal interactions? Are there specific experimental comparisons that demonstrate the trade-off between GRAM and cosine similarity? In other words, under what circumstances is it advisable to choose GRAM over cosine similarity

### Questions
See Weaknesses.

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
This paper proposes a novel Gramian Representation Alignment Measure (GRAM) for multimodal alignment. Compared with the methods based on pairwise cosine similarity, GRAM scales well with the number of modalities.

### Strengths
1.The idea of taking advantage of determinant of the Gram matrix of the representation vectors of all modalities to measure their similarity is novel. Besides, the computational cost of the similarity calculation is low. 

2.The proposed method provides a new insight to understand the representation geometric of multimodal learning.

### Weaknesses
1.The Gram model in the experiment section is obtained from VAST pretaining models, which make it difficult to verify that Gramian measure is superior to cosine similarity in aligning modalities. The reviewer suggests the authors train the model from scratch for a fair comparison.

2.Considering this Gramian measure is a new for modality alignment, the experimental analysis for it is not enough. The reviewer expects to observe how the Gramian similarity varies during training or fintuning, and compare it with cosine similarity.

### Questions
In table 2, all models except for UMT-L and InternVideo-L use 8 frames, and they two use 12 frames? Why adopt a unified setting for a fair comparison?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the problem where cosine similarity effectively represents the correlation between paired modalities in multimodal learning scenarios, but performs poorly with more than two modalities. It proposes a Gramian Representation Alignment Measure (GRAM) to quantify modality correlation by calculating the volume of a parallelotope. And then the traditional contrastive loss is improved with GRAM, which can hold for 2 to n modality and providing more meaningful alignment with respect to previous similarity measures. Extensive experiments validate the effectiveness of the method.

### Strengths
1. This paper proposes a new volume-based modality alignment method, which sounds reasonable and overcomes the limitation of traditional contrastive learning that only computes between paired modalities. 
2. Comprehensive evaluation demonstrates the effectiveness of the proposed methods

### Weaknesses
1. Lack of the details about how to decide anchor modality for Eq. 5-7.
2. When one modality is selected as anchor, minimizing the cosine similarity between the anchor and all other modalities on hypersphere can also minimize the volume of parallelotope. What is the difference between the two in terms of physical meaning? 
3. [A] demonstrated the modality gap from contrastive learning and pointed that varying the modality gap distance has a significant impact in improving the model's downstream zero-shot classification performance and fairness. How to explain this phenomenon by your measure? and is there modality gap from GRAM-based contrastive loss?
4. The setup of the comparison experiment is not entirely fair. Since the proposed model is pretrained with the new loss and data set, the same should be done for the comparison methods. Meanwhile, ablation experiments for different losses ($L_{D2A}$ and $L_{DAM}$) are missing.

### Questions
see in Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
