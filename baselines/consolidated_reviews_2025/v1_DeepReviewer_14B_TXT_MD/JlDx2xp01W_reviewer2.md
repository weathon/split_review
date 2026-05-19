### Summary

This paper introduces SAMRefiner, a novel approach for refining coarse segmentation masks using the Segment Anything Model (SAM). The authors address the challenge of noisy prompts derived from imperfect initial masks by proposing a multi-prompt excavation strategy. This strategy employs distance-guided point prompts, context-aware elastic bounding boxes (CEBoxes), and Gaussian-style mask prompts to collaboratively improve mask quality. For semantic segmentation, they introduce a split-then-merge (STM) pipeline to handle multi-object scenarios effectively. Additionally, they present SAMRefiner++, which incorporates an IoU adaptation step to enhance SAM's dataset-specific performance without requiring additional annotations. The method demonstrates strong performance across various benchmarks, outperforming existing refinement techniques while maintaining efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to refining segmentation masks using SAM, addressing a practical need in weakly-supervised segmentation tasks. The idea of adapting SAM for refinement rather than direct prediction is innovative and leverages SAM's strengths in a new way.
2. The proposed multi-prompt excavation strategy, including distance-guided points, context-aware elastic boxes, and Gaussian-style masks, demonstrates a thoughtful approach to handling noisy prompts. The split-then-merge pipeline for semantic segmentation effectively addresses multi-object scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method. Specifically, the time required for prompt generation and mask refinement should be quantified and compared against existing approaches. The analysis should include a breakdown of the time spent on each step of the multi-prompt excavation strategy (distance-guided point prompts, context-aware elastic boxes, and Gaussian-style mask prompts) and the split-then-merge pipeline, as well as the IoU adaptation step in SAMRefiner++. Furthermore, the memory footprint of the method, especially during the prompt generation phase, should be discussed, as this can be a limiting factor for practical applications.
2. The paper does not adequately explore the sensitivity of the method to the quality of the initial coarse masks. While the method is designed to handle noisy prompts, a more rigorous analysis of how performance degrades with increasing levels of noise and incompleteness in the initial masks is needed. This should include a quantitative evaluation of the method's robustness to different types of noise (e.g., random pixel noise, boundary fuzzing, and object occlusion) and varying degrees of incompleteness (e.g., missing object parts, truncated objects). The evaluation should also consider the impact of different types of initial mask generation methods on the final refinement quality.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time required for each step of their method, including prompt generation (distance-guided points, elastic boxes, and Gaussian masks), the split-then-merge pipeline, and the IoU adaptation step. This analysis should be performed on a standard hardware setup and should include the memory footprint of each step. The authors should compare these results against existing mask refinement techniques, providing a clear understanding of the trade-offs between performance and computational cost. Furthermore, the authors should investigate the potential for optimizing the prompt generation process, such as using more efficient algorithms for distance transform or elastic box computation, to reduce the overall computational overhead. This would make the method more practical for real-world applications where computational resources may be limited.

To address the sensitivity to initial mask quality, the authors should conduct a systematic evaluation of their method using a range of coarse masks with varying levels of noise and incompleteness. This evaluation should include quantitative metrics that measure the accuracy of the refined masks compared to the ground truth, as well as metrics that quantify the degree of noise and incompleteness in the initial masks. The authors should also analyze the impact of different types of noise (e.g., random pixel noise, boundary fuzzing, object occlusion) and incompleteness (e.g., missing object parts, truncated objects) on the final refinement quality. This analysis should provide insights into the limitations of the method and help guide future research in developing more robust mask refinement techniques. The authors should also explore the use of data augmentation techniques to improve the robustness of the method to noisy initial masks.

Finally, the authors should provide a more detailed discussion of the limitations of their method and potential avenues for future research. This discussion should include the challenges of applying the method to different types of images and objects, as well as the potential for combining the method with other techniques to further improve performance. The authors should also discuss the potential for extending their method to other segmentation tasks, such as video segmentation or 3D segmentation. This would help to broaden the impact of their work and inspire future research in this area.

### Questions

1. How does the method handle cases where the coarse mask contains multiple distinct objects of the same category, particularly in semantic segmentation tasks? The paper mentions a split-then-merge pipeline, but more details on how it distinguishes between separate instances of the same category would be beneficial.
2. What is the impact of the choice of prompts (point, box, mask) on the final refinement quality? Are there specific scenarios where one type of prompt significantly outperforms the others?
3. The paper mentions that SAMRefiner++ shows significant improvement over SAMRefiner on the VOC dataset but less so on COCO. What are the underlying reasons for this difference? Is it related to dataset characteristics, or does it reflect limitations in the IoU adaptation strategy?

### Rating

6

### Confidence

4

**********
