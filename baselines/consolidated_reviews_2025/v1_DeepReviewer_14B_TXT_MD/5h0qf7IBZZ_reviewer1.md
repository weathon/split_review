### Summary

This paper focuses on the knowledge distillation (KD) of LLMs. The authors propose to use reverse KL instead of forward KL that is used in existing KD approaches. They provide an optimization approach with policy gradient and some additional techniques such as single-step decomposition, teacher-mixed sampling, and length normalization. The proposed approach is tested on three model families and evaluated with multiple datasets and metrics.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed approach is straightforward and intuitive.
- The choice of reverse KL instead of forward KL for KD of LLMs makes sense to avoid overestimating the low-probability regions of the teacher distribution.
- The empirical results are strong.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed approach might be limited as using reverse KL instead of forward KL has been explored in some KD approaches such as Tailor, which is cited in this paper.
- Some important baselines are missing. The authors should compare the proposed approach with some existing KD approaches such as Tailor and GKD that use different divergence metrics. In addition, the authors should also compare their approach with some other KD baselines for LLM such as Mini-1.3B, which achieves better performance than the proposed approach in Table 1.

### Suggestions

The paper's core idea of using reverse KL divergence for knowledge distillation (KD) of large language models (LLMs) is interesting, but the novelty needs to be more clearly established. While the authors cite Tailor, they should provide a more detailed comparison of their approach with Tailor's specific methodology, highlighting the differences in the training algorithm, optimization techniques, and the specific problem being addressed. A more thorough discussion of how the proposed method differs from Tailor's approach, especially in the context of LLMs, is needed. For example, the paper should clarify whether the single-step decomposition, teacher-mixed sampling, and length normalization techniques are novel or adapted from existing methods, and how they contribute to the overall performance gains. Furthermore, a more detailed analysis of the computational cost of the proposed method compared to Tailor would be beneficial.

In addition to Tailor, the paper should include comparisons with other relevant KD methods, such as GKD, which also explores alternative divergence metrics for KD. The authors should discuss why these methods were not included in the experimental evaluation and how they believe their approach compares to these methods in terms of performance and computational efficiency. The paper should also include a more detailed discussion of the limitations of the proposed method, such as the potential for mode collapse when using reverse KL divergence, and how the proposed method addresses these limitations. The authors should also provide a more detailed analysis of the impact of the hyperparameters on the performance of the proposed method, and how these hyperparameters were chosen.

Finally, the paper should include a more thorough comparison with other KD baselines for LLMs, such as Mini-1.3B. The authors should not only report the performance of Mini-1.3B but also provide a detailed analysis of the differences in the training methodology, model architecture, and the specific tasks being addressed. The paper should also discuss why the proposed method does not outperform Mini-1.3B in Table 1 and how the proposed method could be improved to achieve better performance. The authors should also consider including additional evaluation metrics, such as perplexity or BLEU score, to provide a more comprehensive evaluation of the proposed method.

### Questions

- Why do the authors choose reverse KL instead of other divergence metrics such as TVD in Tailor and GKD in knowledge distillation of LLMs? What are the benefits and drawbacks?
- How does the proposed approach compare with Tailor and GKD?
- How does the proposed approach compare with Mini-1.3B?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
