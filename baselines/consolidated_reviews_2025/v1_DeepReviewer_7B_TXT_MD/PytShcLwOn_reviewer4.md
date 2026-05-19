### Summary

This paper introduces a new task of generating realistic and diverse 3D hand trajectories from single images. The proposed method consists of a pipeline for extracting features at various levels of hand-object interaction details from the single image input, and a conditional motion generation diffusion model that learns to generate realistic and diverse 3D hand trajectories. The authors also introduce task-specific metrics to evaluate the performance of the proposed method. Extensive experiments show that the proposed method generates more natural and diverse hand trajectories than baselines and presents promising generalization capability on unseen objects. The accuracy of the generated hand trajectories is confirmed in a physics simulation setting, showcasing the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is technically sound and well-motivated.
3. The proposed method is evaluated on two datasets, and the results show that the proposed method outperforms baselines.
4. The proposed method is evaluated in a physics simulation setting, which demonstrates the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is evaluated on two datasets, FPHAB and HOI4D. The authors claim that the proposed method generalizes well to unseen objects. However, the evaluation is not convincing. For example, the proposed method is evaluated on only 4 objects in the HOI4D dataset, which is not enough to support the claim that the proposed method generalizes well to unseen objects. The limited number of objects tested makes it difficult to assess the true generalization capability of the method, as the model might be overfitting to the specific characteristics of the four chosen objects. A more rigorous evaluation would involve testing on a larger and more diverse set of objects, including those with varying shapes, sizes, and material properties.
2. The proposed method is evaluated on the FPHAB and HOI4D datasets. However, the proposed method is not compared with existing methods for hand motion generation. The lack of comparison with existing hand motion generation methods makes it difficult to assess the novelty and effectiveness of the proposed approach. It is crucial to compare against relevant baselines to understand the advantages and limitations of the proposed method in the context of the broader field of hand motion generation. This comparison should include both quantitative and qualitative evaluations to provide a comprehensive understanding of the method's performance.
3. The proposed method is evaluated on the FPHAB and HOI4D datasets. However, the proposed method is not compared with existing methods for hand motion generation. The lack of comparison with existing hand motion generation methods makes it difficult to assess the novelty and effectiveness of the proposed approach. It is crucial to compare against relevant baselines to understand the advantages and limitations of the proposed method in the context of the broader field of hand motion generation. This comparison should include both quantitative and qualitative evaluations to provide a comprehensive understanding of the method's performance.

### Suggestions

The evaluation of the proposed method's generalization capability needs to be significantly strengthened. Instead of testing on only four objects from the HOI4D dataset, the authors should evaluate the method on a much larger and more diverse set of objects. This could include objects with varying shapes, sizes, materials, and even different object categories. Furthermore, the evaluation should not only focus on the final pose but also on the trajectory of the hand during the interaction. This would provide a more comprehensive understanding of the method's ability to generalize to unseen objects. The authors should also consider using a more rigorous evaluation protocol, such as cross-validation, to ensure that the results are not biased by the specific choice of objects.

To address the lack of comparison with existing hand motion generation methods, the authors should include a thorough comparison with relevant baselines. This comparison should not only include quantitative metrics, such as FID and Diversity, but also qualitative evaluations, such as visual inspection of the generated hand trajectories. The authors should select a few representative hand motion generation methods and compare their performance with the proposed method on both datasets. This comparison should also include an analysis of the strengths and weaknesses of each method, highlighting the advantages and limitations of the proposed approach. The authors should also discuss the differences in methodology and performance between the proposed method and existing methods, providing a clear understanding of the novelty and contribution of their work.

Finally, the authors should provide a more detailed analysis of the limitations of the proposed method. This analysis should include a discussion of the scenarios where the method is likely to fail and the potential reasons for these failures. For example, the authors should discuss the limitations of the method in handling complex hand-object interactions or in generating hand trajectories for objects with unusual shapes or textures. This analysis would provide a more balanced and realistic assessment of the method's capabilities and limitations, and it would also help to guide future research in this area.

### Questions

1. The proposed method is evaluated on the FPHAB and HOI4D datasets. However, the proposed method is not compared with existing methods for hand motion generation. Could the authors compare the proposed method with existing methods for hand motion generation?
2. The proposed method is evaluated on the FPHAB and HOI4D datasets. However, the proposed method is not compared with existing methods for hand motion generation. Could the authors compare the proposed method with existing methods for hand motion generation?
3. The proposed method is evaluated on the FPHAB and HOI4D datasets. However, the proposed method is not compared with existing methods for hand motion generation. Could the authors compare the proposed method with existing methods for hand motion generation?

### Rating

6

### Confidence

4

**********
