### Summary

This paper presents a novel watermarking framework designed for order-agnostic language models, addressing the limitations of existing methods that are primarily tailored for sequential models. The proposed approach introduces a Markov-chain-based key sequence generation method and a statistical pattern-based detection algorithm, allowing for the embedding and detection of watermarks without requiring access to the original prompt. The authors demonstrate the superiority of their method through comprehensive experiments on protein generation and machine translation tasks, showing improved detection efficiency, generation quality, and robustness compared to baseline methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel watermarking framework specifically designed for order-agnostic language models, which is a significant advancement in the field of watermarking for language models.
2. The proposed method is well-motivated and addresses a critical gap in the literature by providing a solution for watermarking in non-sequential generation models.
3. The authors provide a comprehensive evaluation of their framework, including experiments on protein generation and machine translation tasks, demonstrating its effectiveness in terms of detection efficiency, generation quality, and robustness.
4. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed framework, such as potential vulnerabilities to specific types of attacks or scenarios where the watermark might be difficult to detect. Specifically, the paper lacks a thorough analysis of how the watermark might be affected by common text transformations like paraphrasing, synonym substitution, or adversarial attacks designed to remove or obscure the watermark. The discussion should also consider the impact of different model architectures and training regimes on watermark robustness.
2. The evaluation of the framework could be expanded to include a wider range of order-agnostic language models and tasks, providing a more comprehensive assessment of its generalizability. The current evaluation is limited to protein generation and machine translation, which may not fully represent the diversity of order-agnostic models and tasks. For example, the framework's performance on tasks such as molecule generation or protein structure prediction should be investigated to demonstrate its broad applicability. The paper should also consider evaluating the framework on tasks with different statistical properties to assess its robustness across various data distributions.
3. The paper could provide more insights into the computational cost of the proposed framework, especially in comparison to existing watermarking methods. The paper lacks a detailed analysis of the time and space complexity of the key generation and detection algorithms. This information is crucial for understanding the practical feasibility of the framework, particularly when dealing with large-scale language models and long text sequences. A comparison of the computational overhead with existing watermarking techniques would be beneficial.

### Suggestions

To address the limitations regarding the framework's robustness, the authors should conduct a more thorough evaluation against a wider range of adversarial attacks. This should include attacks specifically designed to remove or obscure the watermark, such as those that manipulate the generated text based on statistical properties or introduce noise. The evaluation should also consider the impact of paraphrasing and text transformations on the watermark's detectability. Furthermore, the authors should investigate the framework's performance under different levels of noise and adversarial perturbations to provide a more comprehensive understanding of its vulnerabilities. This analysis should include quantitative metrics to measure the degree of watermark removal or distortion under various attack scenarios. The authors should also explore techniques to enhance the watermark's robustness against these attacks, such as using more robust statistical patterns or incorporating error-correcting codes.

To improve the evaluation's comprehensiveness, the authors should expand their experiments to include a wider range of order-agnostic language models and tasks. This should include models and tasks that exhibit different statistical properties and data distributions. For example, the framework's performance on tasks such as molecule generation, protein structure prediction, or even tasks involving graph-based models should be evaluated. This would provide a more robust assessment of the framework's generalizability and applicability across various domains. The evaluation should also consider the framework's performance on tasks with varying levels of complexity and data availability. This would help to identify potential limitations and areas for improvement. The authors should also provide a detailed analysis of the framework's performance across different model sizes and architectures to understand its scalability and efficiency.

Finally, the authors should provide a more detailed analysis of the computational cost of the proposed framework. This should include a breakdown of the time and space complexity of the key generation and detection algorithms. The authors should also compare the computational overhead of their framework with existing watermarking techniques. This analysis should consider the impact of different parameters, such as the length of the generated text and the size of the vocabulary, on the computational cost. The authors should also explore techniques to optimize the framework's performance, such as using more efficient algorithms or parallelizing the computations. This would help to ensure that the framework is practical and scalable for real-world applications.

### Questions

1. How does the proposed framework perform against adaptive adversaries who might try to remove or obscure the watermark through specific attacks?
2. Can the framework be extended to other types of order-agnostic language models, such as those used in natural language processing tasks?
3. What are the computational costs associated with the proposed framework, especially for large-scale language models and long text sequences?

### Rating

8

### Confidence

3

**********
