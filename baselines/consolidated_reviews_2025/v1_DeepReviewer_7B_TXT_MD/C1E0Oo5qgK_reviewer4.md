### Summary

This paper identifies and quantifies the problem of model-fitting in guidance during diffusion sampling. The authors propose a simple but effective method called Compress Guidance, which reduces the number of timesteps that involve gradient calculation. This approach addresses a major challenge in applying guidance effectively to generative tasks. The experimental results demonstrate that Compress Guidance not only improves image quality but also significantly accelerates the overall process as shown in Fig. 1.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors clearly articulate the problem, provide a thorough analysis, and present compelling experimental results that support their claims.
2. The proposed method is simple yet effective. The authors demonstrate that Compress Guidance can improve image quality and reduce the required guidance timesteps by nearly 40%.
3. The paper addresses a significant challenge in the field of generative models. By reducing the computational cost of guidance, the authors make it more practical and accessible for a wider range of applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the problem of model-fitting in guidance during diffusion sampling. While the authors propose a solution, the paper could benefit from a more in-depth analysis of the theoretical underpinnings of this phenomenon. Specifically, the paper lacks a rigorous mathematical formulation of the model-fitting problem and how Compress Guidance mitigates it. A deeper dive into the optimization landscape and the convergence properties of the proposed method would strengthen the theoretical contribution.
2. The experiments are conducted on a limited set of datasets and models. While the results are promising, it would be beneficial to evaluate the method on a broader range of datasets and models to demonstrate its generalizability. For example, the paper should include experiments on more complex datasets with higher resolution images and different types of generative models, such as those based on transformers or other architectures. The current evaluation is not sufficient to establish the robustness of the proposed method.
3. The paper could benefit from a more detailed discussion of the limitations of the proposed method. While the authors acknowledge the trade-off between guidance effectiveness and computational efficiency, a more thorough analysis of the scenarios where Compress Guidance might fail or underperform would be valuable. For instance, it would be useful to explore the sensitivity of the method to different hyperparameter settings and the potential impact on the diversity of generated samples.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should provide a more rigorous mathematical analysis of the model-fitting problem in the context of diffusion models. This could involve deriving equations that explicitly model the guidance process and the resulting model-fitting behavior. Furthermore, the authors should explore the connection between the proposed Compress Guidance method and existing optimization techniques, such as adaptive learning rates or momentum-based methods. A theoretical analysis of how Compress Guidance affects the optimization landscape and the convergence properties of the model would be highly beneficial. This would provide a more solid understanding of why the method works and under what conditions it is most effective. The authors should also consider providing a formal definition of model-fitting in the context of diffusion models, which would help to clarify the problem and the proposed solution.

To address the limitations of the experimental evaluation, the authors should conduct experiments on a more diverse set of datasets and models. This should include datasets with varying characteristics, such as different image resolutions, object complexities, and data distributions. The authors should also evaluate the method on different types of generative models, including those based on transformers, normalizing flows, and other architectures. This would help to demonstrate the generalizability of the proposed method and its applicability to a wider range of generative modeling tasks. Furthermore, the authors should provide a detailed analysis of the computational cost of Compress Guidance, including the time and memory requirements. This would allow readers to better understand the trade-offs between guidance effectiveness and computational efficiency. The authors should also consider comparing their method with other existing techniques for reducing the computational cost of guidance, such as early stopping or adaptive guidance.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. This should include an analysis of the scenarios where Compress Guidance might fail or underperform. For example, the authors should explore the sensitivity of the method to different hyperparameter settings and the potential impact on the diversity of generated samples. The authors should also discuss the potential limitations of the method in terms of its applicability to different types of generative models and datasets. A thorough analysis of these limitations would provide a more balanced and realistic assessment of the proposed method and its potential impact. The authors should also consider providing guidelines for choosing the optimal number of guidance steps for different tasks and models.

### Questions

1. How does the proposed method perform on more complex datasets with higher resolution images?
2. Can the authors provide a more detailed analysis of the trade-off between guidance effectiveness and computational efficiency?
3. Are there any specific scenarios or types of generative models where Compress Guidance might not be as effective?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
