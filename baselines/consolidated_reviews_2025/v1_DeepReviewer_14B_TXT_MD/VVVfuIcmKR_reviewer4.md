### Summary

This paper addresses the issue of intra-modal misalignment in pre-trained multi-modal Vision Language Models (VLMs) like CLIP, which are often used for tasks involving only one modality (e.g., image-to-image retrieval). The authors argue that the inter-modal contrastive loss used in training these models leads to a modality gap and misaligned intra-modal representations, causing suboptimal performance in intra-modal tasks. To address this, they propose a modality inversion approach that transforms native modality inputs into inter-modal representations, leveraging the model's inter-modal alignment capabilities. They introduce Optimization-based Visual Inversion (OVI) and adapt Optimization-based Textual Inversion (OTI) to map features from one modality to the other without requiring additional training data or adapters. Through extensive experiments on over fifteen datasets, they demonstrate that this inter-modal approach significantly outperforms traditional intra-modal baselines in tasks like image-to-image retrieval and text-to-text retrieval. They also show that reducing the modality gap or adding intra-modal loss during pre-training mitigates intra-modal misalignment.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper identifies and addresses a fundamental issue in how pre-trained VLMs are used for intra-modal tasks, highlighting the limitations of relying solely on intra-modal similarities.

2. The proposed modality inversion techniques (OVI and OTI) are novel and effective in transforming intra-modal tasks into inter-modal ones, allowing the model to leverage its inter-modal alignment capabilities.

3. The paper provides a thorough experimental evaluation across multiple datasets and tasks, demonstrating the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed modality inversion techniques are computationally expensive, requiring iterative optimization for each input. This limits the practical applicability of the method, especially for large-scale tasks or real-time applications. The iterative optimization, while effective, introduces a significant overhead that could hinder its use in scenarios where rapid processing is crucial. The computational cost scales linearly with the number of inputs, making it impractical for very large datasets or high-throughput systems.

2. The paper primarily focuses on CLIP-like models and does not explore the generalizability of the findings to other types of VLMs or architectures. It is unclear whether the observed intra-modal misalignment and the effectiveness of modality inversion would hold for models with different training objectives or architectures. The reliance on contrastive learning in CLIP might not be representative of all VLMs, and the proposed method's effectiveness could be highly dependent on this specific training paradigm.

3. While the paper demonstrates improved performance on intra-modal tasks, it does not provide a detailed analysis of the trade-offs between intra-modal and inter-modal approaches in different scenarios. The paper lacks a discussion on when it might be more appropriate to use traditional intra-modal methods despite their limitations. A more nuanced analysis of the performance characteristics of both approaches would be beneficial for practitioners.

4. The paper does not thoroughly explore the limitations of the proposed modality inversion techniques. For instance, it is unclear how the quality of the inverted features affects the performance of downstream tasks or whether there are specific types of inputs for which the inversion process fails. The sensitivity of the inversion process to hyperparameters and the potential for introducing artifacts or biases in the inverted features are not adequately addressed.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the proposed modality inversion techniques. Specifically, the authors should provide a breakdown of the time complexity of the iterative optimization process and compare it to the computational cost of traditional intra-modal methods. This analysis should include a discussion of the practical implications of this computational overhead, such as the impact on processing time for large datasets or real-time applications. Furthermore, the authors should explore potential strategies for reducing the computational cost of modality inversion, such as using more efficient optimization algorithms or approximating the inversion process. This would make the proposed method more practical and accessible for a wider range of applications. It would also be beneficial to investigate the trade-offs between computational cost and performance, allowing practitioners to make informed decisions about when to use modality inversion.

To strengthen the paper's claims about the generalizability of the findings, the authors should conduct experiments on a wider range of VLMs with different architectures and training objectives. This would help to determine whether the observed intra-modal misalignment and the effectiveness of modality inversion are specific to CLIP-like models or a more general phenomenon. The authors should also investigate the impact of different training objectives on the modality gap and the effectiveness of modality inversion. This would provide a more comprehensive understanding of the underlying mechanisms driving intra-modal misalignment and the conditions under which modality inversion is most effective. Additionally, the authors should explore the limitations of the proposed method when applied to models with different architectures, such as those that do not rely on contrastive learning.

Finally, the paper should provide a more detailed analysis of the trade-offs between intra-modal and inter-modal approaches in different scenarios. This analysis should include a discussion of the performance characteristics of both approaches, such as their robustness to noise, their sensitivity to hyperparameters, and their computational cost. The authors should also explore the limitations of the proposed modality inversion techniques, such as the potential for introducing artifacts or biases in the inverted features. This would provide a more nuanced understanding of the strengths and weaknesses of both approaches and help practitioners to make informed decisions about when to use each approach. The authors should also consider providing guidelines for choosing between intra-modal and inter-modal approaches based on the specific characteristics of the task and the available resources.

### Questions

1. How does the computational cost of the proposed modality inversion techniques compare to traditional intra-modal methods? Is it feasible for large-scale or real-time applications?

2. Can the proposed modality inversion techniques be extended to other types of VLMs or architectures that are not based on contrastive learning?

3. What are the limitations of the proposed modality inversion techniques? Are there specific types of inputs or tasks for which they are not effective?

4. How does the quality of the inverted features affect the performance of downstream tasks? Is there a way to measure or improve the quality of the inverted features?

### Rating

6

### Confidence

3

**********
