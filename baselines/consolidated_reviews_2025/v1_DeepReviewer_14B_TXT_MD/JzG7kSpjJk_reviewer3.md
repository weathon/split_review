### Summary

The paper proposes a new quantization method for LLMs, which is based on the observation that the outliers in activations will lead to higher sensitivity of weights. The paper proposes to use per-IC quantization to isolate the outliers. Furthermore, the paper proposes to adaptively choose between per-IC and per-OC based on the reconstruction error. The paper shows that the proposed method can improve the performance of LLMs on various benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a novel perspective on the weight sensitivity of LLMs and proposes a simple yet effective method to isolate the outliers.
3. The paper demonstrates the effectiveness of the proposed method on various benchmarks and shows that it can improve the performance of LLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed method. It would be helpful to provide some theoretical justification for why per-IC quantization can isolate the outliers and why adapting between per-IC and per-OC can improve the performance.
2. The paper does not compare the proposed method with other state-of-the-art quantization methods, such as AWQ and SmoothQuant. It is not clear how the proposed method compares to these methods in terms of performance and efficiency.

### Suggestions

The paper's primary weakness lies in its lack of theoretical grounding. While the empirical results are promising, the absence of a theoretical framework makes it difficult to fully understand the mechanisms behind the proposed per-IC quantization and its adaptive selection between per-IC and per-OC. A theoretical analysis should explore why quantizing along the input channel dimension effectively isolates outliers, perhaps by examining the statistical properties of activations and their impact on weight sensitivity. Furthermore, the adaptive selection process based on reconstruction error needs a more rigorous explanation. For instance, under what conditions does per-IC quantization outperform per-OC, and can these conditions be formalized? A theoretical treatment could involve analyzing the Hessian of the loss function with respect to the weights, and how this relates to the chosen quantization axis. Such analysis would not only strengthen the paper's claims but also provide a deeper understanding of the underlying principles.

Another significant limitation is the lack of comparison with other state-of-the-art quantization techniques. While the paper demonstrates improvements over a baseline, it fails to position the proposed method within the broader landscape of quantization methods for LLMs. Specifically, a comparison with methods like AWQ and SmoothQuant is crucial. AWQ, with its adaptive quantization scales, and SmoothQuant, with its smoothing techniques, represent important benchmarks in the field. The paper should include a detailed comparison of these methods, not only in terms of accuracy but also in terms of computational efficiency and memory footprint. This would involve reporting metrics such as inference latency, memory usage, and the number of operations required. Furthermore, the paper should discuss the trade-offs between the proposed method and these existing techniques, highlighting the scenarios where the proposed method is most effective and where it might fall short. This would provide a more comprehensive evaluation of the proposed method's practical utility.

Finally, the paper should also explore the sensitivity of the proposed method to different hyperparameter settings, such as the number of groups used in quantization. It would be beneficial to analyze how the performance of the method varies with different group sizes and provide guidelines for selecting appropriate values. Additionally, the paper should investigate the robustness of the method to different model architectures and datasets. This would involve testing the method on a wider range of LLMs and benchmarks, and reporting the results. Such an analysis would help to establish the generalizability of the proposed method and its applicability to different scenarios. Furthermore, the paper should also discuss the limitations of the proposed method and suggest potential directions for future research.

### Questions

1. Can the authors provide some theoretical analysis of the proposed method?
2. How does the proposed method compare to other state-of-the-art quantization methods, such as AWQ and SmoothQuant?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
