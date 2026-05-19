### Summary

This paper proposes a method called Probability Distribution Estimation (PDE) to estimate full distributions from partial observations, enabling white-box text detection methods to proprietary models. The authors claim that PDE with latest LLMs performs significantly better than its counterparts in terms of accuracy, efficiency, and robustness, highlighting the benefits of using latest LLMs as detectors. The paper is well-written and easy to follow, and the experimental results are comprehensive and convincing. The authors also discuss the limitations of their method and suggest future research directions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors propose a novel method to estimate full distributions from partial observations, which is a creative solution to the problem of using white-box methods with proprietary models.
2. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup.
3. The experimental results are comprehensive and convincing. The authors evaluate the proposed method on multiple datasets and compare it with several baselines. The results show that the proposed method outperforms the baselines in terms of accuracy, efficiency, and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that PDE with latest LLMs performs significantly better than its counterparts in terms of accuracy, efficiency, and robustness, but there is no significant improvement in accuracy in Table 2. The authors should provide more evidence to support their claim.
2. The authors should provide more details about the experimental setup, such as the hardware and software used, the parameter settings, and the evaluation metrics. This would help to ensure the reproducibility of the results.
3. The authors should discuss the limitations of the proposed method and suggest future research directions. This would help to provide a more balanced and comprehensive view of the work.

### Suggestions

The paper would benefit from a more thorough analysis of the accuracy improvements claimed by the authors. While the authors state that their method achieves significantly better accuracy, the results presented in Table 2 do not clearly support this claim. Specifically, the differences in accuracy between the proposed method and the baselines appear to be marginal in many cases. To strengthen their argument, the authors should provide a more detailed statistical analysis of the results, including confidence intervals or p-values, to demonstrate the significance of the observed differences. Furthermore, it would be beneficial to include a more granular breakdown of the accuracy results, perhaps by dataset or by type of text, to identify specific scenarios where the proposed method excels. This would provide a more nuanced understanding of the method's strengths and weaknesses and would allow for a more informed assessment of its overall performance.

To enhance the reproducibility of the results, the authors should provide a more detailed description of the experimental setup. This should include specific information about the hardware used, such as the type of GPUs and CPUs, as well as the software environment, including the versions of the programming languages and libraries used. Furthermore, the authors should provide a detailed explanation of the parameter settings used for each method, including the learning rates, batch sizes, and any other relevant hyperparameters. The evaluation metrics used should also be clearly defined, and the authors should justify their choice of metrics. For example, if AUROC is used, the authors should explain why it is more appropriate than other metrics, such as F1-score or accuracy. Providing these details would allow other researchers to replicate the experiments and verify the results, which is crucial for the advancement of the field.

Finally, the authors should provide a more comprehensive discussion of the limitations of their proposed method. While the paper mentions some limitations, it would be beneficial to explore these in more detail. For example, the authors could discuss the computational cost of their method, its sensitivity to different parameter settings, or its performance on different types of text. Additionally, the authors should suggest specific future research directions that could address these limitations. This could include exploring alternative methods for probability distribution estimation, investigating the use of different types of models, or developing methods to improve the robustness of the approach. By providing a more balanced and comprehensive view of their work, the authors would enhance the overall impact of their paper.

### Questions

1. Can the authors provide more details about the experimental setup, such as the hardware and software used, the parameter settings, and the evaluation metrics?
2. Can the authors provide more evidence to support their claim that PDE with latest LLMs performs significantly better than its counterparts in terms of accuracy, efficiency, and robustness?
3. Can the authors discuss the limitations of the proposed method and suggest future research directions?

### Rating

6

### Confidence

3

**********
