### Summary

This paper introduces a watermarking framework for order-agnostic language models, which cannot be directly watermarked using traditional methods designed for sequentially generated text. The proposed approach, named MARWL, employs a Markov-chain-based key sequence generator to embed watermarks and a statistical pattern-based detection algorithm to identify them. The authors demonstrate the effectiveness of MARWL through experiments on ProteinMPNN and CMLM, showing improvements in detection efficiency, generation quality, and robustness.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a novel and important problem in watermarking order-agnostic language models, which has not been explored in previous work.
- The proposed MARWL framework is well-designed, leveraging Markov chains to generate key sequences and a statistical detection algorithm to identify watermarks effectively.
- The experiments are comprehensive, covering various aspects such as detection efficiency, generation quality, and robustness against attacks. The results demonstrate the superiority of MARWL over baseline methods.

### Weaknesses

#### Some Related Works


#### comment

 - The motivation for watermarking order-agnostic language models could be further elaborated. While the paper mentions potential applications, it would be helpful to provide more concrete examples and discuss the practical implications of such watermarks.
- The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions.
- The paper could benefit from a more detailed comparison with existing watermarking techniques, particularly those that are not specifically designed for order-agnostic models. This would help to better contextualize the contributions of MARWL and highlight its advantages and disadvantages.
- The paper could benefit from a more detailed analysis of the computational complexity of the proposed method, particularly in comparison to existing approaches. This would help to better understand the practical implications of using MARWL in real-world applications.
- The paper could benefit from a more detailed analysis of the sensitivity of the proposed method to different parameters, such as the transition matrix of the Markov chain and the pattern length used for detection. This would help to better understand the robustness of the method and identify potential areas for improvement.

### Suggestions

The paper should provide a more thorough discussion of the practical scenarios where watermarking order-agnostic language models is crucial. While the paper mentions applications like protein design and machine translation, it needs to delve deeper into the specific challenges and benefits in these contexts. For example, in protein design, how would a watermark help in tracing the origin of a specific protein sequence, and what are the potential risks of not having such a watermark? Similarly, for machine translation, what are the implications of not being able to identify the source of a translated text, and how does this differ from the challenges in autoregressive models? Providing concrete examples and use cases would significantly strengthen the motivation for this work. Furthermore, the paper should discuss the potential for misuse of such watermarks and how to mitigate these risks. This would provide a more balanced and comprehensive view of the proposed method.

To improve the analysis of the proposed method, the paper should include a more detailed comparison with existing watermarking techniques, even those not explicitly designed for order-agnostic models. This comparison should not only focus on the performance metrics but also on the underlying mechanisms and assumptions of each method. For instance, how does MARWL's Markov-chain-based key sequence generation compare to the red-green list approach in terms of robustness and computational cost? What are the specific limitations of applying existing methods to order-agnostic models, and how does MARWL overcome these limitations? A more in-depth analysis of these aspects would help to better contextualize the contributions of MARWL and highlight its unique advantages. Additionally, the paper should explore the potential for combining MARWL with existing techniques to further enhance its performance and robustness. This would provide a more comprehensive understanding of the proposed method's capabilities and limitations.

Finally, the paper needs to provide a more detailed analysis of the computational complexity of MARWL, especially in comparison to existing approaches. The current discussion is too high-level and lacks specific details. For example, the paper should analyze the time and space complexity of both the watermark embedding and detection phases. How does the complexity scale with the length of the generated sequence, the size of the vocabulary, and the pattern length used for detection? Furthermore, the paper should discuss the practical implications of these complexities, such as the feasibility of using MARWL in real-time applications. A more detailed analysis of the computational complexity would help to better understand the practical limitations of the proposed method and identify potential areas for optimization. The paper should also explore the sensitivity of the method to different parameters, such as the transition matrix of the Markov chain and the pattern length used for detection, and provide guidelines for selecting appropriate parameter values.

### Questions

- Could the authors provide more concrete examples of real-world applications where watermarking order-agnostic language models is crucial? This would help to better understand the practical significance of the proposed method.
- How does the proposed method compare to existing watermarking techniques in terms of computational complexity and robustness against various attacks? A more detailed comparison would help to better contextualize the contributions of MARWL.
- Are there any potential extensions or modifications of the proposed method that could further improve its performance or applicability to other types of language models? Exploring future research directions would be valuable for the readers.

### Rating

6

### Confidence

3

**********
