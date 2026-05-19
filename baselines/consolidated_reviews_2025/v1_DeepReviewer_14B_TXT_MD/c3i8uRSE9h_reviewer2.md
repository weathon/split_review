### Summary

This paper proposes a fast constrained sampling algorithm for pre-trained diffusion models. The authors propose to leverage the Jacobian of the denoising function w.r.t the noisy data for the optimization. The method is shown to be faster than prior works and achieve comparable results.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The method is fast and achieves good results on two tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The evaluation is limited. The method is only tested on two tasks and one dataset. It would be interesting to see if the method works on other tasks (e.g. colorization, image editing) and other models (SDXL, SD3).
- The method is not consistently better than prior works. For example, in super-resolution task, the method is not better than LDPS and PSLD. In terms of FID for inpainting, it is not the best.
- The method requires warm restarts for super-resolution but not for inpainting. Why is that?

### Suggestions

The paper would benefit from a more thorough evaluation across a wider range of tasks and models. While the authors demonstrate results on inpainting and super-resolution using Stable Diffusion v1.5, it is crucial to assess the method's generalizability. Specifically, testing on tasks like colorization and image editing would provide a more complete picture of the method's capabilities. Furthermore, evaluating the method on more recent models such as SDXL and SD3 is necessary to determine its applicability to state-of-the-art diffusion models. The current evaluation is limited in scope and does not fully demonstrate the robustness of the proposed approach. It would be beneficial to see results on diverse datasets beyond ImageNet to assess the method's performance under different data distributions. This would help to establish the method's practical utility and potential limitations.

It is also important to address the inconsistencies in performance compared to existing methods. The fact that the proposed method does not consistently outperform prior works like LDPS and PSLD in super-resolution raises concerns about its overall effectiveness. A more detailed analysis of the scenarios where the method underperforms is needed. The authors should investigate the reasons behind these performance differences and provide a more in-depth discussion of the trade-offs between speed and accuracy. Furthermore, the FID scores for inpainting, while competitive, are not the best, indicating that there is room for improvement in the quality of the generated images. A more thorough comparison with other state-of-the-art inpainting methods is needed to better understand the strengths and weaknesses of the proposed approach. The authors should also consider exploring different evaluation metrics to provide a more comprehensive assessment of the method's performance.

Finally, the need for warm restarts in super-resolution but not in inpainting requires further investigation and clarification. The authors should provide a more detailed explanation of the underlying reasons for this difference. It would be helpful to understand the specific characteristics of the super-resolution task that necessitate the use of warm restarts. A more thorough analysis of the optimization landscape for both tasks could provide valuable insights into this phenomenon. The authors should also explore alternative optimization strategies that could potentially eliminate the need for warm restarts in super-resolution. This would make the method more robust and easier to use in practice. Additionally, a more detailed explanation of the implementation details of the warm restarts would be beneficial for reproducibility.

### Questions

Please see weaknesses.

### Rating

3

### Confidence

3

**********
