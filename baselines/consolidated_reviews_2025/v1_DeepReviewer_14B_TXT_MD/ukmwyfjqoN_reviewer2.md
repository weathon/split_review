### Summary

The paper proposes a fast video restoration method that can be applied to real-time video enhancement. The proposed method, called ReBotNet, employs a dual-branch framework. The first branch learns spatio-temporal features by tokenizing the input frames along the spatial and temporal dimensions using a ConvNext-based encoder and processing these abstract tokens using a bottleneck mixer. To further improve temporal consistency, the second branch employs a mixer directly on tokens extracted from individual frames. A common decoder then merges the features form the two branches to predict the enhanced frame. In addition, the paper proposes a recurrent training approach where the last frame’s prediction is leveraged to efficiently enhance the current frame while improving temporal consistency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method achieves state-of-the-art performance with low latency on two new datasets.
- The paper proposes two new datasets for video enhancement. These datasets contain multiple synthetic degradations, which is more practical in real-world scenarios.
- The paper provides extensive experiments and ablation studies to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only evaluates the proposed method on synthetic datasets. It would be better to also evaluate the method on real-world datasets to show its practical applicability.
- The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be better to provide a breakdown of the computational cost of each component of the method and compare it with other methods.
- The paper does not discuss the limitations of the proposed method. It would be better to discuss the potential failure cases and the scenarios where the method may not perform well.

### Suggestions

The paper should include a more thorough evaluation on real-world datasets to demonstrate the practical applicability of the proposed method. While synthetic datasets are useful for controlled experiments, they often fail to capture the complexities and nuances of real-world video degradation. The authors should consider using existing real-world video enhancement datasets, or creating a new one, that includes a variety of degradation types, such as noise, blur, and compression artifacts. This would provide a more comprehensive assessment of the method's robustness and generalizability. Furthermore, the evaluation should include a comparison with state-of-the-art methods on these real-world datasets to establish the method's performance in practical scenarios. The analysis should also include a discussion of the types of real-world degradations that the method handles well and those where it struggles, providing a more nuanced understanding of its capabilities.

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost of each component of the proposed method. This should include the number of parameters, the number of floating-point operations (FLOPs), and the memory requirements for each module, such as the ConvNext-based encoder, the bottleneck mixer, and the individual frame mixers. This analysis should be presented in a table or a figure, allowing for a clear comparison with other methods. Furthermore, the authors should discuss the trade-offs between computational cost and performance, and how the proposed method achieves a balance between these two factors. This would provide a more complete understanding of the method's efficiency and its suitability for real-time applications. The analysis should also consider the impact of different hardware platforms on the computational cost, such as GPUs and CPUs.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of potential failure cases, such as scenarios with extreme motion, severe occlusions, or complex lighting conditions. The authors should also discuss the scenarios where the method may not perform well, such as videos with specific types of degradation or videos with low resolution. This discussion should be supported by examples from the experimental results, highlighting the limitations of the method. Furthermore, the authors should discuss potential avenues for future research to address these limitations, such as incorporating motion compensation or using more robust feature representations. This would provide a more complete and balanced view of the method's capabilities and limitations.

### Questions

- How does the proposed method perform on real-world datasets?
- What is the computational complexity of the proposed method compared to other methods?
- What are the limitations of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
