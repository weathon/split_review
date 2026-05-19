### Summary

The paper proposes a method for object completion, which aims to reconstruct a complete object from its partially visible components. The proposed method, named MaskComp, iteratively refines the object mask by alternating between generation and segmentation stages. The object mask is provided as an additional condition to boost image generation, and the generated images are used to improve the mask through segmentation. The combination of one generation and one segmentation stage effectively functions as a mask denoiser. The experiments demonstrate the superiority of MaskComp over existing approaches, such as ControlNet and Stable Diffusion.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. It bridges the gap between image generation and segmentation for object completion.
2. The experiments are extensive and demonstrate the effectiveness of the proposed method. The results show that MaskComp outperforms existing approaches in terms of object completion quality.
3. The paper is well-written and easy to follow. The figures and tables are clear and informative.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires a large number of sampling steps, which can be computationally expensive. It would be beneficial to explore ways to reduce the number of sampling steps without sacrificing performance. Specifically, the paper does not provide a detailed analysis of the computational cost associated with each sampling step, making it difficult to assess the practical feasibility of the method. Furthermore, the paper does not explore the trade-off between the number of sampling steps and the quality of the generated masks, which is crucial for understanding the method's efficiency.
2. The proposed method relies on the quality of the initial mask. If the initial mask is inaccurate or incomplete, it may affect the performance of the method. The paper does not provide a systematic analysis of how the method performs under different initial mask conditions, such as varying levels of occlusion or noise. It is unclear how robust the method is to errors in the initial mask, which is a critical factor for real-world applications.
3. The proposed method may not generalize well to other datasets or domains. It would be beneficial to evaluate the method on a wider range of datasets and domains to assess its generalization ability. The paper only evaluates the method on a limited set of datasets, and it is unclear how the method would perform on datasets with different characteristics, such as different object categories or image resolutions. A more comprehensive evaluation is needed to establish the method's generalization capabilities.

### Suggestions

The paper should provide a more detailed analysis of the computational cost associated with each sampling step. This analysis should include a breakdown of the time spent on different operations, such as image generation and segmentation, and should also explore the trade-off between the number of sampling steps and the quality of the generated masks. Furthermore, the paper should investigate techniques to reduce the number of sampling steps without sacrificing performance, such as using more efficient sampling algorithms or employing early stopping criteria. This would make the method more practical for real-world applications where computational resources are limited. For example, the authors could explore the use of progressive distillation or other acceleration techniques to reduce the computational burden of the sampling process.

To address the issue of initial mask quality, the paper should include a systematic analysis of how the method performs under different initial mask conditions. This analysis should include varying levels of occlusion, noise, and inaccuracies in the initial mask. The paper should also explore techniques to improve the robustness of the method to errors in the initial mask, such as using data augmentation or incorporating prior knowledge about the object's shape. For example, the authors could investigate the use of a more robust segmentation model or explore methods to refine the initial mask before starting the iterative process. This would make the method more reliable in real-world scenarios where the initial mask may not be perfect.

To improve the generalization ability of the method, the paper should evaluate the method on a wider range of datasets and domains. This evaluation should include datasets with different characteristics, such as different object categories, image resolutions, and levels of complexity. The paper should also explore techniques to improve the generalization ability of the method, such as using domain adaptation or transfer learning. For example, the authors could investigate the use of a pre-trained model or explore methods to fine-tune the model on different datasets. This would make the method more versatile and applicable to a wider range of real-world problems.

### Questions

1. How does the proposed method compare to other object completion methods in terms of computational cost and efficiency? It would be helpful to provide a detailed analysis of the computational cost of the proposed method and compare it with other methods.
2. How does the proposed method perform on objects with complex shapes or textures? It would be helpful to provide more examples of objects with complex shapes or textures and show how the proposed method performs on them.
3. How does the proposed method handle cases where the object is heavily occluded or partially visible? It would be helpful to provide more examples of such cases and show how the proposed method performs on them.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
