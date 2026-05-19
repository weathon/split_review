### Summary

This paper finds two unreasonable settings when constructing the edl, namely the setting of the prior weight and the optimization objective. Therefore, this paper proposes the R-EDL method by relaxing these unreasonable settings. The experimental results show that R-EDL is better than EDL.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper has a good motivation and the method is simple and effective.
2. This paper has comprehensive experiments.
3. This paper has good writing and is easy to read.

### Weaknesses

#### Some Related Works


#### comment

1. Although this paper has a good motivation, the novelty of this paper is limited. This paper finds two unreasonable settings when constructing the edl, and then proposes the R-EDL method by relaxing these settings. The method is very simple, and does not have enough contributions to the field.
2. This paper does not have particularly innovative methods. The author simply considers to optimize the edl based on two hyper-parameters. The method is simple and the performance is not significant enough.
3. The author needs to add ablation experiments on the hyper-parameters of the method.

### Suggestions

The paper's core contribution lies in identifying and addressing two specific limitations within the Evidential Deep Learning (EDL) framework: the prior weight and the optimization objective. While the proposed Relaxated-EDL (R-EDL) method offers improvements, the simplicity of the approach raises questions about its overall impact. To strengthen the paper, it would be beneficial to explore the theoretical underpinnings of why relaxing these specific settings leads to the observed performance gains. A more in-depth analysis of the prior weight's influence on the evidence-to-confidence mapping, perhaps through visualizations or mathematical analysis, could provide a more compelling argument for the method's significance. Furthermore, the paper should delve deeper into the optimization objective, explaining why minimizing the variance of the Dirichlet distribution might lead to overconfidence and how the proposed alternative addresses this issue. This would elevate the paper beyond a simple empirical study and provide a more robust theoretical foundation for the proposed method.

To further enhance the paper's contribution, the authors should consider a more comprehensive exploration of the hyper-parameter space. While the paper introduces two key hyper-parameters, a more detailed analysis of their interaction and impact on the model's performance is needed. Specifically, the paper should investigate the sensitivity of the model to different values of these hyper-parameters across various datasets and tasks. This could involve a grid search or a more sophisticated hyper-parameter optimization technique. The results of this analysis should be presented in a clear and concise manner, perhaps through tables or plots, to demonstrate the robustness of the proposed method and provide practical guidance for practitioners. Additionally, the paper should discuss the computational cost associated with tuning these hyper-parameters and how this cost compares to other uncertainty estimation methods.

Finally, the paper would benefit from a more thorough comparison with existing uncertainty estimation techniques. While the paper demonstrates improvements over the standard EDL, it would be valuable to compare the performance of R-EDL with other state-of-the-art methods, particularly those that also focus on addressing overconfidence in deep learning models. This comparison should not only focus on overall performance metrics but also consider other aspects such as computational efficiency, robustness to adversarial attacks, and interpretability of the uncertainty estimates. By providing a more comprehensive evaluation of R-EDL in the context of existing methods, the paper can better establish its contribution and highlight its potential advantages and limitations.

### Questions

1. The author needs to explain the reason for the decrease in performance of r-edl compared to edl in some cases.
2. The author needs to provide the specific values of the hyper-parameters in r-edl.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
