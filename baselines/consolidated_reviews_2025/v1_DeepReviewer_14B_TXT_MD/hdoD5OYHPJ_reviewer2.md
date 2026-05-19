### Summary

This paper proposes a simple method to auto tune zero-shot classifiers. The proposed method tunes per-image weights to each prompt template at inference time based on statistics of class descriptor-image similarities. Extensive experiments demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective.
2. The proposed method is applicable to various existing zero-shot classifiers.
3. The experimental results are extensive.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires one-step gradient ascent to update the weight of each image, which increases the inference time compared to the original zero-shot classifier. It would be better to give a comparison of the inference time between the proposed method and baselines. Specifically, the paper should quantify the overhead of the gradient ascent step, perhaps in terms of milliseconds per image, and compare this to the base inference time of the zero-shot classifier without the proposed tuning. This would provide a clearer picture of the practical cost of the method.
2. The authors do not discuss the potential impact of the proposed method on other zero-shot tasks, such as object detection or segmentation. It is unclear whether the per-image prompt weighting strategy would generalize to tasks beyond image classification, where the output space is more complex and involves bounding boxes or masks. A discussion of the challenges and potential adaptations needed for these tasks would be valuable.

### Suggestions

The paper would benefit from a more detailed analysis of the computational overhead introduced by the proposed method. While the authors mention that the gradient ascent step is simple, it is crucial to quantify its impact on inference time. The paper should include a table or figure that shows the inference time of the baseline zero-shot classifier and the proposed method, broken down by the time spent on the base classifier and the time spent on the prompt tuning step. This analysis should be performed on a variety of image sizes and classifier architectures to demonstrate the scalability of the method. Furthermore, it would be beneficial to compare the inference time of the proposed method with other test-time adaptation techniques, if applicable, to provide a more comprehensive understanding of its efficiency.

To address the lack of discussion on other zero-shot tasks, the authors should explore the potential of applying their method to object detection or segmentation. This could involve a preliminary experiment on a standard benchmark dataset for object detection or segmentation, using a zero-shot approach. The authors should discuss the challenges of adapting the per-image prompt weighting strategy to these tasks, such as how to handle the spatial aspect of the output (e.g., bounding boxes or masks) and how to define the similarity between class descriptors and image regions. Even if the method does not directly translate to these tasks, a discussion of the challenges and potential solutions would be valuable for future research. For example, the authors could explore whether the prompt tuning could be applied to the text prompts used for generating region proposals or whether a different approach is needed for these tasks.

Finally, the paper should include a more in-depth analysis of the cases where the proposed method fails to improve performance. While the authors mention that the method sometimes hurts performance, they do not provide a detailed analysis of the reasons behind these failures. It would be helpful to categorize the failure cases and identify the common characteristics of images where the method does not work well. For example, are these images with unusual viewpoints, occlusions, or other challenging conditions? This analysis could provide insights into the limitations of the method and suggest potential directions for future improvement. Furthermore, the authors could explore whether the method is more effective for certain types of classes or images, and whether there are any patterns in the prompt weights that are learned for these cases.

### Questions

1. In Table 1, why does the proposed method not improve or even hurt the performance when using CLIP templates? Does this mean the CLIP templates are already the optimal templates for each class?
2. In Table 1, why does the proposed method not improve the performance when using the CoCa model?
3. In Table 1, why does the proposed method not improve the performance on the ImageNet dataset when using the DataComp model?
4. In Figure 4, why does the proposed method perform worse when the entropy reduction factor is lower for the Oxford Pets dataset and the EuroSAT dataset?
5. In Figure 6, why does the proposed method perform worse in some cases in the controlled setting? What are the possible reasons for this? Does this mean the proposed method is more effective for certain types of classes or images?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
