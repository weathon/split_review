# Energy-Based Diffusion Language Models for Text Generation

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
\looseness=-1
    Despite remarkable progress in autoregressive language models, alternative generative paradigms beyond left-to-right generation are still being actively explored. Discrete diffusion models, with the capacity for parallel generation, have recently emerged as a promising alternative. Unfortunately, these models still underperform the autoregressive counterparts, with the performance gap increasing when reducing the number of sampling steps. Our analysis reveals that this degradation is a consequence of an imperfect approximation used by diffusion models. In this work, we propose Energy-based Diffusion Language Model (\method), an energy-based model operating at the full sequence level for each diffusion step, introduced to improve the underlying approximation used by diffusion models. More specifically, we introduce an EBM in a residual form, and show that its parameters can be obtained by leveraging a pretrained autoregressive model or by finetuning a bidirectional transformer via noise contrastive estimation. We also propose an efficient generation algorithm via parallel important sampling. Comprehensive experiments on language modeling benchmarks show that our model can consistently outperform state-of-the-art diffusion models by a significant margin, and approaches autoregressive models' perplexity. We further show that, without any generation performance drop, our framework offers a 1.3$\times$ sampling speedup over existing diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a new Discrete Diffusion Model that models an energy function $E_\phi$ to improve sampling procedure from an existing Diffusion Model. The authors propose a novel sampling procedure that incorporates importance sampling steps during generation.

### Strengths
- The paper is clearly written and easy to follow.
- The method is intuitive and based on a solid mathematical foundation.
- The experiments follow the standard setup for evaluating Diffusion Language Models, making it easy to compare with other methods.

### Weaknesses
 - This method requires a pre-trained discrete diffusion model, which increases the overall computational requirements. Thus, it may be unfair to compare it directly with simpler methods like MLDM.
- While the proposed method reduces the Gen PPL metric, it also decreases the entropy of generated texts. One could even argue that it produces similar results to MLDM in terms of Gen PPL and entropy.

### Questions
- Is it correct that the number of parameters used for generation is approximately doubled? While generation time is important, it would also be useful to know the VRAM requirements for generation.
- Is it possible to apply the importance sampling steps at a different interval, i.e. at the middle of the generation rather than at the start? This adjustment might yield improved performance.

### Soundness
2

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
4

### Summary
This work presents a new discrete diffusion language model that uses an energy-based model (EBM) to introduce token dependencies within the text sequence, instead of factorizing the denoising distribution over individual tokens. In practice, this EBM is parameterized in a residual form, with the energy function implemented by either a pretrained auto-regressive Transformer or a fine-tuned bidirectional Transformer. To facilitate efficient sampling, the paper employs self-normalizing importance sampling and draws several samples followed by resampling based on energies to complete each denoising step. The resulting framework, called Energy-based Diffusion Language Models (EDLMs), demonstrates significant advancements over previous discrete diffusion baselines and achieves comparable or better performance to traditional auto-regressive language models on text generation.

### Strengths
- This paper is well-written and well-organized, presenting a simple yet elegant combination of energy-based and discrete diffusion models. EDLM demonstrates strong empirical results that match auto-regressive models with great improvements in sampling speed.
- The adaptation of auto-regressive models to a joint denoising distribution with masked inputs is innovative.
- The application and detailed analysis of importance sampling windows effectively improve the early sampling phases in discrete diffusion models, making a nice empirical contribution to the advancements of discrete diffusion language models.

### Weaknesses
 - While the study aims to address the independence assumptions in discrete diffusion models through EBMs, there is insufficient examination of relevant prior research also involving EBMs for language modeling (e.g., [1]). Given the similarity between EDLMs and [1], a more detailed discussion and comparison would clarify the position and relevance of this study.
- Another concern lies in the significance of applying EBMs to discrete diffusion models. Although vanilla discrete diffusion processes do factorize the denoising distribution over tokens, the bidirectional attention mechanism in transformers can already capture dependencies among tokens within a sequence. Therefore, to account for errors due to parallel decoding, feeding the decoded sequence back into the transformer (i.e., the next denoising step) could potentially identify erroneous tokens and assign low likelihoods to those positions. There is extensive literature on filtering and remasking tokens at each denoising step [2, 3, 4]. An in-depth discussion highlighting the advantages of using an EBM to capture token dependencies would strengthen the paper’s argument.

### Questions
1. For EDLM-AR and EDLM-coAR, which pretrained AR model is used and what is the parameter size of the model?
2. For all EDLM variants, a separate transformer model is used to calculate the energy, which effectively doubles the parameter count and might contribute significantly to performance gains. While the reported performance and efficiency improvements likely go beyond what would be expected from simply doubling the model size, it would strengthen the validity of these findings to include an empirical comparison or an in-depth discussion with a baseline with an equivalent parameter count.

### Soundness
4

### Presentation
4

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
This paper proposes using an autoregressive language model to help the sampling process of a Masked Discrete Diffusion Language Model (which is technically equivalent to a Masked Language Model) by rescoring a selected subset of the generated outputs. The authors further propose to train this model with noise contrastive estimation and find a method to estimate its PPL.

### Strengths
1. Using an AR to help the sampling of Masked Discrete Diffusion Language Model is natural and straightforward.
2. The experiments demonstrate good improvements compared with MDLM baseline.

### Weaknesses
My main concern is that the core technique introduced in this work has been present in the literature for a long time.

1. First, the framework of the absorbing discrete diffusion model is essentially the same as the BERT-like masked language model (MLM). The forward process corresponds to masking tokens in the input, while the backward process corresponds to predicting and remasking tokens during iterative generation in MLMs. Therefore, this work primarily explores how to apply an energy-based framework to assist MLMs in generating text.

2. Importantly, the core part of the proposed method is using an autoregressive model as an energy function to guide the sampling process of an MLM (referred to as the denoising model in this paper). The introduced energy function ($−logp_{AR}(x_0) + logp_θ(x_0|x_t)$) and the Importance Sampling method (Algorithm 1) are identical to reranking (or noisy parallel decoding) methods used in MLM generation/non-autoregressive generation, which have long been established in prior literature. Examples can be found in [1,2,3]. Actually, the practice of using an AR model to rescore multiple outputs from an MLM has long been a standard baseline in non-autoregressive generation tasks.

### Questions
Section 4.3 is not very clear to me. Could you provide a detailed explanation of how you estimated PPL?

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
This paper points out that the existing discrete diffusion models aim to predict all missing tokens in parallel at each intermediate diffusion step, but the denoising joint distribution is simply parameterized as a product of token-wise independent distributions.
The authors propose Energy-based Diffusion Language Model (EDLM) by using an energy-based model to act as a reranker in the intermediate denoising steps to inject sequence-level correlation. Experimental results demonstrate that EDLM outperforms existing diffusion models and achieves sampling speedup without sacrificing generation quality.

### Strengths
- The writing is clear, making the paper easily comprehensible.
- The idea to inject sequence-level correlation in the intermediate denoising steps is intuitive.

### Weaknesses
 - The primary contribution lies in the energy-based reranker, which mostly follows the approach presented in https://arxiv.org/abs/2004.11714. In my view, I tend to have concerns about the novelty given previous work.
- The description of the motivation and the independent factorization in Equation 6 does not seem entirely accurate. For line 156 "$\mu_\theta$ predicts each token in x_0 independently", it may be more precise to state that the sampling operation over the output distribution is done independently, as during training, predictions for all masked token positions are made simultaneously, leading to their hidden representations being interrelated. This implies that predicting a particular token will implicitly involve using representations of other tokens, which makes the the independent factorization in Equation 6 not entirely accurate.
- This paper only evaluates perplexity, and it remains uncertain whether such energy-based reranking translates effectively to downstream tasks.
- I tend to have concerns about the inference cost linked to repetitive sampling and energy function computations in each denoising steps.

### Questions
- What are the used window size and sampling size in Figure 1(a). I am somewhat confused about the 1.3x sampling speedup as EDLM-AR/NCE requires more computation on the intermediate steps. Could you please elaborate on the rationale behind the increased efficiency of EDLM-AR/NCE compared to EDLM?
- In the case of EDLM-NCE, it seems that when the value of t is large, the quality of multiple sampled $x_0$ might all degrade, leading to general closer low scores assigned by the classifier. Given this, why does adding the reranker in the early stages yield better results instead?
- In the context of EDLM-NCE, do you employ separate models or do you utilize a shared rerank and generator approach?
- I am somewhat confused about Figure 3. In my view, as the window size increases, one would expect a higher time cost. However, the graph appears to show the opposite trend. Could you provide insight into this discrepancy?

### Soundness
3

### Presentation
3

### Contribution
2
