# Think while You Generate: Discrete Diffusion with Planned Denoising

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
Discrete diffusion has achieved state-of-the-art performance, outperforming or approaching autoregressive models on standard benchmarks. In this work, we introduce \textit{Discrete Diffusion with Planned Denoising} (\ourmethod), a novel framework that separates the generation process into two models: a planner and a denoiser. At inference time, the planner selects which positions to denoise next by identifying the most corrupted positions in need of denoising, including both initially corrupted and those requiring additional refinement. This plan-and-denoise approach enables more efficient reconstruction during generation by iteratively identifying and denoising corruptions in the optimal order.
\ourmethod~outperforms traditional denoiser-only mask diffusion methods, achieving superior results on language modeling benchmarks such as \texttt{text8}, \texttt{OpenWebText}, and token-based generation on \texttt{ImageNet $256 \times 256$}. Notably, in language modeling, \ourmethod~significantly reduces the performance gap between diffusion-based and autoregressive methods in terms of generative perplexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces Discrete Diffusion with Planned Denoising (DDPD), unlike traditional discrete diffusion models which rely solely on a denoising network, DDPD separates the generation process into two distinct steps: planning and denoising. A planner network identifies the most corrupted positions within a sequence, prioritizing them for correction, while a denoiser network then predicts the correct value for these selected positions. This decomposition simplifies the learning process for each network and allows for a more efficient sampling algorithm. The paper proposes an adaptive sampling scheme based on the Gillespie algorithm, which dynamically adjusts the denoising step size based on the planner's assessment of the sequence's corruption level. This adaptive sampling, coupled with a time correction mechanism, allows DDPD to iteratively refine generated sequences by revisiting previously denoised positions if errors were made. The authors demonstrate experiments on text8, OpenWebText, and ImageNet that DDPD improves sample quality and diversity compared to existing discrete diffusion methods, particularly when inference compute budget is limited. Importantly, DDPD allows for leveraging pre-trained mask diffusion denoisers for uniform diffusion tasks, demonstrating improved performance by combining a strong mask denoiser with a separately trained planner.

### Strengths
- The core idea of decoupling the denoising process in discrete diffusion into separate planning and denoising stages is novel and very interesting. The adaptive sampling scheme based on the Gillespie algorithm, combined with the time correction mechanism, is also a creative contribution that addresses limitations of standard tau-leaping samplers.
- The paper provides a strong theoretical foundation for DDPD, grounding the training objectives in a clear derivation of the ELBO for discrete diffusion. The experimental results are comprehensive, comparing DDPD against strong baselines across diverse tasks including language modeling and image generation, showcasing its consistent performance gains. The ablation studies further strengthen the analysis by demonstrating the robustness of DDPD to imperfect training and the individual contributions of its proposed modifications.
- The paper is dense yet generally well-written and easy to follow.
- DDPD addresses a key challenge in discrete diffusion models: the efficient and effective use of the limited computational budget during sampling. By prioritizing denoising efforts through planning and allowing for self-correction, DDPD offers a promising path towards closing the performance gap between diffusion and autoregressive models in discrete generative modeling. The ability to leverage pre-trained mask diffusion denoisers further enhances the practical significance of DDPD, making it more accessible for researchers working with limited resources.

### Weaknesses
 - The paper acknowledges the increased computational cost of DDPD compared to denoiser-only methods due to the additional planner network and the sequential nature of the Gillespie sampler.
- The clarity can be further improved by adding more description of the training algorithm/procedure of the model confirugrations considered in Sec.6, given that there are many variations and the forward/training objectives/planner&denoiser training can vary. Specifically, the paper lacks details on how the planner and denoiser networks are trained in conjunction, or if they are trained separately, and what specific loss functions are used for each. The description of the adaptive sampling scheme also lacks some clarity, particularly regarding how the time correction mechanism is implemented and how it interacts with the Gillespie algorithm. 
- Lack of empirical NLL/perplexity comparisons on OpenWebText dataset with baseline discrete diffusion models. While this work presents results and analysis in terms of generative perplexity on OWT, this metric is easier to be inflated and sensitive to the precision used in categorical sampling. The more commonly used validation perplexity is not reported, as well as the zero shot perplexity on other datasets.
- Missing reference: The proposed adaptive time correction is interesting and well-motivated. Similar ideas/trick was proposed in [1] with asymmetric time intervals for a different context but not discussed as related work.

### Questions
- What are authors' thoughts on the connections of this work  to the state-dependent masking schedule proposed in MD4?

### Soundness
3

### Presentation
3

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
This paper introduces DDPO, a novel method that separates the generation process of discrete diffusion into two models: a planner and a denoiser. The authors unify the sampling processes of masked diffusion and uniform diffusion in a plan-and-denoise manner and present the advantages of this approach over previous works. Additionally, the authors provide the evidence lower bound (ELBO) for DDPO. Experiments in both text generation and image generation validate the effectiveness of DDPO.

### Strengths
1. This paper focuses on an interesting and important problem in the sampling processes of discrete diffusion models.
2. The writing is clear. The authors logically present the sampling process of DDPO and its advantages compared to previous works. And even with the extra planner, the training objective of DDPO still corresponds to the evidence lower bound.
3. The experiments are thorough, demonstrating the effectiveness of DDPO in both text generation and image generation tasks.

### Weaknesses
1. I suggest the authors use different notations for single-dimensional and multi-dimensional cases, e.g., x and **x**.

2. The authors claim that each sampling step of previous works predicts single-dimension transitions but not joint transitions of all dimensions. However, based on Proposition 3.1, the proposed DDPM also just predicts single-dimension transitions.

3. As presented in [1], the best FID score on ImageNet 256×256 is 1.97. Why are all the results in Table 2, both for the baseline and the proposed DDPO, significantly worse than 1.97? Is it because classifier-free guidance was not used? If so, why are there no results that include classifier-free guidance? This is my main concern; I will improve my score if a clear response is presented.

### Questions
1. The term $p_{1|t}(x_1=j|x_t, z_t=D)$ (in Line 192) indicates that once a dimension is identified as data by the planner (i.e., $z_t=D$), it will not be updated in this step, similar to masked diffusion. I am curious whether a dimension that is recognized as data by the planner early in the sampling process remains unchanged until the end of the sampling. Could the authors provide further theoretical and experimental insights on this issue?
2. DDPO employs a different training objective (i.e., Theorem 4.1). Will this new training objective lead to lower perplexity in language modeling?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper rethinks limitations of the conventional discrete diffusion generation schema that the generated tokens cannot be further corrected and the sampling process cannot be controlled. The authors propose to disentangle the single diffusion denoising process into two models: a planner and a denoiser. This planner is capable of selecting which positions to denoise next by identifying the most corrupted positions in need of denoising, including both initially corrupted and those requiring additional refinement. The plan-and-denoise method allows for adaptive control of the denoising order for efficient reconstruction during generation. The experimental results across text and images domains demonstrate the efficacy of the proposed model.

### Strengths
1. The motivation behind the study is sound, as discrete diffusion models struggle with correcting generated tokens and exhibit inflexibility during the sampling process.
2. The proposed model to disentangle the generation process with a planer and a denoiser is simple. 
3. The theoretical analysis appears robust and well-founded.

### Weaknesses
1. Additional experiments are necessary, such as applying the model to machine translation tasks for texts.
2. Although the planner model can adaptively organize the generation process, performance degradation becomes an issue as the number of sampling steps increases. Specifically, the mechanism by which the planner selects positions for denoising, especially in later stages of the process, is not sufficiently clear, and it is not clear how this impacts the overall performance as the number of steps increases.
3. The narrative is somewhat difficult to follow; I recommend that the authors clarify the main storyline.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper improves on the recent discrete diffusion generative models, with a focus on language modeling. This paper shows that the reverse (generative) rate can be decomposed in a planning and a denoising part. The proposed decomposition optionally allows training separate models for each part, which yields higher quality text samples, for a given inference budget. The decomposition also allows re-using a pre-trained masked discrete diffusion model to sample from a diffusion process with uniform stationary distribution. The training objective is theoretically sound as a decomposition of the ELBO.

### Strengths
- The presentation on Plan-and-Denoise decomposition is clear.
- The comparison of the sampling algorithm (Gillespie) and the comparison with tau-leaping is clear.
- Generally, Section 3 (method) is easy to follow and well-written.
- The note at the beginning of section 5 (experiment), that DDPD uses 2x the number of NFE versus regular absorbing diffusion is good to place there.
- While the main focus of the paper is on discrete diffusion for text generation, the authors have included experiments on images as well.

### Weaknesses
Overall, the method is sound, and the experiments are conducted fairly. The weaknesses noted here lie in the writing, which motivate my score. I have divided my comments into two groups: the first addresses more critical issues that I believe should be resolved, while the second includes suggestions that, while less urgent, could enhance the paper.


### More critical weaknesses
- Because of the description of the Gillespie's algorithm (Algorithm 1), it seems that each sampling iteration updates a single token at a time. But then, I'm confused on how the number of sampling steps can be lower than the number of tokens in Figure 2 (middle, DDPD). In particular, if you are generating sequences of 256 tokens on text8, how can you sample with 250 steps ? Indeed, there is a curve labeled DDPD-T250, which implies only 250 steps, so it feels like a piece of information might be missing here.

- Training Objective (lines 376 to the end of the page): The sentence on the 'coupling dynamics' and how it negatively affects backpropagation is unclear and should be rewritten.

- In Figure 2 (left), it appears that DFM-UNI, was only evaluated at a single temperature (shown by one dot) and others, like DDPD-MaskD, at just two temperatures (with only two dots). Could you confirm whether the models were indeed evaluated across all three temperature values? The missing points on the curve could be explained by missing experiments or dots that fall exactly on the same position for example. Therefore, I think there should be an explanation on this phenomenon.



- The meaning of the stochasticity parameter ($\eta$) on lines 431-432 (end of page 8, beginning of page 9) is not explained. While the context suggests that it comes from the DFM paper, a brief explanation of how it is used here is justified. I suggest adding a concise, high-level sentence about $\eta$, and if more detail is needed, directing readers to a section in the appendix.



### Less critical weaknesses
- Sampling with the Gillespie's algorithm requires sampling the holding time of the markov chain from an exponential distribution. However, for a reader that is not well-versed in simulation of markov chains, it might be unclear why the parameter of the exponential is chosen by summing over the rate for each dimension. I believe it would be good to include a paragraph on this, or at least a footnote to a precise chapter in a book such as the book of J.R. Norris on Markov Chains.

- For a reader short on time, it might be unclear what 'softmax selection' and 'proportional selection' refer to on line 476, as they haven’t been introduced previously. I assume these terms relate to the Gillespie sampler, where a dimension is chosen either by softmaxing the model output or dividing by the sum. To clarify, it would be helpful to label these explicitly. I would suggest mentioning "proportional selection" in bold in section 3.2, and mentioning that alternatively, one could perform "softmax selection" as well, again in section 3.2. This would make it easier for a reader that would search for "softmax selection"/"proportional selection" in the pdf.

- It would be helpful to include a timing comparison between DDPD, the diffusion baselines and the AR model. Indeed, a comparison of the computational resources vs generation quality is relevant for many applications.

### Questions
- Did you experience convergence issues during sampling? More precisely, what happens if you do not limit the maximal number of planning+denoising steps, but iterate until the planning module is sufficiently confident (e.g. assigns a probability at least 0.95, or 0.99) for all the tokens? 
- Related to the above, say you are using a confidence threshold of 0.95 to decide on the convergence. What is the mean/std of the number of sampling (planning + denoising) steps that you observe when averaging over 10'000 examples?
- Do the authors have an explanation or hypothesis on why adding a planner seem detrimental to performance for images, but not for text (table 2 with logits scaling)?
- Have the authors experimented with other types of data already such as DNA sequences? I am curious about such experiments since the setup is relatively different (smaller vocabulary and longer sequences).

### Soundness
3

### Presentation
2

### Contribution
3
