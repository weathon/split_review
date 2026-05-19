### Summary

This paper presents a novel active learning framework for image segmentation, which poses only binary user queries to the users. The authors pose the image and class selection as a constrained optimization problem and derive a linear programming relaxation to select a batch of (image-class) pairs, which are maximally informative to the underlying deep neural network. The proposed framework is evaluated on three challenging datasets and demonstrates substantial reduction in human annotation effort in real-world image segmentation applications.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and addresses a practical problem in image segmentation, where human annotation is time-consuming and laborious.
3. The authors provide a thorough evaluation of the proposed method on three benchmark datasets, demonstrating its effectiveness and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately address the scalability of the proposed method to larger datasets or higher-resolution images. The experiments are limited to relatively small datasets, and there is no discussion of how the computational cost of solving the linear program would scale with the size of the dataset or the number of classes. Specifically, the paper lacks an analysis of the time complexity of the linear programming solver in relation to the number of images and classes, which is crucial for assessing its practical applicability to large-scale problems.
2. The choice of baselines is somewhat limited. While the paper compares against pixel-level, region-level, and binary-level annotation methods, it does not include comparisons with other state-of-the-art active learning techniques for image segmentation, such as those based on uncertainty sampling or diversity sampling. This makes it difficult to assess the relative performance of the proposed method against established approaches in the field. The paper should also consider including more recent methods that specifically address active learning for segmentation tasks.
3. The paper does not explore the sensitivity of the proposed method to different hyperparameter settings, such as the query budget or the parameters in the objective function. The lack of a sensitivity analysis makes it difficult to understand the robustness of the method and how its performance might vary under different configurations. For example, the impact of varying the query budget on the final mIoU and annotation time should be investigated.
4. The paper does not discuss the potential limitations of the binary query approach, such as the possibility of missing important details or the impact of noisy annotations. The paper should address how the method would handle ambiguous cases or noisy user feedback, and whether the binary nature of the queries could lead to a loss of information compared to more informative query types.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed method. The authors should provide a theoretical analysis of the time and space complexity of solving the linear program, and discuss how these complexities scale with the number of images, the number of semantic classes, and the size of the images. This analysis should be complemented by empirical evaluations on larger datasets and with higher-resolution images to demonstrate the practical scalability of the method. Furthermore, the authors should explore and discuss alternative optimization techniques that could potentially reduce the computational cost of solving the linear program, such as approximation algorithms or more efficient solvers. This would make the method more practical for real-world applications with large-scale datasets. The authors should also consider the trade-off between annotation time and annotation quality when choosing between binary and multi-class queries, and provide a more detailed analysis of the performance of the proposed method under different annotation budgets.

To strengthen the empirical evaluation, the authors should include comparisons with a broader range of state-of-the-art active learning methods for image segmentation. This should include methods based on uncertainty sampling, diversity sampling, and other relevant techniques. The comparison should not only focus on the final mIoU but also consider other metrics such as the annotation time, the number of queries, and the convergence rate of the active learning process. The authors should also provide a detailed analysis of the performance of the proposed method under different experimental settings, such as varying the query budget, the number of classes, and the size of the images. This would help to understand the strengths and weaknesses of the method and identify the scenarios where it performs best. Additionally, the authors should investigate the impact of different hyperparameter settings on the performance of the method, and provide guidelines for selecting appropriate values for these parameters. This would make the results more reproducible and provide a better understanding of the method's behavior.

Finally, the paper should address the limitations of the binary query approach and discuss how these limitations could be mitigated. The authors should analyze the potential impact of noisy annotations on the performance of the method, and explore strategies for handling ambiguous cases or uncertain user feedback. For example, the authors could investigate the use of confidence scores for the binary queries or the incorporation of uncertainty into the optimization objective. The paper should also discuss the potential loss of information due to the binary nature of the queries and compare this to more informative query types. This discussion should be supported by empirical evidence, such as experiments with different types of user feedback or different levels of noise in the annotations. The authors should also consider the practical implications of using binary queries in real-world scenarios, where user feedback may not always be precise or consistent.

### Questions

1. How does the proposed method compare to other state-of-the-art active learning techniques for image segmentation, particularly those based on uncertainty sampling or diversity sampling?
2. How sensitive is the performance of the proposed method to different hyperparameter settings, such as the query budget or the parameters in the objective function?
3. How does the binary query approach handle ambiguous cases or noisy annotations? Are there any mechanisms in place to mitigate the impact of uncertain user feedback?
4. How does the proposed method scale to larger datasets or higher-resolution images? What are the computational costs associated with solving the linear program in these scenarios?

### Rating

6

### Confidence

4

**********
