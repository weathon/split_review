### Summary

The paper introduces a novel method for controllable video generation that enables precise manipulation of multi-entity 3D motions. The authors propose a plug-and-play 3D-motion grounded object injector that fuses entity prompts and 3D trajectories, allowing for fine-grained control over video generation. To address the lack of suitable training data, the authors construct a 360-Motion dataset, which features diverse entities and various 3D motion templates. The proposed method achieves state-of-the-art accuracy and generalization in controlling 3D entity motions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach for controllable video generation by enabling precise manipulation of multi-entity 3D motions. This is a significant advancement over traditional 2D control signals, which often fail to capture the inherent 3D nature of object movements.
2. The authors have constructed a comprehensive 360-Motion dataset, which features diverse entities and various 3D motion templates. This dataset not only supports the training of the proposed model but also serves as a valuable resource for future research in controllable video generation.
3. The proposed method, 3DTrajMaster, is technically sound and well-designed. The use of a gated self-attention mechanism for motion fusion further enhances the model's ability to handle multiple entity trajectories.
4. The paper is well-written and clearly presented. The authors provide a detailed explanation of the proposed method, including the dataset construction process, model architecture, and experimental setup. The figures and diagrams are informative and effectively illustrate the key concepts and technical details.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on a synthetic dataset for training, which may limit its ability to generalize to real-world scenarios. The synthetic data, while diverse, might not capture the full range of complexities and variations present in real-world videos, particularly in terms of lighting, occlusions, and dynamic backgrounds. This could lead to a domain shift issue, where the model performs well on the training data but struggles to generalize to unseen real-world videos.
2. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. The training and inference processes involve complex operations such as gated self-attention and 3D self-attention, which can be computationally expensive. The lack of information on training time, memory usage, and inference speed makes it difficult to assess the practical feasibility of the method, especially for real-time applications or deployment on resource-constrained devices.

### Suggestions

The authors should consider expanding the training dataset to include more diverse real-world scenarios. This could involve incorporating videos with varying lighting conditions, occlusions, and dynamic backgrounds. Furthermore, data augmentation techniques could be explored to artificially increase the diversity of the training data and improve the model's robustness. For example, techniques such as random rotations, scaling, and color jittering could be applied to the synthetic data to simulate different real-world conditions. Additionally, the model could be trained on a combination of synthetic and real-world data to leverage the strengths of both. This would require careful consideration of the domain gap between the two datasets and the development of techniques to bridge this gap effectively. The authors should also investigate the use of domain adaptation techniques to improve the model's generalization ability to real-world scenarios.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the computational resources required for training and inference. This should include information on training time, memory usage, and inference speed. The authors should also explore techniques to reduce the computational cost of the method, such as model compression, quantization, and efficient implementation of the attention mechanisms. For example, the authors could investigate the use of sparse attention or low-rank approximations to reduce the computational complexity of the self-attention layers. Furthermore, the authors should consider optimizing the implementation of the method for different hardware platforms, such as GPUs and TPUs, to improve its efficiency. A thorough analysis of the computational cost would provide a more complete understanding of the method's practical feasibility and guide future research efforts.

Finally, the authors should consider exploring the use of more advanced evaluation metrics that can capture the quality of the generated videos more comprehensively. While the current metrics provide some insight into the performance of the method, they may not fully capture the nuances of video quality and motion accuracy. For example, metrics such as perceptual quality scores, temporal consistency scores, and motion smoothness scores could be used to provide a more comprehensive evaluation of the method. Additionally, the authors should consider conducting user studies to assess the subjective quality of the generated videos and to identify any potential issues that may not be captured by the objective metrics. This would provide a more holistic evaluation of the method and guide future improvements.

### Questions

1. How does the model perform on real-world videos with complex backgrounds and diverse lighting conditions?
2. What is the computational cost of training and inference for the proposed method? How does it compare to existing methods?

### Rating

6

### Confidence

3

**********
