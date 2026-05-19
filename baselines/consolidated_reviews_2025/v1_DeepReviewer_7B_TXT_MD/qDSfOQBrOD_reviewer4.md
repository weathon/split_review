### Summary

This paper proposes a neural speech codec that integrates voice-changing capabilities directly into the codec. The proposed method achieves real-time processing with fewer than 1 million parameters. The experiments show that the proposed method outperforms state-of-the-art codecs in timbre adaptation and speech quality.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method achieves real-time processing with fewer than 1 million parameters.
2. The experiments show that the proposed method outperforms state-of-the-art codecs in timbre adaptation and speech quality.
3. The proposed method is suitable for real-time communication systems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately address the novelty of the proposed approach. While the integration of voice-changing functionality into a neural speech codec is presented as a key contribution, the specific technical innovations that enable this integration are not clearly articulated. The paper lacks a detailed comparison with existing methods that also combine codecs with other models, making it difficult to assess the true novelty of the proposed approach. The authors should provide a more in-depth analysis of how their method differs from prior work, particularly in terms of the architectural choices and the specific techniques used for timbre adaptation.
2. The paper lacks a comprehensive discussion of the limitations of the proposed approach. While the authors mention that the system is designed for specific target timbres and that the timbre adaptation is limited to pre-defined speakers, a more detailed analysis of the potential failure modes and the scenarios where the system might not perform well is missing. For example, the paper does not discuss how the system would handle out-of-distribution timbres or how the timbre adaptation would be affected by changes in the acoustic environment. A more thorough discussion of these limitations would provide a more balanced view of the proposed approach.

### Suggestions

The authors should provide a more detailed explanation of the specific architectural choices that enable the integration of voice-changing functionality into the VChangeCodec. This should include a breakdown of the components of the causal projection network and how it interacts with the codec to achieve real-time processing. A comparison with existing methods that combine codecs with other models is crucial to highlight the novelty of the proposed approach. This comparison should not only focus on the overall architecture but also on the specific algorithms and techniques used for timbre adaptation. For example, the authors could discuss the specific loss functions used for training the projection network and how they contribute to the desired timbre adaptation performance. Furthermore, the authors should provide a more detailed analysis of the trade-offs between computational complexity and performance, which would help to understand the practical implications of the proposed approach.

To address the limitations, the authors should include a more thorough discussion of the potential failure modes of the proposed approach. This should include an analysis of how the system would handle out-of-distribution timbres, such as those significantly different from the pre-defined speakers used during training. The authors should also discuss how the timbre adaptation would be affected by changes in the acoustic environment, such as background noise or reverberation. Furthermore, the authors should explore the robustness of the system to variations in the input speech signal, such as changes in pitch or speaking style. A more detailed analysis of these limitations would provide a more balanced view of the proposed approach and would help to identify areas for future research. The authors should also consider including experiments to evaluate the system's performance under these challenging conditions.

Finally, the authors should consider including additional experiments to further validate the proposed approach. For example, they could evaluate the system's performance on a wider range of timbres and speech patterns, including those with significant variations in pitch, tone, and speaking style. They could also conduct experiments to assess the system's robustness to different acoustic conditions, such as background noise and reverberation. Furthermore, the authors could compare the performance of their system with other state-of-the-art voice-changing methods, providing a more comprehensive evaluation of its strengths and weaknesses. These additional experiments would help to provide a more robust and reliable assessment of the proposed approach and would further strengthen the paper's contribution.

### Questions

Please refer to the weakness.

### Rating

6

### Confidence

3

**********
