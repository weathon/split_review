### Summary

This paper proposes an active learning algorithm for image segmentation. Given a binary query budget, the algorithm selects images and classes to pose binary queries about the presence of the class in the image. The selection is posed as an optimization problem and solved using LP relaxation. Experimental results on three datasets show that the proposed method achieves decent performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

+ The idea of formulating image and class selection as an optimization problem is interesting.

+ The paper is easy to follow.

### Weaknesses

#### Some Related Works

[1] J. Sinha, P. Gehler, V. Koltun, and T. Brox. Deep active learning for semantic segmentation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 9714–9723, 2019

#### comment

 - The paper lacks discussion and comparison with other active learning strategies that pose binary queries for image segmentation. For example, [1] allows users to point to regions of interest of any shape and let the system automatically annotate them. The user only needs to correct the generated mask if it is inaccurate, significantly reducing the annotation effort. In contrast, the proposed method requires users to provide pixel-level annotations.

- The paper lacks a user study to compare the proposed method with other baselines in terms of annotation effort and accuracy. The authors should conduct experiments to compare the proposed method with other baselines in terms of annotation effort and accuracy. For example, the authors can measure the time required for users to annotate images using different methods and the accuracy of the annotations.

- The paper does not discuss the impact of the proposed method on different types of images and classes. For example, the authors can analyze the performance of the proposed method on images with different levels of complexity and classes with different levels of difficulty.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing active learning methods for image segmentation, particularly those employing binary queries. The current comparison is insufficient, and the authors should include a detailed analysis of methods that, like the proposed approach, aim to minimize user annotation effort through binary feedback. Specifically, the authors should consider methods that leverage user input more efficiently, such as those that allow for interactive refinement of segmentation masks based on initial binary queries. A more detailed comparison should not only focus on the final segmentation accuracy but also on the number of user interactions required to achieve a certain level of performance. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses relative to the state-of-the-art.

Furthermore, the lack of a user study is a significant limitation. While the authors propose a novel approach, the practical implications of their method cannot be fully assessed without empirical data on user annotation time and accuracy. The authors should conduct a user study where participants are asked to annotate images using the proposed method and other baselines. This study should measure the time taken by users to complete the annotation tasks and the accuracy of the resulting annotations. The study should also include a variety of images with different levels of complexity and classes with different levels of difficulty to provide a more comprehensive evaluation of the proposed method. The results of this user study would provide valuable insights into the practical usability of the proposed method and its potential for real-world applications.

Finally, the paper needs a more in-depth analysis of the proposed method's performance across different image types and classes. The authors should investigate how the method performs on images with varying levels of complexity, such as those with cluttered backgrounds or multiple objects. Similarly, the authors should analyze the method's performance on classes with different levels of difficulty, such as those with ambiguous boundaries or rare instances. This analysis should include a discussion of the factors that contribute to the method's performance on different types of images and classes. This would help to identify the limitations of the proposed method and suggest potential avenues for future research. Such an analysis would also provide a more nuanced understanding of the method's applicability to different real-world scenarios.

### Questions

Please see Weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
