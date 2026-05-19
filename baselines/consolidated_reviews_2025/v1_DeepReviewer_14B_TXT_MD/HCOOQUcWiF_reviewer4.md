### Summary

The paper proposes a differentiable polygon-based instance segmentation method. The authors propose PolygonAlign to address the alignment between a predicted K-vertex polygon and a target ground-truth L-vertex polygon. The authors also propose a variant of the active contour model for polygon parameterization. The proposed method is tested on the MS-COCO 2017 benchmark using the Sparse R-CNN framework and obtains state-of-the-art performance compared with the prior art of polygon modeling methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel PolygonAlign method that addresses the alignment between predicted polygons and ground-truth polygons. This method facilitates using a simple mean squared error as the polygon prediction loss function in end-to-end learning.
2. The paper presents an affine transformation decoupled vertex displacement based parameterization method for polygons. This method supports the proposed PolygonAlign and simplifies the iterative updating with an one-step refiner.
3. The proposed method obtains state-of-the-art performance in MS-COCO compared with the prior art of contour-based instance segmentation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes a fixed topology (i.e., a predefined and fixed number of vertices, K) for the predicted polygons. While this is common in prior art, it may limit the flexibility of the model to represent objects with varying shapes and complexities. In reality, the number of vertices required to accurately represent a polygon may vary depending on the object's shape. Forcing a fixed number of vertices might lead to either oversimplification of complex shapes or unnecessary complexity for simpler shapes. This could potentially affect the model's ability to generalize well to unseen data with diverse object shapes.
2. The paper does not extensively discuss the limitations of assuming fixed topology. It would be beneficial to acknowledge and discuss potential scenarios where this assumption might not hold or could lead to suboptimal results. For instance, objects with highly irregular or intricate boundaries might not be well-represented by a fixed number of vertices. A more thorough discussion of these limitations would provide a more balanced perspective on the proposed method's applicability and potential areas for future improvement.
3. The paper does not compare its method with other approaches that do not assume fixed topology. Including comparisons with such methods would provide a more comprehensive evaluation of the proposed method's performance and its advantages and disadvantages compared to alternative approaches. This would help to better understand the trade-offs involved in assuming fixed topology and the potential benefits of exploring methods that allow for more flexible polygon representations.

### Suggestions

The paper's core contribution, the PolygonAlign method, is promising for aligning predicted and ground-truth polygons, but its reliance on a fixed number of vertices (K) introduces limitations that should be addressed. While the authors justify this choice by referencing prior art, it is crucial to acknowledge that this constraint can hinder the model's ability to capture the full diversity of object shapes. For example, highly complex objects with intricate boundaries might require a significantly larger number of vertices than simpler objects, and forcing all polygons to have the same fixed K could lead to either over-parameterization or under-fitting. Future work should explore methods to dynamically adjust the number of vertices based on the complexity of the object's shape. This could involve incorporating a mechanism that predicts the optimal number of vertices or using a hierarchical approach where the polygon representation is refined iteratively, adding vertices where needed. Such an approach would enhance the model's flexibility and potentially improve its performance on datasets with a wide range of object complexities.

Furthermore, the paper would benefit from a more thorough analysis of the impact of the fixed topology assumption on the model's performance. The authors should investigate how the choice of K affects the accuracy of the segmentation, especially for objects with varying levels of complexity. This could involve conducting experiments with different values of K and analyzing the resulting performance metrics. Additionally, it would be valuable to explore the sensitivity of the model to the initial contour initialization. While the paper mentions a learnable contour initialization module, it does not provide a detailed analysis of its effectiveness or its impact on the final segmentation results. A more in-depth investigation of these aspects would provide a more comprehensive understanding of the model's strengths and weaknesses.

Finally, the paper should include a more comprehensive comparison with alternative methods that do not assume fixed topology. This would provide a more complete picture of the proposed method's performance relative to the state-of-the-art. Specifically, it would be beneficial to compare the proposed method with approaches that use implicit representations or deformable models that can adapt to the shape of the object without being constrained by a fixed number of vertices. Such a comparison would help to highlight the advantages and disadvantages of the fixed topology assumption and guide future research in this area. The authors should also consider exploring the use of adaptive loss functions that can penalize errors more effectively based on the complexity of the object's shape, rather than relying solely on a simple L2 norm.

### Questions

1. How does the choice of the fixed number of vertices (K) affect the performance of the model? Is there an optimal range for K, or does it depend on the specific dataset or application? It would be helpful to provide more insights into how to choose an appropriate value for K and the trade-offs involved.
2. The paper mentions that the proposed method obtains state-of-the-art performance compared to prior art of polygon modeling methods. However, it would be beneficial to provide a more detailed comparison with other instance segmentation methods, including both polygon-based and mask-based approaches. This would help to better understand the relative strengths and weaknesses of the proposed method in the context of the broader instance segmentation literature.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
