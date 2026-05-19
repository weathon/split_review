### Summary

This paper presents a novel mapping function for NeRFs that addresses the challenge of rendering unbounded scenes. The authors identify limitations in existing mapping functions, which often fail to capture distant objects effectively, particularly when camera poses are far from the scene origin. To overcome this, they propose a geometrically aware mapping function based on a p-norm distance, allowing for adaptive sampling of rays based on scene geometry. This approach allocates more capacity to nearby objects and distant contents, depending on the scene's shape. Additionally, they introduce a new ray parameterization technique that considers the distortion of the embedding space, ensuring more even sampling across different regions. The proposed method is evaluated on various datasets, including 360° object-centric and free trajectory scenes, demonstrating state-of-the-art novel view synthesis results compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper is well-structured and clearly written, making it easy to follow the proposed method and its rationale. The authors provide a thorough analysis of the limitations of existing mapping functions and effectively demonstrate how their proposed p-norm-based mapping function addresses these issues. The introduction of a ray parameterization that considers the distortion of the embedding space is a novel contribution that enhances the uniformity of sampling across different regions of the scene. The experimental results are compelling, showing significant improvements over state-of-the-art methods in various challenging unbounded scene scenarios. The authors also provide a detailed ablation study, which helps to understand the contribution of each component of their method.

### Weaknesses

#### Some Related Works


#### comment

While the paper provides a good overview of the related work, a more detailed comparison with recent state-of-the-art methods, particularly those that also address unbounded scenes, would be beneficial. This would help to better contextualize the contributions of the proposed method and highlight its advantages and limitations compared to other approaches. Specifically, the paper lacks a discussion of methods that employ learned mapping functions or those that use a combination of local and global representations. The current comparison is limited to methods that use fixed mappings, which does not fully capture the landscape of techniques available for unbounded scene rendering. Furthermore, the paper does not adequately address the computational cost of the proposed method, particularly the p-norm calculation and ray parameterization, which could be a limiting factor for real-time applications. A more thorough analysis of the computational complexity and memory requirements would be valuable.

### Suggestions

To strengthen the paper, the authors should include a more comprehensive comparison with recent state-of-the-art methods for unbounded scene rendering. This comparison should not only focus on quantitative metrics like PSNR, SSIM, and LPIPS, but also include a qualitative analysis of the visual quality of the rendered images, highlighting the specific scenarios where the proposed method excels or falls short compared to other approaches. The comparison should also include a discussion of the underlying techniques used by these methods, such as learned mapping functions or hybrid representations, to provide a more nuanced understanding of the proposed method's advantages and limitations. For example, the authors could compare their method with techniques that use neural implicit representations or those that employ a combination of local and global coordinate systems. This would help to contextualize the contributions of the proposed method within the broader field of unbounded scene rendering.

Furthermore, the authors should provide a more detailed analysis of the computational cost of their proposed method. This analysis should include a breakdown of the time complexity of the p-norm calculation and the ray parameterization, as well as the memory requirements. The authors should also compare the computational cost of their method with that of existing methods, both in terms of theoretical complexity and empirical runtime. This analysis should consider the impact of different parameters, such as the number of rays and the complexity of the scene, on the computational cost. It would also be beneficial to discuss potential optimizations that could be applied to reduce the computational cost of the proposed method, such as using more efficient algorithms for p-norm calculation or ray parameterization. This would help to make the method more practical for real-time applications.

Finally, the authors should consider including a discussion of the limitations of their proposed method. While the paper demonstrates state-of-the-art results on several datasets, it is important to acknowledge the scenarios where the method may not perform as well. For example, the authors could discuss the limitations of their method in handling scenes with complex occlusions or highly dynamic lighting conditions. They could also discuss the sensitivity of the method to the choice of parameters, such as the p-norm parameter and the ray parameterization parameters. This would provide a more balanced and realistic assessment of the proposed method and help to guide future research in this area.

### Questions

1. How does the proposed method handle scenes with complex occlusions or highly dynamic lighting conditions?
2. What are the limitations of the proposed method in terms of computational cost and memory requirements, especially for real-time applications?
3. How does the choice of the p-norm parameter affect the performance of the method, and is there a systematic way to determine the optimal value for different scenes?
4. How does the proposed method compare to other state-of-the-art methods that also address unbounded scenes, particularly those that use different mapping functions or ray parameterizations?

### Rating

6

### Confidence

4

**********
