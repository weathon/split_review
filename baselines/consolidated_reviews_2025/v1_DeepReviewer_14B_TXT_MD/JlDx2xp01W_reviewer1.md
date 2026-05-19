### Summary

The paper presents SAMRefiner, a universal approach to enhance coarse segmentation masks, making them more reliable for training segmentation models with reduced annotation costs. Unlike task-specific refinement techniques, SAMRefiner adapts the Segment Anything Model (SAM) for mask refinement using a noise-tolerant prompting scheme. This includes a multi-prompt excavation strategy that generates diverse prompts, such as distance-guided points and context-aware elastic bounding boxes, to improve initial coarse masks. Additionally, the split-then-merge (STM) pipeline aids in handling multi-object scenarios in semantic segmentation. An enhanced version, SAMRefiner++, further improves performance by introducing an Intersection over Union (IoU) adaptation step that is self-boosted and requires no additional annotations. The framework is flexible, efficient, and demonstrates improved accuracy across various benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is universal and can refine segmentation masks for different segmentation methods.
2. The proposed method is efficient and does not require any additional retraining.
3. The proposed method shows competitive performance on various datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only evaluates SAMRefiner on a limited number of datasets. It would be beneficial to see how it performs on a broader range of datasets, especially those with different types of images and segmentation challenges. The current evaluation, while showing promise, does not fully demonstrate the robustness of the method across diverse real-world scenarios. For example, datasets with highly cluttered backgrounds, significant occlusions, or extreme variations in object scale are not thoroughly explored.
2. The paper does not provide a detailed analysis of the computational resources required for SAMRefiner. This information would be valuable for researchers who want to use the method in their own work. Specifically, the memory footprint and the inference time on different hardware configurations are not clearly stated, making it difficult to assess its practical applicability in resource-constrained environments.

### Suggestions

To address the limited dataset evaluation, the authors should consider including datasets that present more challenging segmentation scenarios. For instance, datasets with medical images, satellite imagery, or high-resolution natural images could provide a more comprehensive evaluation of the method's generalization capabilities. Furthermore, it would be beneficial to analyze the performance of SAMRefiner on datasets with varying levels of annotation quality, as this would reflect real-world scenarios where coarse masks may not be uniformly accurate. This would help to understand the method's sensitivity to the quality of the initial coarse masks and its ability to handle noisy or incomplete annotations. The analysis should also include a discussion of the types of errors that SAMRefiner tends to make on different datasets, which could provide insights into its limitations and potential areas for improvement.

Regarding the computational resource analysis, the authors should provide a detailed breakdown of the memory usage and inference time of SAMRefiner on different hardware configurations. This should include the GPU memory consumption, CPU usage, and the time taken to process a single image or a batch of images. It would also be useful to compare the computational cost of SAMRefiner with other mask refinement methods, which would help to assess its efficiency. The authors should also investigate the impact of different optimization techniques on the computational performance of SAMRefiner, such as model quantization or pruning. This would provide valuable guidance for researchers who want to deploy the method in resource-constrained environments. Furthermore, the authors should specify the software and library versions used in their experiments to ensure reproducibility.

Finally, the authors should explore the limitations of the multi-prompt strategy more thoroughly. While the paper mentions that the multi-prompt strategy is effective, it does not provide a detailed analysis of the scenarios where it might fail or underperform. For example, it would be useful to investigate the impact of the number of prompts on the refinement quality and the computational cost. The authors should also analyze the sensitivity of the method to the type of prompts used, as some prompts might be more effective than others in certain scenarios. A more detailed analysis of the prompt generation process and its impact on the final segmentation quality would be beneficial. This could involve visualizing the generated prompts and analyzing their correlation with the refined masks.

### Questions

1. Can you provide more insights into how the noise-tolerant prompting scheme was developed? What were the key challenges in designing this scheme, and how were they addressed?
2. The split-then-merge (STM) pipeline is introduced to handle multi-object cases in semantic segmentation. Can you provide more details on how this pipeline works and its effectiveness in different scenarios?
3. How does SAMRefiner compare to other state-of-the-art mask refinement methods in terms of accuracy and efficiency?
4. Can you discuss any limitations or challenges you encountered while developing SAMRefiner and how you addressed them?
5. How does SAMRefiner perform on datasets with different levels of annotation quality? Does the performance degrade significantly when the initial coarse masks are of poor quality?
6. What are the computational requirements for running SAMRefiner, and how does it compare to other mask refinement methods in terms of computational efficiency?
7. Can you provide more details on the multi-prompt excavation strategy and its effectiveness in different scenarios? Are there any limitations to this strategy, and how can they be addressed?

### Rating

6

### Confidence

4

**********
