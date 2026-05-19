### Summary

This paper proposes a two-stage text-video retrieval architecture, CrossTVR, which first uses a cosine similarity network to efficiently obtain text video candidate pairs. In the second stage, the proposed re-ranker is applied for fine-grained retrieval. Experimental results on text-video retrieval datasets demonstrate the effectiveness and scalability of the proposed re-ranker when combined with existing mainstream one-stage text-video retrieval approaches.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.
2. The paper is well-written and easy to follow.
3. The experiments are conducted on multiple datasets and compared with multiple baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is incremental. The proposed method mainly consists of two parts, a contrastive learning-based method and a cross-attention-based method, which have been widely used in text-video retrieval. The novelty of the proposed method is limited.
2. The paper is not well organized. The details of the proposed method are not clearly presented. For example, in the second stage, how to obtain the refined retrieval results is not clearly described. The authors should provide more details about the proposed method.
3. The experimental results are not convincing. The proposed method is only compared with a few baseline methods. More state-of-the-art methods should be compared to demonstrate the effectiveness of the proposed method.
4. The authors claim that the proposed method can scale to larger pre-trained vision models. However, the authors only use two vision encoders (ViT-B and ViT-G) to evaluate the proposed method. More experiments should be conducted to support the claim.

### Suggestions

The paper's primary weakness lies in its incremental nature and limited novelty. While the combination of contrastive learning and cross-attention is not entirely new, the specific implementation and its application to text-video retrieval could be more clearly articulated. The authors should provide a more detailed explanation of how their approach differs from existing methods that use similar components. For example, they could discuss the specific design choices of their cross-attention module and how it addresses the limitations of previous approaches. Furthermore, the paper lacks a thorough analysis of the computational complexity of the proposed method, especially when compared to existing state-of-the-art techniques. A detailed comparison of the computational cost, including training and inference time, would be beneficial to understand the practical implications of the proposed method.

To address the lack of clarity in the method description, the authors should provide a more detailed explanation of the second stage, particularly how the refined retrieval results are obtained. The current description is vague and does not provide sufficient information for readers to fully understand the proposed method. A step-by-step explanation of the process, including the specific operations performed on the attention weights and how they are used to refine the initial retrieval results, would be helpful. Additionally, the authors should provide a more detailed explanation of the token selector module and how it contributes to the overall performance of the proposed method. The paper would benefit from a more in-depth analysis of the impact of different token selection strategies on the final retrieval performance.

Finally, the experimental evaluation needs to be significantly strengthened. The authors should compare their method with a wider range of state-of-the-art text-video retrieval methods, including those that use more advanced techniques such as graph neural networks or transformer-based architectures. This would provide a more comprehensive evaluation of the proposed method's effectiveness and demonstrate its advantages over existing approaches. Furthermore, the authors should conduct more experiments with larger pre-trained vision models to support their claim of scalability. This would provide more convincing evidence that the proposed method can be effectively applied to real-world scenarios with larger and more complex datasets. The authors should also consider evaluating their method on a more diverse set of datasets to assess its generalizability.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
