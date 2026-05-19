### Summary

This paper proposes a mask refinement method for coarse masks. The core of this method is the multi-prompt strategy, which uses multiple prompts to guide the SAM model to refine the coarse masks. Additionally, this paper introduces SAMRefiner++, which further enhances the performance of the generic SAMRefiner on the target dataset. The method is evaluated on various benchmarks, demonstrating its effectiveness in improving the quality of coarse masks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is a universal and efficient approach that can be adapted to various segmentation models and tasks.
2. The multi-prompt strategy effectively addresses the mask refinement task, and the introduction of SAMRefiner++ further improves performance without requiring additional annotations.
3. The method is evaluated on a wide range of benchmarks, demonstrating its effectiveness in improving the quality of coarse masks.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on the quality of the coarse masks, and its performance may degrade with extremely poor-quality inputs. Specifically, the paper does not explore the sensitivity of the method to different types of noise or artifacts in the coarse masks, such as salt-and-pepper noise, blur, or incorrect object boundaries. This lack of analysis makes it difficult to understand the robustness of the approach under various real-world conditions.
2. The computational cost of running SAM for multiple prompts could be a concern for large-scale applications. The paper does not provide a detailed analysis of the inference time and memory usage of the proposed method, especially when compared to other mask refinement techniques. This makes it hard to assess the practical feasibility of the approach for resource-constrained environments.
3. The IoU adaptation step in SAMRefiner++ requires training, which might not be suitable for all scenarios, especially when no additional data is available. The paper does not discuss the potential for overfitting to the specific dataset used for adaptation, and how this might affect the generalization performance on unseen data. Furthermore, the paper does not explore the impact of the size of the coarse mask dataset used for adaptation on the final performance.

### Suggestions

The paper should include a more thorough analysis of the method's sensitivity to the quality of the input coarse masks. Specifically, the authors should evaluate the performance of SAMRefiner under various types of noise and artifacts, such as salt-and-pepper noise, Gaussian blur, and different levels of boundary inaccuracies. This could be achieved by artificially degrading the coarse masks used for evaluation and analyzing the corresponding changes in the refinement performance. Such an analysis would provide a more comprehensive understanding of the method's robustness and its limitations when dealing with real-world noisy data. Furthermore, the authors should investigate the impact of different prompt types on the final refinement quality. For instance, it would be beneficial to analyze the performance of the method when using only point prompts, only box prompts, or only mask prompts, and compare these results with the multi-prompt strategy. This would help to identify the most effective prompt types and potentially lead to a more efficient refinement process.

To address the computational cost concerns, the authors should provide a detailed analysis of the inference time and memory usage of SAMRefiner and SAMRefiner++. This analysis should include a breakdown of the time spent on different stages of the refinement process, such as prompt generation, SAM inference, and mask selection. The authors should also compare the computational cost of their method with other mask refinement techniques, such as iterative bounding box refinement or graph-cut based methods. This comparison should be performed on a standard hardware setup and should include both the inference time and memory usage. Additionally, the authors should explore potential optimizations to reduce the computational cost of their method, such as using a smaller SAM model or implementing more efficient prompt generation strategies. This would make the method more practical for large-scale applications and resource-constrained environments.

Finally, the paper should provide a more detailed analysis of the IoU adaptation step in SAMRefiner++. Specifically, the authors should investigate the potential for overfitting to the specific dataset used for adaptation and how this might affect the generalization performance on unseen data. This could be achieved by evaluating the performance of SAMRefiner++ on a held-out dataset that is different from the dataset used for adaptation. The authors should also explore the impact of the size of the coarse mask dataset used for adaptation on the final performance. This could be done by training SAMRefiner++ with different sizes of coarse mask datasets and analyzing the corresponding changes in the refinement performance. Furthermore, the authors should discuss the limitations of the IoU adaptation step and provide guidelines for when it is appropriate to use this step and when it is not.

### Questions

1. How does the method perform when the coarse masks are generated from different sources, such as human annotations versus model predictions?
2. Can the authors provide more insights into the choice of hyperparameters, such as the expansion ratio for CEBoxes and the parameters for Gaussian-style masks?
3. How does the method handle cases where the coarse mask contains multiple objects of the same category in semantic segmentation?
4. What is the impact of the IoU adaptation step on the generalization ability of the model to unseen datasets?

### Rating

6

### Confidence

4

**********
