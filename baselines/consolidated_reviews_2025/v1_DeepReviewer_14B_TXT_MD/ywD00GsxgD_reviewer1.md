### Summary

This paper introduces a novel approach to model training by using synthetic data as a validation set for checkpoint selection. The authors generate synthetic tumors in healthy liver CT scans to create a large and diverse validation set. They demonstrate that using synthetic data for validation improves model performance on both in-distribution and out-of-distribution data for the task of liver tumor segmentation. The approach also alleviates the need for large amounts of real annotated data for validation, which can be costly and time-consuming to acquire, especially for early-stage tumors.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel approach to address the challenge of limited annotated data for training and validation of AI models in medical imaging. The use of synthetic data as a validation set is an innovative idea that can potentially improve model performance and generalization.
- The paper demonstrates the effectiveness of the proposed approach through experiments on multiple datasets and evaluation metrics. The results show that the synthetic data validation set can select model checkpoints that generalize well to both in-distribution and out-of-distribution data.

### Weaknesses

#### Some Related Works


#### comment

 - The quality of the generated synthetic tumors is a concern. While the paper describes a multi-step process for generating tumors, there is limited discussion or evaluation of the realism of the synthetic tumors. It is unclear how well the generated tumors mimic real tumors in terms of shape, texture, and appearance. The method uses basic image processing techniques such as ellipsoid shaping and Gaussian noise for tumor generation, which may not capture the full complexity of real tumors. A more rigorous evaluation of the synthetic tumor quality, including quantitative comparisons with real tumors using metrics like shape feature distributions and texture analysis, is needed to justify the effectiveness of the proposed approach.
- The paper focuses on a single application (liver tumor segmentation) and it is unclear how well the proposed approach would generalize to other medical imaging tasks or domains. The use of synthetic data for validation is an interesting idea, but it may not be applicable to all types of medical images or segmentation tasks. For example, the method's reliance on specific anatomical structures and the ability to easily insert synthetic anomalies may not translate well to more complex or variable anatomical regions. The paper should include a discussion of the limitations of the approach and potential challenges in applying it to other tasks, such as segmenting small vessels or lesions with complex morphologies.

### Suggestions

The authors should conduct a more thorough evaluation of the synthetic tumor quality. This could involve a quantitative comparison of the generated tumors with real tumors using metrics such as shape feature distributions (e.g., sphericity, compactness), texture analysis (e.g., gray-level co-occurrence matrix features), and intensity histograms. Additionally, a perceptual study with medical experts could be performed to assess the realism of the synthetic tumors. This would provide a more objective measure of the quality of the generated data and help to justify the use of synthetic data for validation. The authors should also explore more advanced techniques for tumor generation, such as generative adversarial networks (GANs) or variational autoencoders (VAEs), which have shown promise in generating realistic medical images.

To address the generalizability concerns, the authors should discuss the limitations of their approach and potential challenges in applying it to other medical imaging tasks. For example, they could discuss how the method might be adapted to segment different types of anomalies, such as lesions with irregular shapes or textures. They could also explore the use of synthetic data for validation in other medical imaging modalities, such as MRI or ultrasound. Furthermore, the authors should consider the impact of domain shift on the performance of the model when using synthetic data for validation. A more detailed analysis of the sensitivity of the approach to the quality and diversity of the synthetic data would be beneficial. This could involve experiments with different synthetic data generation parameters or different types of synthetic anomalies.

Finally, the authors should provide more details on the implementation of their method, including the specific parameters used for tumor generation and the training procedure. This would allow other researchers to reproduce their results and build upon their work. The paper should also include a discussion of the computational cost of generating synthetic data and using it for validation. This would help to assess the practicality of the proposed approach in real-world settings. The authors should also consider the potential for bias in the synthetic data and how this might affect the performance of the model.

### Questions

- How sensitive is the performance of the model to the quality and diversity of the synthetic tumors generated? Are there specific characteristics of the synthetic tumors that are more important for model performance?
- What are the potential limitations or challenges of using synthetic data as a validation set in other medical imaging tasks or domains? How could the proposed approach be adapted to handle different types of medical images or segmentation tasks?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
