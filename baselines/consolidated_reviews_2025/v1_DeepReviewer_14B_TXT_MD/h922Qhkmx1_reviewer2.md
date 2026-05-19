### Summary

This paper proposes a diffusion-based generative model to perform music synthesis and source separation. The proposed method is capable of performing total generation, partial generation (imputation), and source separation. The proposed method is evaluated on the Slakh2100 dataset.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is clearly written and easy to follow. The idea of using a single model to perform generation and separation is interesting.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is evaluated only on the Slakh2100 dataset, which limits the generalizability of the findings. The Slakh2100 dataset, while valuable for source separation tasks, is synthesized by adding dry recordings of individual sources. This synthesis process does not fully capture the complexities of real-world recordings, where reverberation, microphone characteristics, and other artifacts are present. Therefore, the performance of the proposed method on real-world data remains uncertain.
- The performance of the proposed method is not as good as the baseline Demucs on source separation task. The paper reports that the proposed method achieves a SI-SDR of 16.48 dB, while Demucs achieves 17.73 dB. This difference, while seemingly small, is significant in the context of source separation. The fact that the proposed method does not surpass the baseline on this task raises concerns about its practical utility for source separation.
- The paper claims that the proposed method is a step towards general audio models. However, the evaluation is limited to a single dataset and a single task (source separation). To support this claim, the method should be evaluated on a wider range of datasets and tasks, such as speech enhancement, music transcription, or sound event detection. The current evaluation is insufficient to justify the claim of generality.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. Diffusion models are known to be computationally expensive, and the lack of information about the training and inference time makes it difficult to assess the practical feasibility of the method.

### Suggestions

The authors should evaluate their method on more diverse datasets that include real-world recordings with varying degrees of reverberation and noise. Datasets such as MUSDB18, which contains studio-recorded music, or datasets from the DCASE challenges, which include environmental sounds and speech, would be appropriate. This would provide a more comprehensive assessment of the method's generalizability and robustness. Furthermore, the authors should consider evaluating their method on tasks beyond source separation, such as music generation or audio editing. This would provide a more compelling argument for the method's generality and potential impact.

To improve the source separation performance, the authors could explore different architectures for the score network, such as incorporating attention mechanisms or using more efficient convolutional layers. They could also investigate different training strategies, such as using a larger batch size or employing data augmentation techniques. Additionally, the authors should provide a more detailed analysis of the failure cases of their method. This would help to identify the limitations of the method and guide future research. For example, it would be useful to know if the method struggles with certain types of sources or in specific acoustic conditions.

Finally, the authors should provide a detailed analysis of the computational cost of their method, including the training time, inference time, and memory requirements. This information is crucial for assessing the practical feasibility of the method. They should also compare the computational cost of their method to that of other state-of-the-art methods, such as Demucs. This would help to determine whether the proposed method offers a good trade-off between performance and computational cost. The authors should also consider exploring techniques for reducing the computational cost of their method, such as model compression or quantization.

### Questions

- How does the proposed method perform on real-world recordings, such as those in the MUSDB18 dataset, which include reverberation and other artifacts?
- How does the proposed method compare to other state-of-the-art source separation methods on a wider range of datasets and tasks?
- What is the computational cost of the proposed method, and how does it compare to that of other methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
