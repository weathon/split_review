### Summary

The paper presents a novel watermarking framework for order-agnostic language models (LMs), specifically designed to address the challenges posed by the non-sequential nature of these models. Unlike traditional LMs, order-agnostic LMs generate content without a fixed left-to-right sequence, making conventional watermarking techniques ineffective. The authors propose MARWL, a pattern-based watermarking framework that utilizes a Markov-chain-based key sequence generator and a statistical pattern-based detection algorithm. The key contributions of the paper include:

1. A new watermarking method for order-agnostic LMs that does not rely on sequential generation.
2. A Markov-chain-based key sequence generator that produces high-frequency key patterns.
3. A statistical pattern-based detection algorithm that can recover the key sequence and perform statistical tests to detect watermarks with a controlled false positive rate.
4. Extensive experiments demonstrating the effectiveness of MARWL in terms of detection efficiency, generation quality, and robustness against attacks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. Originality: The paper introduces a novel approach to watermarking order-agnostic LMs, a problem that has not been extensively addressed in prior work. The use of a Markov chain to generate key sequences and a statistical pattern-based detection algorithm is a creative solution to the challenges posed by non-sequential generation.
2. Quality: The paper provides a thorough experimental evaluation of the proposed MARWL framework. The experiments cover various aspects, including detection efficiency, generation quality, and robustness against attacks. The results demonstrate the superiority of MARWL over baseline methods.
3. Clarity: The paper is well-structured and clearly written. The authors provide a detailed explanation of the proposed method, including the mathematical formulation and algorithms. The experimental setup and results are presented in a clear and concise manner.
4. Significance: The paper addresses an important problem in the field of language model watermarking. As order-agnostic LMs become more prevalent in various applications, the ability to watermark their output is crucial for intellectual property protection, content authentication, and other security-related concerns.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed MARWL framework. While the authors mention that the algorithms are efficient, a formal analysis of the time and space complexity would be beneficial. Specifically, the paper lacks a discussion on how the complexity scales with the length of the generated sequence, the size of the vocabulary, and the dimension of the Markov chain. This is crucial for understanding the practical applicability of the method, especially for large-scale models and datasets.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, how does the performance of MARWL degrade under different types of attacks, and what are the potential vulnerabilities of the framework? The paper should explore the sensitivity of the watermark to various perturbations, such as token substitutions, insertions, and deletions, and how these attacks might affect the detection rate. A more detailed analysis of the trade-offs between watermark robustness and generation quality is needed.
3. The paper focuses on two specific order-agnostic LMs, ProteinMPNN and CMLM. It would be helpful to discuss the generalizability of the proposed method to other order-agnostic LMs and different types of tasks. The paper should address whether the Markov-chain-based key sequence generator and the statistical pattern-based detection algorithm can be effectively applied to other models with different architectures and training objectives. It is unclear if the method is equally effective across different domains or if it requires specific adjustments for each new application.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of both the watermark generation and detection processes. This should include a formal analysis of how the complexity scales with key parameters such as the length of the generated sequence (n), the size of the vocabulary (V), and the dimension of the Markov chain (l). For instance, the authors could analyze the number of operations required for each step of the Markov chain key sequence generation and the statistical pattern detection, expressing these in terms of n, |V|, and l. This analysis should also consider the memory requirements for storing the key sequences and intermediate results. Furthermore, the authors should provide empirical measurements of the runtime and memory usage for different parameter settings to validate their theoretical analysis. This would provide a clearer understanding of the practical limitations of the method and guide users in selecting appropriate parameter values for their specific applications.

To enhance the discussion of limitations, the authors should conduct a more comprehensive evaluation of the robustness of MARWL against a wider range of attacks. This should include not only token modifications but also more sophisticated attacks such as paraphrasing, reordering, and adversarial perturbations. For each type of attack, the authors should analyze how the detection rate and false positive rate are affected, and discuss the underlying reasons for these changes. For example, the authors could investigate how the statistical properties of the key patterns are altered by different types of attacks and how this impacts the detection algorithm. Additionally, the authors should explore the trade-offs between watermark robustness and generation quality, providing a more detailed analysis of how different parameter settings affect both aspects. This could involve varying the strength of the watermark and analyzing its impact on metrics such as BLEU score or protein diversity. This would provide a more nuanced understanding of the limitations of the method and guide users in selecting appropriate parameter values for their specific applications.

To address the generalizability of the proposed method, the authors should conduct experiments on a wider range of order-agnostic LMs and tasks. This should include models with different architectures, training objectives, and application domains. For example, the authors could evaluate the performance of MARWL on models used for time series forecasting, speech generation, or other tasks where order-agnostic LMs are commonly used. The authors should also discuss the potential challenges and limitations of applying the method to these different contexts. For instance, they could analyze how the statistical properties of the generated sequences vary across different tasks and how this affects the performance of the watermark. Furthermore, the authors should investigate whether any adjustments or modifications are needed to adapt the method to different types of models or tasks. This would provide a more comprehensive understanding of the generalizability of the method and guide users in applying it to new applications.

### Questions

1. Can the authors provide a more detailed analysis of the computational complexity of the proposed MARWL framework? How does the complexity scale with the length of the generated sequence, the size of the vocabulary, and the dimension of the Markov chain?
2. How does the performance of MARWL degrade under different types of attacks, and what are the potential vulnerabilities of the framework? Can the authors provide a more in-depth discussion of the limitations of the proposed method?
3. How generalizable is the proposed method to other order-agnostic LMs and different types of tasks? Can the authors provide more insights into the applicability of MARWL beyond the two specific models considered in the paper?

### Rating

6

### Confidence

3

**********
