### Summary

This paper introduces VChangeCodec, a novel neural speech codec designed for real-time communication (RTC) that integrates a voice changer directly into the codec. The key innovation is embedding a lightweight causal projection network within the encoding module, allowing seamless switching between original and customized voice modes. The proposed method achieves ultra-low latency (40 ms) and requires fewer than 1 million parameters, making it suitable for RTC applications like online conferencing. The authors demonstrate the effectiveness of VChangeCodec through comprehensive subjective and objective evaluations, showing superior performance compared to state-of-the-art voice conversion methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The integration of voice changing capabilities directly into the codec is a novel approach that addresses the limitations of traditional cascaded VC-codec systems.
2. The proposed method achieves impressive efficiency, with a very low latency of 40 ms and a small number of parameters (<1M), making it highly suitable for real-time communication applications.
3. The paper provides a thorough evaluation of the proposed method, including both subjective and objective assessments, demonstrating its effectiveness in terms of speech quality and timbre adaptation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method compared to existing approaches. While the number of parameters is mentioned, a more comprehensive comparison of real-time factors (RTF) or latency would be beneficial. Specifically, the paper lacks a breakdown of the computational cost associated with each component of the VChangeCodec, such as the encoder, the causal projection network, and the decoder. This makes it difficult to assess the practical feasibility of the method on resource-constrained devices. Furthermore, the paper does not discuss the memory footprint of the model, which is a crucial factor for real-time applications, especially on mobile devices.
2. The evaluation of the voice changer mode is limited to a specific set of target timbres. It would be valuable to see how the proposed method performs with a wider range of target speakers and timbres. The paper does not explore the robustness of the method to variations in speaker characteristics, such as age, gender, and accent. This raises concerns about the generalizability of the approach to diverse real-world scenarios. Additionally, the paper does not provide any analysis of the method's performance when the target timbre is significantly different from the source timbre, which could reveal potential limitations of the approach.
3. The paper does not provide a detailed analysis of the potential privacy implications of the proposed method. While the ethical statement mentions that the method is designed for operator-oriented networks, it would be beneficial to discuss potential risks and mitigation strategies in more detail. For example, the paper does not address the potential for the voice changer to be used for malicious purposes, such as impersonation or deepfake attacks. Furthermore, the paper does not discuss the potential for the system to be vulnerable to adversarial attacks, which could compromise the security of the communication system.

### Suggestions

To address the lack of detailed computational complexity analysis, the authors should provide a breakdown of the real-time factor (RTF) for each component of the VChangeCodec, including the encoder, the causal projection network, and the decoder. This should be done on a variety of hardware platforms, including both high-end and resource-constrained devices. Furthermore, the authors should provide a detailed analysis of the memory footprint of the model, including the size of the weights, activations, and intermediate representations. This analysis should be accompanied by a discussion of the trade-offs between computational complexity, memory footprint, and performance. The authors should also compare the computational complexity of their method with existing state-of-the-art voice conversion and speech coding techniques, providing a clear understanding of the efficiency gains achieved by their approach. This would allow readers to better assess the practical feasibility of the method for real-time communication applications.

To improve the evaluation of the voice changer mode, the authors should conduct experiments with a wider range of target speakers and timbres, including speakers with different ages, genders, and accents. This would provide a more comprehensive assessment of the method's robustness and generalizability. The authors should also analyze the method's performance when the target timbre is significantly different from the source timbre, and discuss any potential limitations or trade-offs. Furthermore, the authors should consider using more objective metrics to evaluate the quality of the voice conversion, such as Mel-Cepstral Distortion (MCD) and speaker identification accuracy. This would provide a more quantitative assessment of the method's performance. The authors should also include a subjective evaluation with a larger number of participants to ensure the reliability of the results.

To address the potential privacy implications, the authors should provide a more detailed discussion of the risks associated with the proposed method, including the potential for malicious use and adversarial attacks. They should also propose mitigation strategies to address these risks, such as access control mechanisms and watermarking techniques. The authors should also discuss the ethical implications of using voice changers in real-time communication systems, and propose guidelines for responsible use. This discussion should be accompanied by a clear explanation of the limitations of the proposed method in terms of preventing misuse. The authors should also consider the potential for the system to be used for discriminatory purposes, and propose measures to prevent this.

### Questions

1. How does the proposed method perform with a wider range of target speakers and timbres? Are there any limitations in terms of the types of timbre adaptations that can be achieved?
2. What are the potential privacy implications of the proposed method, and how can they be mitigated?
3. How does the proposed method compare to existing approaches in terms of computational complexity and latency?

### Rating

6

### Confidence

3

**********
