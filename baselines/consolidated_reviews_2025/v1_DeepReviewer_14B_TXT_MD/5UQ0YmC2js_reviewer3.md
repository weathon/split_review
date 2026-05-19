### Summary

This paper introduces AdvI2I, a novel framework that exposes vulnerabilities in Image-to-Image (I2I) diffusion models by manipulating input images to generate NSFW content. Unlike previous adversarial text prompt attacks, AdvI2I optimizes a generator to create adversarial images that bypass existing defenses, such as Safe Latent Diffusion (SLD). An enhanced version, AdvI2I-Adaptive, is also proposed to adapt to potential countermeasures and minimize detectable patterns. Extensive experiments demonstrate the effectiveness of both AdvI2I and AdvI2I-Adaptive in circumventing current safeguards, highlighting the need for stronger security measures in I2I diffusion models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper introduces AdvI2I, a novel framework that exposes vulnerabilities in Image-to-Image (I2I) diffusion models by manipulating input images to generate NSFW content. Unlike previous adversarial text prompt attacks, AdvI2I optimizes a generator to create adversarial images that bypass existing defenses, such as Safe Latent Diffusion (SLD). An enhanced version, AdvI2I-Adaptive, is also proposed to adapt to potential countermeasures and minimize detectable patterns. Extensive experiments demonstrate the effectiveness of both AdvI2I and AdvI2I-Adaptive in circumventing current safeguards, highlighting the need for stronger security measures in I2I diffusion models.
2. This paper is well-written and easy to follow. The motivation is clear and the method is well described.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers two baselines, which is not enough. More baselines should be added.
2. The paper only considers two types of concepts, which is not enough. More concepts should be added.
3. The paper only considers two defense methods, which is not enough. More defense methods should be added.

### Suggestions

The paper's evaluation is limited by the small number of baselines used for comparison. While the authors introduce a novel attack framework, it is crucial to demonstrate its superiority over a wider range of existing adversarial attack methods. Specifically, the paper should include comparisons with more established adversarial attack techniques, such as those based on gradient-based methods or optimization-based methods, to provide a more comprehensive understanding of the proposed method's effectiveness. Furthermore, the selection of baselines should be justified, and the paper should discuss why the chosen baselines are relevant for comparison. This would strengthen the paper's claims and provide a more robust evaluation of the proposed method.

Expanding the scope of the concepts considered in the experiments is also essential. The current focus on only two types of concepts limits the generalizability of the findings. The paper should explore a wider range of concepts, including those that are more abstract or complex, to demonstrate the robustness of the proposed attack framework. For example, the paper could consider concepts related to different types of objects, scenes, or styles. This would provide a more comprehensive understanding of the attack's capabilities and limitations. Additionally, the paper should discuss the challenges associated with generating adversarial examples for different types of concepts and how the proposed method addresses these challenges.

Finally, the paper should consider a broader range of defense methods to evaluate the robustness of the proposed attack. The current evaluation only considers two defense methods, which is insufficient to demonstrate the attack's effectiveness against a wide range of potential countermeasures. The paper should include comparisons with more advanced defense techniques, such as adversarial training, input transformation methods, or detection-based methods. This would provide a more comprehensive understanding of the attack's limitations and potential vulnerabilities. Furthermore, the paper should discuss the challenges associated with defending against adversarial attacks in I2I diffusion models and how the proposed method can be adapted to address these challenges.

### Questions

See Weaknesses.

### Rating

6

### Confidence

4

**********
