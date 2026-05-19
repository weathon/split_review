### Summary

The paper introduces a novel attack method aimed at increasing the energy-latency cost of large vision-language models (VLMs) during inference. The authors propose the use of "verbose images," which are crafted by adding imperceptible perturbations to images, to induce VLMs to generate longer sequences. The attack leverages three loss functions: a delayed EOS loss to encourage the model to generate more tokens, an uncertainty loss to increase the randomness of each generated token, and a token diversity loss to enhance the variety of tokens in the generated sequence. A temporal weight adjustment algorithm is also introduced to balance these loss functions during optimization. The experimental results demonstrate that the proposed method can significantly increase the length of generated sequences, leading to higher energy consumption and latency compared to original images and other baseline methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel concept of using verbose images to induce high energy-latency costs in VLMs, which is a unique approach to exploring the attack surface of these models.

2. The authors provide a comprehensive experimental evaluation of their method across multiple VLMs and datasets, demonstrating the effectiveness of verbose images in increasing the length of generated sequences and the associated energy-latency costs.

3. The paper is well-organized and clearly written, making it easy to follow the methodology and understand the experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the image captioning task. It would be beneficial to explore the effectiveness of verbose images in other multi-modal tasks, such as visual question answering (VQA) and visual reasoning, to demonstrate the generalizability of the proposed method. The current evaluation lacks a thorough investigation into how the proposed method performs across diverse tasks that leverage vision-language models, limiting the scope of the findings.

2. The authors should consider the potential defenses that could be employed to mitigate the impact of verbose images, such as input sanitization or model hardening techniques. A discussion of these aspects would enhance the practical relevance of the paper. The absence of a discussion on potential countermeasures leaves a gap in understanding the real-world implications of this attack.

3. The paper could benefit from a more detailed analysis of the trade-off between the magnitude of the perturbation and the resulting increase in energy-latency cost. It is important to understand the sensitivity of the method to different perturbation magnitudes. The paper does not provide a granular analysis of how different perturbation levels affect the attack's efficacy and the perceptual quality of the images, which is crucial for practical applications.

### Suggestions

The paper introduces an interesting approach to attacking vision-language models (VLMs) by inducing high energy consumption and latency through verbose images. However, the evaluation is limited to image captioning, and it is crucial to assess the method's effectiveness across a broader range of multi-modal tasks. Specifically, the authors should explore tasks like visual question answering (VQA) and visual reasoning, which involve more complex interactions between visual and textual inputs. This would involve adapting the loss functions and optimization strategies to the specific requirements of these tasks. For instance, in VQA, the goal would be to generate longer, more complex answers, while in visual reasoning, the focus would be on extending the reasoning chain. Furthermore, the evaluation should include a diverse set of datasets for each task to ensure the generalizability of the findings. This would provide a more comprehensive understanding of the attack's capabilities and limitations across different task scenarios.

In addition to expanding the task scope, the paper should address the potential defenses against verbose image attacks. The authors should investigate techniques such as input sanitization, which could involve filtering or modifying the perturbed images before they are fed into the VLM. This could include methods like denoising or adversarial training to make the model more robust to perturbations. Another avenue to explore is model hardening, which involves modifying the VLM itself to be more resistant to verbose images. This could involve techniques like adversarial training or regularization methods that penalize the model for generating overly long sequences. A thorough analysis of these defenses would provide a more complete picture of the practical implications of the proposed attack and guide the development of more robust VLMs. The paper should also discuss the trade-offs between the effectiveness of these defenses and their impact on the model's performance on benign inputs.

Finally, the paper needs a more detailed analysis of the perturbation magnitude and its impact on the attack's effectiveness and the perceptual quality of the images. The authors should conduct experiments with a range of perturbation magnitudes and evaluate the resulting energy-latency costs, sequence lengths, and image quality. This analysis should include both quantitative metrics, such as the LPIPS score, and qualitative assessments of the perturbed images. Furthermore, the paper should provide a detailed breakdown of the computational resources required to generate verbose images, including the time, memory, and hardware requirements. This information is crucial for assessing the scalability of the proposed method to larger datasets and more complex models. The authors should also discuss the potential for optimizing the generation process to reduce the computational overhead.

### Questions

1. How does the performance of verbose images vary across different types of images (e.g., natural images, synthetic images, images with different levels of complexity)?

2. What are the potential defenses that could be employed to mitigate the impact of verbose images, and how effective are these defenses against the proposed method?

3. How does the proposed method perform on state-of-the-art VLMs that are not included in the experimental evaluation?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
