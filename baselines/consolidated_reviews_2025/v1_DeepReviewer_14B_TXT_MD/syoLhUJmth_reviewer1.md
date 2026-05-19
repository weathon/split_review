### Summary

This paper studies different vision encoders within MLLMs and finds that shallow layer features of CLIP and DINOv2 are good for fine-grained tasks. Thus, it proposes COMM that integrates CLIP and DINOv2 with multi-level features merging.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to understand.

2. The motivation is reasonable. The deep layer features are superior at global understanding while the shallow layer features are good for local understanding. Thus, it makes sense to use multi-level feature merging.

3. The experiments are extensive.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty is limited. It seems that the proposed COMM is a combination of existing approaches. 

2. There is no comparison between COMM and the vision encoder of FLAVA that also merges DINOv2 and CLIP features.

3. In Table 4, COMM performs worse than FLAVA on VQAv2 and OK-VQA, which makes the proposed method less convincing. The performance discrepancy on these tasks is significant, and the paper does not provide sufficient analysis to explain why COMM underperforms on these specific tasks while showing improvement on others. This lack of analysis makes it difficult to assess the true effectiveness of the proposed multi-level feature merging approach.

4. The COMM is based on ViT-Large. It would be better to compare different vision backbones, e.g., ViT-Huge. The absence of experiments with different backbone sizes limits the generalizability of the findings and makes it unclear whether the proposed method's performance is robust across different model scales. This is a crucial aspect to consider for practical applications and further research.

### Suggestions

The paper should provide a more in-depth analysis of the performance differences between COMM and FLAVA, especially on VQAv2 and OK-VQA. It is not sufficient to simply state that COMM is designed for fine-grained tasks and FLAVA is trained on more data. A detailed investigation into the specific types of questions and images where COMM struggles compared to FLAVA is needed. This could involve analyzing the error cases and identifying patterns in the failures. For example, are there specific types of visual reasoning or question-comprehension tasks where COMM's multi-level feature merging approach is less effective? Furthermore, the authors should explore whether the training data or the model architecture of FLAVA contributes more to its superior performance on these tasks. This analysis should include ablations to isolate the impact of different components.

To address the concern about the backbone size, the authors should conduct experiments with different vision encoder backbones, such as ViT-Huge, and report the performance on all the tasks. This would help to determine whether the performance of COMM is consistent across different model scales. If the performance of COMM degrades or improves significantly with a larger backbone, it would provide valuable insights into the scalability and robustness of the proposed method. Additionally, the authors should analyze the computational cost and memory requirements of using different backbone sizes to provide a comprehensive evaluation of the trade-offs. This analysis should also consider the impact of different backbone sizes on the training time and convergence rate.

Finally, the paper should include a more detailed comparison with FLAVA, specifically focusing on the feature merging strategies. While the paper mentions that COMM integrates DINOv2 and CLIP features, it does not provide a detailed comparison of the specific merging techniques used in both methods. A thorough analysis of the differences in the merging strategies, such as the layers used for merging, the fusion techniques, and the training objectives, would help to better understand the advantages and disadvantages of each approach. This comparison should also include an analysis of the computational complexity and memory requirements of the different merging strategies. This would provide a more comprehensive understanding of the proposed method and its relation to existing approaches.

### Questions

See Weaknesses.

### Rating

5

### Confidence

4

**********
