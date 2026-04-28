# Training-Free Diffusion Model Alignment with Sampling Demons

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 5, 6, 6

## Abstract
Aligning diffusion models with user preferences has been a key challenge.
Existing methods for aligning diffusion models either require retraining or are limited to differentiable reward functions.
To address these limitations, we propose a stochastic optimization approach, dubbed \emph{Demon}, to guide the denoising process at inference time without backpropagation through reward functions or model retraining.
Our approach works by controlling noise distribution in denoising steps to concentrate density on regions corresponding to high rewards through stochastic optimization.
We provide comprehensive theoretical and empirical evidence to support and validate our approach, including experiments that use non-differentiable sources of rewards such as Visual-Language Model (VLM) APIs and human judgements.
To the best of our knowledge, the proposed approach is the first inference-time, backpropagation-free preference alignment method for diffusion models.
Our method can be easily integrated with existing diffusion models without further training.
Our experiments show that the proposed approach significantly improves the average aesthetics scores for text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of aligning diffusion models without additional training or backpropagation. The main idea is to optimize the sampling at inference time, by optimizing the noise used during generation based on a (possibly differentiable) reward signal. To compute the (expected) reward on a given noise, the method leverages a reduction from SDE to ODE dynamics.

### Strengths
- very clearly written and polished writing
- clear motivation
- compares to prior methods systematically, and shows consistent improvements

### Weaknesses
 - It's hard to gauge the significance/improvements in some of the results. For example, Appendix G.2 the numbers are all tightly concentrated around 0.2, so being unfamiliar with the metric, it's hard to know whether the differences are statistically significant or interesting.
- It would be nice to see more experiments with more realistic/extreme use cases of alignment. Most of the variations explored in the paper seem sort of minor. For example, make the model (not) generate NSFW material (or something else distributionally more obvious). Or is there a reason why such examples were note explored?

### Questions
- Given that the "noise" is now optimized over, is there a good intuitive way to think about it from a different perspective (diffusion, physics, or bayesian inference, etc.)? (other than the "noise" obviously corresponding to the latent vector)
- My intuition for the proposed sampling strategies improving over "best-of-N" sampling is that now you additionally get to optimize over the simplex spanned by the sampled noise samples (rather than just querying the "vertices" of the simplex). 
Could there be more intelligent ways to choose the "basis" vectors for the simplex other than random sample?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a backpropagation-free, inference-time method for preference alignment in diffusion models. Specifically, the method synthesizes an optimal noise distribution via stochastic optimization thus enhancing the final reward of the generated image.

### Strengths
Overall, this paper is thoroughly written, with comprehensive theoretical and empirical analysis. The implementation details are carefully listed, and various qualitative and quantitative metrics are displayed.

### Weaknesses
In the “Alignment with Preferences of VLMs” experiment, the role of the VLM doesn’t seem to exhibit a clear preference for a specific style, etc. I understand that the goal is to demonstrate that your method can optimize for a particular non-differentiable preference, such as a VLM API. However, based on the results presented, I’m not convinced that this experiment design effectively shows that your method truly optimizes for a specific preference.

The paper primarily compares the results with DOODL in terms of computational cost and performance. I would be curious to see how this method compares with other methods mentioned in Table 1 and how it performs with different base models (e.g., SDXL).

Additionally, I would like to know where the performance and computational cost of CM without your method are positioned in Figure 4.

### Questions
The paper primarily compares the results with DOODL in terms of computational cost and performance. I would be curious to see how this method compares with other methods mentioned in Table 1 and how it performs with different base models (e.g., SDXL).

Additionally, I would like to know where the performance and computational cost of CM without your method are positioned in Figure 4.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Demon, an inference-time method for aligning diffusion models with user preferences without retraining or backpropagation. Using stochastic optimization, it guides denoising to focus on high-reward regions, even with non-differentiable rewards like VLM APIs and human judgments. Experiments across three diverse tasks demonstrate improved improvements.

### Strengths
1. The concept of analyzing noise quality is interesting
2. The proposed method is a backpropagation-free preference alignment approach that operates during inference, allowing it to be applied flexibly across various conditions.

### Weaknesses
1. The comparison includes only a single baseline method, and quantitative results for BoN are missing in Table 3.
2. The evaluation is limited to a small subset of the dataset from DDPO [1]. Expanding the evaluation to include larger datasets, such as the full set from DDPO [1] and the Human Preference Dataset (HPDv2) [2], is recommended.
3. In Table 2, there remains a large performance gap between the 1-step CM and the 6-step ODE. It would be beneficial to consider additional state-of-the-art solvers of diffusion sampling for comparison.

### Questions
- The authors used the Consistency Model [1] to accelerate computation. Could this model be applied to other diffusion models with different learned data distributions? A more general acceleration method would be beneficial.

[1] Song, Yang, et al. "Consistency models." arXiv preprint arXiv:2303.01469 (2023).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this study, the authors develop a method to align the outputs of diffusion models with human preference at inference time. Specifically, the authors address the alignment from the perspective of noise generation. They first propose to measure the quality of noises in each denoising step. Then, they combined different noises to search for an ''optimal'' noise towards a high reward of outputs. Experimental results show that the proposed method effectively improves the aesthetic score of generated images.

### Strengths
+ The authors first develop a method to align the generation of diffusion models without training the model or computing the gradient of the reward model.
+ They conducted experiments on various reward models and preference types.
+ The paper is well-organized and easy to follow.

### Weaknesses
 - Is the proof in this study based on the linear assumption of the reward model? Given that the human preference for images is extremely complicated and certainly nonlinear, does it apply to the scenario of complex human preference labels?
- The noise is flipped in Figure 3, but this operation is neither included in Eq. (11) nor discussed in the main text. Is it a standard operation in your method? On the other hand, I'm not at all convinced that flipping it can ``transform it into high-reward noise’’ because the reward space is not linear and symmetric.
- The comparison between the proposed method and best-of-N is interesting. However, the experiment settings of best-of-N is unclear. I’m not sure whether they selected the final generation with the highest reward or selected the noise at each step. Second, it would be better if the authors could discuss why is the proposed method better than best-of-N based on their theoretical analysis.
- The baseline methods for comparison in experiments are not sufficient. First, they should compare the method with a baseline which always selects the best noise $z^{(k)}$ with the highest reward $(r\odot c)(\cdot)$ at each denoising step. Second, I expect a comparison between the proposed method with more methods based on gradient guidance (Bansal et al. 2024).
- The quantitative results in Section 5 are based on 22 simple prompts of animals, which are not convincing enough.

### Questions
Please refer to the above weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach for aligning diffusion models with user preferences at inference time without needing model retraining or backpropagation. The method, named Demon, leverages stochastic optimization to control the noise distribution during the denoising steps of diffusion models, steering the generation process towards user-specified rewards. This paper provides theoretical backing and empirical evidence, including experiments with non-differentiable reward sources such as Visual-Language Model (VLM) APIs and human judgments.

### Strengths
1.	This paper presents an interesting approach that eliminates the need for model retraining or backpropagation, which is an advancement in the field of diffusion models and user preference alignment.
2.	The proposed method can be easily integrated with existing diffusion models without further training, making it accessible for immediate application.

### Weaknesses
1.	Computational complexity of the proposed method needs to be discussed. While the authors claim ease of integration, the computational complexity of implementing the stochastic optimization approach might be high. I suggest the authors provide the required inference time and GPU memory in Table 3.
2.	Many strong baseline methods have been neglected. I suggest the authors compare with DDPO, DPO, and DPOK in Tables 3 and 4.
3.	The effectiveness of the Demon may be heavily dependent on the quality and fidelity of the reward signal, which may not always be reliable or accurate. Therefore, I suggest the authors conduct experiments to quantitatively compare the results between the human reward signal and a pre-trained reward model.
4.	The writing quality could be further improved. The overall intuition of the proposed method is easy to understand, but the description in Section 4.2 is a bit redundant and complex.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
