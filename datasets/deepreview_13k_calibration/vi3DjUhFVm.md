# Alignment without Over-optimization: Training-Free Solution for Diffusion Models

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
Diffusion models excel in generative tasks, but aligning them with specific objectives while maintaining their versatility remains challenging. Existing fine-tuning methods often suffer from reward over-optimization, while approximate guidance approaches fail to optimize target rewards effectively. Addressing these limitations, we propose a training-free sampling method based on Sequential Monte Carlo (SMC) to sample from the reward-aligned target distribution. Our approach, tailored for diffusion sampling and incorporating tempering techniques, achieves comparable or superior target rewards to fine-tuning methods while preserving diversity and cross-reward generalization. We demonstrate its effectiveness in single-reward optimization, multi-objective scenarios, and online black-box optimization. This work offers a robust solution for aligning diffusion models with diverse downstream objectives without compromising their general capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes DAS, a training-free approach for aligning diffusion models with specific objectives. It uses Sequential Monte Carlo (SMC) with tempering for reward alignment. This method is demonstrated across generative tasks, including single-reward and multi-objective cases, with performance comparable to fine-tuning methods in terms of target reward optimization and diversity.

### Strengths
1. DAS does not require additional training, which reduces computational cost.
2.The use of SMC with tempering is justified through asymptotic properties.
3. DAS balances reward optimization and diversity, and is demonstrated across single-reward, multi-objective, and online settings.

### Weaknesses
1. While DAS is compared with fine-tuning and guidance methods, comparisons to baselines like STEGANODE or controlled diffusion could have strengthened the evaluation. Specifically, methods that directly optimize for a reward function, such as those using reinforcement learning or gradient-based optimization, should be included for a more comprehensive comparison. The absence of these comparisons makes it difficult to assess the relative strengths and weaknesses of DAS.
2. DAS assumes differentiable reward functions, which may limit applicability in scenarios involving non-differentiable objectives. Many real-world reward functions, such as those based on human perception or complex simulations, are not easily differentiable, and the paper does not adequately address how DAS would handle such cases. This limitation could significantly restrict the practical use of the method.
3. Most experiments use Stable Diffusion v1.5, and additional models would have enhanced the generality of the findings. The performance of diffusion models can vary significantly across different architectures and training datasets. The lack of experiments on other models raises concerns about the robustness and generalizability of the proposed method.
4. The paper can do more image tasks. Currently it emphasizes findings on aesthetic score, which might not generalize well to other tasks. While aesthetic score is a common metric, it is not representative of all potential applications of diffusion models. The paper should include experiments on a wider range of image tasks to demonstrate the versatility of the proposed method.
5. Limitations: the setup of SMC with tempering, intermediate targets, and backward kernels can be technically demanding. And the effectiveness of DAS depends on the pre-trained model's quality, limiting performance on models with low initial diversity or reward alignment.

### Questions
1. The method relies on specific tempering schemes and parameters, and the practical guidelines for selecting these could be more detailed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a training-free diffusion sampling method based on Sequential Monte Carlo (SMC) to sample from the reward-aligned target distribution. By incorporating tempering techniques, it offers a robust solution for aligning diffusion models with arbitrary rewards
while preserving general capabilities

### Strengths
1. This paper is overall well-written and the motivation is clear. It aims to address the trade-off in diffusion models that align them with specific objectives while maintaining their versatility, which is a critical problem in generative modeling.

2. DAS’s effectiveness is comprehensively validated across diverse scenarios, including toy distribution simulation, single-reward, multi-objective, and online black-box optimization tasks.

### Weaknesses
1. More intuitive explanations of SMC are suggested to add between the motivation and method to make it more consistent and intuitive since the introduction of SMC in supplementary material is a bit abstruse to understand, making the superiority of adopting SMC to address the training problem unclear.

2. How to choose hyperparameters such as $\gamma, \alpha$ and particles should be discussed across different scenarios.

### Questions
Please see the weaknesses part above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel, training-free sampling method aimed at generating samples from a target distribution, with a specific focus on applications in Reinforcement Learning from Human Feedback (RLHF). The authors compare their approach against existing fine-tuning baselines and guidance techniques.

### Strengths
- The introduction provides a clear overview of the problem.

- The proposed method appears promising and might be innovative (see Question 5.)

### Weaknesses
 - The choice of finetuning-based RLHF baselines may not be appropriate (see Question 1).

- The paper is sometimes hard to follow due to the delayed definition of new notations. For instance, the symbol $\gamma$ is used on line 208 but is not defined until line 250.

- The evaluation metrics used in the paper (line 355 and onward) are not explained, making it difficult to assess their relevance and meaning.

### Questions
1. Baselines for Comparison: The authors correctly state that RLHF can be formulated as learning to sample from an unnormalized target distribution (Section 3.2). They show that current fine-tuning approaches in RLHF struggle to sample from multimodal target distributions, which highlights the limitations of these methods. However, this comparison may not be sufficient. There is significant research on using diffusion methods for sampling from multimodal distributions which would not fail at the examples presented in Figure 1 (e.g., [1], [2], [3] for continuous-time models, and [4] for discrete-time models). Including these approaches would provide a more convincing set of baselines. If this is not possible within the rebuttal phase's timeline, I believe it is necessary to at least mention this line of work in the paper. 

2. Clarification on Calculations: The calculation presented on line 153 and the following lines is unclear. Can you provide a detailed derivation?

3. Explanation of Evaluation Metrics: The evaluation metrics mentioned in line 355 and onward lack a clear explanation. Currently, understanding them requires consulting multiple references. Could you include a brief explanation in the paper for clarity?

4. Inference Time Comparison: How does the inference time of your method compare with fine-tuning techniques? It seems plausible that fine-tuning methods might produce samples more quickly. Is this the case?

5. Novelty of the Method: Is the proposed method entirely new, or is it simply novel in the context of RLHF? How does it compare to other Sequential Monte Carlo methods?

I will initially give a score of 3, but I am willing to update my score if my questions are properly addressed.

# References
[1] Zhang, Qinsheng, and Yongxin Chen. "Path Integral Sampler: A Stochastic Control Approach For Sampling." International Conference on Learning Representations.

[2] Berner, Julius, Lorenz Richter, and Karen Ullrich. "An Optimal Control Perspective on Diffusion-Based Generative Modeling." Transactions on Machine Learning Research.

[3] Vargas, Francisco, Will Sussman Grathwohl, and Arnaud Doucet. "Denoising Diffusion Samplers." Eleventh International Conference on Learning Representations.

[4] Sanokowski, Sebastian, Sepp Hochreiter, and Sebastian Lehner. "A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization." Forty-First International Conference on Machine Learning.

[5] Dongjun Kim, Yeongmin Kim, Se Jung Kwon, Wanmo Kang, Il-Chul Moon Proceedings of the 40th International Conference on Machine Learning, PMLR 202:16567-16598, 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper propose a training-free sampling method based on Sequential Monte Carlo (SMC)  to align the diffusion models with specific objectives. Specially, Diffusion Alignment as Sampling (DAS) is designed to address the  limitations of the previous alignment approaches include fine-tuning and guidance methods. The author also provide theoretical analysis of DAS’s asymptotic properties and empirically validate DAS’s effectiveness across different tasks. Meanwhile, the authors conducte sufficient experiments to verify the validity of the DAS methodology.

### Strengths
The paper is clearly written and there is a good discussion of the work involved. Based on the fact that the existing fine-tuning methods lead to the reward overoptimization problem while the guidance methods lead to the under-optimization problem, the authors propose the DAS method to alleviate these deficiencies. In addition, the authors provide a theoretical analysis of the method and give the relevant code, making the work very solid. Figure 1 illustrates the shortcomings of the existing methods as well as the advantages of the proposed method, and the experimental results are visualized by using an example of a mixed Gaussian distribution.

### Weaknesses
+ The models underlying the experiments in this paper have some weaknesses, and the Stable Diffusion (SD) v1.5 model is somewhat outdated now. The Consistency model [1] and Flow model (SD3) [2]  are widely used nowadays, so I suggest the authors to conduct some experiments on the newer model so as to further illustrate the validity of the proposed method. It is important to demonstrate the method's effectiveness on state-of-the-art models, as the performance on older models might not directly translate to current architectures. Specifically, the SD v1.5 model lacks certain architectural improvements and training techniques present in newer models, which could impact the generalizability of the results.

+ In addition to mixing Gaussian distributions, **Swiss rolls** are also commonly used to visualize whether a distribution has been learned or not, and due to their structural features, which can further reflect the model's ability to fit the distribution, the authors can give some visualizations that further illustrate the strengths of the proposed method. The use of Swiss roll datasets is crucial because they offer a non-linear manifold structure that can expose limitations in sampling methods, particularly in capturing the underlying data distribution's topology. This is a more rigorous test compared to simple Gaussian mixtures.

### Questions
Please refer to Weaknesses. I will also refer to other reviewers' comments

### Soundness
4

### Presentation
3

### Contribution
3
