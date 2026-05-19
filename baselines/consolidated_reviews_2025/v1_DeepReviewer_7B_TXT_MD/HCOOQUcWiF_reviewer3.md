### Summary

The paper presents a method for instance segmentation that uses polygonal modeling, which is an underexplored area in the field. The authors introduce two key components: PolygonAlign, which aligns predicted polygons with ground truth by re-sampling vertices, and a learnable contour initialization method that reduces the need for extensive polygon vertex optimization. The method is tested on the MS-COCO dataset and shows state-of-the-art performance compared to existing contour-based methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses an underexplored area in instance segmentation, specifically polygonal modeling, which could inspire further research in this direction.
2. The proposed method achieves state-of-the-art results on the MS-COCO dataset, demonstrating its effectiveness and potential for practical applications.
3. The paper is well-organized and easy to follow, with clear explanations of the proposed method and its components.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the MS-COCO dataset, which may limit the generalizability of the results to other datasets with different characteristics. The method's performance on datasets with varying object sizes, shapes, and complexities is not thoroughly explored. For instance, the paper does not discuss how the polygon initialization and optimization would be affected by highly irregular or concave shapes, which are common in real-world scenarios but may be less prevalent in MS-COCO.
2. While the paper compares the proposed method with existing contour-based methods, it lacks a comprehensive comparison with other state-of-the-art instance segmentation techniques, such as those based on transformers or graph neural networks. This makes it difficult to assess the true advancement of the proposed method in the broader context of instance segmentation. The absence of comparisons with methods that utilize different feature representations or loss functions makes it challenging to determine the specific advantages of the polygon-based approach.
3. The paper does not provide a detailed analysis of the computational cost and efficiency of the proposed method, which is crucial for practical applications. The computational complexity of the polygon alignment and optimization steps, especially with varying polygon sizes and numbers of vertices, is not discussed. This lack of analysis makes it difficult to assess the scalability of the method for large-scale datasets or real-time applications.

### Suggestions

To address the limitations regarding dataset generalizability, the authors should conduct experiments on a more diverse set of datasets, including those with varying object complexities and characteristics. This could include datasets with more challenging object shapes, such as those with significant concavities or highly irregular forms, as well as datasets with a wider range of object sizes and scales. Furthermore, the authors should analyze the performance of the proposed method under different conditions, such as varying levels of image noise or occlusion, to better understand its robustness. This would provide a more comprehensive evaluation of the method's applicability in real-world scenarios. The analysis should also include a discussion of the limitations of the method and the types of scenarios where it may not perform optimally.

To provide a more comprehensive comparison, the authors should include a detailed analysis of the performance of the proposed method against state-of-the-art instance segmentation techniques, including those based on transformers and graph neural networks. This comparison should not only focus on overall performance metrics but also delve into the strengths and weaknesses of each method in different scenarios. For example, the authors could compare the performance of the polygon-based method with transformer-based methods in terms of accuracy, speed, and memory usage. Additionally, the authors should analyze the impact of different feature representations and loss functions on the performance of the proposed method. This would provide a more nuanced understanding of the advantages and disadvantages of the polygon-based approach compared to other methods.

Finally, the authors should provide a detailed analysis of the computational cost and efficiency of the proposed method. This analysis should include a breakdown of the computational complexity of each step, including polygon alignment and optimization, and how it scales with the number of vertices and the size of the input images. The authors should also compare the computational cost of the proposed method with other instance segmentation techniques. This analysis should include both theoretical complexity analysis and empirical measurements of runtime and memory usage. This would provide a more complete picture of the practical applicability of the proposed method and its potential for real-world deployment.

### Questions

1. How does the proposed method handle occluded objects or objects with complex shapes that may not be well-represented by polygons?
2. What is the computational cost of the proposed method, and how does it compare to other instance segmentation techniques?
3. Can the proposed method be extended to handle multi-class instance segmentation, and if so, what modifications would be required?

### Rating

6

### Confidence

4

**********
