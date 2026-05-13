# Morse: Fast Sampling for Accelerating Diffusion Models Universally

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
In this paper, we present Morse, a simple and universal framework for accelerating diffusion models. The key insight of Morse is to reformulate the iterative generation (from noise to data) process via taking advantage of fast jump sampling and adaptive residual feedback strategies. Specifically, Morse involves two models called Dash and Dot that interact with each other. The Dash model is just the pre-trained diffusion model of any type, but operates in a jump sampling regime, creating sufficient space for sampling efficiency improvement. The Dot model is significantly faster than the Dash model, which is learnt to generate residual feedback conditioned on the observations at the current jump sampling point on the trajectory of the Dash model, lifting the noise estimate to easily match the next-step estimate of the Dash model without jump sampling. By chaining the outputs of the Dash and Dot models run in a time-interleaved fashion, Morse exhibits the merit of flexibly attaining desired image generation performance while improving overall runtime efficiency. With our proposed weight sharing strategy between the Dash and Dot models, Morse is efficient for training and inference. We validate the efficacy of our method under a variety of experimental setups. Our method shows an average speedup of 1.78× to 3.31× over a wide range of sampling step budgets relative to baseline diffusion models. Furthermore, we show that our method can be also generalized to improve the Latent Consistency Model (LCM-SDXL, which is already accelerated with consistency distillation technique) tailored for few-step text-to-image synthesis. The code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a framework for the acceleration of any diffusion model. The kay idea is the use of a dual-model design, that consists of a heavy and a light model. The heavy model in this case is the original diffusion model, where the light one is a similar model but operating in a lower resolution. The approach has been seen in many other fields, but the claim here is that this is the fist time that is applied to diffusion models, and the main challenge was the design of the light model and the decision on the information that it had to consider. This is a heavy experimental paper, where the authors demonstrate in a number of settings the efficacy of their approach.

### Strengths
The approach is quite simple and easy to apply. It is orthogonal to many other approaches in the area.
A good set of experiments under varying settings that demonstrate the efficacy of the method

### Weaknesses
 There is limited discussion on how the scheduling of Morse is decided. A5 provides some insight on the performance of various configurations, but no actual approach is given.

Fig 4 and 5 show the performance gains for a number of scenarios. However the reported overall gains take into account non meaningful FID scores (which is also the case where the proposed method provides the largest gains). I would suggest to focus the reported of the gain to a narrower FID band.

A simple (and faster rectifier) would be a combination of the original model but with a down sampled input followed by an up sampling block. Assign this comparison would add more information about the value that is actually added by the tuning of the new proposed model, given that the demonstrated gains are mainly due to the down sampling of the input. Table 4 and the relevant discussion addresses part of it but a)what about other samplers, and b) how statistical significant are the differences in FID scores?

### Questions
There is a trade-off between the relative computational cost of the Dot compared to Dash and the similarity of the two models. A2 provides some insight of the construction of the Dot model, but gives little insight on the actual space cost-quality. Have other design approaches attempted?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new methodology for sampling in diffusion models called Morse. It has two components, the first one is the "Jump Sampling" which uses different existing samplers to reduce the number of diffusion steps to converge to the generated image. The second component is the use of a smaller and much more efficient "dot" model to effectively interpolate between samples, providing residual feedback, leading to faster convergence. The dot model utilizes weight sharing with the main model (dubbed dash) to decrease overall training time. The paper demonstrates the compatibility of their system with multiple existing samplers including DDIM, DDPM, SDE and DPM, showing a speedup, especially in the low FID regime with few steps.

### Strengths
This paper provides a novel methodology to improve the sampling speed of diffusion models and is compatible with many samplers. The paper provides many details and nuances to make this system practical, especially when it comes to training the smaller model and how it is used in conjunction with the larger model. The evaluation is fairly comprehensive, although I do have more comments on that in the weaknesses section. I thought it was great that the authors also showed their results on multiple model sizes.

### Weaknesses
I view this paper's contributions as an efficiency technique for diffusion models. As such, I expected to see (1) and end-to-end implementation of the system showing measured speedup, and (2) some comparison/compatibility with other efficiency techniques. Both of these things are missing from the paper. I realize that the latter (2) may be hard to do comprehenesively, but at least a quantitative comparison to distilled/quantized diffusion models would make sense here. For the first weakness (1) the use of LDM is very confusing to me. Is this measured speed per step? Why not show the end-to-end time for generating an image? I imagine having two models has more room for system-level optimization which might have not been done in this work? The final weakness is that presentation of results which is shown on a log-log scale. I don't think an FID of 320 matters, so a bigger focus on the low FID regime would make more sense. It seems that speedup generally decreases as more time is given to the diffusion process. Is this method useful for high-quality image generation? or is only useful in lower-quality and faster latency regime? I think both are fine but it would be good to clarify the numbers at both extremes.

### Questions
Please see weaknesses. Most of my questions are there.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces "Morse," a novel framework designed to enhance the efficiency of diffusion models, which are essential in generating high-quality images. The authors tackle the challenge of maintaining high sampling efficiency while minimizing information loss, a common issue with jump sampling techniques. By leveraging fast jump sampling and adaptive residual feedback, Morse offers a promising solution.



**Experimental Evaluation**

The authors conducted extensive experiments using datasets such as CIFAR-10 and LSUN-Church, and tested Morse with various samplers. The results are impressive, showing that Morse can accelerate diffusion models by an average of 1.78x to 3.31x compared to baseline models. This demonstrates Morse's capability to enhance runtime efficiency significantly.



In conclusion, Morse represents an advancement in the field of diffusion models, providing a balanced solution to the trade-off between speed and quality. Future research could explore optimizing the Dot model's resource demands and expanding Morse's applicability to a wider range of diffusion scenarios.

### Strengths
**Key Contributions and Methods**

The standout feature of Morse is its dual-model approach: the Dash and Dot models. The Dash model operates within a jump sampling regime, while the Dot model, which is significantly faster, compensates for any information loss through residual feedback. This combination allows for flexible and efficient image generation without compromising performance.

The paper situates Morse within the broader context of diffusion models, referencing established samplers like DDPM, DDIM, DPM-Solver, and SDE. This contextualization not only highlights the relevance of Morse but also underscores its potential to improve upon existing methods.

### Weaknesses
While Morse offers substantial improvements, it does come with some limitations. The introduction of the Dot model requires additional training and computational resources. Furthermore, Morse's effectiveness is limited to scenarios where increasing the number of sampling steps enhances sample quality. The authors also touch on the ethical considerations, acknowledging the potential misuse of such generative models in creating deceptive content.

### Questions
1. Could the authors provide a more detailed analysis of the trade-offs and limitations of Morse, as highlighted in the Discussion section? The paper mentions that Morse "introduces an extra lightweight Dot model, which requires additional training and computational memory." A deeper exploration of these drawbacks would help readers better understand the practical implications of using Morse. Specifically, a quantitative comparison of the additional training time and memory requirements introduced by the Dot model versus the runtime speedups achieved would be particularly beneficial for readers.


2. Are there any plans to release Morse as an open-source project? Open-sourcing it could enhance its impact by allowing the diffusion community to build upon its contributions, fostering collaboration, and broader adoption.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Morse, a framework to accelerate Diffusion model. Morse leverages fast jumping sampling and adaptive residual feedback strategies to reformulate the iterative generation models. Two models called Dash model and Dot model are involved in Morse. The proposed method shows significant speed-ups compared with some baseline methods.

### Strengths
The paper is clearly written. The experiments are extensive, and demonstrate the practical efficiency and effectiveness of Morse. Besides, some theoretical properties are also discussed. The proposed framework is novel and interesting.

### Weaknesses
The main concern is that the Morse needs an extra model called Dot model, which needs extra and non-negligible computing resources. While the paper demonstrates speed-ups, it is unclear if these speed-ups are consistent across all sampling steps and generation quality targets. Specifically, when the number of sampling steps (LSDs) is high, the performance of Morse seems to converge to that of the baseline DPM-Solver, with minimal or no speedup. This raises questions about the practical benefits of Morse in scenarios requiring very high generation quality, where the overhead of the additional Dot model might not be justified. Furthermore, the paper does not fully clarify the conditions under which Morse significantly outperforms DPM-Solver, and when it might be comparable or even slightly slower due to the overhead of the Dot model.

### Questions
1, On page 6, you mention that Morse gets speed-ups around 1.0x compared with DPM solver on both DDPM and SDE with 100 LSDs, and they are not considered in the calculation of the average speed-ups. However, these are cases in practical scenarios. I wonder what the average speed-up is if they are considered.

2, In practice, how should we set the batch size and training iterations of the Dot Model?

### Soundness
3

### Presentation
2

### Contribution
2
