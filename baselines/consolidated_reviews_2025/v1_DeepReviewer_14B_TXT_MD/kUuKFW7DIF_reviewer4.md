### Summary

This paper introduces a self-supervised speech learning model, multi-resolution HuBERT, which extends HuBERT by employing multi-resolution masked unit prediction in conjunction with a hierarchical transformer architecture. Comprehensive evaluations across various benchmarks reveal that MR-HuBERT substantially outperforms the original HuBERT model across a broad spectrum of speech processing tasks. These include, but are not limited to, speech recognition, spoken language understanding, multilingual speech recognition, and speech enhancement. Beyond these performance gains, the model also exhibits computational efficiencies, specifically a 9-13% reduction in computational complexity, addressing efficiency concerns.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper introduces a novel hierarchical framework, namely multi-resolution HuBERT (MR-HuBERT) designed to encode speech information across multiple resolutions in a single model. The model is pre-trained using objectives for multi-resolution masked unit prediction, which are integrated with HuBERT-style clustering units.
3. The paper conducts extensive experiments on various benchmarks, including LibriSpeech, SUPERB, and ML-SUPERB, and demonstrates that MR-HuBERT substantially outperforms the original HuBERT model across a broad spectrum of speech processing tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed model. While the authors mention that the model has a 9-13% reduction in computational complexity, it would be helpful to provide more details on the computational cost of the model, such as the number of parameters and the training time. Specifically, a breakdown of the parameter count for each module (e.g., downsampling, upsampling, high/low-resolution transformers) would be beneficial. Furthermore, reporting the FLOPs for both training and inference would allow for a more comprehensive comparison with existing models. The training time should also be reported, including the time per epoch and the total training time, to provide a complete picture of the computational resources required.
2. The paper does not provide a detailed analysis of the limitations of the proposed model. It would be helpful to discuss the potential limitations of the model and suggest directions for future research. For example, the paper could discuss the model's performance on out-of-domain data or its robustness to noisy environments. Additionally, the paper could explore the model's sensitivity to hyperparameter settings and discuss the potential for further optimization.

### Suggestions

To address the lack of detailed computational analysis, the authors should include a comprehensive breakdown of the model's computational cost. This should include a table detailing the number of parameters for each module, such as the downsampling layers, upsampling layers, and the high and low-resolution transformer encoders. Furthermore, the authors should report the FLOPs (Floating Point Operations per Second) for both training and inference, providing a clear comparison with the original HuBERT model and other relevant baselines. The training time should also be reported, including the time per epoch and the total training time, to provide a complete picture of the computational resources required. This detailed analysis would allow readers to better understand the trade-offs between performance and computational cost, and would facilitate the adoption of the proposed model in resource-constrained environments. Additionally, it would be beneficial to include a discussion on the memory footprint of the model, as this is a crucial factor for deployment on devices with limited memory.

To address the lack of discussion on limitations, the authors should include a dedicated section that discusses the potential limitations of the proposed model. This section should include an analysis of the model's performance on out-of-domain data, such as speech from different languages or accents, and its robustness to noisy environments. The authors should also explore the model's sensitivity to hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A discussion on the potential for further optimization, such as exploring different training strategies or architectural modifications, would also be valuable. For example, the authors could investigate the impact of different masking strategies or the use of data augmentation techniques. Furthermore, the authors could explore the model's performance on specific downstream tasks, such as speech translation or speech summarization, to identify potential areas for improvement.

Finally, the authors should consider including an ablation study to analyze the contribution of each component of the proposed model. This would involve training the model with different combinations of modules, such as removing the downsampling or upsampling layers, or using a single-resolution transformer encoder. This would help to understand the importance of each component and identify potential areas for further optimization. For example, the authors could investigate the impact of different downsampling and upsampling techniques, or the effect of varying the number of layers in the high and low-resolution transformers. This analysis would provide a deeper understanding of the model's architecture and would guide future research in this area.

### Questions

1. Can the authors provide more details on the computational cost of the proposed model, such as the number of parameters and the training time?
2. Can the authors provide a more detailed analysis of the limitations of the proposed model and suggest directions for future research?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
