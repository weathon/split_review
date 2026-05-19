### Summary

This paper proposes a single-view large reconstruction model that can be trained with single-view images. The model is trained with two losses: cycle-consistency rendering loss and semantic rendering loss. The cycle-consistency loss is used to ensure the consistency between the input view and the rendered novel views. The semantic rendering loss is used to ensure the semantic similarity between the input view and the rendered novel views. The model is trained on a dataset of single-view images and can be used to reconstruct 3D objects from single-view images.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to understand.
2. The proposed method is simple and effective.
3. The proposed method achieves state-of-the-art performance on several datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is simple and effective, but it is not very novel. The cycle-consistency loss and semantic rendering loss are not new and have been used in many other papers.
2. The paper does not provide a detailed analysis of the limitations of the proposed method. For example, how does the method perform on objects with complex shapes or textures? How does the method handle occlusions?

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed approach. While the individual components, cycle-consistency loss and semantic rendering loss, are not novel in themselves, the specific way they are combined and applied to the single-view reconstruction task could be highlighted more clearly. The authors should elaborate on the specific challenges of single-view reconstruction that their approach addresses, and how their method differs from existing techniques that use these loss functions. For example, a detailed comparison with methods that use cycle-consistency for multi-view reconstruction, but adapted for single-view, would be beneficial. This would help to clarify the unique contributions of this work and justify its significance.

Furthermore, the paper should include a more comprehensive analysis of the method's limitations. The authors should investigate the performance of the method on objects with varying levels of complexity, including those with intricate shapes and fine details. It would be useful to see a quantitative analysis of how the method performs on different object categories, and whether there are specific types of objects that are more challenging for the proposed approach. Additionally, the paper should address how the method handles occlusions, which are common in single-view images. A discussion of the limitations of the method in handling extreme occlusions, or a comparison with methods that explicitly address this issue, would be valuable. The authors could also explore the use of data augmentation techniques to improve the robustness of the method to occlusions.

Finally, the paper should include a more detailed discussion of the computational cost of the proposed method. While the authors mention that the method is efficient, a quantitative analysis of the training time and memory requirements would be helpful. This would allow readers to better understand the practical implications of using the proposed method. The authors should also discuss the scalability of the method to larger datasets and more complex scenes. This would provide a more complete picture of the method's capabilities and limitations.

### Questions

1. How does the proposed method handle the case where the input image is noisy or has a low resolution?
2. How does the proposed method handle the case where the input image contains occlusions?

### Rating

6

### Confidence

3

**********
