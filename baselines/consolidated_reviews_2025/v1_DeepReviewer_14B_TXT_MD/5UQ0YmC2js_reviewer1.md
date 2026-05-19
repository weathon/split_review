### Summary

AdvI2I introduces a framework that demonstrates how I2I diffusion models can be manipulated to generate NSFW content through adversarial image attacks. The authors propose a method to optimize an adversarial image generator, which crafts images that, when processed by diffusion models, result in NSFW outputs without altering the text prompts. They also introduce an enhanced version, AdvI2I-Adaptive, which is designed to bypass potential defenses by minimizing the detectability of adversarial images. The paper provides empirical evidence showing that AdvI2I can effectively circumvent existing safeguards, highlighting a significant security vulnerability in I2I diffusion models.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

AdvI2I exposes a previously underexplored vulnerability in I2I diffusion models, shifting the focus from text-based to image-based adversarial attacks. By demonstrating that adversarial images can induce NSFW content generation, the authors broaden the understanding of potential risks associated with diffusion models. The empirical results presented in the paper effectively demonstrate that AdvI2I can bypass existing defense mechanisms, such as Safe Latent Diffusion (SLD), highlighting the limitations of current approaches in ensuring model safety. AdvI2I-Adaptive further strengthens the attack's resilience by adapting to potential defenses, which underscores the need for more robust security measures in I2I diffusion models.

### Weaknesses

#### Some Related Works


#### comment

The study primarily focuses on generating NSFW content, limiting its exploration of the attack's versatility across different types of harmful or misleading outputs. The attack's effectiveness may be influenced by variations in model architectures, datasets, and training configurations of I2I diffusion models. There is a lack of discussion on practical defense strategies that could be implemented to mitigate the risks posed by AdvI2I. The paper does not thoroughly analyze the trade-offs between attack effectiveness and the perceptual quality of adversarial images, which is crucial for understanding the practical limitations of the attack.

### Suggestions

The paper should explore the potential of AdvI2I to generate a broader range of harmful content beyond NSFW images. This could include investigating the generation of misleading information, deepfakes, or other forms of malicious content. Such an investigation would require adapting the adversarial image generation process to target different types of outputs, which could involve modifying the loss functions or the training procedure. For example, the authors could explore how to manipulate the adversarial images to generate images that promote harmful stereotypes or spread misinformation. This would provide a more comprehensive understanding of the attack's capabilities and limitations, and would make the paper more relevant to a wider audience.

Furthermore, the paper needs to investigate the robustness of AdvI2I across different I2I diffusion model architectures and training configurations. The current study seems to focus on a limited set of models, and it is unclear how the attack would perform on models with different architectures, datasets, or training parameters. The authors should conduct experiments on a more diverse set of models to assess the generalizability of their approach. This should include models trained on different datasets, with different architectures, and with different training parameters. This would help to identify the factors that influence the attack's effectiveness and would provide a more robust evaluation of the proposed method. Additionally, the paper should explore the impact of different image resolutions and aspect ratios on the attack's success rate. This would provide a more complete picture of the attack's limitations and would help to identify potential defense strategies.

Finally, the paper should include a more detailed discussion of potential defense mechanisms against AdvI2I. While the authors introduce AdvI2I-Adaptive, which is designed to bypass potential defenses, they do not provide a comprehensive analysis of practical defense strategies. The paper should explore various defense mechanisms, such as adversarial training, input sanitization, or anomaly detection, and evaluate their effectiveness against AdvI2I. This would provide a more balanced perspective on the problem and would help to guide future research in this area. The discussion should also include the trade-offs between the effectiveness of the defense mechanisms and their impact on the utility of the diffusion models. This would help to identify the most promising defense strategies and would provide a more practical guide for practitioners.

### Questions

Can the AdvI2I framework be adapted to generate other types of harmful content beyond NSFW, such as misinformation or manipulated media? How would the attack's effectiveness vary across different I2I diffusion model architectures and training configurations? What are the trade-offs between the attack effectiveness and the perceptual quality of adversarial images? Could the authors discuss potential defense mechanisms against AdvI2I, and how might these be integrated into existing diffusion model frameworks?

### Rating

5

### Confidence

4

**********
