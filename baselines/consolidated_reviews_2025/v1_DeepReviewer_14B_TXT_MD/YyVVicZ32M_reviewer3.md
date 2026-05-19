### Summary

The paper introduces a new decoding method called Permute-and-Flip (PF) decoder. The PF decoder is shown to be more efficient than softmax sampling while maintaining the same stability properties. The paper also proposes a watermarking scheme for PF decoder, which is shown to be effective in detecting watermarked texts. The experimental results show that the PF decoder and its watermarked counterpart outperform softmax sampling and its watermarked counterpart in terms of perplexity and detection accuracy.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a new decoding method called Permute-and-Flip (PF) decoder, which is more efficient than softmax sampling while maintaining the same stability properties.
2. The paper proposes a watermarking scheme for PF decoder, which is shown to be effective in detecting watermarked texts.
3. The experimental results show that the PF decoder and its watermarked counterpart outperform softmax sampling and its watermarked counterpart in terms of perplexity and detection accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the PF decoder and its watermarked counterpart. It is important to understand the computational cost of the proposed methods, especially when compared to softmax sampling. The paper should include a breakdown of the operations involved in the PF decoder, such as the number of comparisons and memory accesses, and compare these to the operations required by softmax sampling. This analysis should consider both the theoretical complexity and the practical runtime, potentially including a comparison of the number of floating-point operations (FLOPs) or other relevant metrics.
2. The paper does not provide a detailed analysis of the robustness of the PF watermarking scheme against different types of attacks. While the paper mentions detection accuracy, it does not explore the resilience of the watermark to common text manipulation techniques. For example, it is unclear how the watermark would perform against paraphrasing, synonym substitution, or other forms of text editing. A thorough evaluation should include a range of attacks and provide quantitative metrics for the watermark's robustness under each attack scenario.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the operations involved in the PF decoder. This should include a step-by-step analysis of the algorithm, counting the number of comparisons, memory accesses, and arithmetic operations. The analysis should be compared to the corresponding operations in softmax sampling, highlighting the differences in computational cost. Furthermore, the authors should consider providing a theoretical analysis of the time complexity of both methods, using Big-O notation to express how the runtime scales with the size of the input. It would also be beneficial to include a practical runtime comparison, potentially by measuring the actual time taken to decode a fixed-length sequence using both methods on the same hardware. This could be presented in a table or graph, showing the runtime for different sequence lengths or model sizes. Such an analysis would provide a more complete picture of the computational efficiency of the PF decoder.

To improve the evaluation of the watermarking scheme, the authors should conduct a more comprehensive analysis of its robustness against various text manipulation attacks. This should include a range of attacks, such as paraphrasing, synonym substitution, sentence reordering, and the addition of noise or adversarial examples. For each attack, the authors should measure the detection accuracy of the watermark, quantifying how well the watermark can be detected after the text has been modified. This could be presented in a table or graph, showing the detection accuracy for each attack scenario. The authors should also discuss the limitations of the watermarking scheme, identifying the types of attacks that it is most vulnerable to. This would provide a more complete understanding of the practical limitations of the proposed watermarking scheme and help guide future research in this area.

Finally, the authors should consider exploring the impact of different hyperparameter settings on the performance of the PF decoder and its watermarked counterpart. This could include parameters such as the temperature parameter T, the length of the prefix used for watermarking, and the strength of the watermark. By varying these parameters, the authors could gain a better understanding of how they affect the perplexity, detection accuracy, and computational cost of the proposed methods. This analysis could be presented in a series of tables or graphs, showing how the performance metrics change as the hyperparameters are varied. This would provide valuable guidance for practitioners who wish to use the proposed methods in their own applications.

### Questions

1. Can the authors provide a detailed analysis of the computational complexity of the PF decoder and its watermarked counterpart, and compare it to the computational complexity of softmax sampling?
2. Can the authors provide a detailed analysis of the robustness of the PF watermarking scheme against different types of attacks, such as paraphrasing, synonym substitution, and sentence reordering?

### Rating

6

### Confidence

3

**********
