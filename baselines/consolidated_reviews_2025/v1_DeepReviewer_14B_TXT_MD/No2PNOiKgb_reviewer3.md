### Summary

The paper proposes two main improvements over the state-of-the-art method for parsing indoor scenes using a regression approach to predict a starting point with a fixed set of primitives. The improvements include incorporating a small number of negative primitives in the sense of constructive solid geometry (CSG) and using an ensembling method with multiple predictors, each trained to predict a start point with a different number of primitives. The paper demonstrates that these improvements lead to significant accuracy gains in depth and normal prediction and scene segmentation.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces the use of negative primitives in the sense of CSG, which expands the range of geometries that can be encoded and complicates the fitting problem.
2. The ensembling method, which uses multiple predictors trained to predict start points with different numbers of primitives, results in significant improvements in accuracy.
3. The paper provides extensive experiments on a standard dataset (NYUv2) to confirm the usefulness of negative primitives and the effectiveness of the refine-then-choose strategy.

### Weaknesses

#### Some Related Works


#### comment

1. The method requires ensembling a number of regressors, which leads to increased costs in training and inference time. The paper does not provide a detailed analysis of the computational overhead associated with the ensemble, such as the number of forward passes required during inference and the memory footprint of storing multiple models. This lack of analysis makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments.
2. While the method is shown to outperform state-of-the-art methods in terms of accuracy, it is not clear how useful the primitives are in simplifying reasoning tasks. The paper does not provide a clear evaluation of the parsimony of the primitive representations, such as the average number of primitives used per scene and how this number varies across different scenes. Without this analysis, it is difficult to determine if the method is truly learning a simplified representation of the scene or just overfitting to the training data.
3. The paper does not provide a detailed analysis of the failure cases of the method. It would be helpful to understand the types of scenes or geometries where the method struggles to produce accurate fits. For example, does the method perform poorly on scenes with complex occlusions or highly non-convex objects? A more detailed analysis of the failure cases would provide valuable insights into the limitations of the method and guide future research directions.

### Suggestions

The paper should include a more thorough analysis of the computational cost associated with the ensembling approach. This analysis should include a breakdown of the time required for each stage of the pipeline, including the forward passes for each regressor in the ensemble, the refinement process, and the final selection step. Furthermore, the memory footprint of storing multiple models should be quantified. This analysis should be performed on a standard hardware setup to allow for comparison with other methods. It would also be beneficial to explore techniques to reduce the computational overhead of the ensemble, such as knowledge distillation or model pruning, to make the method more practical for real-world applications. The paper should also investigate the trade-off between the number of regressors in the ensemble and the resulting accuracy to determine the optimal number of models for a given application.

To better evaluate the usefulness of the learned primitives, the paper should include a detailed analysis of the parsimony of the primitive representations. This analysis should include the average number of primitives used per scene, the distribution of the number of primitives across different scenes, and the complexity of the individual primitives. It would also be helpful to compare the primitive representations learned by the proposed method with those learned by other methods, if available. The paper should also explore the use of the learned primitives for downstream tasks, such as scene understanding or object recognition, to demonstrate the practical value of the learned representations. This would provide a more compelling argument for the usefulness of the primitives beyond just improving fitting accuracy.

Finally, the paper should include a more detailed analysis of the failure cases of the method. This analysis should include a qualitative assessment of the types of scenes or geometries where the method struggles to produce accurate fits. For example, the paper should investigate the performance of the method on scenes with complex occlusions, highly non-convex objects, or scenes with a large number of objects. The paper should also provide a quantitative analysis of the error patterns, such as the types of errors that are most common in the depth and normal predictions. This analysis should be used to identify the limitations of the method and guide future research directions. For example, the paper could explore the use of more sophisticated primitive representations or the incorporation of additional constraints to improve the robustness of the method.

### Questions

1. How does the method handle scenes with complex occlusions or highly non-convex objects?
2. What is the computational cost of the ensembling approach, and how does it compare to other methods?
3. How many primitives are typically needed to represent a scene, and how does this number vary across different scenes?
4. How do the learned primitives compare to those learned by other methods in terms of parsimony and usefulness for downstream tasks?
5. What are the common failure cases of the method, and what are the potential reasons for these failures?

### Rating

5

### Confidence

3

**********
