### Summary

This paper introduces a novel approach to model inversion attacks (MIAs) by leveraging diffusion models instead of GANs. The authors propose two methods: a single-step generator for model inversion and a diffusion distillation MIA (DDMI). They also extend the application of generative MIAs to CLIP models. The paper demonstrates the effectiveness of the proposed methods through white-box and black-box experiments, showing that their approach achieves state-of-the-art (SOTA) performance.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow.
2. The authors conduct comprehensive experiments that validate their claims.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's novelty is somewhat limited, as the initial parts of the methodology section mainly apply existing techniques to the MIA problem. However, it is acceptable since the application of diffusion models to this problem is still beneficial to the research community.
2. While the authors propose two methods, there is insufficient comparison between them. It is unclear which method is superior or in what scenarios each method performs best. For example, the paper does not discuss the computational cost or inversion quality differences between the single-step generator and DDMI. Furthermore, the paper lacks a detailed analysis of the trade-offs between the two approaches, such as the number of diffusion steps required for DDMI to achieve comparable results to the single-step method, and how this impacts computational efficiency.
3. The paper lacks a thorough discussion of the limitations of the proposed methods. This is crucial for providing a complete picture and avoiding an overly positive tone without sufficient justification. For instance, the paper does not address how the performance of the methods degrades with increasing noise in the target model's output probabilities, or how sensitive the methods are to the choice of hyperparameters, particularly in the diffusion process. Additionally, the paper does not explore the potential for the methods to fail when the target model has been trained with robustness techniques such as adversarial training.

### Suggestions

The paper would benefit from a more detailed comparison of the two proposed methods, specifically focusing on their computational costs and inversion quality. The authors should include experiments that directly compare the single-step generator and DDMI across various settings, such as different numbers of diffusion steps for DDMI, and analyze the trade-offs between inversion quality and computational efficiency. For example, the authors could measure the inference time for both methods and plot inversion quality (e.g., using KNN distance) against inference time to show the performance trade-offs. Furthermore, a discussion on the scenarios where each method is most effective would be beneficial. For instance, is the single-step method more robust to noise in the target model's output, or does DDMI perform better with more complex target models? This analysis should also include a discussion of the memory requirements for each method, as DDMI may require more memory due to the iterative nature of the diffusion process.

To address the lack of discussion on limitations, the authors should include experiments that explore the robustness of their methods under various conditions. Specifically, they should evaluate how the performance of the methods degrades with increasing noise in the target model's output probabilities. This could be done by adding Gaussian noise to the output probabilities and measuring the impact on inversion quality. Additionally, the authors should analyze the sensitivity of their methods to the choice of hyperparameters, particularly those related to the diffusion process, such as the number of diffusion steps and the noise schedule. The paper should also explore the potential for the methods to fail when the target model has been trained with robustness techniques such as adversarial training. This could involve testing the methods on target models that have been adversarially trained and analyzing the impact on inversion quality. A thorough discussion of these limitations would provide a more complete picture of the proposed methods and their applicability.

Finally, the paper should include a more detailed discussion of the failure modes of the proposed methods. This could include examples of cases where the methods fail to produce realistic or accurate reconstructions, and an analysis of the reasons for these failures. For example, the authors could investigate whether the methods struggle with specific types of images or target models. This analysis should also consider the impact of the public dataset used for training the diffusion model on the inversion results. For instance, how does the performance of the methods change when the public dataset is significantly different from the private dataset used to train the target model? This would provide a more comprehensive understanding of the limitations of the proposed methods and their potential for improvement.

### Questions

1. In Table 1, the authors use CelebA as the public dataset. If the private dataset is also CelebA, would using CelebA as the public dataset still yield good results? Could you provide the results for this scenario?
2. In Table 2, the authors use FFHQ as the public dataset. If the private dataset is also FFHQ, would using FFHQ as the public dataset still yield good results? Could you provide the results for this scenario?
3. For the first method (single-step generator for model inversion), have you tested its performance when the output probabilities from the target model are perturbed? For instance, what happens if we add Gaussian noise to the output probabilities?
4. Could you provide results for the first method (single-step generator for model inversion) in the same settings as the experiments in Section 4.2? This would help in comparing the two methods.
5. What are the advantages and disadvantages of the two methods? Are there specific scenarios where one method performs better than the other?
6. Could you provide results for the second method (DDMI) in the same settings as the experiments in Section 4.2? This would help in comparing the two methods.
7. What are the limitations of the proposed methods? Are there cases where they might fail or perform poorly?

### Rating

5

### Confidence

4

**********
