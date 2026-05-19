### Summary

This paper proposes a two-stage text-video retrieval framework. In the first stage, it uses a contrastive learning-based method to obtain an initial retrieval result. In the second stage, it introduces a cross-attention-based method to refine the initial retrieval results. The proposed method is evaluated on five text-video retrieval datasets, and the experimental results show that the proposed method outperforms the baseline methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method is evaluated on five text-video retrieval datasets.
2. The proposed method outperforms the baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is incremental. The proposed method mainly consists of two parts, a contrastive learning-based method and a cross-attention-based method, which have been widely used in text-video retrieval. The novelty of the proposed method is limited.
2. The paper is not well organized. The details of the proposed method are not clearly presented. For example, in the second stage, how to obtain the refined retrieval results is not clearly described. The authors should provide more details about the proposed method.
3. The experimental results are not convincing. The proposed method is only compared with a few baseline methods. More state-of-the-art methods should be compared to demonstrate the effectiveness of the proposed method.
4. The authors claim that the proposed method can scale to larger pre-trained vision models. However, the authors only use two vision encoders (ViT-B and ViT-G) to evaluate the proposed method. More experiments should be conducted to support the claim.

### Suggestions

The paper would benefit significantly from a more thorough explanation of the second stage of the proposed method. Specifically, the mechanism by which the cross-attention module refines the retrieval results needs to be detailed. The authors should clarify how the attention weights are used to adjust the initial retrieval scores and how this process leads to improved accuracy. For example, are the attention weights directly added to the scores, or is there a more complex transformation involved? A clear mathematical formulation of this process would greatly enhance the paper's clarity and allow for a more rigorous evaluation of the method's effectiveness. Furthermore, the authors should provide a more detailed explanation of the token selector module and how it contributes to the overall performance. It is not clear how the token selector is trained and how it selects the most informative tokens for the cross-attention module. A more detailed description of the token selector's architecture and its training procedure is necessary.

To strengthen the experimental evaluation, the authors should include comparisons with more state-of-the-art text-video retrieval methods. The current comparisons are limited and do not fully demonstrate the advantages of the proposed method over existing approaches. The authors should consider including methods that use more advanced techniques, such as those based on transformer architectures or graph neural networks. Additionally, the authors should provide a more detailed analysis of the experimental results, including ablation studies to evaluate the contribution of each component of the proposed method. For example, it would be useful to see how the performance of the method changes when the cross-attention module is removed or when different token selection strategies are used. This would help to better understand the importance of each component and to identify potential areas for improvement. The authors should also provide more details about the hyperparameter settings used in the experiments and justify their choices.

Finally, the authors should provide more evidence to support their claim that the proposed method can scale to larger pre-trained vision models. While the use of ViT-B and ViT-G is a good starting point, it is not sufficient to demonstrate the scalability of the method. The authors should consider conducting experiments with even larger vision encoders, such as ViT-L or ViT-H, to show that the method can effectively leverage the increased capacity of these models. Furthermore, the authors should analyze the computational cost of the proposed method when using larger vision encoders and discuss the trade-offs between performance and computational resources. This would provide a more comprehensive evaluation of the method's scalability and practical applicability.

### Questions

Please refer to the weakness.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
