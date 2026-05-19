### Summary

This paper proposes a retrieval-augmented test-time adaptation (TTA) method for vision-language models (VLMs), which leverages external knowledge from a web-scale image database to adapt VLMs to test data. The method uses fine-grained text descriptions to retrieve relevant external images and refine VLMs' predictions. Extensive evaluations on 17 datasets show that the proposed method outperforms state-of-the-art TTA methods by a large margin.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is novel and effective. It addresses the limitation of existing TTA methods that rely solely on the internal knowledge of VLMs by incorporating external knowledge from a web-scale image database.
2. The method fully exploits the bi-modality of VLMs by using fine-grained text descriptions for both retrieving relevant external images and refining VLMs' predictions.
3. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and its components, and the figures and tables are helpful for understanding the results.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires a large external image database, which may not be available in all scenarios. The reliance on a web-scale image database introduces a practical limitation, as access to such resources is not universally guaranteed. This dependence could hinder the method's applicability in resource-constrained environments or when dealing with sensitive data where external access is restricted. The paper should discuss the implications of this dependency and potential mitigation strategies, such as using smaller, curated datasets or exploring methods for generating synthetic data.
2. The method may be computationally expensive due to the need to retrieve and process external images. The computational overhead of retrieving and processing images from a large database could be significant, especially when dealing with high-resolution images or large batch sizes. The paper lacks a detailed analysis of the computational cost, including the time required for retrieval, feature extraction, and integration into the VLM. This analysis should consider the impact on different hardware configurations and provide insights into the method's scalability.

### Suggestions

The paper should explore the impact of the external image database's quality and diversity on the method's performance. While the authors mention using a web-scale database, they should investigate how the characteristics of this database affect the results. For example, does the performance degrade if the database contains noisy or irrelevant images? What is the minimum level of diversity required to achieve satisfactory results? A sensitivity analysis of the database's properties would provide valuable insights into the method's robustness and limitations. Furthermore, the authors should consider alternative strategies for scenarios where a large, high-quality database is not available. This could involve techniques such as data augmentation, synthetic data generation, or the use of smaller, domain-specific datasets. The paper should also discuss the trade-offs between the size and quality of the external database and the computational cost of retrieval and processing.

To address the computational concerns, the authors should provide a detailed breakdown of the time complexity of each step in their method, including image retrieval, feature extraction, and integration into the VLM. This analysis should consider the impact of different parameters, such as the number of retrieved images, the size of the image embeddings, and the batch size. The paper should also explore techniques for optimizing the computational efficiency of the method, such as using approximate nearest neighbor search algorithms for image retrieval, employing efficient feature extraction methods, and parallelizing the computation across multiple GPUs. A comparison of the computational cost of the proposed method with existing TTA methods would also be beneficial. The authors should also investigate the potential for caching retrieved images and features to reduce the computational overhead for repeated test samples.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. While the authors acknowledge the need for a large external image database, they should also address other potential limitations, such as the sensitivity of the method to the quality of the text descriptions used for retrieval, the potential for bias in the external database, and the generalizability of the method to different types of VLMs and datasets. A more comprehensive discussion of these limitations would provide a more balanced and realistic assessment of the method's strengths and weaknesses.

### Questions

1. How does the performance of the proposed method vary with the size and quality of the external image database?
2. What are the computational costs of the proposed method, and how do they compare to existing TTA methods?
3. How does the proposed method perform on datasets with different types of distribution shifts, such as covariate shift, concept shift, and semantic shift?

### Rating

8

### Confidence

4

**********
