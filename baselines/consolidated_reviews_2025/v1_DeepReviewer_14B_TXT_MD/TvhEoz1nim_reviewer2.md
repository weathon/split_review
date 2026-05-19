### Summary

This paper explores the use of diffusion models in generative model inversion attacks (MIAs), addressing limitations in GAN-based approaches, such as instability and low fidelity in reconstructed samples. The authors propose a novel framework called diffusion distillation MIAs (DDMI), which utilizes a single-step generator distilled from pretrained diffusion models to enhance the inversion process. By constraining the search space to the generator's manifold, DDMI significantly improves the visual fidelity and accuracy of reconstructed samples. Additionally, the paper investigates privacy leakage in CLIP models, revealing vulnerabilities in large-scale multimodal systems. Extensive experiments demonstrate that DDMI outperforms state-of-the-art GAN-based MIAs in both white-box and black-box settings, highlighting the need for robust privacy defenses in machine learning models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the methodology and results.
2. The authors provide extensive experimental results that demonstrate the effectiveness of DDMI over existing GAN-based methods, particularly in terms of visual fidelity and reconstruction accuracy.
3. The exploration of privacy risks in CLIP models is a novel contribution, expanding the scope of MIAs to multimodal systems and revealing important security implications.
4. The use of single-step diffusion models addresses key limitations of GANs, such as instability and mode collapse, leading to more reliable and higher-quality reconstructions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the proposed DDMI framework. Specifically, the runtime and memory requirements for both training and inference stages are not clearly outlined, making it difficult to assess the practical feasibility of the approach, especially when considering the potential for scaling to larger models or datasets. A breakdown of the computational demands of the distillation process, as well as the inversion process, would be beneficial.
2. While the paper demonstrates improvements over GAN-based methods, it lacks a comprehensive comparison with other recent generative models beyond GANs, such as normalizing flows or autoregressive models, which could also be adapted for generative MIAs. This limits the understanding of DDMI's relative performance within the broader landscape of generative techniques. The paper should include a more thorough discussion of why these alternatives were not considered and what the potential benefits or drawbacks might be.
3. The evaluation metrics used in the experiments are primarily quantitative, such as FID and KNN distance, but lack a qualitative analysis of the reconstructed samples. While quantitative metrics provide a numerical assessment, they do not fully capture the perceptual quality and semantic fidelity of the reconstructed images. A more detailed qualitative analysis, perhaps including a user study or a more in-depth visual inspection, would strengthen the evaluation.
4. The paper does not explore potential defense mechanisms against DDMI. Addressing possible countermeasures or discussing the robustness of DDMI against defenses would provide a more balanced view of the framework's practical implications and limitations. The paper should at least acknowledge the existence of potential defenses and discuss how they might impact the effectiveness of the proposed attack.

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the time and memory requirements for each stage of the DDMI framework. This should include the cost of pretraining the diffusion model, the distillation process, and the inversion process itself. Furthermore, the analysis should consider how these costs scale with the size of the model and the dataset. For example, providing a table that shows the training time and memory usage for different model sizes (e.g., number of parameters) and dataset sizes (e.g., number of images) would be very helpful. This would allow readers to better understand the practical limitations of the approach and assess its feasibility for different applications. Additionally, the authors should discuss the potential for optimizing the computational cost of DDMI, such as through the use of more efficient distillation techniques or model compression methods.

To strengthen the comparison with other generative models, the authors should include a more thorough discussion of the potential benefits and drawbacks of using alternative generative models for MIAs. For example, they could discuss how normalizing flows, with their exact likelihood computation, might offer advantages in terms of sample quality or training stability, or how autoregressive models, with their ability to model complex dependencies, might be better suited for certain types of data. The authors should also consider adapting these models for generative MIA tasks and providing a comparative analysis of their performance against DDMI. This would provide a more comprehensive understanding of the strengths and weaknesses of DDMI relative to other state-of-the-art generative techniques. Furthermore, the authors should discuss the challenges associated with adapting these models for MIA tasks, such as the need for specific training strategies or the potential for increased computational cost.

Finally, to address the lack of qualitative analysis, the authors should include a more in-depth visual inspection of the reconstructed samples, focusing on the perceptual quality and semantic fidelity of the reconstructions. This could involve a user study where participants are asked to rate the quality of the reconstructed images or a more detailed visual analysis by the authors, focusing on specific features and details. The authors should also discuss the limitations of the quantitative metrics used in the paper and explain why a qualitative analysis is necessary to fully evaluate the performance of DDMI. Furthermore, the authors should acknowledge the existence of potential defenses against DDMI and discuss how these defenses might impact the effectiveness of the proposed attack. This could include a discussion of techniques such as differential privacy or adversarial training, and how they might be used to mitigate the privacy risks associated with MIAs.

### Questions

1. Can the authors provide more details on the computational cost of the DDMI framework, including training and inference times, and how it compares to GAN-based methods?
2. How does the performance of DDMI scale with the size of the model and the dataset? Are there any limitations in terms of computational resources or time?
3. What are the potential defense mechanisms against DDMI, and how robust is the framework against such countermeasures?

### Rating

5

### Confidence

3

**********
