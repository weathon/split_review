### Summary

This paper proposes a new method for video enhancement, called ReBotNet. ReBotNet employs a dual-branch framework, where the first branch learns spatio-temporal features by tokenizing the input frames along the spatial and temporal dimensions, and the second branch improves temporal consistency by processing tokens extracted from individual frames. A common decoder then merges the features from the two branches to predict the enhanced frame. The authors also propose a recurrent training approach to efficiently enhance the current frame while improving temporal consistency. The paper evaluates the proposed method on multiple datasets and shows that it outperforms existing approaches with lower computations, reduced memory requirements, and faster inference time.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to understand.
2. The proposed method is novel and effective, achieving state-of-the-art performance on multiple datasets.
3. The paper provides extensive experiments and ablation studies to demonstrate the effectiveness of the proposed method.
4. The paper is well-organized and clearly presents the proposed method, experimental results, and analysis.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only evaluates the proposed method on synthetic datasets. It would be better to also evaluate the method on real-world datasets to show its practical applicability.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be better to provide a breakdown of the computational cost of each component of the method and compare it with other methods.
3. The paper does not discuss the limitations of the proposed method. It would be better to discuss the potential failure cases and the scenarios where the method may not perform well.

### Suggestions

The paper would benefit significantly from a more thorough evaluation on real-world datasets. While synthetic datasets offer controlled environments for testing, they often fail to capture the complexities and nuances of real-world video enhancement scenarios. Specifically, the paper should consider evaluating the proposed method on datasets that include a variety of real-world degradations, such as noise, blur, compression artifacts, and lighting variations. This would provide a more robust assessment of the method's practical applicability and its ability to generalize to unseen data. Furthermore, the evaluation should include a comparison with state-of-the-art methods on these real-world datasets to establish the method's performance in practical scenarios. The analysis should also include a discussion of the types of real-world degradations that the method handles well and those where it struggles, providing a more nuanced understanding of its capabilities.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost of each component of the proposed method. This should include the number of parameters, the number of floating-point operations (FLOPs), and the memory requirements for each module, such as the ConvNext-based encoder, the bottleneck mixer, and the individual frame mixers. This analysis should be presented in a table or a figure, allowing for a clear comparison with other methods. Furthermore, the authors should discuss the trade-offs between computational cost and performance, and how the proposed method achieves a balance between these two factors. This would provide a more complete understanding of the method's efficiency and its suitability for real-time applications. The analysis should also consider the impact of different hardware platforms on the computational cost, such as GPUs and CPUs.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of potential failure cases, such as scenarios with extreme motion, severe occlusions, or complex lighting conditions. The authors should also discuss the scenarios where the method may not perform well, such as videos with specific types of degradation or videos with low resolution. This discussion should be supported by examples from the experimental results, highlighting the limitations of the method. Furthermore, the authors should discuss potential avenues for future research to address these limitations, such as incorporating motion compensation or using more robust feature representations. This would provide a more complete and balanced view of the method's capabilities and limitations.

### Questions

Please refer to the weakness part.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
