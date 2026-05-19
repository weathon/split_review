### Summary

The paper introduces Permute-and-Flip (PF) decoding, a novel decoding method for large language models (LLMs) that aims to balance stability and perplexity. The authors also propose a watermarking scheme for PF decoding that can detect watermarked text with low false positive rates. The paper provides theoretical analysis and empirical results to support the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a theoretical analysis of the PF decoding method and its stability properties, which is a valuable contribution to the field of LLM decoding.
- The paper introduces a novel watermarking scheme for PF decoding that can detect watermarked text with low false positive rates, which is a valuable contribution to the field of LLM watermarking.
- The paper provides empirical results to support the effectiveness of the proposed method, which is a valuable contribution to the field of LLM decoding and watermarking.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed comparison of the proposed PF decoding method with other existing decoding methods, such as beam search and top-k sampling. It is unclear how the proposed method compares to these methods in terms of stability, perplexity, and computational cost. Specifically, the paper lacks a discussion on the trade-offs between the proposed method and these alternatives, making it difficult to assess the practical advantages of PF decoding.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, which is an important consideration for practical applications. The paper should include a discussion on the time and space complexity of the proposed method, as well as a comparison with other decoding methods. This is crucial for understanding the feasibility of deploying the proposed method in real-world scenarios.
- The paper does not provide a detailed analysis of the robustness of the proposed watermarking scheme. It is unclear how the watermarking scheme performs under different types of attacks, such as paraphrasing, editing, and adversarial attacks. The paper should include a discussion on the limitations of the proposed watermarking scheme and potential avenues for improvement. Furthermore, the paper should discuss the false positive rate of the watermarking scheme in more detail, as this is a critical metric for practical applications.

### Suggestions

The paper would benefit from a more thorough comparison of the proposed Permute-and-Flip (PF) decoding method with existing decoding techniques. Specifically, the authors should provide a detailed analysis of how PF decoding compares to methods like beam search and top-k sampling in terms of stability, perplexity, and computational cost. This analysis should include a discussion of the trade-offs between these methods and the proposed approach. For example, the authors could compare the perplexity of PF decoding with that of beam search and top-k sampling across various datasets and model sizes. Additionally, the authors should analyze the computational cost of PF decoding, including the time and space complexity, and compare it to other decoding methods. This would help readers understand the practical advantages and limitations of the proposed method. Furthermore, the authors should provide a more detailed explanation of the theoretical underpinnings of PF decoding, including a discussion of the assumptions and limitations of the method.

To address the lack of analysis on the computational cost, the authors should provide a more detailed breakdown of the time and space complexity of the PF decoding algorithm. This should include a discussion of the number of operations required for each step of the algorithm, as well as the memory requirements. The authors should also compare the computational cost of PF decoding to other decoding methods, such as beam search and top-k sampling, and discuss the factors that contribute to the differences in computational cost. For example, the authors could analyze the impact of the sequence length and the size of the vocabulary on the computational cost of PF decoding. This analysis would help readers understand the practical implications of using PF decoding in different scenarios. The authors should also consider providing empirical results on the runtime of the proposed method on different hardware platforms.

Finally, the paper needs a more comprehensive analysis of the robustness of the proposed watermarking scheme. The authors should evaluate the performance of the watermarking scheme under various types of attacks, such as paraphrasing, editing, and adversarial attacks. This analysis should include a discussion of the limitations of the proposed watermarking scheme and potential avenues for improvement. For example, the authors could investigate the robustness of the watermarking scheme against different types of adversarial attacks, such as those that modify the text to remove or alter the watermark. The authors should also provide a more detailed discussion of the false positive rate of the watermarking scheme, including a comparison with other watermarking methods. This would help readers understand the practical implications of using the proposed watermarking scheme in real-world applications.

### Questions

- How does the proposed PF decoding method compare to other existing decoding methods, such as beam search and top-k sampling, in terms of stability, perplexity, and computational cost?
- What is the computational cost of the proposed PF decoding method, and how does it compare to other decoding methods?
- How robust is the proposed watermarking scheme, and how does it perform under different types of attacks, such as paraphrasing, editing, and adversarial attacks?
- What is the false positive rate of the proposed watermarking scheme, and how does it compare to other watermarking methods?

### Rating

6

### Confidence

2

**********
