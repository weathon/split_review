### Summary

This paper introduces VChangeCodec, a neural speech codec designed for real-time communication systems, especially for voice-changing applications. VChangeCodec integrates voice-changing function directly into the codec, supporting both original and customized voice modes with low latency. VChangeCodec uses a lightweight causal projection network for timbre adaptation at the token level, achieving real-time processing with fewer than 1 million parameters. Experimental results show VChangeCodec outperforms state-of-the-art codecs in timbre adaptation and speech quality, with an ultra-low 40ms latency, making it suitable for applications like online streaming.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. VChangeCodec integrates voice-changing functionality directly into the codec, supporting real-time switching between original and customized voice modes with low latency.
2. VChangeCodec uses a lightweight causal projection network for timbre adaptation at the token level, achieving real-time processing with fewer than 1 million parameters.
3. Experimental results show VChangeCodec outperforms state-of-the-art codecs in timbre adaptation and speech quality, with an ultra-low 40ms latency, making it suitable for applications like online streaming.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately address the novelty of the proposed approach. While the integration of voice-changing functionality into a neural speech codec is presented as a key contribution, the specific technical innovations that enable this integration are not clearly articulated. The paper lacks a detailed comparison with existing methods that also combine codecs with other models, making it difficult to assess the true novelty of the proposed approach. The authors should provide a more in-depth analysis of how their method differs from prior work, particularly in terms of the architectural choices and the specific techniques used for timbre adaptation.
2. The paper lacks a comprehensive discussion of the limitations of the proposed approach. While the authors mention that the system is designed for specific target timbres and that the timbre adaptation is limited to pre-defined speakers, a more detailed analysis of the potential failure modes and the scenarios where the system might not perform well is missing. For example, the paper does not discuss how the system would handle out-of-distribution timbres or how the timbre adaptation would be affected by changes in the acoustic environment. A more thorough discussion of these limitations would provide a more balanced view of the proposed approach.

### Suggestions

The authors should provide a more detailed explanation of the technical innovations that enable the integration of voice-changing functionality into the VChangeCodec. This should include a clear description of the specific architectural choices and the techniques used for timbre adaptation. For example, the authors could elaborate on the design of the causal projection network and how it interacts with the codec to achieve real-time processing. A comparison with existing methods that combine codecs with other models would also be beneficial, highlighting the unique aspects of the proposed approach. This comparison should not only focus on the overall architecture but also on the specific algorithms and techniques used for timbre adaptation. Furthermore, the authors should discuss the trade-offs between the computational complexity and the performance of the proposed method, providing a more comprehensive understanding of its strengths and weaknesses.

The paper should also include a more thorough discussion of the limitations of the proposed approach. This discussion should go beyond the mention of specific target timbres and pre-defined speakers. The authors should analyze the potential failure modes of the system, such as its performance with out-of-distribution timbres, its robustness to changes in the acoustic environment, and its ability to handle complex speech patterns. For example, the authors could discuss how the system would perform with speakers that have significantly different vocal characteristics than those used during training. They could also analyze the impact of background noise and reverberation on the timbre adaptation process. A more detailed analysis of these limitations would provide a more balanced view of the proposed approach and would help guide future research in this area. The authors should also discuss the potential ethical implications of their work, particularly in the context of voice-changing applications.

Finally, the authors should consider including additional experiments to further validate the proposed approach. For example, they could evaluate the system's performance on a wider range of timbres and speech patterns, including those with significant variations in pitch, tone, and speaking style. They could also conduct experiments to assess the system's robustness to different acoustic conditions, such as background noise and reverberation. Furthermore, the authors could compare the performance of their system with other state-of-the-art voice-changing methods, providing a more comprehensive evaluation of its strengths and weaknesses. These additional experiments would help to provide a more robust and reliable assessment of the proposed approach and would further strengthen the paper's contribution.

### Questions

1. How does VChangeCodec handle out-of-distribution timbres, especially those significantly different from the pre-defined speakers used during training?
2. What are the potential limitations of VChangeCodec in real-world applications, such as its robustness to changes in acoustic environment or its ability to handle complex speech patterns?

### Rating

5

### Confidence

4

**********
