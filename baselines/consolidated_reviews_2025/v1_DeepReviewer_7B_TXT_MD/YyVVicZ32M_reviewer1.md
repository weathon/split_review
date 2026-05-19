### Summary

The paper introduces a new decoding method for LLMs called Permute-and-Flip (PF) decoding, which aims to improve upon existing methods like softmax sampling by achieving a better balance between perplexity and stability. The authors also propose a watermarking scheme for PF decoding that can detect watermarked text with low false positive rates. The experiments show that PF decoding outperforms traditional methods in terms of perplexity while maintaining stability, making it a promising approach for LLM decoding.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel decoding method, Permute-and-Flip (PF) decoding, which is theoretically grounded and has provable stability properties. This is a significant contribution to the field of LLM decoding, as it addresses the limitations of existing methods like softmax sampling and greedy decoding.
2. The authors provide a comprehensive comparison of PF decoding with other decoding methods, including Gumbel watermarking, demonstrating the advantages of PF decoding in terms of perplexity and stability. The theoretical analysis of PF decoding is thorough and well-supported by empirical results.
3. The paper introduces a watermarking scheme for PF decoding that can detect watermarked text with low false positive rates. This is an important contribution to the field of LLM watermarking, as it enables the verification of LLM-generated text without compromising its quality.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the practical implications of PF decoding in real-world applications. While the theoretical analysis is thorough, it would be helpful to understand how PF decoding performs in different scenarios, such as long-form text generation or complex reasoning tasks. Specifically, the paper lacks a discussion on the computational overhead of the permuting step, which could be a bottleneck for large-scale applications. Furthermore, the impact of the permuting step on the convergence rate of the decoding process is not explored, leaving a gap in understanding its practical implications.
2. The paper could explore the robustness of PF decoding against adversarial attacks or paraphrasing attempts. It would be valuable to understand how the watermarking scheme performs under different types of attacks and whether it can be made more robust. The current evaluation focuses on basic paraphrasing and editing attacks, but it does not consider more sophisticated attacks such as those that involve semantic manipulation or the insertion of backdoors. A more comprehensive evaluation of the watermark's resilience is needed to assess its practical applicability.
3. The paper could include a more detailed analysis of the limitations of PF decoding and potential areas for future research. For example, the paper does not discuss the potential for the permuting step to introduce biases or artifacts into the generated text. A more thorough analysis of these limitations would provide a more balanced perspective on the strengths and weaknesses of the proposed method. Additionally, the paper could explore alternative decoding strategies that could potentially further improve the performance of PF decoding.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the Permute-and-Flip (PF) decoding method. Specifically, the authors should quantify the time complexity of the permuting step and compare it to the computational cost of other decoding methods. This analysis should consider the impact of the sequence length and the size of the vocabulary on the overall runtime. Furthermore, the authors should investigate the convergence rate of the PF decoding algorithm and compare it to other methods. This would provide a more complete picture of the practical implications of using PF decoding in real-world applications. The authors should also explore potential optimizations to reduce the computational overhead of the permuting step, such as using more efficient data structures or parallelizing the computation.

To enhance the robustness of the watermarking scheme, the authors should conduct a more comprehensive evaluation against a wider range of adversarial attacks. This should include attacks that involve semantic manipulation, such as paraphrasing using more sophisticated models, and attacks that aim to remove or alter the watermark. The authors should also explore the use of more robust watermarking techniques, such as those based on error-correcting codes or cryptographic hash functions. The evaluation should also consider the trade-off between watermark robustness and text quality, as more robust watermarking techniques may introduce some degradation in the quality of the generated text. The authors should also investigate the potential for backdoors to be introduced by the watermarking process and propose methods to mitigate this risk.

Finally, the paper should include a more detailed discussion of the limitations of the PF decoding method and potential areas for future research. This should include an analysis of the potential for the permuting step to introduce biases or artifacts into the generated text. The authors should also explore alternative decoding strategies that could potentially further improve the performance of PF decoding. For example, they could investigate the use of adaptive permuting strategies that adjust the permutation based on the context of the input sequence. The authors should also consider the potential for the PF decoding method to be used in other applications beyond text generation, such as image or speech synthesis. A more thorough discussion of these limitations and future directions would provide a more balanced perspective on the strengths and weaknesses of the proposed method.

### Questions

1. How does the computational cost of PF decoding compare to other decoding methods, especially in terms of runtime and memory usage?
2. How robust is the PF watermarking scheme against adversarial attacks or paraphrasing attempts? Can the authors provide more details on the evaluation of the watermark's resilience?
3. What are the limitations of PF decoding, and what are the potential areas for future research? Are there any specific scenarios where PF decoding might not perform well?

### Rating

5

### Confidence

4

**********
