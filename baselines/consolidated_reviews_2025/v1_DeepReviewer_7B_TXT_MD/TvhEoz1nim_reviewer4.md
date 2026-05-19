### Summary

This paper proposes a new model inversion attack (MIA) framework, termed diffusion distillation MIAs (DDMI), which addresses the limitations of traditional GAN-based MIAs by leveraging generative diffusion models. The authors demonstrate that DDMI significantly outperforms SOTA GAN-based MIAs in both white-box and black-box settings, achieving substantial improvements in traditional metrics and greatly enhancing the visual fidelity of reconstructed samples. Additionally, the paper explores privacy leakage in CLIP models, highlighting the urgent need for robust defense mechanisms against such attacks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.
3. The paper explores privacy leakage in CLIP models, which is an important and timely topic.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with recent works, such as [1], which also proposes a model inversion attack (MIA) method using diffusion models. The authors should include a comparison with this work to demonstrate the advantages of their method. Specifically, the paper should clarify the differences in methodology, such as the specific diffusion model architectures used, the inversion optimization techniques, and the evaluation metrics. Without this, it is difficult to assess the novelty and contribution of the proposed approach.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be beneficial to include a comparison of the computational resources required by the proposed method and the baseline methods. This should include the training time, memory usage, and inference time for both the diffusion model and the inversion process. This analysis is crucial for understanding the practical applicability of the proposed method, especially when dealing with large-scale datasets or real-time applications.
3. The paper does not explore the robustness of the proposed method against different types of defenses or adversarial attacks. It would be beneficial to investigate how the proposed method performs when the target model is modified or protected by techniques such as differential privacy or adversarial training. This analysis should include a discussion of the potential vulnerabilities of the proposed method and how these vulnerabilities could be exploited by an adversary. This is important for understanding the security implications of the proposed method.

### Suggestions

The authors should provide a more detailed comparison with existing diffusion-based model inversion attacks, specifically addressing the differences in the diffusion model architectures, inversion optimization techniques, and evaluation metrics. A table summarizing these differences would be beneficial. Furthermore, the authors should clarify the specific advantages of their approach over existing methods, such as improved reconstruction quality, faster convergence, or better robustness to adversarial attacks. This comparison should not only focus on quantitative results but also on qualitative aspects, such as the visual fidelity of the reconstructed images and the diversity of the generated samples. The authors should also discuss the limitations of their approach and identify potential areas for future research.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the computational resources required by their method, including the training time, memory usage, and inference time for both the diffusion model and the inversion process. This analysis should be compared with the computational cost of baseline methods, such as GAN-based MIAs. The authors should also discuss the scalability of their method to larger datasets and more complex models. This analysis should include a discussion of the trade-offs between computational cost and performance, and it should provide practical guidance for users of the proposed method. For example, the authors could discuss the impact of different hyperparameter settings on the computational cost and performance of the method.

Finally, the authors should investigate the robustness of their method against different types of defenses and adversarial attacks. This should include an evaluation of the method's performance when the target model is modified or protected by techniques such as differential privacy or adversarial training. The authors should also discuss the potential vulnerabilities of their method and how these vulnerabilities could be exploited by an adversary. This analysis should include a discussion of the limitations of their approach and identify potential areas for future research. For example, the authors could explore the use of adversarial training techniques to improve the robustness of their method.

### Questions

Please see the weakness.

### Rating

6

### Confidence

3

**********
