# CADS: Unleashing the Diversity of Diffusion Models through Condition-Annealed Sampling

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
While conditional diffusion models are known to have good coverage of the data distribution, they still face limitations in output diversity, particularly when sampled with a high classifier-free guidance scale for optimal image quality or when trained on small datasets. We attribute this problem to the role of the conditioning signal in inference and offer an improved sampling strategy for diffusion models that can increase generation diversity, especially at high guidance scales, with minimal loss of sample quality. Our sampling strategy anneals the conditioning signal by adding scheduled, monotonically decreasing Gaussian noise to the conditioning vector during inference to balance diversity and condition alignment. Our Condition-Annealed Diffusion Sampler (CADS) can be used with any pretrained model and sampling algorithm, and we show that it boosts the diversity of diffusion models in various conditional generation tasks. Further, using an existing pretrained diffusion model, CADS achieves a new state-of-the-art FID of 1.70 and 2.31 for class-conditional ImageNet generation  at 256$\times$256 and 512$\times$512 respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Although diffusion models are known for good mode coverage, the sample diversity of conditional diffusion models is still challenging when sampling at a high classifier-free guidance (CFG) scale. This work examines the conditional diffusion models and attributes this problem to how the conditional information should be mixed into the reverse diffusion process. 

To tackle this problem, it introduces an annealed sampling scheme for conditional generation, Conditional Annealed Diffusion Sampler (CADS). The core principle of CADS is to gradually increase the strength of conditional information in the reverse time diffusion process, letting the unconditional score model explore better data modes in the early stage (noisy region) and guiding the sampling converge to the conditional distribution using the conditional information in the final stage (data region).

This work conducted detailed experiments on class-conditional generation, pose-to-image generation, identity-conditioned face generation, and text-to-image generation. CADS consistently improves the sample diversity of baseline conditional diffusion models without retraining.

### Strengths
This is a good paper for conditional diffusion models. Its merits span the following aspects:

1. The proposed method is intuitive and does not require further finetuning on pretrained diffusion models. This allows for improving a wide range of models and samplers. The straightforward approach should be amenable to the broader audience of ICLR.
2. This work also provides a theoretical explanation for CADS. I found this explanation helpful. It should be added to the main paper using the extra granted page after acceptance.
3. Decent experimental results. The proposed sampler offers consistent improvements over the baseline diffusion models.
4. Detailed ablation studies. The ablation studies clearly show the influence of hyperparameters introduced in this sampler.
5. Writing clarity. This paper is well presented. The methods and experiment sections are well organized. Please move Appendix C. to the main article.

### Weaknesses
While the paper possesses several strengths, there is room for enhancement in articulating the motivation behind the methodology. The issue of sample diversity has been clearly defined, yet the rationale for the solution could benefit from a stronger motivation. Ideally, the approach should be presented as a natural derivation from the first principle, rather than retroactively justified through theoretical exposition.

This critique should not be seen as a detriment to the overall quality of the work. It is, in essence, a good paper for improving the conditional information in diffusion models.

### Questions
1. How does this work determine where to add noises to the conditional information? For example, CADS mostly injects noises into the embeddings. However, for the pose-to-image generation, this work adopts the noise injection to the pose image. Is there a guidance to choose the position for conditional noise injection? What if inject noises into the internal layers of the conditional information extractor? What if we also adopt the embeddings noise injection scheme for the face-to-image generation? In other words, how large can the influence of noise injection position be regarding different choices?
2. Notably, the experiments in this work utilize relatively large sampling steps (>= 100 NFEs). Will the proposed sampler deteriorate at a limited number of function evaluations? How does the conditional generation under CADS change along different sampler steps/NFEs?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Although conditional Diffusion Models have shown impressive performance in good coverage of the real data distribution, it is still limited in covering all the modes of the complex real distribution. In this paper, the authors are proposing a simple but effective sampling method of pretrained Diffusion Models for sampling more diverse results without additional time cost. Comprehensive experiments demonstrate the performance improvements of the proposed method.

### Strengths
- Good paper writing. Most parts of the paper is written understandable and reasonable. 
- Simple but effective method.
- Performance improvement (w.r.t. diversity) in Pose-to-image generation is impressive.
- Experiments are done comprehensively.
- The proposed method is theoretically analyzed and also proven to be effective by toy dataset experiment. (in Appendix)

### Weaknesses
1. “Adaptive” may not be an appropriate term. To my knowledge, ‘adaptive’ is used for a method of which parameters are dynamically changed depending on a given input value [1]. Here, $z_t$ is the input I was expecting rather than $t$ since $t$ is a value within a fixed time window.

2. There are a lot of sampling methods including DDIM [2] while only the original DDPM sampler is used to compare. Considering the fact that DDIM is a more widely used sampling method than the original DDPM sampling method, additional comparison with DDIM is needed.

### Questions
1. The definition of “diversity” is provided right under Section 3. 
What is the meaning of “random seed”? Does it mean the seed of the randomness (e.g., random.seed(1) in Python) or different $x_T$? To me, comparing samples from different seed is less clear than comparing different samples from the fixed seed.
For example, we have two $x_T$ sampled from the standard normal, i.e., $x_T^{(0)}$, $x_T^{(1)}$. Let’s say the regular sampling method is $f$ (e.g., DDPM), the proposed sampling method is $g$, and an arbitrary metric of the semantic distance between two images is $h$.
To me, the effect of the proposed method would be understandable if $h(f(x_T^{(0)}), f(x_T^{(1)})) < h(g(x_T^{(0)}), g(x_T^{(1)}))$ because we can consider that more modes in the real distribution are covered by the standard gaussian. However, if the noise samples $x_T^{(0)}$, $x_T^{(1)}$ are sampled from different random seed respectively, maybe it's a trivial issue, but it sounds somehow unclear to me. Further clarifications on this point are needed.

2. What is the justification for the higher IS of DDPM across most of $w_{\text{CFG}}$ in Fig. 5?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, conditional-annealed diffusion sampler (CADS) is proposed to address the limited diversity of diffusion models with a high classifier-free guidance scale or when trained on small datasets. Specifically, during early inference, the conditional signal is perturbed largely and then restored gradually  during late inference. The proposed method is simple and effective, amplifying the diversity of the generated samples. Besides, it requires minimal computational overhead and easy to implement. In addition, this paper provides extensive experiments on various tasks and ablation studies, validating the effectiveness and novelty of the proposed method.

### Strengths
+ The proposed method is simple but effective. It is easy to implement and validated with various experiments. Besides, it outperforms a naive and intuitive approach, termed as adaptive CFG, confirming its technical contributions.
+ To validate the proposed method, this paper provides extensive experiments on various tasks and ablation studies. Thus, it is a solid paper.

### Weaknesses
- In Appendix G, this paper provides sampling and evaluation details, shown in Table 12. The sampling hyperparameters is set deliberately for these experiments. To my knowledge, the training setting is mostly fixed for the same dataset even though it is an ablation study. But, as shown in Table 12, this rule is broken. For example, the setting of ImageNet 256 in Table 1 is different from the setting of ImageNet 256 in Table 6a. How do you set the sampling hyperparameters? It is unclear how the authors chose the specific values for parameters like τ1, ψ, and s, and whether these choices were based on a systematic search or heuristic tuning. This lack of clarity makes it difficult to assess the robustness of the method and to reproduce the results.
- As shown in Table 2, there is a missing comparison. The authors should provide the result of DiT-XL/2 with CADS($w_{CFG=1.5}$) or the result of DiT-XL/2 ($w_{CFG=2}$), alleviating the effects of different cfgs. The absence of these direct comparisons makes it challenging to isolate the specific benefits of the proposed CADS method from the effects of simply using different classifier-free guidance (CFG) scales. Without these comparisons, it's hard to determine if the improvements are due to the method itself or just the change in CFG scale.
- Empirically, with high guidance weights, the diffusion sampler can produce unnatural images and sometimes even diverges. There is a concern about the proposed method: is it easy to produce bad images? Specifically, how does the method behave when pushed to its limits with extremely high guidance scales? Does the gradual restoration of the conditional signal prevent the generation of artifacts or unnatural images, or does it simply delay the onset of these issues? The paper should provide more insights into the failure modes of the proposed method.

### Questions
- Empirically, with high guidance weights, the diffusion sampler can produce unnatural images and sometimes even diverges. There is a concern about the proposed method: is it easy to produce bad images?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
