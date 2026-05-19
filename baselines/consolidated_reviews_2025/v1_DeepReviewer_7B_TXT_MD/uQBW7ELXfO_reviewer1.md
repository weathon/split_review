### Summary

This paper proposes a novel approach to image-to-image translation between unpaired datasets. The authors formulate the problem as a Schrödinger Bridge problem and solve it using adversarial learning. The proposed method is evaluated on several datasets and shows competitive performance compared to existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of their proposed method.

2. The authors provide a comprehensive evaluation of their method on several datasets. The results show that the proposed method is competitive with existing methods.

3. The authors provide a theoretical analysis of their method and show that it is able to learn the optimal transport map between two distributions.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their method can handle high-resolution images, but they only evaluate their method on 256x256 images. It would be more convincing if they could show results on higher resolution images, such as 512x512 or 1024x1024.

2. The authors claim that their method is able to handle unpaired datasets, but they only evaluate their method on datasets where the paired data is available for training. It would be more convincing if they could show results on datasets where the paired data is not available for training.

3. The authors do not provide a detailed analysis of the computational cost of their method. It would be helpful to know how the training time and inference time scale with the size of the dataset and the image resolution.

4. The authors do not provide a detailed analysis of the sensitivity of their method to the choice of hyperparameters. It would be helpful to know how the performance of the method varies with different choices of hyperparameters.

5. The authors do not provide a comparison with other state-of-the-art methods for image-to-image translation. It would be helpful to know how the performance of the proposed method compares with other methods on a range of datasets and metrics.

### Suggestions

The authors should provide a more thorough evaluation of their method on higher resolution images. While 256x256 is a common starting point, the claim of handling high-resolution images requires empirical validation on resolutions such as 512x512 or 1024x1024. This would involve not only increasing the input image size but also demonstrating the method's ability to maintain image quality and structural integrity at these higher resolutions. Furthermore, the computational cost associated with increasing resolution should be analyzed, including memory usage and training time. This analysis should include a breakdown of the computational cost of each component of the method, such as the adversarial training and the Schrödinger Bridge computation, to identify potential bottlenecks and areas for optimization. It would also be beneficial to show results on more diverse datasets, including those with more complex image content and variations in lighting and pose, to demonstrate the robustness of the method.

To further strengthen the claim of handling unpaired datasets, the authors should evaluate their method on datasets where the paired data is not available for training. This could involve using datasets where only unpaired images from the source and target domains are available, or where the paired data is generated using a different method. The authors should clearly define the limitations of their method in terms of the availability of paired data and discuss how this limitation affects the applicability of their method in real-world scenarios. It would also be beneficial to compare the performance of the proposed method with other methods that are designed for unpaired image-to-image translation. This would provide a more comprehensive evaluation of the method's strengths and weaknesses and help to position it within the existing literature.

Finally, the authors should provide a more detailed analysis of the sensitivity of their method to the choice of hyperparameters. This should include a systematic study of how the performance of the method varies with different choices of hyperparameters, such as the learning rate, the batch size, and the number of training iterations. The authors should also provide guidelines for selecting appropriate hyperparameter values for different datasets and tasks. Furthermore, the authors should compare their method with other state-of-the-art methods for image-to-image translation, using a range of datasets and metrics. This would provide a more comprehensive evaluation of the method's performance and help to establish its position within the existing literature. The comparison should include both quantitative metrics, such as FID and KID, and qualitative comparisons of the generated images.

### Questions

1. How does the proposed method handle images with complex structures or textures?

2. How does the proposed method handle images with significant variations in lighting or pose?

3. How does the proposed method compare with other state-of-the-art methods for image-to-image translation?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
