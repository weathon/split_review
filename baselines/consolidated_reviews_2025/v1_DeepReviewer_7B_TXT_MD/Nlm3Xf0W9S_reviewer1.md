### Summary

This paper proposes a watermarking method for order-agnostic language models. The method is based on a Markov-chain-based key sequence generation and a statistical pattern-based detection algorithm. The experimental results show that the proposed method outperforms the baseline methods in terms of detection efficiency, generation quality, and robustness.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is specifically designed for order-agnostic language models.
2. The experimental results show that the proposed method outperforms the baseline methods in terms of detection efficiency, generation quality, and robustness.

### Weaknesses

#### Some Related Works

[1] A watermark for machine translation

#### comment

1. The proposed method is very similar to the method proposed by Kirchenbauer et al. (2023) [1]. The main difference is that the proposed method uses a Markov chain to generate the key sequence, while the method proposed by Kirchenbauer et al. (2023) [1] uses a deterministic approach. However, the paper does not provide a detailed analysis of the advantages and disadvantages of these two approaches.
2. The experimental results are not convincing. The paper only compares the proposed method with three baseline methods, which are not specifically designed for order-agnostic language models. It is unclear whether the proposed method can outperform other state-of-the-art watermarking methods for order-agnostic language models.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is unclear whether the proposed method is efficient enough for large-scale language models.

### Suggestions

The paper should provide a more thorough comparison with existing watermarking techniques, especially those designed for order-agnostic language models. The current comparison with only three baselines is insufficient to demonstrate the superiority of the proposed method. It is crucial to compare against state-of-the-art methods that also address the challenges of watermarking in non-sequential generation models. For example, the paper could include comparisons with methods that use different key generation strategies or statistical detection algorithms. Furthermore, the paper should provide a more detailed analysis of the advantages and disadvantages of using a Markov chain for key sequence generation compared to other approaches, such as deterministic methods or random key generation. This analysis should include a discussion of the trade-offs between detection accuracy, robustness, and computational complexity.

To strengthen the experimental results, the paper should include a more comprehensive evaluation of the proposed method's performance under various conditions. This could include varying the length of the generated sequences, the number of watermark patterns, and the strength of the watermark signal. The paper should also evaluate the method's robustness against different types of attacks, such as paraphrasing, synonym substitution, and text editing. It is important to demonstrate that the proposed method can maintain high detection accuracy even when the generated text is modified. Additionally, the paper should provide a more detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for both key generation and detection. This analysis should be compared to the computational complexity of other watermarking methods to demonstrate the efficiency of the proposed approach.

Finally, the paper should provide a more detailed explanation of the key sequence generation process, including the specific parameters used in the Markov chain and how these parameters affect the detection accuracy and robustness of the watermark. The paper should also provide a more detailed explanation of the statistical pattern-based detection algorithm, including the specific patterns used for detection and how these patterns are selected. The paper should also discuss the limitations of the proposed method and suggest directions for future research. This discussion should include potential vulnerabilities of the method and how these vulnerabilities could be addressed in future work.

### Questions

1. What is the main difference between the proposed method and the method proposed by Kirchenbauer et al. (2023) [1]?
2. Why does the proposed method outperform the baseline methods in terms of detection efficiency, generation quality, and robustness?

### Rating

5

### Confidence

3

**********
