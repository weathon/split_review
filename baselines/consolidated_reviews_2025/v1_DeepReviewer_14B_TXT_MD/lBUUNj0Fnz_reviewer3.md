### Summary

This paper proposes a novel active learning framework for image segmentation, which selects a batch of informative images and semantic classes for binary user feedback. The proposed method formulates the image and class selection as a constrained optimization problem and derives a linear programming relaxation to select maximally informative (image-class) pairs. Extensive empirical studies on three challenging datasets demonstrate the effectiveness of the proposed method in reducing human annotation effort.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is well-motivated and technically sound. The idea of using binary user feedback to reduce human annotation effort is novel and interesting.
2. The paper is well-organized and easy to follow. The authors provide clear explanations of the proposed method and the experimental results.
3. The authors conduct extensive empirical studies on three challenging datasets to demonstrate the effectiveness of the proposed method. The results show that the proposed method can significantly reduce human annotation effort while achieving comparable or even better performance than existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the assumption that the user can provide accurate binary feedback. However, in real-world scenarios, the user may not always be able to provide accurate feedback, especially for complex images or classes. This could affect the performance of the proposed method. The paper does not adequately address the potential for user error, such as mislabeling a class or providing inconsistent feedback across similar images, and how this might propagate through the active learning process. The impact of such errors on the convergence and final performance of the model is unclear.
2. The proposed method may not be suitable for all types of images or classes. For example, for images with small or thin objects, the binary feedback may not be sufficient to accurately annotate the objects. The method's reliance on binary feedback might struggle with fine-grained segmentation tasks where the boundaries between classes are not clearly defined, or where objects exhibit significant intra-class variability. The paper lacks a discussion on the limitations of binary feedback for complex segmentation scenarios.
3. The proposed method may require a large number of iterations to achieve good performance, which could be time-consuming and labor-intensive. The paper does not provide a clear analysis of the convergence rate of the proposed method, nor does it compare the number of iterations required to reach a certain performance level with other active learning methods. This makes it difficult to assess the practical efficiency of the approach.

### Suggestions

The paper should include a more detailed analysis of the impact of noisy or inaccurate user feedback on the performance of the proposed method. This could involve simulating different levels of user error and evaluating how the model's performance degrades under these conditions. Furthermore, the authors should explore strategies to mitigate the effects of user error, such as incorporating a mechanism to detect and correct inconsistent feedback or using a robust loss function that is less sensitive to noisy labels. A sensitivity analysis of the method's performance with respect to the quality of user feedback would be beneficial. The authors could also consider incorporating a confidence measure for the user feedback, allowing the model to weigh more reliable feedback more heavily during training. This would make the method more robust to real-world scenarios where user feedback is not always perfect.

To address the limitations of binary feedback for complex segmentation tasks, the authors could explore incorporating additional information into the feedback mechanism. For example, they could allow the user to provide bounding boxes or scribbles in addition to binary labels. This would provide more detailed information about the location and shape of objects, which could be particularly useful for fine-grained segmentation tasks. Alternatively, the authors could investigate methods for automatically refining the binary feedback, such as using a conditional random field (CRF) to enforce spatial consistency in the predicted segmentation masks. This would help to reduce the ambiguity associated with binary feedback and improve the accuracy of the segmentation results. The authors should also discuss the trade-offs between the simplicity of binary feedback and the potential for improved performance with more detailed feedback mechanisms.

The paper should include a more thorough analysis of the convergence rate of the proposed method and compare it with other active learning methods. This analysis should include a comparison of the number of iterations required to reach a certain performance level, as well as the computational cost of each iteration. The authors should also investigate strategies to accelerate the convergence of the method, such as using a more efficient optimization algorithm or incorporating a warm-start strategy. A detailed analysis of the computational complexity of the proposed method would be beneficial. The authors could also consider using a stopping criterion based on the change in performance over successive iterations, which would allow the method to terminate early when it has reached a satisfactory level of performance.

### Questions

1. How does the proposed method handle noisy or inaccurate user feedback? Are there any strategies to mitigate the effects of noisy feedback?
2. How does the proposed method perform on images with small or thin objects? Are there any strategies to improve the performance on such images?
3. How does the proposed method compare to other active learning methods in terms of the number of iterations required to achieve good performance?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
