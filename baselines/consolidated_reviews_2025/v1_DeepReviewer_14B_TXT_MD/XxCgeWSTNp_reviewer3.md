### Summary

This paper proposes a new sampling method for Levy-Ito diffusion models. The authors introduce a parametric family of reverse-time SDEs that rely only on the fractional score function and have the same marginal densities as the forward SDE. This new reverse dynamics allows for improved performance when the number of function evaluations is limited, without sacrificing sample diversity. The authors also demonstrate the advantages of Levy-Ito diffusion models on imbalanced datasets through experiments on image and speech generation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the proposed method, showing that the solutions of the reverse SDEs have the same marginal densities as the forward SDE.
3. The experimental results demonstrate the effectiveness of the proposed method in improving the performance of Levy-Ito diffusion models when the number of function evaluations is limited.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate the proposed method on CIFAR10, which is a relatively small and simple dataset. It would be beneficial to see how the method performs on more complex and realistic datasets, such as ImageNet or CelebA-HQ. The lack of evaluation on datasets with higher resolution and more complex structures makes it difficult to assess the generalizability of the proposed sampling method. Specifically, the performance of the method on datasets with fine-grained details and greater variability in object scales and poses remains unclear.
2. The authors mention that the proposed method is applicable to diverse domains, but only provide experimental results on image and speech generation tasks. It would be interesting to see how the method performs on other domains, such as text generation or 3D shape generation. The absence of experiments in other domains limits the understanding of the method's applicability and potential limitations. For example, it is unclear how the method would perform in sequence-to-sequence tasks or in generating complex 3D structures with intricate geometries.

### Suggestions

To strengthen the evaluation of the proposed method, it is crucial to conduct experiments on more challenging and diverse datasets. Specifically, the authors should consider evaluating their method on ImageNet, which is a standard benchmark for image generation tasks and would provide a more rigorous test of the method's ability to handle complex images with varying object categories and backgrounds. Furthermore, evaluating on datasets like CelebA-HQ, which contains high-resolution face images, would help assess the method's performance on datasets with fine-grained details. These additional experiments would provide a more comprehensive understanding of the method's strengths and weaknesses and its potential for real-world applications. It would also be beneficial to include a comparison with other state-of-the-art sampling methods on these datasets to provide a clear benchmark for the proposed approach.

In addition to expanding the range of datasets, the authors should also explore the applicability of their method to other domains beyond image and speech generation. For instance, evaluating the method on text generation tasks, such as those using the WikiText-103 dataset, would provide insights into its ability to handle sequential data and generate coherent text. Similarly, experiments on 3D shape generation using datasets like ShapeNet would help assess its performance in generating complex 3D structures. These experiments would not only demonstrate the versatility of the proposed method but also reveal potential limitations or areas for improvement. It would be particularly interesting to see how the method performs in domains where the data has different characteristics, such as high dimensionality or complex dependencies.

Finally, the authors should provide a more detailed analysis of the computational cost of their method, especially when applied to larger datasets and more complex models. This analysis should include a breakdown of the time spent on different steps of the sampling process, such as the computation of the fractional score function and the numerical integration of the reverse-time SDE. This would help users understand the trade-offs between sample quality and computational efficiency and make informed decisions about the applicability of the method in different scenarios. Furthermore, it would be beneficial to explore potential optimizations to reduce the computational cost of the method, such as using more efficient numerical integration schemes or approximating the fractional score function.

### Questions

1. How does the proposed method perform on larger and more complex datasets, such as ImageNet or CelebA-HQ?
2. Can the authors provide more details on the computational cost of the proposed method, especially when applied to larger datasets and more complex models?

### Rating

6

### Confidence

2

**********
