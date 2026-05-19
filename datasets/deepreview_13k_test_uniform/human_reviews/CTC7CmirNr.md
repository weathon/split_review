# Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Masked diffusion models (MDMs) have emerged as a popular research topic for generative modeling of discrete data, thanks to their superior performance over other discrete diffusion models, and are rivaling the auto-regressive models (ARMs) for language modeling tasks. The recent effort in simplifying the masked diffusion framework further leads to alignment with continuous-space diffusion models and more principled training and sampling recipes. 
In this paper, however, we reveal that both training and sampling of MDMs are theoretically free from the time variable, arguably the key signature of diffusion models, and are instead equivalent to masked models. The connection on the sampling aspect is drawn by our proposed first-hitting sampler (FHS). Specifically, we show that the FHS is theoretically equivalent to MDMs' original generation process while significantly alleviating the time-consuming categorical sampling and achieving a 20$\times$ speedup. In addition, our investigation raises doubts about whether MDMs can truly beat ARMs in text generation. We identify, for the first time, an underlying numerical issue, even with the commonly used 32-bit floating-point precision, which results in inaccurate categorical sampling. 
We show that it lowers the effective temperature both theoretically and empirically, and the resulting decrease in token diversity makes previous evaluations, which assess the generation quality solely through the incomplete generative perplexity metric, somewhat unfair.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper has two primary objectives. First, it draws a connection between masked diffusion models and time-agnostic; second, the paper examines various strategies for diffusion model training and examines implications of their choices (in particular, caching, samping techniques, and choice of floating point precision).

### Strengths
There are aspects of the paper I perceive to be strengths. 

For example, empirical evaluations seem by and large well-designed. 

The writing is clear; points are argued; there seem to be extensive details in the Appendices.

### Weaknesses
There are aspects of the paper I perceive to be weaknesses, or at least invitations for further discussion. 

Parts of the text read more like a text book - useful, but I am left wanting to see the implications drawn out. For example, some claims could be elaborated upon, and might be hard for readers to get. For example, the mixture of experts claims on p. 4 has significance not clearly outlined (why does the observation matter, other than as an observation?). 

The paper is also not particularly "tight" in the sense of capturing one primary contribution. It is an investigation into a range of phenomena associated with the training of masked diffusion models. The investigation is also very different in its theoretical exploration and its empirical exploration (with the two not really depending on each other much, at least in the float32 discussion). This might make the paper's contribution a bit difficult for readers to find or grasp. 

Because at least a part of the paper's contributions are about numerical issues, some experiments about how the resulting issues affect performance in programs with other backends could be instructive for the reader (e.g., JAX, MLX). Some of the numerical precision analysis is of course theoretical but the interaction of the multiple layers of approximation and discretization could play out very differently in different settings. 

Overall, the work appears solid, but is seems to be weakened by what could seen as lack of connection between different parts of the paper.

### Questions
What do you think is the reason that "we find the truncation under 32-bit precision not influential in the token-by-token decoding process of ARMs."?

If float32 truncation effectively reduces the temperature of the Gumbel, would comparisons between appropriately temperature set ARM and MDM models be fair?

### Soundness
3

### Presentation
2

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
In this paper, the authors revealed theoretical essence of MDMs, including: 1) MDMs, in both training and sampling, are essentially time-agnostic masked models. 2) MDMs could be significantly lagging behind ARMs in generative perplexity.

### Strengths
1.	The paper provides a comprehensive theoretical analysis of Masked Diffusion Models (MDMs), revealing that both their training and sampling processes are effectively time-agnostic and equivalent to masked models. The theory is novel.
2.	The authors introduce the First-Hitting Sampler, a novel sampling method that is theoretically equivalent to the original MDM sampling process but significantly more efficient, enhancing MDM's computational efficiency.
3.	The structure of the article is well organized, with detailed proofs and a thorough analysis of the core ideas.

### Weaknesses
1.	The paper shows that MDMs do not outperform ARMs in text generation. It would be beneficial to propose improvements for MDMs.
2.	The experiments are only conducted on text generation; more discrete data generation should be considered. Image generation could also be extended to discrete diffusion models and other discrete data like music generation.

### Questions
1.	Have you considered modifications to the model architecture that might help close the performance gap with ARMS?
2.	Will MDM outperform ARMs on other discrete data like music generation?

### Soundness
4

### Presentation
4

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
This work provides a deeper understanding of the recently proposed masked diffusion models for discrete generation. It reveals three issues regarding MDM:

1. A key issue is that MDMs's training is free of the time variable and likely learns as time-agnostic masked models. The NELBO objective for training can be reparametrized as time-independent. According to proposition 3.2, the optimal MDM is irrelevant to time. I did not check the seemingly correct proof in detail, but this could be a valuable observation regarding the limitations of MDMs.

2. The sota sampling strategies are time-consuming. Instead, this paper proposes a first-hitting sampler that can achieve better efficiency.

3. There is a numerical fault regarding the 32-bit Gumbel sampling, causing the previous evaluations to be unfair (positively biased) for the MDM. This work offers a fair evaluation and reveals that MDM cannot effectively model discrete generations, such as texts, compared to autoregressive models.

Disclaimer: My review may change if other reviewers identify any problematic issues in the proofs and I have validated them.

### Strengths
Novel and recent research problem. MDMs have become popular since 2023, but the theoretical foundations are relatively overlooked. This paper presents key theoretical insights regarding the training and sampling of MDMs.

Technically solid claims and high potential impact. The proofs in the appendix look good to me. The parametrization of training MDMs using NELBO objective to be time-agnostic could facilitate further research on the fundamentals of MDMs.

Some of the claims are validated with experiment results on the main pages, and a re-evaluation of MDMs is presented.

### Weaknesses
As there are multiple claims and they seem to be disconnected, I felt it hard to follow sometimes, especially when the topic shifts from training to sampling. As there is much content presented in this paper, I would suggest having a paragraph in the introduction commenting on the organization and flow of this paper. 

This paper does not offer detailed experimental validation of the proposed first-hitting sampler compared to existing sampling strategies, like the mentioned works on caching strategies, line 263.

Maybe more experiments can be conducted on the generation quality of different MDM training strategies in Appendix I.2.3, but using the same prompts rather than the current version. Additionally, there seems to be no analysis with a link to I.2.3 anywhere in the main texts or appendix.

I have no idea how to reproduce the results from the paper, and I don't see any supplementary material.

Minor: 
1. Figure 1 is a bit ambiguous. You prove MDM = Masked Model, but MDM falls into the Discrete Diffusion region.
2. I was confused when looking at the title. The "Secretly" in this paper title actually marks a negative result on MDM, but for the reader who knows the source from the DPO paper last year [1], it is easy for them to interpret it as a positive result. Additionally, the numerical fault is not included. I cannot come up with any better candidate, to be honest, but I would suggest reconsidering the paper title.

[1] Direct Preference Optimization: Your Language Model is Secretly a Reward Model. NeurIPS 2023.

### Questions
1. Can you comment on the limitations of this research and its potential impact on society as well as the research community?

2. Is it possible to mitigate the time-agnostic issue by re-designing or regulating the training objective?

I think this paper offers adequate and solid theoretical insights, and I am inclined to give it a rating of 8. However, I am not entirely confident and would appreciate it if you could address the weaknesses I have mentioned. Thank you.

### Soundness
3

### Presentation
2

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
The paper investigates Masked Diffusion Models (MDMs), which have gained popularity for discrete generative tasks, particularly for language modeling, where they are now competitive with auto-regressive models (ARMs). Recent work has simplified MDMs by aligning them with continuous-space diffusion models, improving training and sampling strategies. However, the authors reveal a key insight: MDMs’ training and sampling processes do not fundamentally rely on time variables (a typical diffusion model feature) and are instead equivalent to masked models. This finding is illustrated through their proposed "first-hitting sampler" (FHS), which mirrors MDMs' original sampling process but is up to 20 times faster by avoiding time-intensive categorical sampling.

The paper also challenges the assumption that MDMs outperform ARMs in text generation. It identifies a numerical limitation, even with 32-bit floating-point precision, that leads to inaccurate categorical sampling. This flaw reduces the effective temperature, thereby lowering token diversity in generated text. Consequently, the authors suggest that previous quality evaluations using perplexity metrics alone may not accurately reflect MDMs' performance.

### Strengths
1.The paper uncovers MDMs' time-agnostic properties, showing they align closely with masked models, simplifying their conceptual and practical applications.
2.The First-Hitting Sampler (FHS) reduces categorical sampling inefficiencies, achieving a 20x speedup, beneficial for real-time applications.
3.Addressing the 32-bit Gumbel sampling precision issue highlights the authors’ rigor, demonstrating 64-bit sampling better preserves entropy and token diversity.
4.Standardizing precision and sampling provides a fair comparison with ARMs, challenging prior MDM superiority claims in generative tasks.

### Weaknesses
1.While the authors advocate for MDMs' applications in order-agnostic settings, their comparative analysis still favors ARMs in text generation tasks, possibly limiting the generalizability of the claims for broader applications.
2.The proposed First-Hitting Sampler and high-order sampling extensions add a layer of complexity that might limit accessibility for practitioners less versed in advanced diffusion techniques
3.The experiments primarily focus on language tasks and lack extensive cross-domain testing (e.g., images, audio), where MDMs might exhibit different performance dynamics, which limits the scope of applicability

### Questions
1.Could the authors provide additional insight into how MDMs might perform in non-text generation tasks, specifically in visual or audio data domains?
2.How sensitive is the First-Hitting Sampler to different vocabulary sizes or sequence lengths? Would the efficiency gains remain consistent across a wider range of data?
3.Are there scenarios where 32-bit sampling could be advantageous, considering computational resources, or is 64-bit sampling universally superior for maintaining token diversity?

### Soundness
4

### Presentation
4

### Contribution
3
