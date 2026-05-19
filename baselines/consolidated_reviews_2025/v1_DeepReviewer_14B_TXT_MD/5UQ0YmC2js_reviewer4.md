### Summary

This paper proposes a novel adversarial attack method called AdvI2I, which targets Image-to-Image (I2I) diffusion models. The authors demonstrate that by manipulating input images, they can induce the generation of NSFW content, even when benign text prompts are used. The paper also introduces an enhanced version, AdvI2I-Adaptive, which is designed to bypass potential defense mechanisms by minimizing the similarity between adversarial images and NSFW concept embeddings. The authors conduct extensive experiments to show the effectiveness of their approach in circumventing existing safeguards.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to adversarial attacks on I2I diffusion models by focusing on image-based manipulation rather than text-based manipulation. This is a significant contribution as it exposes a previously underexplored vulnerability in these models.
2. The authors provide a clear and well-structured methodology for their attack, including the extraction of NSFW concept vectors and the training of an adversarial image generator. The use of a pre-trained VAE as the adversarial image generator is a clever choice that ensures greater similarity between the adversarial and original images.
3. The introduction of AdvI2I-Adaptive, which is designed to bypass potential defenses, demonstrates a forward-thinking approach to adversarial attacks. The authors consider potential countermeasures and develop a method that is more resilient against them.
4. The paper includes a comprehensive evaluation of the proposed attack, including comparisons with baseline methods and an analysis of the attack's performance under different defense mechanisms. The results clearly demonstrate the effectiveness of AdvI2I and AdvI2I-Adaptive in generating NSFW content.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on generating NSFW content, which limits its exploration of the attack's versatility across different types of harmful or misleading outputs. It would be beneficial to see how the proposed method could be adapted to generate other types of adversarial content, such as manipulated media or misinformation. The current scope, while significant, does not fully explore the potential breadth of the attack vector.
2. The paper does not provide a detailed analysis of the computational cost associated with training the adversarial image generator. Understanding the resources required for training is crucial for assessing the practicality of the proposed method. The lack of information on training time, memory usage, and hardware requirements makes it difficult to evaluate the feasibility of the approach for real-world applications.
3. While the paper demonstrates the effectiveness of AdvI2I-Adaptive against specific defense mechanisms, it does not explore the potential for more sophisticated defenses that could be developed in response. A discussion of potential future defense strategies and how the proposed attack might be adapted to counter them would strengthen the paper's contribution. The current evaluation, while thorough, does not fully address the dynamic nature of adversarial attacks and defenses.

### Suggestions

The authors should consider expanding the scope of their work to include a broader range of adversarial content beyond NSFW material. This could involve exploring the generation of manipulated media, such as deepfakes or altered images, as well as the creation of misleading or harmful information. For example, the adversarial image generator could be trained to introduce subtle changes to images that, when processed by the I2I diffusion model, result in altered content that conveys a false narrative or promotes misinformation. This would demonstrate the versatility of the attack and highlight its potential impact in various contexts. Furthermore, the authors could investigate the transferability of the attack across different I2I diffusion models, which would provide a more comprehensive understanding of its robustness and generalizability.

To address the lack of computational cost analysis, the authors should provide detailed information on the resources required for training the adversarial image generator. This should include the training time, memory usage, and hardware requirements, such as the specific GPU model used. Additionally, the authors could explore techniques to optimize the training process, such as using more efficient optimization algorithms or reducing the size of the adversarial image generator. This would make the proposed method more practical for real-world applications and allow for a more accurate assessment of its feasibility. The authors could also investigate the impact of different training parameters on the attack's effectiveness and computational cost, providing a more comprehensive understanding of the trade-offs involved.

Finally, the authors should discuss potential future defense strategies that could be developed to counter the proposed attack. This could include exploring techniques such as adversarial training, input sanitization, or anomaly detection. The authors should also discuss how the proposed attack might be adapted to counter these defenses, highlighting the dynamic nature of the adversarial landscape. For example, the authors could investigate the use of more sophisticated adversarial perturbations that are less detectable by defense mechanisms, or explore techniques to bypass input sanitization methods. This would provide a more comprehensive understanding of the limitations of the proposed attack and guide future research in this area.

### Questions

1. How does the computational cost of training the adversarial image generator compare to other adversarial attack methods? Are there any specific hardware requirements or optimizations that are necessary for the proposed approach?
2. Can the AdvI2I framework be adapted to generate other types of adversarial content beyond NSFW, such as manipulated media or misinformation? What modifications would be necessary to achieve this?
3. What are the potential defense mechanisms that could be developed to counter the AdvI2I attack? How might the AdvI2I-Adaptive version be further improved to bypass these defenses?

### Rating

6

### Confidence

3

**********
