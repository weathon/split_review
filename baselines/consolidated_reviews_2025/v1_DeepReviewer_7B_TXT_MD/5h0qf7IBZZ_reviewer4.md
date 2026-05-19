### Summary

This paper proposes a new method for distilling knowledge from large language models to smaller language models. The method is based on minimizing reverse Kullback-Leibler (KL) divergence instead of forward KL divergence. The authors also propose several techniques to stabilize and accelerate training. The proposed method is evaluated on various generative language models and shows good performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and effective.
- The paper is well-written and easy to follow.
- The experiments are comprehensive and show good performance.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is incremental. It is not clear what the key factors that lead to the performance gain.
- The paper claims that the proposed MiniLLM produces more precise responses. It would be great if the authors could provide some examples to support this claim.

### Suggestions

The paper introduces a method for knowledge distillation using reverse KL divergence, which is a novel approach. However, the paper lacks a thorough analysis of why this method outperforms standard forward KL divergence based distillation. It would be beneficial to include ablation studies that isolate the impact of the reverse KL divergence and the proposed stabilization techniques. For example, the authors could compare the performance of their method with a baseline that uses forward KL divergence without the proposed stabilization techniques. This would help to clarify the specific contributions of each component of the proposed method. Furthermore, it would be useful to analyze the training dynamics of the proposed method, such as the convergence rate and the stability of the training process. This could provide insights into the reasons for the observed performance gains.

To support the claim that MiniLLM produces more precise responses, the authors should provide concrete examples that illustrate the differences between MiniLLM and the baseline methods. These examples should focus on scenarios where MiniLLM demonstrates a clear advantage in terms of response quality. For instance, the authors could present cases where the baseline models generate responses that are either too verbose, contain factual inaccuracies, or fail to capture the nuances of the input prompt. In contrast, the authors should highlight instances where MiniLLM generates more concise, accurate, and contextually relevant responses. These examples should be carefully selected to highlight the specific strengths of MiniLLM, and should include both quantitative metrics and qualitative analysis. Furthermore, it would be beneficial to analyze the types of errors made by each model, and to discuss the potential reasons for these errors.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the experimental results are promising, it is important to acknowledge the potential shortcomings of MiniLLM. For example, the authors could discuss the computational cost of training MiniLLM, or the potential for overfitting to the training data. It would also be valuable to explore the generalizability of MiniLLM to different datasets and tasks. A thorough discussion of these limitations would provide a more balanced and nuanced view of the proposed method, and would help guide future research in this area.

### Questions

See above.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
