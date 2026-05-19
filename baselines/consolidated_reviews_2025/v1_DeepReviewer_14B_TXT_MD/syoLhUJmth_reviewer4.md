### Summary

This paper investigates the effectiveness of different visual encoders within MLLMs. The authors find that the shallow layer features of CLIP offer particular advantages for fine-grained tasks such as grounding and region understanding. Surprisingly, the vision-only model DINO, which is not pretrained with text-image alignment, demonstrates promising performance as a visual branch within MLLMs. By simply equipping it with an MLP layer for alignment, DINO surpasses CLIP in fine-grained related perception tasks. The authors propose a simple yet effective feature merging strategy, named COMM, that integrates CLIP and DIN0 with Multi-level features Merging, to enhance the visual capabilities of MLLMs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The motivation is clear and the method is simple yet effective.
2. The experiments are comprehensive and the results are promising.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The COMM is based on ViT-Large. It would be better to compare different vision backbones, e.g., ViT-Huge. 
2. In Table 4, COMM performs worse than FLAVA on VQAv2 and OK-VQA, which makes the proposed method less convincing.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of different vision encoder backbones. While the authors chose ViT-Large, it is crucial to understand how the proposed COMM method scales with larger models like ViT-Huge. This is particularly important given the trend towards larger models in the field. The current results leave open the question of whether the performance gains observed with ViT-Large would translate to larger models, or if the method is specifically tailored to the ViT-Large architecture. Exploring this would provide a more complete picture of the method's generalizability and potential for further improvement. It would also be beneficial to analyze the computational cost and memory requirements associated with different backbones, as this is a practical consideration for real-world applications.

Furthermore, the performance discrepancy between COMM and FLAVA on VQAv2 and OK-VQA needs further analysis. While the authors argue that COMM is designed for fine-grained tasks, the lower performance on these general VQA tasks raises concerns about the method's overall robustness. It is important to understand why COMM struggles on these tasks, and whether this is due to the training data, the model architecture, or the feature merging strategy itself. A more detailed analysis of the failure cases on these benchmarks could provide valuable insights into the limitations of the approach. It would also be helpful to explore whether the performance gap can be reduced by incorporating additional training data or by modifying the training procedure. The current results make it difficult to fully assess the practical value of the proposed method.

Finally, the paper should include a more detailed comparison with other state-of-the-art MLLMs. While the authors compare their method with several baselines, a more comprehensive comparison with a wider range of models would provide a better understanding of the method's strengths and weaknesses. This comparison should include not only performance metrics but also computational cost and memory requirements. It would also be beneficial to analyze the qualitative differences between the predictions of COMM and other models, as this could provide insights into the method's unique capabilities. A more thorough comparison would help to better position the proposed method within the broader landscape of MLLMs.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
