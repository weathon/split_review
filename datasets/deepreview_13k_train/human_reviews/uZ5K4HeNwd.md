# Beyond Auto-Regression: Fast LLMs via Self-Distillation Through Time

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Autoregressive (AR) Large Language Models (LLMs) have demonstrated significant success across numerous tasks. However, the AR modeling paradigm presents certain limitations; for instance, contemporary autoregressive LLMs are trained to generate one token at a time, which can result in noticeable latency. Recent advances have indicated that search and repeated sampling can enhance performance in various applications, such as theorem proving, code generation, and alignment, by utilizing greater computational resources during inference. In this study, we demonstrate that diffusion language models are capable of generating at least 32 tokens simultaneously, while exceeding the performance of AR models in text quality and on the LAMBADA natural language understanding benchmark. This outcome is achieved through a novel distillation method for discrete diffusion models, which reduces the number of inference steps by a factor of 32-64. Practically, our models, even without caching, can generate tokens at a rate that is up to 8 times faster than AR models employing KV caching, and we anticipate further improvements with the inclusion of caching. Moreover, we demonstrate the efficacy of our approach for diffusion language models with up to 860M parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel distillation method for discrete diffusion models: SDTT (Self distillation through time), which significantly reduces inference steps, leading to a generation process that is up to 8 times faster than AR models with KV-caching. They ablate with different distillation alternatives. They evaluate the effectiveness of MDLMs with model sizes up to 860M parameters under unconditional generation, conditional generation, and downstream LAMBADA benchmark.

### Strengths
- Improved Generation Quality and Speed: The paper achieves remarkable improvements in both generation quality and efficiency, with fewer decoding steps required. This is a significant advancement for the field.
- Clarity of Writing: The paper is well-written, with clear explanations of the methodologies and results, making it accessible to a wide audience.

### Weaknesses
 - Insufficient Validation on Generation Speed: While generation speed is a key advantage highlighted in the paper, the validation seems inadequate in Section 4.4 and Figure 2b. The experimental settings lack clarity. For instance, it's not clear if the reported 8x speedup is based on 32 steps, 1.3B, and a batch size of 8. Additionally, the paper does not clarify whether the quality (generation perplexity) is comparable between 1.3B DLM and AR models.
- Impact of Batch Size and Model Size: There is a need for further validation on how batch size affects memory usage and decoding speed for both diffusion and AR models. Similarly, the paper should explore how model size impacts generation speed.
- Effect of Flash-Attention: The paper does not address whether the advantage of DLMs over AR models persists when flash-attention is employed.
- More downstream tasks such as math reasoning are encouraged.

### Questions
- Does the self-distillation process affect the generation diversity? There is an ongoing discussion regarding potential model collapse when AI models are trained on recursively generated data, which may be relevant here.
- How was the decision made to set the number of rounds to 7? 
- The paper focuses on discrete diffusion models and generation speed for reasoning tasks but fails to cite these related works: 
(1) A Reparameterized Discrete Diffusion Model for Text Generation;
(2) Diffusion of Thoughts: Chain-of-Thought Reasoning in Diffusion Language Models.

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
This paper proposes self-distillation through time to speed up sampling from text diffusion models. The method trains student reconstruction models to predict ahead in time, given a teacher model. This method can be applied iteratively, using students to train even coarser students. Experiments demonstrate that the method results in achieving a given generative perplexity at fewer function evaluations.

### Strengths
The method is simple and intuitive. The results for generative perplexity and number of function evaluations look promising. However, wall-clock time / latency is most important.

### Weaknesses
The primary weakness is presentation and writing. The abstract claims that the generates tokens 8x faster than an AR baseline with KV-caching. This must be presented in a figure as early as possible (see comment 10).

1. Notation nit: In the discrete case, with fully-factored reverse model, $p(z_s \mid z_t) = \sum_x p(z_s \mid x)p(x \mid z_t)$ can be computed efficiently (see D3PM) and (also in the discrete, fully-factored case) $x_\theta(z_t, t) = p(x \mid z_t)$.
2. Notation nit: Equation 3 can be written as $\log p(x \mid z_t)$, rather than writing a probability as the inner-product of the mean-parameters with a one-hot vector.
3. Writing: Please move iterated SDTT to the methods section and formally describe it with one equation and a few sentences. Something like a telescoping sum of divergences. Be sure to introduce terminology like "rounds" formally and do not use both "times" and "rounds" in order to minimize terms.
4. Writing: Are figure 2 and 3 referred to in the body of the text?
5. Writing: Notation such as `dt` should be formally defined in the methods section. Could you explain what `dt` is? Is it $\Delta$? Could you also define $\Delta$? In MDLM, $\Delta$ refers to a simplex rather than time-step or increment.
6. Writing: In general, "steps" can be ambiguous and can refer to sampling steps, decoding steps, or training steps. Please be clear which one is being used, for example in the beginning of section 4.1 it should be training steps. Also, likely sampling = decoding steps.
7. Question: In this setting, is MSE roughly chi-square divergence? It's surprising that using MSE results in better generative perplexity. Any thoughts on why?
8. Experiment: Could you also report the conditional likelihoods / perplexity alongside the MAUVE scores for conditional generation? It's not completely clear what MAUVE measures [1].
9. Question: It's very interesting that distilling more than 2 steps at a time, as well as more training steps per round hurt the student (Figure 11).

10: Figure request and section 4.4: In section 4.4, the following claim is made: "We successfully reproduce the results of Deschenaux & Gulcehre (2024), which showed a 4x improvement when sampling with 32 steps, only this time, we retain the text quality because of SDTT." Please add a figure that clearly shows this. A figure with latency vs generative perplexity is extremely important for this paper. Additionally, Section 4.4 is likely the most important experimental section, and should be the first result discussed.

### Questions
1. Notation nit: In the discrete case, with fully-factored reverse model, $p(z_s \mid z_t) = \sum_x p(z_s \mid x)p(x \mid z_t)$ can be computed efficiently (see D3PM) and (also in the discrete, fully-factored case) $x_\theta(z_t, t) = p(x \mid z_t)$.
2. Notation nit: Equation 3 can be written as $\log p(x \mid z_t)$, rather than writing a probability as the inner-product of the mean-parameters with a one-hot vector.
3. Writing: Please move iterated SDTT to the methods section and formally describe it with one equation and a few sentences. Something like a telescoping sum of divergences. Be sure to introduce terminology like "rounds" formally and do not use both "times" and "rounds" in order to minimize terms.
4. Writing: Are figure 2 and 3 referred to in the body of the text?
5. Writing: Notation such as `dt` should be formally defined in the methods section. Could you explain what `dt` is? Is it $\Delta$? Could you also define $\Delta$? In MDLM, $\Delta$ refers to a simplex rather than time-step or increment.
6. Writing: In general, "steps" can be ambiguous and can refer to sampling steps, decoding steps, or training steps. Please be clear which one is being used, for example in the beginning of section 4.1 it should be training steps. Also, likely sampling = decoding steps.
7. Question: In this setting, is MSE roughly chi-square divergence? It's surprising that using MSE results in better generative perplexity. Any thoughts on why?
8. Experiment: Could you also report the conditional likelihoods / perplexity alongside the MAUVE scores for conditional generation? It's not completely clear what MAUVE measures [1].
9. Question: It's very interesting that distilling more than 2 steps at a time, as well as more training steps per round hurt the student (Figure 11). 

10: Figure request and section 4.4: In section 4.4, the following claim is made: "We successfully reproduce the results of Deschenaux & Gulcehre (2024), which showed a 4x improvement when sampling with 32 steps, only this time, we retain the text quality because of SDTT." Please add a figure that clearly shows this. A figure with latency vs generative perplexity is extremely important for this paper. Additionally, Section 4.4 is likely the most important experimental section, and should be the first result discussed.

[1] Pimentel, Tiago, Clara Meister and Ryan Cotterell. “On the Usefulness of Embeddings, Clusters and Strings for Text Generator Evaluation.” ICLR 2023.

### Soundness
3

### Presentation
2

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
In this work, the authors propose Self-Distillation Through Time (SDTT), a training strategy for decreasing the number of sampling steps required during discrete text diffusion. Given a pretrained discrete diffusion model, the method works by using the token distribution of the base model at later denoising timesteps as the target for a student network at an early denoising timestep. The student model is initialized to be the same as the base diffusion model. The authors demonstrate that through multiple rounds of SDTT they can sample with 32x fewer steps while maintaining quality. They also compare to standard auto-regressive decoding, finding that they can achieve the same perplexity with an 8x reduction in wall clock time during generation.

### Strengths
* The SDTT methodology appears to significantly improve the decoding speed of discrete diffusion models, and the authors provide evidence of this over a large set of experiments. Compressing discrete diffusion sampling to this degree seems like an important contribution that will be used by future text diffusion works.

* The paper conducts a thorough set of ablations justifying key design choices such as the particular divergence measure and the number of steps compressed per SDTT round.

* The authors demonstrate that text diffusion models can scale up to 860 million parameters and promise to release said model which is a valuable contribution for future research on text-based diffusion models.

### Weaknesses
 * Performing multiple rounds of SDTT seems integral to the empirical success the paper has but the detail that SDTT is performed over multiple rounds seems to be introduced in the experiments section. It would help the clarity of the paper if this technique was introduced as a core part of the algorithm.

* As mentioned by the authors, previous work has explored distilling multiple diffusion steps in the continuous diffusion setting. While the technique in SDTT has slight differences and is applied to the discrete diffusion setting, its similarity to prior work in continuous diffusion, particularly the idea of distilling multiple steps into a single step, may limit the novelty of SDTT. The core idea of using a student network to mimic the output of a teacher network at a later timestep is conceptually similar to existing distillation techniques, even if the specific application to discrete diffusion has not been thoroughly explored.


### Questions
* It would be interesting to look at why more SDTT rounds work but distilling a larger number of steps in a single round doesn’t. Did you investigate progressively growing the distillation step size throughout training?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores progressive distillation, a technique commonly used in continuous image diffusion models, in the context of discrete diffusion language models. Starting with a trained discrete diffusion model that might take many denoising steps to generate a text sequence, the proposed framework iteratively distills the slower teacher into a faster student diffusion model, effectively halving the number of sampling steps in each distillation iteration. The distillation process involves collecting predicted logits for all tokens from the teacher model and then training the student diffusion model to match the teacher’s logit predictions according to a defined divergence measure. This self-distillation yields a significantly faster diffusion model, capable of generating text with up to 32 times fewer sampling steps, all while improving generation quality.

### Strengths
- This work makes a valuable contribution by extending progressive distillation techniques to diffusion language models, achieving much faster generation with improved generation quality.
- This work also includes extensive ablation experiments that carefully examine each design component of the distillation framework, demonstrating the solid empirical performance of SDTT. These results offer useful insights for future advancements in discrete diffusion language models.

### Weaknesses
 - The paper appears to be written hastily and lacks clarity and organization. Beyond typos and formatting issues (examples below), key concepts are introduced ambiguously. For instance, only in the experiments section is it clarified that SDTT consists of multiple distillation rounds rather than a direct distillation; and the progressive nature of SDTT is not immediately evident in the main text or Algorithms 1 and 2, becoming clear only in experimental results. In addition, the number of distillation iterations can only be inferred indirectly from `dt`, which is quite unintuitive and causes more confusion. It would greatly improve understanding by emphasizing the progressive formulation early in the methods section, and annotating the number of distillation rounds explicitly instead of relying on `dt=1/k`.
- Inconsistent use of x-axis labels in figures also adds to the confusion. Some figures, such as Figures 1(a), 1(b), 8, 9(b), 15(a), and 15(b), use “sampling step size” as the x-axis (e.g., `1/512`) while others use the “number of sampling steps” (e.g., 1024). If these two metrics are equivalent to each other (e.g., 512 sampling steps correspond to a sampling step size of 1/512), unifying the x-axis to the “number of sampling steps” across all figures would greatly enhance clarity; and also prevent confusion between terms like “sampling step size = 1/512” and “dt=1/512”, which, despite similar notation, have different meanings. Furthermore, the lack of a clear explanation of the relationship between the sampling step size and the number of steps in the main text makes it difficult to understand the practical implications of the results.
- In Figure 2(a), the relationship between the figure and various distillation rounds is ambiguous. If I understand correctly, “Round 1” and “Round 2” in the figure actually denote different denoising steps within a single distillation round, rather than separate distillation rounds. The use of the term “round” in this context is particularly confusing since it is also used to describe the iterative distillation process, and this ambiguity should be addressed.
- The concept of progressive self-distillation is not new within diffusion models. The proposed framework SDTT largely resembles progressive distillation [1] with modifications such as the construction of targets and distillation objectives, both of which are straightforward following the formulation of discrete diffusion. While SDTT adapts distillation techniques to a different application and presents strong results, this paper does not sufficiently discuss its related work [1] throughout the introduction and the methods section, making it difficult to evaluate how SDTT differs from previous contributions [1]. The paper should provide a more detailed comparison, highlighting the specific novelties and differences in the context of discrete diffusion models.

### Questions
1. Typos:
    1. Line 96: `(MDLM.)` → `(MDLM).`
    2. Line 785: `the the MAUVE` → `the MAUVE`
    3. Line 785 `resuts` → `results`
2. Clarifications on contributions:
    1. In Line 79, “Unlike many distillation methods for continuous diffusion models, SDTT does not rely on deterministic mappings such as DDIM” might require further elaboration. Given that discrete diffusion models inherently lack a clear connection to deterministic processes akin to DDIM, what is the implication of this distinction? Specifically, how does the absence of deterministic mappings influence the theoretical foundations or empirical performance of SDTT?

### Soundness
3

### Presentation
2

### Contribution
3
