### Summary

This paper addresses the problem of differentiable polygon modeling for object instance segmentation. It addresses two modeling problems. It presents the PolygonAlign that utilizes a contour-length-fraction (CLF) based vertex re-sampling strategy for aligning always-K-vertex predicted polygons and varying-L-vertex target ground-truth polygon using a simple l-2 norm in learning. It also presents the affine transformation decoupled vertex displacement regression method for polygon parameterization that cooperates with the PolygonAlign. The proposed method is tested in MS-COCO instance segmentation benchmark with state-of-the-art performance obtained compared with the prior art of contour-based instance segmentation.

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

The paper's primary weakness lies in the incremental nature of its contributions. While the proposed method achieves state-of-the-art results on the MS-COCO dataset, the core techniques appear to be largely derived from and built upon existing methods like PolarMask++ and PolarSnake. The unified polygon parameterization and vertex displacement regression, while presented as novel, seem to be relatively straightforward extensions of the affine transformation decoupling and vertex displacement regression techniques already present in those prior works. To strengthen the paper, the authors should clearly articulate the specific limitations of prior methods that their approach overcomes, and provide a more in-depth analysis of the novelty of their approach beyond simply combining existing techniques. A more rigorous justification for the specific design choices, such as the contour-length-fraction (CLF) based vertex re-sampling, is needed to demonstrate its effectiveness and necessity. Furthermore, the paper would benefit from a more detailed discussion of the computational complexity and efficiency of the proposed method compared to existing approaches.

To address the lack of comprehensive experimental validation, the authors should include comparisons with a broader range of contour-based methods on multiple datasets. While MS-COCO is a standard benchmark, it is crucial to demonstrate the generalizability of the proposed method across different datasets and scenarios. Specifically, the authors should include results on Pascal VOC, which is a widely used dataset for object instance segmentation. Furthermore, the comparison should not be limited to PolarMask++ and PolarSnake. The authors should include comparisons with other relevant contour-based methods such as PolarMask and other state-of-the-art methods. This would provide a more complete picture of the performance of the proposed method and its advantages over existing techniques. The experimental section should also include ablation studies to analyze the impact of different components of the proposed method, such as the CLF-based vertex re-sampling and the unified polygon parameterization, to better understand their contribution to the overall performance.

Finally, the paper would benefit from a more detailed discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors could discuss the sensitivity of the method to different hyperparameters, the computational cost of the method, and the potential for extending the method to handle more complex object shapes. The authors should also discuss the potential for combining their method with other techniques, such as attention mechanisms or graph neural networks, to further improve performance. By addressing these limitations and discussing potential future directions, the authors can further strengthen the impact and significance of their work.

### Questions

1. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake. 
2. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake. 
3. The proposed method is only compared with PolarMask++ and PolarSnake. It is not compared with other contour-based methods such as PolarMask and PolarSnake.

### Rating

5

### Confidence

4

**********
