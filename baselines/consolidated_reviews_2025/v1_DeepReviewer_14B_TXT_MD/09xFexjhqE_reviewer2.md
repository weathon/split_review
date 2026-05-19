### Summary

This paper introduces a novel approach to Robust Fine-Tuning (RFT) by addressing the challenge of divergent gradient directions when optimizing for both adversarial and natural objectives. The authors propose AutoLoRa, a framework that disentangles these objectives using a low-rank (LoRa) branch, optimizing natural objectives through this branch and adversarial objectives through the feature extractor (FE). Additionally, AutoLoRa incorporates automated scheduling for learning rates and loss term scalars, enhancing the stability and effectiveness of the fine-tuning process. Empirical results demonstrate that AutoLoRa achieves state-of-the-art adversarial robustness across various downstream tasks, providing a practical solution for converting pre-trained models into adversarially robust models without extensive hyperparameter tuning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces AutoLoRa, a novel framework that effectively addresses the issue of divergent gradient directions in Robust Fine-Tuning (RFT) by using a low-rank (LoRa) branch to disentangle natural and adversarial objectives. This approach not only enhances adversarial robustness but also maintains parameter efficiency, as the LoRa branch introduces only a small number of additional trainable parameters.
2. AutoLoRa automates the scheduling of learning rates and loss term scalars, reducing the need for manual hyperparameter tuning. This automation makes the framework more practical and accessible for real-world applications, as it simplifies the process of achieving adversarial robustness.
3. The paper provides a thorough empirical evaluation of AutoLoRa across multiple datasets and model architectures, demonstrating consistent improvements in adversarial robustness compared to existing methods like vanilla RFT and TWINS. The results are compelling and support the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's contribution is incremental. The proposed method is a combination of LoRA and RFT. Although the experimental results show improvement, the novelty of the method is limited. The core idea of using a low-rank adaptation for fine-tuning is not new, and the application to robust fine-tuning, while practical, does not introduce a fundamentally novel approach. The disentanglement of objectives using separate branches is a straightforward extension of existing techniques, and the automated scheduling, while useful, is not a major theoretical advancement.
2. Lack of theoretical analysis. The paper primarily focuses on empirical results, but it lacks a deep theoretical exploration of why the proposed method works. A more rigorous theoretical foundation could strengthen the contribution. Specifically, the paper does not provide any analysis of the convergence properties of the proposed method, nor does it offer any insights into the optimization landscape and how the low-rank branch affects the gradient flow. A theoretical analysis of the gradient similarity and how the LoRA branch mitigates the divergence would be beneficial.
3. The paper could benefit from a clearer and more structured presentation. Some sections are dense and could be streamlined for better readability. The description of the automated scheduling of loss term scalars is not sufficiently detailed, making it difficult to understand the exact mechanism and its impact on the overall performance. The paper would benefit from a more detailed explanation of the specific algorithms used for scheduling.

### Suggestions

The paper would be significantly strengthened by a more in-depth analysis of the theoretical underpinnings of the proposed method. While empirical results are important, a theoretical framework would provide a deeper understanding of why the low-rank branch effectively disentangles the natural and adversarial objectives. Specifically, the authors should consider exploring the convergence properties of their method, perhaps by analyzing the gradient flow and the impact of the low-rank adaptation on the optimization landscape. This could involve examining the Hessian of the loss function and how the LoRA branch affects its eigenvalues, which could provide insights into the stability and convergence of the optimization process. Furthermore, a theoretical analysis of the gradient similarity between the natural and adversarial objectives, and how the proposed method mitigates the divergence, would be highly valuable. This could involve deriving bounds on the gradient similarity or providing a formal proof of convergence under certain conditions.

To improve the clarity and presentation of the paper, the authors should provide a more detailed explanation of the automated scheduling of loss term scalars. This should include a clear description of the specific algorithms used for scheduling, as well as a discussion of the rationale behind the chosen scheduling strategy. For example, the authors could provide a step-by-step explanation of how the scalars are adjusted during training, and how these adjustments affect the balance between the natural and adversarial objectives. Furthermore, the authors should consider restructuring some of the denser sections to improve readability. This could involve breaking down long paragraphs into smaller, more digestible chunks, and using more visual aids, such as diagrams and flowcharts, to illustrate the key concepts. A clearer presentation would make the paper more accessible to a wider audience and enhance its overall impact.

Finally, the authors should consider expanding the experimental evaluation to include a wider range of datasets and model architectures. While the current results are promising, it would be beneficial to demonstrate the robustness of the proposed method across a more diverse set of scenarios. This could involve testing the method on datasets with different characteristics, such as those with imbalanced classes or noisy labels, and evaluating its performance on different model architectures, such as transformers or recurrent neural networks. Additionally, the authors could consider comparing their method to a wider range of baseline methods, including more recent and state-of-the-art approaches. This would provide a more comprehensive evaluation of the proposed method and further strengthen the paper's contribution.

### Questions

See weakness.

### Rating

5

### Confidence

3

**********
