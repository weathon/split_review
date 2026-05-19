### Summary

This paper proposes a new method for object completion, named MaskComp, which aims to reconstruct a complete object image from its partial observation. The method iteratively refines the mask and image using a generation stage and a segmentation stage. In the generation stage, the method generates a new image based on the input partial image and the current mask. In the segmentation stage, the method refines the mask using the generated image and the original mask. The method is evaluated on two datasets, AHP and DYCE, and compared with several baselines, including ControlNet, Kandinsky 2.1, and Stable Diffusion 1.5.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The proposed method is simple and easy to understand. The idea of iteratively refining the mask and image is intuitive and makes sense. The method achieves good performance on the evaluated datasets.

### Weaknesses

#### Some Related Works

[1] Image-to-Image Transformation Enlargement for High-Fidelity Image Super-Resolution
[2] Image inpainting for natural images
[3] Image Inpainting with Patch-Mix Transformer

#### comment

1. The novelty of the proposed method is limited. The iterative refinement of the mask and image is similar to existing image inpainting methods, such as those based on GANs or diffusion models. The core idea of alternating between image generation and mask refinement is not new, and the paper does not adequately distinguish its approach from these existing methods. For example, the paper does not discuss how the proposed method differs from image inpainting techniques that also use iterative refinement, or how the specific choice of diffusion models impacts the novelty of the approach. The paper needs to clearly articulate the unique aspects of its method compared to these existing techniques.

2. The paper lacks a thorough comparison with existing methods for object completion. While the paper compares the proposed method with ControlNet, Kandinsky 2.1, and Stable Diffusion 1.5, it does not compare with other relevant methods in the field. For example, the paper does not compare with methods that use generative models for object completion, or methods that use other techniques such as GANs or transformers. The paper needs to provide a more comprehensive comparison with existing methods to demonstrate the advantages of the proposed method.

3. The paper does not provide a detailed analysis of the performance of the proposed method under different conditions. For example, the paper does not analyze how the performance of the method is affected by the size of the occluded region, the complexity of the object, or the quality of the input mask. The paper needs to provide a more detailed analysis of the performance of the method under different conditions to understand its strengths and limitations.

4. The paper does not provide a detailed analysis of the computational cost of the proposed method. The paper does not report the inference time or the memory usage of the method. The paper needs to provide a detailed analysis of the computational cost of the method to understand its practicality.

5. The paper does not provide a detailed analysis of the limitations of the proposed method. The paper does not discuss the limitations of the method, such as its inability to handle certain types of objects or occlusions. The paper needs to provide a detailed analysis of the limitations of the method to understand its scope and potential for future work.

### Suggestions

The paper should provide a more detailed comparison with existing image inpainting methods, particularly those that use iterative refinement. The authors should discuss how their approach differs from methods like those based on GANs or diffusion models, and how the specific choice of diffusion models impacts the novelty of their approach. A more thorough analysis of the differences in the underlying mechanisms and assumptions of these methods is needed to justify the novelty of the proposed method. For example, the paper should discuss how the proposed method handles boundary conditions and occlusions differently from existing methods. The paper should also discuss the limitations of the proposed method compared to existing methods, such as its inability to handle certain types of objects or occlusions.

The paper should include a more comprehensive comparison with existing methods for object completion. The authors should compare their method with other relevant methods in the field, including those that use generative models, GANs, or transformers. The comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated images. The paper should also discuss the advantages and disadvantages of the proposed method compared to these existing methods. For example, the paper should discuss the computational cost, memory usage, and the ability of the method to handle different types of objects and occlusions. The paper should also discuss the limitations of the proposed method compared to existing methods, such as its inability to handle certain types of objects or occlusions.

The paper should provide a more detailed analysis of the performance of the proposed method under different conditions. The authors should analyze how the performance of the method is affected by the size of the occluded region, the complexity of the object, and the quality of the input mask. The paper should also discuss the limitations of the method, such as its inability to handle certain types of objects or occlusions. The paper should also discuss the computational cost of the method, including the inference time and the memory usage. The paper should also discuss the practicality of the method, including its applicability to real-world scenarios. The paper should also discuss the potential for future work, such as improving the performance of the method under different conditions and reducing its computational cost.

### Questions

1. How does the proposed method differ from existing image inpainting methods that also use iterative refinement?
2. How does the proposed method compare with other object completion methods that use different techniques, such as GANs or transformers?
3. How does the performance of the proposed method vary under different conditions, such as different occlusion ratios or object complexities?
4. What is the computational cost of the proposed method, including the inference time and memory usage?

### Rating

5

### Confidence

4

**********
