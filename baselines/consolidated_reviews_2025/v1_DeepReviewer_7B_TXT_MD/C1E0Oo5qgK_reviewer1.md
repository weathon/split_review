### Summary

This paper identifies and quantifies the problem of "model-fitting" in guidance during diffusion sampling, where excessive guidance can lead to the model overfitting to classifier features rather than generalizing to the intended conditions. The authors propose "Compress Guidance," a method that reduces the number of timesteps at which guidance is applied, thereby addressing the model-fitting issue. The paper demonstrates that Compress Guidance improves image quality and diversity while reducing the required guidance timesteps by nearly 40%.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written, with clear explanations of the problem and the proposed solution. The use of figures and tables effectively illustrates the concepts and results.
2. The authors provide a thorough analysis of the problem of model-fitting in diffusion models, using on-sampling and off-sampling losses to quantify the issue. The experimental results demonstrate the effectiveness of Compress Guidance in reducing the model-fitting problem and improving image quality and diversity.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's core idea of reducing the number of guidance steps is not entirely novel, as similar approaches have been explored in prior work. The authors should more clearly differentiate their method from existing techniques and highlight the specific advantages of their approach.
2. While the paper demonstrates the effectiveness of Compress Guidance on ImageNet datasets, it would be beneficial to evaluate the method on a wider range of datasets and tasks to assess its generalizability. The current evaluation is limited to image generation tasks, and it is unclear how well the method would perform on other types of data or tasks.
3. The paper lacks a detailed analysis of the computational cost associated with Compress Guidance. While the authors mention a reduction in the number of guidance timesteps, they do not provide a comprehensive comparison of the computational resources required by their method versus standard guidance. This makes it difficult to assess the practical benefits of the proposed approach.
4. The paper does not explore the sensitivity of Compress Guidance to different hyperparameter settings. A more thorough analysis of the method's performance under different hyperparameter configurations would be valuable for understanding its robustness and applicability.

### Suggestions

The authors should provide a more detailed comparison of their method with existing techniques that reduce the number of guidance steps. Specifically, they should discuss the differences in the underlying mechanisms, the types of guidance information used, and the computational trade-offs. For example, they could compare their approach with methods that use adaptive guidance schedules or those that selectively apply guidance based on the current state of the diffusion process. A more thorough discussion of these differences would help to clarify the novelty and specific advantages of Compress Guidance. Furthermore, the authors should provide a more detailed explanation of how the guidance is compressed and how this compression affects the quality of the generated images. This would help to better understand the mechanism behind the improved performance of Compress Guidance.

To strengthen the evaluation, the authors should extend their experiments to a wider range of datasets and tasks. This could include evaluating the method on datasets with different characteristics, such as different image resolutions or different types of content. Additionally, the authors should explore the performance of Compress Guidance on other types of tasks, such as image editing or inpainting. This would help to assess the generalizability of the method and its applicability to a wider range of problems. The authors should also provide a more detailed analysis of the computational cost of Compress Guidance, including the time and memory requirements. This analysis should compare the computational cost of Compress Guidance with that of standard guidance and other related methods. This would help to assess the practical benefits of the proposed approach and its suitability for different applications.

Finally, the authors should conduct a more thorough analysis of the sensitivity of Compress Guidance to different hyperparameter settings. This should include an investigation of how the performance of the method varies with different values of the hyperparameters, such as the number of guidance steps and the compression rate. The authors should also provide a discussion of the optimal hyperparameter settings for different tasks and datasets. This would help to better understand the robustness and applicability of the method and provide practical guidance for users. The authors should also consider providing a more detailed explanation of the theoretical underpinnings of Compress Guidance, which would help to better understand the method's behavior and its limitations.

### Questions

1. How does Compress Guidance compare to other methods for reducing the number of guidance steps in diffusion models? What are the specific advantages of your approach over existing techniques?
2. Can you provide more details on the computational cost of Compress Guidance? How does it compare to standard guidance in terms of time and memory requirements?
3. How sensitive is Compress Guidance to different hyperparameter settings? What are the optimal settings for different tasks and datasets?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
