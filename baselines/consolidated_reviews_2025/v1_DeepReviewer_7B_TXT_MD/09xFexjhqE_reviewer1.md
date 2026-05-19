### Summary

This paper presents AutoLoRa, an automated robust fine-tuning framework for deep learning models. The authors identify a key issue in existing robust fine-tuning (RFT) methods: divergent gradient directions when optimizing both adversarial and natural objectives through the feature extractor (FE), leading to unstable optimization and sensitivity to hyperparameters. To address this, AutoLoRa introduces a low-rank (LoRa) branch that disentangles RFT, optimizing natural objectives via the LoRa branch and adversarial objectives via the FE. Additionally, the paper proposes heuristic strategies for automating the scheduling of learning rates and scalars, eliminating the need for manual hyperparameter tuning. Experimental results demonstrate that AutoLoRa achieves state-of-the-art adversarial robustness across various downstream tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the motivation, methodology, and experimental results.
2. The proposed AutoLoRa framework addresses a significant issue in robust fine-tuning by disentangling the optimization of natural and adversarial objectives, leading to improved adversarial robustness and reduced sensitivity to hyperparameters.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The core idea of disentangling natural and adversarial objectives has been explored in previous works, such as TWINS. The main difference lies in the introduction of the LoRa branch, which, while effective, does not represent a substantial conceptual advance over existing methods.
2. The paper lacks a thorough comparison with other state-of-the-art methods in robust fine-tuning. The experimental evaluation primarily focuses on vanilla RFT and TWINS, which are not the most competitive baselines in the field. A more comprehensive comparison with recent and advanced methods is needed to demonstrate the superiority of the proposed approach.
3. The paper does not provide sufficient details on the computational cost and efficiency of the proposed method. While the authors claim that the LoRa branch is parameter-efficient, they do not provide quantitative comparisons of training time, memory usage, and inference speed with other methods. This makes it difficult to assess the practical applicability of the proposed approach.
4. The paper's evaluation is limited to image classification tasks. The authors do not explore the performance of AutoLoRa on other types of data, such as natural language processing or time-series data. This limits the generalizability of the findings and raises questions about the applicability of the proposed method to other domains.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the proposed method's novelty. While the introduction of the LoRa branch is a practical contribution, the core idea of disentangling natural and adversarial objectives is not new. The authors should clearly articulate how their approach differs fundamentally from existing methods, such as TWINS, and what specific advantages it offers. A more detailed discussion of the theoretical underpinnings of the method, including a formal analysis of the convergence properties and the impact of the LoRa branch on the optimization landscape, would also strengthen the paper. Furthermore, the authors should provide a more thorough comparison with other state-of-the-art robust fine-tuning methods. The current experimental evaluation is insufficient to demonstrate the superiority of the proposed approach. The authors should include comparisons with recent and advanced methods, such as those based on adversarial training or robust optimization techniques, to provide a more comprehensive assessment of the method's performance. This would help to establish the method's position in the field and highlight its unique contributions.

To address the lack of information on computational cost and efficiency, the authors should provide a detailed analysis of the training time, memory usage, and inference speed of the proposed method. This analysis should include quantitative comparisons with other methods, such as vanilla RFT and TWINS, to demonstrate the practical applicability of the proposed approach. The authors should also discuss the trade-offs between performance and efficiency, and provide guidance on how to choose the appropriate parameters for different applications. Furthermore, the authors should expand the evaluation of the proposed method to include other types of data, such as natural language processing or time-series data. This would help to establish the generalizability of the method and demonstrate its applicability to a wider range of domains. The authors should also discuss the limitations of the proposed method and identify areas for future research.

Finally, the authors should provide a more detailed explanation of the heuristic strategies for automating the scheduling of learning rates and scalars. While the authors mention that these strategies are inspired by AutoAttack, they do not provide a clear explanation of how these strategies are implemented and how they affect the performance of the proposed method. A more detailed analysis of the impact of different scheduling strategies on the convergence and robustness of the model would be beneficial. The authors should also discuss the limitations of their heuristic strategies and identify areas for future research. In summary, the paper has potential, but it needs to be strengthened by a more thorough analysis of the proposed method's novelty, a more comprehensive experimental evaluation, and a more detailed discussion of the computational cost and efficiency.

### Questions

1. How does the proposed method compare to other state-of-the-art robust fine-tuning methods in terms of performance and efficiency?
2. What is the impact of the LoRa branch on the convergence and robustness of the model?
3. How does the proposed method perform on other types of data, such as natural language processing or time-series data?

### Rating

5

### Confidence

4

**********
