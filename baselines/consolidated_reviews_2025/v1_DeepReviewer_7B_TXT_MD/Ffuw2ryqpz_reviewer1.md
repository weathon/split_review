### Summary

This paper introduces a LRM framework that can be trained using single-view images. The method employs a self-training strategy, leveraging the LRM itself to render novel views of the reconstruction results. The primary challenge addressed is establishing correspondences between these rendered novel views and the single input view. To tackle this, the authors propose a cycle-consistency rendering loss and a semantic rendering loss. Additionally, the paper presents an automatic data curation method for selecting high-quality single-view data.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method demonstrates strong performance on both in-domain and out-of-domain datasets.
3. The ablation study is comprehensive, providing thorough insights into the contributions of each component.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method appears to be a combination of existing techniques, lacking significant novelty. The cycle consistency loss is directly borrowed from TripoSR, and the semantic guidance is derived from CLIP. While the application of these techniques to single-view reconstruction is novel, the core components themselves are not new. The cycle consistency loss, while adapted for single-view, still relies on the fundamental idea of enforcing consistency between forward and inverse mappings, which is a well-established concept. Similarly, the use of CLIP for semantic guidance, while effective, is not a novel contribution in itself, as it has been widely adopted in various vision-language tasks. The paper does not introduce any significant modifications or improvements to these core components, which limits the overall novelty of the work.
2. The paper lacks a thorough analysis of the computational cost associated with the proposed method. It would be beneficial to include a comparison of the training and inference times with existing methods. Furthermore, the paper should provide a detailed breakdown of the computational resources required for each component of the method, such as the cycle consistency loss and the semantic rendering loss. This would allow for a more comprehensive understanding of the method's efficiency and scalability. The absence of such analysis makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments.
3. The paper does not adequately address the limitations of the proposed method. For example, it would be beneficial to discuss the sensitivity of the method to the quality of the input images, the potential for artifacts in the reconstructed 3D models, and the generalization capabilities of the method to unseen object categories. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the method's performance.

### Suggestions

The authors should consider exploring more innovative ways to integrate the cycle consistency and semantic guidance losses, rather than simply adapting existing techniques. For example, they could investigate adaptive weighting schemes for these losses, or explore alternative loss functions that are specifically tailored to the single-view reconstruction setting. Furthermore, the authors could investigate the use of more advanced techniques for establishing correspondences between the rendered novel views and the single input view, such as incorporating attention mechanisms or exploring more sophisticated feature matching strategies. This would demonstrate a deeper understanding of the underlying challenges and contribute more significantly to the field.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the computational cost of each component of their method, including the time required for rendering, loss calculation, and optimization. This analysis should be compared against existing methods, such as LRM*, to provide a clear understanding of the trade-offs between performance and computational cost. The authors should also investigate techniques for optimizing the computational efficiency of their method, such as using more efficient network architectures or exploring parallelization strategies. This would make the method more practical for real-world applications. Additionally, the authors should provide a more detailed analysis of the memory requirements of their method, which is an important factor for training and inference.

Finally, the authors should provide a more comprehensive discussion of the limitations of their method, including its sensitivity to input image quality, the potential for artifacts in the reconstructed 3D models, and its generalization capabilities to unseen object categories. They should also discuss the potential failure cases of their method and provide recommendations for mitigating these issues. For example, they could investigate the use of data augmentation techniques to improve the robustness of their method to variations in input image quality. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the method's performance and would help guide future research in this area.

### Questions

1. Could the authors provide more details on the training process, specifically regarding the number of iterations and the time required for training?
2. How does the proposed method handle cases where the input images are of low quality or contain significant noise?
3. What strategies could be employed to improve the generalization capabilities of the method to unseen object categories?

### Rating

5

### Confidence

4

**********
