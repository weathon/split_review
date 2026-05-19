### Summary

This paper introduces a novel approach to address the issue of modality gap in pre-trained multi-modal vision-language models. The authors propose a method that transforms intra-modal tasks into inter-modal ones, leveraging the inter-modal alignment of CLIP to improve performance. They introduce Optimization-based Textual Inversion (OTI) and Optimization-based Visual Inversion (OVI) to map features from one modality to another. The experiments on various datasets demonstrate that their approach significantly outperforms intra-modal baselines, highlighting the importance of inter-modal representations for intra-modal tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper identifies and addresses the issue of intra-modality misalignment in pre-trained vision-language models, which is an novel insight.

2. The proposed method of transforming intra-modal tasks to inter-modal ones via modality inversion is simple yet effective.

3. The paper provides extensive experimental evidence to support their claims.

### Weaknesses

#### Some Related Works


#### comment

1. The introduction could benefit from a more detailed explanation of the modality gap and intra-modality misalignment issues. Specifically, the paper should elaborate on the nature of the modality gap, whether it's a constant or variable gap, and how it manifests in the feature space. The explanation of intra-modality misalignment is also vague; it would be helpful to provide concrete examples of how this misalignment affects performance in tasks like image-to-image retrieval.

2. The method section could provide more details on the modality inversion techniques. For example, what are the specific optimization objectives used for OTI and OVI? What are the hyperparameter settings, and how sensitive is the performance to these settings? The paper lacks a detailed explanation of the iterative optimization process, making it difficult to reproduce the results or understand the underlying mechanisms.

3. The discussion on the relationship between the modality gap and intra-modal misalignment could be more in-depth. The paper mentions that a narrower modality gap diminishes the impact of intra-modal misalignment, but it does not explore the underlying reasons for this phenomenon. A more detailed analysis of how these two concepts interact would strengthen the paper's claims.

### Suggestions

To improve the introduction, the authors should provide a more detailed explanation of the modality gap, including visualizations of the feature space to illustrate how the gap manifests. They should also discuss whether the gap is consistent across different datasets and model architectures. For intra-modality misalignment, the authors should provide concrete examples of how this misalignment affects performance in specific tasks, such as image-to-image retrieval. For instance, they could show examples where semantically similar images are mapped far apart in the feature space due to intra-modality misalignment, leading to poor retrieval performance. This would make the motivation for the proposed method more compelling and easier to understand.

In the method section, the authors should provide a more detailed explanation of the optimization objectives used for OTI and OVI. They should include the specific loss functions, hyperparameter settings, and the iterative optimization process. It would also be beneficial to include an ablation study to show the sensitivity of the performance to different hyperparameter settings. Furthermore, the authors should discuss the computational cost of the proposed method and compare it to other existing methods. This would help readers understand the practical implications of using the proposed method. The paper should also include a discussion of the limitations of the proposed method, such as cases where it might not be effective or where it might be outperformed by other methods.

Finally, the discussion on the relationship between the modality gap and intra-modal misalignment should be expanded. The authors should explore the underlying reasons for why a narrower modality gap diminishes the impact of intra-modal misalignment. This could involve a more detailed analysis of the feature space and how the modality gap affects the alignment of intra-modal features. The authors could also explore the impact of different training strategies on the modality gap and intra-modal misalignment. This would provide a deeper understanding of the proposed method and its limitations, and it would also help guide future research in this area.

### Questions

1. Can you provide more details on the modality inversion techniques and how they were adapted from previous work?

2. How does the proposed method perform on other intra-modal tasks not covered in the experiments?

3. What are the limitations of the proposed method, and are there cases where it might not be effective or where other methods might be preferable?

### Rating

6

### Confidence

3

**********
