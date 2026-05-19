### Summary

This paper explores the effectiveness of different visual encoders within MLLMs. It finds that shallow layer features of CLIP are beneficial for fine-grained tasks, and DINOv2 performs well in MLLMs with an MLP layer for alignment. Based on these observations, this paper proposes COMM that integrates CLIP and DINOv2 with multi-level features merging, to enhance the visual capabilities of MLLMs. Experimental results demonstrate the superior performance of COMM compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper conducts an extensive investigation into the effectiveness of different visual encoders for MLLMs, which is valuable for the community.
2. The proposed COMM that integrates CLIP and DINOv2 with multi-level features merging is simple yet effective.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed COMM integrates CLIP and DINOv2 with multi-level features merging, which is a combination of existing approaches. The novelty is somewhat limited.
2. The COMM is based on ViT-Large. It would be better to compare different vision backbones, e.g., ViT-Huge.
3. In Table 4, COMM performs worse than FLAVA on VQAv2 and OK-VQA, which makes the proposed method less convincing.

### Suggestions

The paper's primary weakness lies in its limited novelty. While the integration of CLIP and DINOv2 with multi-level feature merging is a reasonable approach, it largely combines existing techniques without introducing significant conceptual advancements. The core idea of leveraging different layers of visual encoders for various tasks is not entirely new, and the specific implementation, while effective, does not represent a substantial leap in methodology. To strengthen the contribution, the authors could explore more innovative ways to combine these features, such as adaptive weighting schemes or attention mechanisms that dynamically adjust the contribution of each feature based on the input. Furthermore, a more thorough analysis of the feature space and the specific information captured by each layer would provide a deeper understanding of the method's effectiveness and potential for further improvement. The current approach feels like a straightforward combination rather than a novel synthesis of existing ideas.

Another area for improvement is the limited exploration of different vision backbones. The paper focuses solely on ViT-Large, which restricts the generalizability of the findings. It is crucial to evaluate the proposed method with other backbones, such as ViT-Huge, to assess its robustness and scalability. Different backbones may exhibit varying performance characteristics, and the effectiveness of the multi-level feature merging strategy could be dependent on the specific architecture. For instance, larger backbones might benefit more from the fine-grained features of DINOv2, while smaller backbones might be more sensitive to the computational overhead. A comprehensive evaluation across different backbones would provide a more complete picture of the method's strengths and limitations, and would also allow for a more direct comparison with other state-of-the-art models that utilize different backbones. This would also help to determine if the performance gains are specific to ViT-Large or if they generalize to other architectures.

Finally, the performance of COMM on VQAv2 and OK-VQA is a concern. The fact that it underperforms FLAVA on these benchmarks raises questions about the method's overall effectiveness. While the authors argue that COMM is designed for fine-grained tasks, the lower performance on these general VQA tasks suggests that the multi-level feature merging strategy may not be universally beneficial. A more detailed analysis of the failure cases on these benchmarks is needed to understand the limitations of the approach. It would be beneficial to investigate whether the performance difference is due to the training data, the model architecture, or the feature merging strategy itself. Furthermore, the authors should consider exploring alternative training strategies or data augmentation techniques to improve the performance on these tasks. The current results make it difficult to fully assess the practical value of the proposed method.

### Questions

Please see the weaknesses above.

### Rating

6

### Confidence

4

**********
