# T-Stitch: Accelerating Sampling in Pre-Trained Diffusion Models with Trajectory Stitching

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Sampling from diffusion probabilistic models (DPMs) is often expensive for high-quality image generation and typically requires many steps with a large model. 
In this paper, we introduce sampling Trajectory Stitching (\textbf{T-Stitch}), a simple yet efficient technique to improve the sampling efficiency with little or no generation degradation. Instead of solely using a large DPM for the entire sampling trajectory, T-Stitch first leverages a smaller DPM in the initial steps as a cheap drop-in replacement of the larger DPM and switches to the larger DPM at a later stage. Our key insight is that different diffusion models learn similar encodings under the same training data distribution and smaller models are capable of generating good global structures in the early steps. Extensive experiments demonstrate that T-Stitch is training-free, generally applicable for different architectures, and complements most existing fast sampling techniques with flexible speed and quality trade-offs. On DiT-XL, for example, 40\% of the early timesteps can be safely replaced with a 10x faster DiT-S without performance drop on class-conditional ImageNet generation. We further show that our method can also be used as a drop-in technique to not only accelerate the popular pretrained stable diffusion (SD) models but also improve the prompt alignment of stylized SD models from the public model zoo.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces T-Stitch, a training-free approach to accelerate sampling in diffusion models by strategically utilizing different-sized models across the denoising trajectory. The key insight is that small and large models trained on the same data distribution learn similar encodings, particularly in early steps where low-frequency components dominate. By leveraging this property, T-Stitch uses smaller models for early steps (global structure) and larger models for later steps (fine details), achieving significant speedup without quality degradation. The method demonstrates broad applicability across various architectures (DiT, U-Net, Stable Diffusion) and shows interesting benefits for stylized models' prompt alignment. Extensive experiments validate the effectiveness across different settings, samplers, and guidance scales.

### Strengths
### Novel & Foundational Insight
  - Deep understanding of diffusion models' behavior across timesteps
  - Thorough empirical validation of latent space similarity between models
  - Clear frequency analysis supporting the theoretical foundation
  - Novel perspective on leveraging model size differences temporally

### Practicality
- Training-free nature enables immediate deployment
- Compatible with existing acceleration techniques
- Works across various architectures and model families
- Clear implementation guidelines and deployment considerations


### Comprehensive Empirical Validation
- Extensive experiments across multiple architectures
- Thorough ablation studies covering various aspects
- Clear demonstration of speedup-quality tradeoffs


### Broader Impact & Applications
- Unexpected benefits in prompt alignment for stylized models
- Natural interpolation between style and content
- Practical applications in Stable Diffusion ecosystem
- Potential implications for efficient model deployment

### Weaknesses
### Critical Absence of Limitations Analysis
- Paper lacks a dedicated section for discussing limitations
- No systematic analysis of failure cases
- Insufficient discussion of edge cases and potential risks
- Missing critical self-reflection on method boundaries

### Theoretical Gaps
- No mathematical justification for the 40% threshold
- Lack of theoretical guarantees for quality preservation
- Missing analysis of optimal model size ratios
- Incomplete understanding of feature compatibility requirements

### Architectural Considerations
- Limited analysis of cross-architecture compatibility
- No clear guidelines for multi-model (>2) scenarios
- Insufficient investigation of feature space alignment
- Missing discussion of architecture-specific optimization

### Practical Implementation Challenges
- Memory overhead management not thoroughly addressed
- Pipeline complexity implications understated
- Limited guidance for scenarios without suitable small models
- Deployment considerations in resource-constrained environments lacking


### +)
- The absence of a dedicated limitations section limits the paper's completeness

### Questions
- How does the method perform when architectural differences between small and large models are more significant? Are there specific architectural compatibility requirements?
- The improved prompt alignment for stylized models is intriguing. Could you provide more analysis of why this occurs and how generally applicable this finding is?
- What are the primary failure modes of T-Stitch? Are there specific scenarios where the method consistently underperforms?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a method to accelerate sampling in diffusion models by using a sequence of two denoising networks, a smaller one followed by larger one (instead of using the same network for all sampling steps as is traditionally done). In their experiments, they show their method can lead to meaningful computational savings at little to no cost to the quality of generated images.

### Strengths
- Their main idea of leveraging model of various sizes throughout the diffusion sampling process is simple, yet it is shown to be effective. The simplicity is an added benefit in my opinion, as it makes the method more reproducible and more likely to be adopted
- I also believe their idea to be novel (though I am not fully up to date with the diffusion literature due to its high pace)
-  The experiments are very comprehensive, they try out their trajectory-stitching approach on various backbone architectures (DiT, UNet), with various samplers, for unconditional/conditional cases etc.
- Also, I like how instead of proposing yet another new efficient diffusion model (and thus contributing to the model zoo), the authors find a smart way to combine/reuse the existing models via their trajectory-stitching approach

### Weaknesses
 - I think the writing can be improved. For camera-ready it would make sense to move the background/preliminaries to the main text and perhaps to move some of the experiments to the appendix. Also I find Section 3 quite chaotic (it talks about too many different things, from motivation to model design and connection to the other efficiency techniques like speculative decoding)
- It is not clear how to select the switching point/threshold between the small and large model (r1). While I understand that by varying it you can get a Pareto frontier, however, that still requires running/evaluating a large number of candidate thresholds.

### Questions
- Your idea reminds me a bit of works on early-exit diffusion models [1,2] where the depth on the denoising network is made adaptive based on the estimated difficulty of the sampling step. Could be interesting to draw further parallels between early-exit and your stitching approach


[1] [AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation](https://arxiv.org/abs/2309.17074)

[2] [DuoDiff: Accelerating Diffusion Models with a Dual-Backbone Approach](https://arxiv.org/abs/2410.09633)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new method to speed up the sampling efficiency of diffusion models. By using smaller models for the initial denoising steps and larger models in later stages, this approach greatly boosts sampling speed while keeping quality on par. Notably, this method is distinct from existing training-based or training-free techniques aimed at improving sampling efficiency. The authors demonstrate the effectiveness of their approach through extensive experiments, highlighting improved quality-efficiency trade-offs with a clear Pareto frontier.

### Strengths
Overall this is a well-written paper which presents a simple but effective approach for accelerating sampling speed of large diffusion models. The authors convey their ideas clearly and support their approach through extensive experiments. I guess the key significance of this stitching approach is that it is orthogonal to other techniques, like model distillation or improved ODE solvers, allowing it to be easily combined with other methods to further reduce inference time.

### Weaknesses
Even if we ignore the inference time needed for running the small models, the time to generate samples of comparable quality can still be reduced by 30-40% at most. It is hard to say this method is a groundbreaking technique for improving sampling efficiency in diffusion models. While the paper presents a comparison of the Pareto frontiers between T-stitching and M-stitching, it might be more insightful to compare it with methods like progressive distillation, which can be much faster and does not need store multiple models.

Additionally, the approach uses models of different scales along the same denoising trajectory, which necessitates that both the small and large models predict score functions in the same latent space. This requirement may limit its applicability.

The work primarily relies on the observation of the alignment of noise predictions between models of different scales during the early stages of the denoising process (Fig. 3). While this is an intriguing phenomenon, the paper does not provide sufficient explanation for why this occurs. Furthermore, the magnitude of the latent vectors is also important. Does the $L^2$-distance exhibit a similar pattern as shown in Fig. 3?

I believe that the requirement for a shared latent space is a strict condition for this method. It is unclear whether this method is also robust for models trained with different configurations, such as varying noise schedules (like variance-preserving versus cosine) and different diffusion steps (e.g., T=100 versus T=500).

Is it possible that small models trained only over larger T steps (for example, $t \sim [70, 100]$ with a total $T=100$) yield better results?

### Questions
The work primarily relies on the observation of the alignment of noise predictions between models of different scales during the early stages of the denoising process (Fig. 3). While this is an intriguing phenomenon, the paper does not provide sufficient explanation for why this occurs. Furthermore, the magnitude of the latent vectors is also important. Does the $L^2$-distance exhibit a similar pattern as shown in Fig. 3?

I believe that the requirement for a shared latent space is a strict condition for this method. It is unclear whether this method is also robust for models trained with different configurations, such as varying noise schedules (like variance-preserving versus cosine) and different diffusion steps (e.g., T=100 versus T=500).

Is it possible that small models trained only over larger T steps (for example, $t \sim [70, 100]$ with a total $T=100$) yield better results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a training-free acceleration technique named T-Stitch for diffusion models. The core spirit of the approach is to employ a compact model for early timesteps and a more substantial model for later stages. The authors have provided empirical evidence that model performance remains unaffected even when the lighter model is employed for 40% of the initial steps. While the proposed method is simple and efficacious, parts of its evaluation appear to rely heavily on empirical evidence, and in my opinion, falls to a typical trap of this type of papers of not including further limit studies.

### Strengths
Generally, I believe this is a good paper backed by solid experimentation. It has extensive comparative analysis involving various timesteps and samplers, and also compares itself against other methods, including those that are training-based, training-free, and search-based.

The paper is also well written and clearly motivated.

### Weaknesses
In my view, theoretical insights and empirical studies hold equal value; the simplicity of an idea does not de-value from its merit if it is proven effective, especially if it is a topic like Efficient AI. However, my primary issue with such papers lies in my preference for a clear explanation of the method's limitations, also through sets of experiments.

First, the authors of the T-Stitch paper state that 40% is an appropriate cutoff for switching models, a decision purely grounded in empirical evidence. This raises the question of how well-founded this choice is. If I were to apply this switching method to a different set of diffusion pairs of the models, would the 40% value still be relevant? Intuitively, the cutoff point likely hinges on the performance disparity between the more and less powerful models. From that perspective, if you put the model difference (Strong model FLOPs - Weak Model FLOPs) on x-axis, and the best cut-off point on y-axis, do you simply expect a flat line at 40% cut-off?

Second, although the authors did claim that the method can go beyond pari-wise, and have demonstrated how switching (I would maybe actually call this switching rather than stitching) can happen across 3 models, it is unclear about the limitation on this. Clearly the increased number of models would complicate the decision making on where to switch, and potentially make this method becomes a search-based one. More importantly, there must exhibits certain limitation on this switching especially when one has limited diffusion time steps. When you have N models to stitch/switch with M time steps. When N becomes larger or M becomes smaller, the return of this optimization should inevitably becomes diminishing.  

Also something minor: Figure 5: the bottom of the images are cropped.

### Questions
Please see the two points about limitations I have raised in my Weakness section

### Soundness
3

### Presentation
4

### Contribution
3
