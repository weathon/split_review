### Summary

This paper presents a new model inversion attack (MIA) framework that leverages diffusion models, called diffusion distillation MIAs (DDMI). The proposed method uses a single-step generator distilled from a pre-trained diffusion model to constrain the search space for the inversion process. The authors demonstrate that DDMI outperforms state-of-the-art GAN-based MIAs in both white-box and black-box settings, achieving substantial improvements in reconstruction quality and privacy leakage. Additionally, the paper explores the privacy risks of CLIP models, revealing that these models can be vulnerable to generative MIAs, which can reconstruct images that closely resemble private training data. This research uncovers vulnerabilities in CLIP models and opens new research directions in generative MIAs.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. This paper is well-written and easy to follow.
2. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Inversion attacks against image generative models.

#### comment

1. The paper lacks a comparison with recent works, such as [1], which also proposes a model inversion attack (MIA) method using diffusion models. The authors should include a comparison with this work to demonstrate the advantages of their method. Specifically, the paper should clarify the differences in methodology, such as the specific diffusion model architectures used, the inversion optimization techniques, and the evaluation metrics. Without this, it is difficult to assess the novelty and contribution of the proposed approach.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be beneficial to include a comparison of the computational resources required by the proposed method and the baseline methods. This should include the training time, memory usage, and inference time for both the diffusion model and the inversion process. This analysis is crucial for understanding the practical applicability of the proposed method, especially when dealing with large-scale datasets or real-time applications.
3. The paper does not explore the robustness of the proposed method against different types of defenses or adversarial attacks. It would be beneficial to investigate how the proposed method performs when the target model is modified or protected by techniques such as differential privacy or adversarial training. This analysis should include a discussion of the potential vulnerabilities of the proposed method and how these vulnerabilities could be exploited by an adversary. This is important for understanding the security implications of the proposed method.

### Suggestions

The authors should provide a more detailed comparison with existing diffusion-based model inversion attacks, specifically addressing the differences in the diffusion model architectures, inversion optimization techniques, and evaluation metrics. A table summarizing these differences would be beneficial. Furthermore, the authors should clarify the specific advantages of their approach over existing methods, such as improved reconstruction quality, faster convergence, or better robustness to adversarial attacks. This comparison should not only focus on quantitative results but also on qualitative aspects, such as the visual fidelity of the reconstructed images and the diversity of the generated samples. The authors should also discuss the limitations of their approach and identify potential areas for future research.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the computational resources required by their method, including the training time, memory usage, and inference time for both the diffusion model and the inversion process. This analysis should be compared with the computational cost of baseline methods, such as GAN-based MIAs. The authors should also discuss the scalability of their method to larger datasets and more complex models. This analysis should include a discussion of the trade-offs between computational cost and performance, and it should provide practical guidance for users of the proposed method. For example, the authors could discuss the impact of different hyperparameter settings on the computational cost and performance of the method.

Finally, the authors should investigate the robustness of their method against different types of defenses and adversarial attacks. This should include an evaluation of the method's performance when the target model is modified or protected by techniques such as differential privacy or adversarial training. The authors should also discuss the potential vulnerabilities of their method and how these vulnerabilities could be exploited by an adversary. This analysis should include a discussion of the limitations of their approach and identify potential areas for future research. For example, the authors could explore the use of adversarial training techniques to improve the robustness of their method.

### Questions

1. What are the advantages of the proposed method compared to existing diffusion-based model inversion attacks?
2. What is the computational cost of the proposed method compared to baseline methods?

### Rating

6

### Confidence

3

**********
