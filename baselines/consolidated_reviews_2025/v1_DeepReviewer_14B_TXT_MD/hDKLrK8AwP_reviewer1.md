### Summary

The paper introduces a framework for generating Scalable Vector Graphics (SVG) with a focus on code readability, alongside visual accuracy. The authors define three key aspects of readable SVG code—logical structure, appropriate element use, and redundant element removal—and propose corresponding metrics (SPI, ESS, RQ) and differentiable loss functions to optimize these aspects. Experiments demonstrate that their approach improves code readability without compromising visual fidelity.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses an under-explored yet important aspect of SVG generation—code readability—which is crucial for practical applications involving manual adjustments and understanding of generated graphics.
- The paper is well-structured and clearly written, with defined desiderata for readability and corresponding metrics and loss functions.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed Structural Proximity Index (SPI) seems overly simplified. In SVGs, elements can be nested within each other, so the distance between two elements is not necessarily indicative of their structural relationship. For example, consider two paths <path d="M10 10 h 80 v 80 h -80 z"/><path d="M30 30 h 40 v 40 h -40 z"/>. According to the authors' definition, the structural proximity between the two paths is the distance between the centroid of the two paths. But the "real" structural proximity is very close because the two paths are nested.
- Following from the first point, the Structural Consistency Loss also seems overly simplified. This loss only accounts for the spatial distance between elements, but as mentioned before, SVG elements can be nested, which is not considered in this loss.
- The authors claim that the Element Simplicity Score (ESS) and Element Appropriateness Loss (L_EA) encourage the model to favor simpler SVG elements. However, I don't see why the model would choose a circle over a path if the former cannot represent the desired shape. According to Occam's razor, the model should prefer shapes that directly correspond to the target shape, even if they are more complex. For example, if the target shape is a circle, the model should choose a circle. But if the target shape is a star, the model should choose a path even if a 200-circle group could also form a star.
- The authors propose using total edge length as a measure of shape simplicity, which is then incorporated into the Element Appropriateness Loss. However, this measure is highly sensitive to shape complexity and can lead to inaccurate representations. For example, a circle has a longer edge length than a square, and a rough square has a longer edge length than a perfect square. This suggests that edge length may not be an appropriate metric for encouraging the use of simpler elements.
- The authors introduce a Redundancy Quotient (RQ) to measure redundancy by perturbing each element and observing its impact on the rendered image. However, this approach is not differentiable, which is a significant limitation for gradient-based optimization. While the authors propose an alternative differentiable proxy loss, they do not provide experimental results for this proxy, making it difficult to assess its effectiveness. Furthermore, the RQ calculation requires rendering the SVG and then perturbing each element, which is computationally expensive and may not be feasible for real-time applications.

### Suggestions

The paper's core idea of incorporating readability into SVG generation is valuable, but the proposed metrics and loss functions need further refinement. The Structural Proximity Index (SPI) and Structural Consistency Loss (L_SC) should be revised to account for the hierarchical nature of SVGs. Instead of relying solely on spatial distance, the model should consider the parent-child relationships between elements. One approach could be to use a tree-based metric that calculates the distance between elements based on their positions in the SVG tree. For example, the distance between two nested elements should be smaller than the distance between two non-nested elements, even if they are spatially far apart. This could be achieved by incorporating a term that penalizes deviations from the expected parent-child relationships. Furthermore, the model should be able to learn the importance of different structural relationships, rather than treating all relationships equally. This could be done by introducing learnable weights for different types of relationships, such as nesting, grouping, and ordering.

The Element Simplicity Score (ESS) and Element Appropriateness Loss (L_EA) also need to be improved. The current approach of using total edge length as a measure of shape simplicity is not robust and can lead to suboptimal results. Instead, the model should be trained to select the most appropriate element for a given shape, rather than simply favoring simpler elements. This could be achieved by introducing a classification loss that encourages the model to predict the correct element type. For example, the model could be trained to predict whether a shape is best represented by a circle, rectangle, or path. The loss function could then be designed to penalize incorrect predictions. Additionally, the model should be able to handle complex shapes that cannot be represented by a single simple element. In such cases, the model should be able to decompose the shape into simpler components and represent each component using the most appropriate element. This could be achieved by introducing a hierarchical decomposition mechanism that allows the model to recursively break down complex shapes into simpler parts.

Finally, the Redundancy Quotient (RQ) needs to be made differentiable and computationally efficient. The current approach of perturbing each element and observing its impact on the rendered image is not suitable for gradient-based optimization. A more effective approach would be to use a differentiable proxy loss that measures the redundancy of elements based on their visual impact. For example, the model could be trained to predict the visual impact of each element and then use this prediction to identify redundant elements. The proxy loss could be designed to penalize elements that have a low visual impact. Furthermore, the model should be able to handle complex SVGs with a large number of elements. The current approach of perturbing each element one by one is computationally expensive and may not be feasible for real-time applications. A more efficient approach would be to use a batch-based method that perturbs multiple elements simultaneously. This could be achieved by introducing a batch-based perturbation mechanism that allows the model to update the parameters of multiple elements in a single step.

### Questions

- The authors propose using total edge length as a measure of shape simplicity, which is then incorporated into the Element Appropriateness Loss. However, this measure is highly sensitive to shape complexity and can lead to inaccurate representations. For example, a circle has a longer edge length than a square, and a rough square has a longer edge length than a perfect square. This suggests that edge length may not be an appropriate metric for encouraging the use of simpler elements.
- The authors introduce a Redundancy Quotient (RQ) to measure redundancy by perturbing each element and observing its impact on the rendered image. However, this approach is not differentiable, which is a significant limitation for gradient-based optimization. While the authors propose an alternative differentiable proxy loss, they do not provide experimental results for this proxy, making it difficult to assess its effectiveness. Furthermore, the RQ calculation requires rendering the SVG and then perturbing each element, which is computationally expensive and may not be feasible for real-time applications.

### Rating

3

### Confidence

4

**********
