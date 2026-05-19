### Summary

This paper presents a new method called Hierarchical Side-Tuning (HST) for Parameter-Efficient Transfer Learning (PETL), specifically designed to adapt Vision Transformers (ViTs) to a wide range of downstream visual tasks. HST introduces a lightweight Hierarchical Side Network (HSN) that leverages intermediate activations from the ViT backbone to capture multi-scale features, enhancing prediction capabilities. The authors conduct extensive experiments across various visual tasks, including classification, object detection, instance segmentation, and semantic segmentation. The results show that HST achieves competitive performance on the VTAB-1K benchmark and outperforms existing PETL methods on object detection and semantic segmentation tasks on the COCO and ADE20K datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed HST method is a novel approach in PETL, particularly for adapting ViTs to diverse downstream tasks. The use of a lightweight HSN to model multi-scale features is a creative solution to the limitations of existing PETL methods in handling complex vision tasks.
2. The paper provides a thorough evaluation of HST across a range of visual tasks and benchmarks. The experimental setup is well-described, and the results are clearly presented.

### Weaknesses

#### Some Related Works

[1] Side-tuning for vision transformers

#### comment

1. The paper does not include comparisons with the latest PETL methods, such as STT [1]. Including these comparisons would provide a more comprehensive evaluation of HST's performance relative to the state-of-the-art.

2. The paper does not analyze the training time and inference speed of HST compared to other PETL methods. This analysis is crucial for understanding the practical implications of using HST in real-world applications.

3. The paper does not explore the potential limitations or challenges of applying HST to other types of vision models, such as ConvNeXt. 

4. The paper does not discuss the potential impact of HST on the broader field of visual recognition tasks. While the method is shown to be effective on the specific tasks evaluated, its generalizability and potential impact on the field are not fully explored.

### Suggestions

The paper would benefit significantly from a more thorough comparison against recent Parameter-Efficient Transfer Learning (PETL) techniques. Specifically, the absence of a direct comparison with methods like STT [1] leaves a gap in understanding the relative performance of HST. It is crucial to benchmark HST against a wider range of state-of-the-art PETL methods across all evaluated tasks, not just on a select few. This would involve not only reporting the final performance metrics but also analyzing the trade-offs in terms of parameter efficiency, training time, and inference speed. Furthermore, the comparison should include a detailed analysis of the computational cost associated with the proposed Hierarchical Side Network (HSN), including the number of parameters and the FLOPs required for both training and inference. This would provide a more complete picture of the practical advantages and limitations of HST compared to other PETL approaches.

In addition to performance comparisons, a more detailed analysis of the computational overhead of HST is needed. The paper should include a comprehensive evaluation of the training time and inference speed of HST, compared to other PETL methods and full fine-tuning. This analysis should consider the impact of the HSN on the overall computational cost, including the time required for forward and backward passes. It would be beneficial to provide a breakdown of the computational cost associated with different components of HST, such as the side network and the hierarchical feature fusion. Furthermore, the paper should explore the scalability of HST to larger models and datasets, and discuss the potential challenges in deploying HST in resource-constrained environments. This analysis should include a discussion of the memory footprint of HST, and how it compares to other PETL methods.

Finally, the paper should address the limitations of HST and its potential for generalization. The current evaluation is primarily focused on Vision Transformers (ViTs), and it is unclear how well HST would perform on other types of vision models, such as ConvNeXt or ResNets. The paper should explore the applicability of HST to these other architectures, and discuss any modifications that might be necessary. Furthermore, the paper should discuss the potential impact of HST on the broader field of visual recognition tasks, and how it could contribute to the development of more efficient and effective transfer learning methods. This discussion should include a consideration of the limitations of HST, and the potential challenges in applying it to more complex tasks or datasets. The paper should also explore the potential for extending HST to other modalities, such as natural language processing or audio processing.

### Questions

See Weaknesses

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
