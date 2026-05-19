### Summary

This paper proposes a differentiable polygon-based method for object instance segmentation. The proposed method includes a polygon alignment module and a polygon refinement module. The polygon alignment module aligns the predicted polygon with the ground-truth polygon using a contour-length-fraction (CLF) based vertex re-sampling strategy. The polygon refinement module refines the predicted polygon using a one-step vertex-guided deformation module. The proposed method is evaluated on the MS-COCO dataset and achieves state-of-the-art performance compared with the prior art of contour-based instance segmentation.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method achieves state-of-the-art performance on the MS-COCO dataset.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a simple extension of PolarMask++. The main difference is that it proposes a unified polygon parameterization method for both bit-mask and contour-based modeling. The unified polygon parameterization is also a simple extension of the affine transformation decoupled vertex displacement regression in PolarSnake. The main difference is that it proposes a unified vertex displacement regression for bit-mask and contour-based modeling. The unified vertex displacement regression is also a simple extension of the vertex displacement regression in PolarMask++. The unified polygon parameterization and unified vertex displacement regression are not novel enough.
2. The proposed method only achieves state-of-the-art performance on MS-COCO instance segmentation benchmark. It is not compared with the prior art on other datasets such as Pascal VOC.
3. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake.

### Suggestions

The core weakness of this paper lies in the incremental nature of its contributions. While the authors present a unified polygon parameterization and a unified vertex displacement regression, these appear to be straightforward extensions of existing techniques. Specifically, the unified polygon parameterization, which combines bit-mask and contour-based modeling, seems to be a direct application of existing affine transformation decoupling and vertex displacement regression. Similarly, the unified vertex displacement regression, which is applied to both bit-masks and contours, appears to be a simple extension of the vertex displacement regression used in PolarMask. The paper needs to clearly articulate the specific limitations of prior methods that this unified approach overcomes, and provide a more in-depth analysis of the novelty of their approach beyond simply combining existing techniques. A more rigorous justification for the specific design choices, such as the contour-length-fraction (CLF) based vertex re-sampling, is needed to demonstrate its effectiveness and necessity. The paper should also explore more complex polygon parameterizations or displacement regression techniques that could further enhance the performance and robustness of their method.

Furthermore, the experimental evaluation is limited by the lack of comparisons on other datasets. While the MS-COCO benchmark is a standard for instance segmentation, it is crucial to demonstrate the generalizability of the proposed method on other datasets, such as Pascal VOC. The absence of such comparisons makes it difficult to assess the method's performance in different scenarios and its potential for real-world applications. The paper should include experiments on additional datasets to provide a more comprehensive evaluation of their method. Additionally, the paper should include comparisons with a broader range of contour-based methods, including PolarMask and other state-of-the-art techniques. This would provide a more complete picture of the method's performance relative to the existing literature and help to establish its position in the field. The current comparisons are insufficient to fully validate the effectiveness of the proposed method.

Finally, the paper should address the potential for combining the proposed method with other techniques, such as attention mechanisms or graph neural networks, to further improve performance. The authors should discuss the potential benefits and challenges of such combinations and provide some preliminary results or insights. This would demonstrate the versatility of the proposed method and its potential for future research. The paper should also include a more detailed discussion of the limitations of the proposed method and potential avenues for future work. This would provide a more balanced and comprehensive view of the method's strengths and weaknesses. The current discussion of limitations is too brief and does not fully address the potential for improvement.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

5

**********
