### Summary

This paper proposes a method of differentiable polygon modeling for object instance segmentation under the active contour / snake modeling framework. It addresses two modeling problems. It presents the PolygonAlign that utilizes a contour-length-fraction (CLF) based vertex re-sampling strategy for aligning always-K-vertex predicted polygons and varying-L-vertex target ground-truth polygon using a simple l-2 norm in learning. It also presents the affine transformation decoupled vertex displacement regression method for polygon parameterization that cooperates with the PolygonAlign. The proposed method is tested in MS-COCO instance segmentation benchmark with state-of-the-art performance obtained compared with the prior art of contour-based instance segmentation.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well written and easy to follow. 
2. The proposed method is simple and effective. 
3. The proposed method achieves state-of-the-art performance on MS-COCO instance segmentation benchmark.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a simple extension of PolarMask++ and PolarSnake. The main difference is that it proposes a unified polygon parameterization method for both bit-mask and contour-based modeling. The unified polygon parameterization is also a simple extension of the affine transformation decoupled vertex displacement regression in PolarSnake. The main difference is that it proposes a unified vertex displacement regression for bit-mask and contour-based modeling. The unified vertex displacement regression is also a simple extension of the vertex displacement regression in PolarMask++. The unified polygon parameterization and unified vertex displacement regression are not novel enough.
2. The proposed method only achieves state-of-the-art performance on MS-COCO instance segmentation benchmark. It is not compared with the prior art on other datasets such as Pascal VOC. 
3. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake.
4. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake.
5. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake.

### Suggestions

The paper's core contribution, the unified polygon parameterization and vertex displacement regression, needs further justification regarding its novelty. While the authors claim a novel approach, the methods appear to be incremental extensions of existing techniques. Specifically, the unified polygon parameterization, which combines bit-mask and contour-based modeling, seems to be a straightforward application of existing affine transformation decoupling and vertex displacement regression. The paper should provide a more detailed analysis of the limitations of existing methods that this unified approach overcomes, and why the proposed method is a significant improvement. A more rigorous comparison with existing methods, highlighting the specific advantages of the proposed approach, is needed to establish its novelty and contribution. The authors should also consider exploring more complex polygon parameterizations or displacement regression techniques that could further enhance the performance and robustness of their method.

Furthermore, the experimental evaluation is limited by the lack of comparisons on other datasets. While the MS-COCO benchmark is a standard for instance segmentation, it is crucial to demonstrate the generalizability of the proposed method on other datasets, such as Pascal VOC. The absence of such comparisons makes it difficult to assess the method's performance in different scenarios and its potential for real-world applications. The authors should include experiments on additional datasets to provide a more comprehensive evaluation of their method. Additionally, the paper should include comparisons with a broader range of contour-based methods, including PolarMask and other state-of-the-art techniques. This would provide a more complete picture of the method's performance relative to the existing literature and help to establish its position in the field. The current comparisons are insufficient to fully validate the effectiveness of the proposed method.

Finally, the paper should address the potential for combining the proposed method with other techniques, such as attention mechanisms or graph neural networks, to further improve performance. The authors should discuss the potential benefits and challenges of such combinations and provide some preliminary results or insights. This would demonstrate the versatility of the proposed method and its potential for future research. The paper should also include a more detailed discussion of the limitations of the proposed method and potential avenues for future work. This would provide a more balanced and comprehensive view of the method's strengths and weaknesses. The current discussion of limitations is too brief and does not fully address the potential for improvement.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

4

**********
