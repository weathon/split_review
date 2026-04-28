# Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning

- Decision: Accept
- Scores: 6, 6, 5, 5

## Abstract
Diffusion Policies have become widely used in Imitation Learning, offering several appealing properties, such as generating multimodal and discontinuous behavior.
As models are becoming larger to capture more complex capabilities, their computational demands increase, as shown by recent scaling laws. 
Therefore, continuing with the current architectures will present a computational roadblock. 
To address this gap, we propose Mixture-of-Denoising Experts (MoDE) as a novel policy for Imitation Learning.
MoDE surpasses current state-of-the-art Transformer-based Diffusion Policies while enabling parameter-efficient scaling through sparse experts and noise-conditioned routing, reducing both active parameters by 40\% and inference costs by 80\% via expert caching.
Our architecture combines this efficient scaling with noise-conditioned self-attention mechanism, enabling more effective denoising across different noise levels. 
MoDE achieves state-of-the-art performance across 134 tasks in four established imitation learning benchmarks (CALVIN and LIBERO).
Notably, by pretraining MoDE on diverse robotics data, we achieve a new state-of-the-art result of 3.98 on CALVIN and 0.95 on LIBERO-90. It surpasses both CNN-based and Transformer Diffusion Policies by an average of $20\%$ in all settings, while using 80\% fewer FLOPs and fewer active parameters.
Furthermore, we conduct comprehensive ablations on MoDE's components, providing insights for designing efficient and scalable Transformer architectures for Diffusion Policies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel policy architecture for imitation learning based on sparse Mixture of Experts and EDM diffusion policies. The architecture is shown to improve performance in most cases across four domains (two from LIBERO, and two from CALVIN benchmarks), while jointly improving efficiency by reducing the number of active parameters required to perform inference and sample from the policy. The main architectural contributions are (1) a noise-conditioned routing mechanism that selects experts based on the timestep and noise level of the diffusion process, and (2) a noise-conditioned attention mechanism.

The proposed method, MoDE, is the first policy to achieve a `>90%` success rate in the LIBERO-10 benchmark, and performs competitively with models pre-trained on significantly more data (GR-1, RoboFlamingo), despite training only on data available from target benchmarks. Thorough ablations showcase the importance of each of the two main architectural contributions, and explore the space of key hyper-parameters, including the number of experts, and the extent of router load balancing regularization.

While the idea of sparse routing layers for transformers is not new, and has been shown to lead to comparable gains in scaling + inference efficiency in pure language modeling, this paper takes the important step of applying these techniques to Diffusion-based policies in decision-making tasks.

### Strengths
## Originality:

The idea of sparse routing layers is not new, as mentioned in my summary. This technique is generally expected to produce gains in inference efficiency by reducing the number of active parameters, and has been used in LLM with Mixtral [1], and in Diffusion transformers in [2], showing similar efficiency gains as this paper shows for imitation learning tasks. The main originality in this paper comes from the architectural contributions, including the noise-conditioned routing mechanism, and noise-conditioned attention mechanism. In previous work in [2], the sparse MoE router is conditioned on previous layer hidden states, whereas in this paper the sparse MoE router is conditioned on just the noise token. This design choice has the potential to simplify the router’s learning task, acting as an implicit regularization, and causing experts to specialize to different denoising steps, rather than different tokens.

[1] Mixtral of Experts, Albert Q. Jiang et al. 2024

[2] Scaling Diffusion Transformers to 16 Billion Parameters, Zhengcong Fei et al. 2024

To my knowledge, these architecture contributions are original, and their great performance across four benchmark domains highlights their value for efficient learning.

---

## Quality:

The paper is organized well, concepts are introduced and explained thoroughly, and experiments are chosen to highlight the improvements in policy performance, reduced inference cost, and the role that each component of the proposed method has to overall performance. Experiments are thorough, and appropriate baselines are chosen, including the dense version of the proposed method, previous diffusion-based policies, and previous models pretrained at scale on internet data (which would be expected to have an advantage to the larger source of data). Its impressive that on CALVIN ABC→D tasks, MoDE performs comparable to GR-1, despite lacking a large-scale pre-training step.

A minor quality issue with Table 1: performance is reported as a percent without a confidence interval. The experimental quality is generally good in this paper, but could be further improved by reporting confidence intervals for the results, so that readers can judge how statistically significant the improvements are.

Another manner by which to improve the paper would be to include more examples in “HOW DOES THE MODEL DISTRIBUTE THE TOKENS TO DIFFERENT EXPERTS?” In particular, for different load balancing weights, how does this impact the observed usage of the experts? In addition, results in Figure “(b) Scaling performance of MoDE” (the figure number seems to be missing here) show that performance saturates at 4 experts. Its unclear from the results if this is just an artifact of the limited training data available in LIBERO and CALVIN domains, and it would strengthen results to explain this behavior, and to include more examples of what happens to the experts' usage as the number of experts increases.

A similar analysis can be done to study the impact of the top k routing parameter.

---

## Clarity:

Writing is clear, organized well, and easy to follow. Design choices for the main contributions are explained carefully, and clearly. Questions that remained after reading the main text, such as hyperparameters, benchmark settings, are presented in the supplementary materials.

---

## Significance:

The main contributions, while performant and efficient, are not particularly surprising. Previous works such as [1] and [2] have shown the viability of sparse Mixture of Experts for improving performance and inference efficiency in other domains, and [2] in particular has shown this for Diffusion transformers. What’s significant about this paper is the empirical study of what type of sparse MoE mechanism works best for Imitation Learning in robotics, where data is often much smaller than for pure text and image generation. Getting MoE to perform well in this data-limited regime is challenging, and findings in this paper, such as the noise-conditioned routing that pre-computes routing paths upfront, improve the viability of MoE in this setting.

### Weaknesses
Weaknesses have been woven into the strengths section, see above.

### Questions
Questions have been woven into the strengths section, see above.

### Soundness
4

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
The paper proposes to implement the architecture for a deep imitation learning policy model by a Mixture of Denoising Experts (MoDE). It enables parameter efficient scaling and reduces the inference cost. The paper introduces a routing scheme that conditions the expert selection on the current noise level. The experiments show that the proposed MoDE model performs better than CNN and Transformer-based baselines.

### Strengths
- The idea is straightforward and the writing is easy to follow.
- The experiments show that the proposed idea performs better than the baselines.
- The experiments are thorough, exploring different aspects of performance, speed, routing strategy, and expert utilization.

### Weaknesses
- I think the novelty of the paper is a bit limited. I am not expert in the imitation learning literature, but the paper seems to be mostly applying mixture of experts idea (that is already been in the LLMs literature) to the diffusion-based imitation learning setup. For instance, using the top-k router and load balancing regularizations are not new contributions.
- The improvements on the LIBERO-90 and CALVIN datasets are marginal.

### Questions
- Does the model generate all of the sequential actions' decisions at the same time? For instance, in the ABCD->D experiment, it involves interactions each consisting of 64 timesteps and 34 diverse tasks. Does the model determine the 64 timesteps' actions at the same time after denoising in Fig. 1?

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
4

### Summary
To address the issue of models becoming increasingly large and difficult to capture more complex functions, along with their rising computational demands, this paper proposes a Mixture of Denoising Experts (MoDE) as a new strategy for imitation learning. MoDE is based on a diffusion strategy using Transformers and achieves parameter-efficient scaling, significantly reducing inference costs. To achieve this, MoDE employs sparse experts combined with a novel routing strategy that selects experts based on the current noise level of the denoising process. This is further enhanced by a noise-regulated self-attention mechanism. MoDE achieves state-of-the-art performance across 134 tasks in four established imitation learning benchmarks (Calvin and LIBERO).

### Strengths
1.	The structure of the paper is logical, and the text is clearly articulated and easy to read.

2.	The layout of the tables in the article is reasonable, and the overall formatting of the paper is quite aesthetically pleasing.

3.The paper provides rich experimental results with a sufficient number of figures and tables.

### Weaknesses
1、The innovation of this paper lies solely in the introduction of a Mixture-of-Experts Diffusion Policy, merely combining MOE with diffusion methods without sufficiently demonstrating the novelty of their approach. Additionally, the overall workload appears to be insufficient.

2、In Figure 1, the authors propose a new router strategy, but the figure does not clearly illustrate how this strategy selects different experts, failing to convey the core idea of the paper. Furthermore, the framework diagram is overly simplified and lacks sufficient depth.

3、The methods section of the paper is too brief, and much of the content is drawn from existing research, with the authors not highlighting their contributions effectively.

4、In the experimental section, the authors do not provide a comparison of FLOPs and inference times with other baseline methods, which may lead to unfair comparisons. Moreover, the experimental results for ABC→D in Table 1 are worse than the baseline methods, and the explanations in the paper are not sufficiently convincing.

### Questions
1、Can you elaborate on the specific innovations introduced by your Mixture-of-Experts Diffusion Policy that differentiate it from existing methods in the literature? What novel insights does your approach provide beyond the combination of MOE and diffusion methods?
2、In Figure 1, how does your proposed router strategy select different experts based on the current noise level? Could you provide additional details or examples to clarify this process and better illustrate its implementation?
3、The methods section appears to be brief and heavily based on existing research. Can you elaborate on the unique contributions of your work and how they extend beyond the existing literature? What specific methodologies have you developed or modified?
4、Regarding the experimental results for ABC→D in Table 1, which are lower than those of the baseline methods, could you provide further justification or insight into why this occurred? What factors might have influenced these results, and how should they be interpreted in the context of your overall findings?

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
3

### Summary
This paper introduces a MOE diffusion model for embodied AI, which applies a noise-based router for policy diffusion. This MOE structure reduces the active parameters and FLOPs, and also achieves better performance in CALVIN challenges.

### Strengths
1. Authors claim that the proposed method increases the performance with fewer parameters and FLOPs.
2. Good writing. This paper is easy to follow.

### Weaknesses
1. This paper mainly measures the computational and storage costs of diffusion models with FLOPs and parameters. However, latency (response time for one input instance) and memory footprint are more important metrics. I highly recommend authors report them since the reduction in FLOPs and parameters does not always bring real benefits. Besides, I'm really curious about the computation costs of diffusion models in the overall pipeline of embodied AI, since it seems that the diffusion model only contains 8 layers, which are much smaller than the perception model. This will make compression and acceleration for the diffusion model not important for embodied AI.
2. MOE may bring additional parameters. How do the overall parameters (instead of active parameters) in Table 1.
3. Some typos. 285, wrong usage for quotes. You should use `` instead.
4. Table 1 shows that MoDe works better than other methods without pertaining, which is good. However, it can be better to report MoDe with pretraining for a fail comparison with GR-1.
5. Section 3.3 seems to be a direct adaptation of the classific MOE method. Could you provide a concrete comparison between the MOE utilized in this work and previous works?

### Questions
Please refer to the weakness. My major concern is w1-2 &5. I would like to increase my rating  if authors address my concern, especially w5.

### Soundness
3

### Presentation
3

### Contribution
3
