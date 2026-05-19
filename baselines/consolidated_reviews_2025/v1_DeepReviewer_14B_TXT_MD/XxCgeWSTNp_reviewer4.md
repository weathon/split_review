### Summary

The paper proposes a parametric family of reverse-time SDEs for Lévy-Itô diffusion models, which rely on the fractional score function and have the same marginal densities as the forward SDE. The authors demonstrate the benefits of using these SDEs at inference in terms of generated samples quality on image generation task and verify that samples diversity does not suffer if we generate data with the proposed SDEs. They also train a Lévy-Itô text-to-speech model on a highly imbalanced dataset and evaluate its performance for speakers with different amount of training data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough theoretical analysis of the proposed method, including proofs of the main results.
3. The experimental results are comprehensive and convincing, demonstrating the effectiveness of the proposed method on both image and speech generation tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate the proposed method on CIFAR10, which is a relatively small and simple dataset. It would be beneficial to see how the method performs on more complex and realistic datasets, such as ImageNet or CelebA-HQ.
2. The authors mention that the proposed method is applicable to diverse domains, but only provide experimental results on image and speech generation tasks. It would be interesting to see how the method performs on other domains, such as text generation or 3D shape generation.

### Suggestions

The paper would significantly benefit from a more extensive evaluation on a wider range of datasets. While CIFAR10 provides a good starting point, it is crucial to assess the method's performance on more complex and higher-resolution datasets like ImageNet or CelebA-HQ. These datasets present challenges such as greater variability in object scale, pose, and background complexity, which would provide a more rigorous test of the proposed reverse-time SDEs. Furthermore, the evaluation should include a comparison against state-of-the-art generative models on these datasets to establish the relative performance of the proposed method. This would help to determine if the method can scale to more realistic scenarios and if it offers any advantages over existing approaches in terms of sample quality and diversity. The current evaluation, while promising, is not sufficient to fully validate the method's potential.

In addition to expanding the range of datasets, the authors should also explore the applicability of their method to other domains beyond image and speech generation. For example, evaluating the method on text generation tasks, such as those using the WikiText-103 dataset, would provide insights into its ability to handle sequential data and generate coherent text. Similarly, experiments on 3D shape generation using datasets like ShapeNet would help assess its performance in generating complex 3D structures. These experiments would not only demonstrate the versatility of the proposed method but also reveal potential limitations or areas for improvement. It would be particularly interesting to see how the method performs in domains where the data has different characteristics, such as high dimensionality or complex dependencies. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method, especially when applied to larger datasets and more complex models. This analysis should include a breakdown of the time spent on different steps of the sampling process, such as the computation of the fractional score function and the numerical integration of the reverse-time SDE. This would help users understand the trade-offs between sample quality and computational efficiency and make informed decisions about the applicability of the method in different scenarios. Furthermore, it would be beneficial to explore potential optimizations to reduce the computational cost of the method, such as using more efficient numerical integration schemes or approximating the fractional score function.

### Questions

1. How does the proposed method perform on larger and more complex datasets, such as ImageNet or CelebA-HQ?
2. Can the authors provide more details on the computational cost of the proposed method, especially when applied to larger datasets and more complex models?

### Rating

6

### Confidence

3

**********
