### Summary

This paper proposes the Adaptive Prompt Prototype Learning (APPLe) method, which employs multiple prompts as class prototypes to significantly enhance the zero-shot performance of CLIP. To mitigate noise and flaws within the prompts, an adaptive attention mechanism is designed, assigning lower confidence to logits from less representative prototypes and higher confidence to those that are accurate and representative.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The motivation is clear and the paper is well written.
2. The proposed method is simple and effective.
3. The experimental evaluation is thorough and comprehensive.

### Weaknesses

#### Some Related Works

[1] Prototype-based multi-modal prompt learning for vision-language models.
[2] Prompt learning with optimal transport for vision-language models.

#### comment

1. The technical novelty is somewhat limited. The idea of prototype-based prompt learning is not entirely new. For example, [1] proposes a similar approach, although it is not clear how the two methods compare technically.
2. The experimental comparison is not comprehensive. While Table 1 presents results for several methods, it is unclear how APPLe compares to other recent approaches, such as [2]. Specifically, the comparison lacks a detailed analysis of the computational cost and efficiency of APPLe relative to these other methods. The paper should include a more thorough comparison of the computational resources required by APPLe and how it scales with the number of prototypes and classes.

### Suggestions

The paper should provide a more detailed technical comparison with existing prototype-based methods, such as the one mentioned in [1]. This comparison should go beyond a high-level overview and delve into the specific technical differences in how prototypes are generated, used, and optimized. For instance, the paper could discuss how the adaptive attention mechanism in APPLe differs from the prototype update strategies in other methods. A more granular analysis of the mathematical formulations and algorithmic steps would help clarify the novelty of the proposed approach. Furthermore, the authors should include a discussion of the limitations of their method, such as potential sensitivity to the initial prompt selection or the computational cost of the adaptive attention mechanism. This would provide a more balanced and comprehensive view of the proposed method.

To address the lack of comprehensive experimental comparison, the authors should include a more detailed analysis of the computational cost and efficiency of APPLe. This should include a comparison of the training and inference time, as well as the memory requirements, with other recent approaches. The paper should also investigate how the performance of APPLe scales with the number of prototypes and classes. This analysis should include a discussion of the trade-offs between performance and computational cost. For example, the authors could explore how the number of prototypes affects the accuracy and the computational resources required. This would provide a more practical perspective on the applicability of the proposed method. Additionally, the authors should consider including ablation studies to demonstrate the effectiveness of each component of APPLe, such as the adaptive attention mechanism and the multiple prompt prototypes.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include a discussion of the potential sensitivity of APPLe to the initial prompt selection, the computational cost of the adaptive attention mechanism, and the scalability of the method to large datasets. The authors should also discuss the potential impact of the choice of the prototype decorrelation loss on the performance of the method. A more detailed analysis of these limitations would provide a more balanced and comprehensive view of the proposed method and help guide future research in this area. The authors should also consider including a discussion of potential future research directions, such as exploring different types of prototypes or incorporating other forms of attention mechanisms.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
