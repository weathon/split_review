### Summary

This paper proposes a novel method called Compress Guidance for improving the efficiency of conditional diffusion models. The authors observe that applying guidance throughout the entire sampling process is often unnecessary and can even be counterproductive, leading to a "model-fitting" issue where the generated samples are overly tailored to the guidance model's parameters. 

The key idea of Compress Guidance is to reduce the number of timesteps where guidance is applied during sampling. The authors argue that the guidance loss is primarily active in the early stages of the sampling process, and it becomes less significant as the image structure emerges. Therefore, they propose to concentrate the guidance steps in the early stages and skip guidance in the later stages. 

This approach leads to several benefits:
1) Improved image quality and diversity: By reducing the model-fitting issue, Compress Guidance generates images that are more faithful to the desired conditions and exhibit greater diversity.
2) Reduced computational cost: Applying guidance at fewer timesteps significantly speeds up the sampling process.
3) Better generalization: The generated samples are less specific to the guidance model's features and generalize better to different classifiers.

The authors provide extensive experimental results on various datasets (ImageNet, MSCOCO) and tasks (label-conditional generation, text-to-image generation) to validate the effectiveness of their method. They demonstrate improvements in image quality, diversity, and computational efficiency compared to baseline methods. The authors also provide theoretical analysis and ablation studies to support their claims.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1) Novel observation and solution to the model-fitting issue: The paper identifies an important problem in conditional diffusion models and proposes an effective solution that improves both image quality and efficiency.
2) Comprehensive theoretical analysis and experimental validation: The authors provide thorough theoretical justification for their approach, along with extensive experiments on various datasets and tasks to demonstrate its effectiveness.
3) Significant improvement in efficiency: The proposed method achieves substantial reductions in computational cost while maintaining or improving image quality.
4) Clear writing and presentation: The paper is well-written, with clear explanations of the problem, methodology, and results.

### Weaknesses

#### Some Related Works


#### comment

1) The paper primarily focuses on improving the efficiency of single-condition generation. It's not clear how well the proposed method would scale to more complex scenarios with multiple conditions or iterative refinement processes. Specifically, the paper does not explore how the method would perform when multiple conditions are applied sequentially or when the generation process requires multiple iterations to converge to a high-quality image. This limits the applicability of the method to more complex real-world scenarios.
2) While the authors demonstrate improvements in image quality, it would be beneficial to explore the potential trade-offs between efficiency gains and image quality in more detail. For example, how does the proposed method perform on extremely high-resolution images or when generating images with very fine-grained details? The paper lacks a thorough analysis of the method's performance under these challenging conditions, making it difficult to assess its robustness and limitations. It is unclear if the observed improvements hold across a wide range of image complexities and resolutions.
3) The paper primarily focuses on classifier guidance and classifier-free guidance. It would be interesting to investigate the applicability of Compress Guidance to other types of guidance, such as attention-based guidance or feature-based guidance. The current scope of the paper is limited, and it does not explore how the proposed method could be adapted to other guidance mechanisms that are commonly used in diffusion models. This limits the generalizability of the findings.

### Suggestions

The authors should investigate the performance of Compress Guidance in more complex scenarios, such as multi-conditional generation and iterative refinement processes. This could involve experiments where multiple conditions are applied sequentially, or where the generation process is iterated multiple times to improve image quality. It would be beneficial to analyze how the method's efficiency and image quality are affected in these scenarios. For example, the authors could explore how the number of guidance steps affects the convergence rate and the final image quality when multiple conditions are involved. Furthermore, the authors should provide a more detailed analysis of the trade-offs between efficiency and image quality, particularly when generating high-resolution images or images with fine-grained details. This could involve experiments with varying levels of compression and a more thorough evaluation of image quality metrics, such as perceptual quality and structural similarity. It would also be useful to explore the limitations of the method and identify the conditions under which it performs best. This analysis should include a discussion of the potential for artifacts or degradation in image quality when the method is pushed to its limits.

To broaden the scope of the paper, the authors should investigate the applicability of Compress Guidance to other types of guidance, such as attention-based guidance or feature-based guidance. This could involve adapting the method to work with different guidance mechanisms and evaluating its performance on a range of tasks. For example, the authors could explore how Compress Guidance performs when used with attention-based guidance in models like DiT, or with feature-based guidance in models like Stable Diffusion. This would demonstrate the generalizability of the method and its potential for wider adoption. The authors should also provide a more detailed analysis of the theoretical underpinnings of Compress Guidance, including a discussion of why it is effective in reducing the model-fitting issue. This could involve a more in-depth analysis of the loss landscape and the dynamics of the sampling process. A deeper theoretical understanding would help to further validate the method and provide insights into its limitations.

Finally, the authors should consider including a more comprehensive comparison with other acceleration techniques for diffusion models. This could involve comparing Compress Guidance with methods such as progressive distillation or consistency models. This would help to contextualize the method's performance and highlight its advantages and disadvantages compared to existing approaches. The authors should also provide a more detailed analysis of the computational cost of the method, including the time required for training and inference. This would help to assess the practical feasibility of the method and its potential for real-world applications. The authors should also discuss the potential for further optimization of the method, such as using more efficient guidance mechanisms or adaptive step size control.

### Questions

1) How does the proposed method compare to other acceleration techniques for diffusion models, such as progressive distillation or consistency models?
2) Can the authors provide more insights into the theoretical underpinnings of Compress Guidance? For example, why does it effectively mitigate the model-fitting issue?
3) How does the performance of Compress Guidance vary with different diffusion model architectures or parameter settings?

### Rating

6

### Confidence

4

**********
