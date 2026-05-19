### Summary

This paper proposes a new two-stage text-video retrieval architecture, CrossTVR, which first uses a cosine similarity network to obtain the top-k candidates and then applies a multi-grained cross-attention module to refine the retrieval results. Experiments on five text-video retrieval benchmarks demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The proposed method is a simple combination of existing techniques. The core idea of using a two-stage approach, with an initial coarse retrieval followed by a refinement stage, is not new in the field of text-video retrieval. The specific implementation of multi-grained cross-attention, while effective, does not introduce a fundamentally novel mechanism. The paper lacks a detailed analysis of how this specific combination of existing techniques leads to a significant performance boost, beyond what could be expected from the individual components.
2. The experiments are insufficient. The authors only compare their method with a few baseline methods, such as TS2Net and CLIP-ViP. More recent and advanced methods should be included for a comprehensive evaluation. The lack of comparison with state-of-the-art methods makes it difficult to assess the true contribution of the proposed approach. The experimental setup also lacks details on hyperparameter tuning and sensitivity analysis, which are crucial for reproducibility and understanding the method's robustness.
3. The authors claim that the proposed method can scale to larger pre-trained vision models. However, they only use ViT-B/32 and ViT-G/14 as the visual encoder. More experiments should be conducted to support this claim. The limited range of visual encoders tested does not provide sufficient evidence for the scalability claim. The paper should include experiments with larger and more recent vision models to demonstrate the generalizability of the proposed method.

### Suggestions

The paper would benefit significantly from a more thorough analysis of the proposed method's novelty. While the combination of existing techniques is not inherently problematic, the authors need to provide a more in-depth explanation of why this specific combination leads to a significant performance improvement. This should include a detailed ablation study that examines the contribution of each component, such as the initial coarse retrieval stage and the multi-grained cross-attention module. The authors should also explore alternative implementations of the cross-attention module to demonstrate the robustness of their design choices. Furthermore, a more detailed comparison with existing methods, including a discussion of the differences in implementation and performance, would be beneficial. This would help to clarify the specific advantages of the proposed approach over existing state-of-the-art methods.

To address the insufficient experiments, the authors should include a more comprehensive evaluation of their method. This should involve comparing their method with a wider range of recent and advanced text-video retrieval methods. The experimental setup should also include a detailed description of hyperparameter tuning and sensitivity analysis. This would help to ensure the reproducibility of the results and provide a more robust evaluation of the method's performance. The authors should also consider using a more diverse set of datasets to evaluate the generalizability of their method. This would help to demonstrate the method's effectiveness across different scenarios and datasets. The paper should also include a discussion of the limitations of the proposed method and potential areas for future research.

Finally, the authors should provide more evidence to support their claim of scalability to larger pre-trained vision models. This should include experiments with a wider range of visual encoders, including larger and more recent models. The paper should also include a detailed analysis of the computational cost of the proposed method when using different visual encoders. This would help to demonstrate the method's scalability and its potential for use in real-world applications. The authors should also discuss the limitations of their approach in terms of computational resources and potential areas for future research in this direction.

### Questions

Please refer to the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
