### Summary

This paper proposes a new way to combine CLIP and DINOv2 visual encoders to enhance the visual capabilities of MLLMs. The authors first conduct an extensive investigation into the effectiveness of different visual encoders for MLLMs and find that shallow layer features contain low-level detailed information which is helpful for fine-grained tasks such as grounding and region understanding, while deep layer features contain more fine-grained visual information. Based on the analysis, the authors propose a COMM framework that integrates CLIP and DINOv2 with a multi-level feature merging strategy to enhance the visual capabilities of MLLMs. Experimental results demonstrate the superiority of COMM over existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to investigate the effectiveness of different visual encoders for MLLMs.
3. The proposed COMM framework is simple yet effective, and the experimental results demonstrate its superiority over existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only conduct experiments on the CLIP and DINOv2. It would be better to conduct experiments on more visual encoders to make the conclusions more convincing.
2. The authors only conduct experiments on the ViT-Large. It would be better to conduct experiments on other visual backbones to make the conclusions more convincing.
3. The authors only conduct experiments on the 224x224 resolution. It would be better to conduct experiments on other resolutions to make the conclusions more convincing.

### Suggestions

The paper's investigation into visual encoders for MLLMs is a valuable contribution, but the scope of the experiments could be significantly broadened to strengthen the conclusions. Specifically, the authors should consider including a wider range of visual encoders beyond CLIP and DINOv2. For instance, exploring models like ResNet-based encoders or other transformer-based architectures with different pre-training objectives could provide a more comprehensive understanding of the impact of various visual encoders on MLLM performance. This would help to determine if the observed trends are consistent across different model architectures or if they are specific to the chosen encoders. Furthermore, it would be beneficial to analyze the computational cost and efficiency of each encoder, as this is a crucial factor for practical applications of MLLMs. The authors should also consider the impact of different pre-training datasets on the performance of the encoders, as this can also influence the quality of the learned representations.

In addition to expanding the range of visual encoders, the authors should also investigate the impact of different visual backbones. While the use of ViT-Large is a reasonable starting point, exploring other architectures such as ResNet50 or ResNet101 could reveal interesting insights. These models have different inductive biases and may capture different types of visual information. For example, ResNet architectures might be better at capturing hierarchical features, while ViT-Large might be better at capturing global context. Furthermore, the authors should analyze the impact of different pre-training datasets on the performance of the encoders, as this can also influence the quality of the learned representations. It would also be beneficial to explore the impact of different training strategies, such as fine-tuning or transfer learning, on the performance of the encoders.

Finally, the authors should consider experimenting with different input resolutions. While 224x224 is a common resolution, exploring other resolutions, such as 384x384 or even higher, could reveal how the performance of the encoders scales with image size. This is particularly important for real-world applications where images can have varying sizes. The authors should also analyze the impact of different input resolutions on the computational cost and efficiency of the models. It would also be beneficial to explore the impact of different input resolutions on the performance of the encoders. This would provide a more complete picture of the strengths and weaknesses of each encoder and would help to guide the selection of the most appropriate encoder for a given task.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
