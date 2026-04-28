# Interpolating Autoregressive and Discrete Denoising Diffusion Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Diffusion language models offer unique benefits over autoregressive (AR) models due to their potential for parallelized generation and controllability, yet they lag in likelihood modeling and are limited to fixed-length generation. In this work, we introduce a class of semi-autoregressive (SAR) diffusion models that interpolate between discrete denoising diffusion and autoregressive models. 
We propose a recipe for building effective SAR models that includes an efficient training algorithm, estimators of gradient variance, and data-driven noise schedules to minimize the variance. SAR models overcome key limitations of diffusion language models, setting a new state-of-the-art performance on language modeling benchmarks and enabling generation of arbitrary-length sequences.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
A new generative model on discrete label sequences is proposed: A hybrid between discrete diffusion and auto-regressive model. Specifically, it operates auto-regressively on a block level, and within a block, it uses a diffusion model. This model is called semi-autoregressive denoising discrete diffusion language model (SAD3-LM).

The model is evaluated on standard language modeling benchmarks. Different noise schedules are compared. For the special case of L'=1, the model also requires a special (no-op) noise schedule to be able to recover the performance of the auto-regressive model, due to the grad variance we get from the noise schedule otherwise.

### Strengths
- Discrete diffusion is an interesting research direction with potential interesting applications. This work here presents a new way to improve this, allowing to interpolate between auto-regressive and diffusion models by changing the block size.

- Good experiments, good studies.

### Weaknesses
 - Some details are unclear (but I think these can be solved quite easily).

- Some discussion on the motivation of such models would be nice.

- No speed measurements (for the different cases: Training, sampling, evaluating log probs for given seqs). Also for the vectorized training.

- p3 l143: "computational artifacts for efficient training" - unclear what this means.

- Table 2, Table 3, Table 4: I think it would be nice to also include L'=1 here for completeness.


- Sec 2.2 "The marginalization is tractable" - What exactly do you mean by that? You mean that you can parallelize over the frames in x (L' for SAD3-LM)? But still you can not calculate the full marginalization, or can you? If not, I'm not sure I would call it like that. Maybe better "the approximation of the marginalization is tractable"? And how is this calculated then? You sample from p(x|x_t)? Or take the N-best from p(x|x_t)?


- Sec 2.2: You give some examples of what Q_t could be. But what Q_t do you actually use here in this work? How do you compute the q(x_s^b|x_t^b,x^b) exactly? How do you sample from it for the ELBO? I think this should be specified exactly.


- In eq 3, you define the loss L via the negative ELBO, but in eq 5, the loss is using the positive ELBO. Thus, something is wrong here. I assume you want to put some negative sign somewhere.


- Sec 3.2: What happens when you do just one forward pass on noisy inputs and directly compute the loss that way? I understand that this is not totally correct, as the auto-regressive model part depends on clean input, but it might still work, and maybe even helps for regularization. It would be interesting to try.


- Sec 4.1 Masked SAD3-LMs: The title of the section suggests that this is a different model (p), but from the text, I understand that only the noise process, only the q is different, right? Ah, but this effectively then changes also the SAD3-LM itself via equation 2? Please clarify this.


- Sec 4.2 "Although the objectives are equivalent in expectation" - can you show this? (maybe just in the appendix)


- Sec 4.2: When you show the variance of the grad, I assume this is the L2 norm? You should write that in the formula, or not? (Same also for equation 9.)

- Sec 4.2: What about other methods to reduce the gradient variance? E.g. using multiple samples from q for the ELBO, or gradient clipping, or other methods? (Ah, I see that you discuss this further in Sec 5, where you propose some other methods.)

- Sec 4.2 / Table 1: How exactly is the PPL for SAD3-LM calculated? This uses equation 5 and equation 3? How is x_{t(0)} sampled from q? What is T? How are the other x_t sampled?


- Table 2, Table 6: The PPL, are they exact or just upper bounds?
What kind of hardware is used for training? How many epochs do you train? How long does it take?

### Questions
More general: What is the motivation to use diffusion models for language modeling? Maybe potentially even better PPL than auto-regressive models? We don't see that here. Or better speed? I assume this is the case, but this is not shown here. Or what else? Some discussion on this would be good.

p3 l143: "computational artifacts for efficient training" - unclear what this means.

Table 2, Table 3, Table 4: I think it would be nice to also include L'=1 here for completeness.


Sec 2.2 "The marginalization is tractable" - What exactly do you mean by that? You mean that you can parallelize over the frames in x (L' for SAD3-LM)? But still you can not calculate the full marginalization, or can you? If not, I'm not sure I would call it like that. Maybe better "the approximation of the marginalization is tractable"? And how is this calculated then? You sample from p(x|x_t)? Or take the N-best from p(x|x_t)?


Sec 2.2: You give some examples of what Q_t could be. But what Q_t do you actually use here in this work? How do you compute the q(x_s^b|x_t^b,x^b) exactly? How do you sample from it for the ELBO? I think this should be specified exactly.


In eq 3, you define the loss L via the negative ELBO, but in eq 5, the loss is using the positive ELBO. Thus, something is wrong here. I assume you want to put some negative sign somewhere.


Sec 3.2: What happens when you do just one forward pass on noisy inputs and directly compute the loss that way? I understand that this is not totally correct, as the auto-regressive model part depends on clean input, but it might still work, and maybe even helps for regularization. It would be interesting to try.


Sec 4.1 Masked SAD3-LMs: The title of the section suggests that this is a different model (p), but from the text, I understand that only the noise process, only the q is different, right? Ah, but this effectively then changes also the SAD3-LM itself via equation 2? Please clarify this.




Sec 4.2 "Although the objectives are equivalent in expectation" - can you show this? (maybe just in the appendix)


Sec 4.2: When you show the variance of the grad, I assume this is the L2 norm? You should write that in the formula, or not? (Same also for equation 9.)

Sec 4.2: What about other methods to reduce the gradient variance? E.g. using multiple samples from q for the ELBO, or gradient clipping, or other methods? (Ah, I see that you discuss this further in Sec 5, where you propose some other methods.)

Sec 4.2 / Table 1: How exactly is the PPL for SAD3-LM calculated? This uses equation 5 and equation 3? How is x_{t(0)} sampled from q? What is T? How are the other x_t sampled?


Table 2, Table 6: The PPL, are they exact or just upper bounds?
What kind of hardware is used for training? How many epochs do you train? How long does it take?

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
4

### Summary
In this paper the authors propose a semi-autoregressive model for text generation called SAD3-LM (semi-autoregressive denoising discrete diffusion), which divides the input sequence of length $L$ in $B$ blocks of length $L’$ ($B = L / L’$) and trains a (transformer-implemented) discrete diffusion model (a la D3PM [7], but focusing more on a recent implementation called MDLM [8] that only performs masking) on each block $b$, which is conditioned on the previous blocks $1,…, b-1$. The authors offer an efficient implementation which caches the $K, V$ values of the transformer computations of previous blocks, where training can be parallelized in a single pass (concatenating the clean input $\textbf{x}$ with a noisy version of the input $\textbf{x}_{\text{noisy}}$ and applying a specialised attention mask, and inference proceeds over the blocks sequentially. The authors, focusing on the masking model, additionally propose a theoretical study of the tightness of the NELBO objective varying the block length (showing is tighter when one reduces block length) and show that the semi-autoregressive training increases variance with respect to standard autoregressive training, proposing a way to reduce it by masking in a clipped range of the number of applied mask tokens (which is learned during training). The authors show extensive experimental results comparing with both standard autoregressive models and diffusion models for text data (D3PM [7], SEDD, MDLM [8], SSD-LM) on a wide variety of benchmarks (LM1B, Lambada, AG News, Pubmed, Arxiv) reaching good results in terms of perplexity and number of function evaluations (when comparing to SSD-LM).

References:

- [7] Austin, J., Johnson, D. D., Ho, J., Tarlow, D., & Van Den Berg, R. (2021). Structured denoising diffusion models in discrete state-spaces. Advances in Neural Information Processing Systems, 34, 17981-17993.
- [8] Sahoo, S. S., Arriola, M., Gokaslan, A., Marroquin, E. M., Rush, A. M., Schiff, Y., ... & Kuleshov, V. Simple and Effective Masked Diffusion Language Models. In ICML 2024 Workshop on Efficient and Accessible Foundation Models for Biological Discovery.

### Strengths
1. The idea of a semi-autoregressive model, while not new (there is already a rich literature of models combining autoregression with diffusion, while focusing more on continuous diffusion like SSD-LM (see Weakness point 2), in this paper is developed via discrete diffusion. This is a way of proceeding that is very natural, and shares many parallels with novel methods in the literature focusing on block-wise parallel decoding such as [1] (https://aclanthology.org/2023.acl-long.689). It seems clear that a combination of sequential and parallel inference is a good solution, especially for speeding up the models, but this aspect is not much explored in this work (see Weakness point 4). Also the fact that one can generate sentences of arbitrary length is a big improvement over previous models in terms of usability, paired with the ability to estimate likelihoods (which SSD-LM cannot do).
2. Showing the tightness of the NELBO (Appendix C) is an interesting theoretical argument that relates the standard autoregressive objective to discrete diffusion objectives.
3. Good experimental section and good results over previous discrete diffusion approaches. Still one should have done experiments without first pre-training auto-regressively (see Weakness point 3)
4. The paper is written in a good way, having a good structure, not containing errors and being easy to follow. Still there are two sections (Section 4 and 5) in which some parts are not clear (see Weakness point 1), but apart from those the execution is solid.

References:

- [1] Andrea Santilli, Silvio Severino, Emilian Postolache, Valentino Maiorca, Michele Mancusi, Riccardo Marin, and Emanuele Rodola. 2023. Accelerating Transformer Inference for Translation via Parallel Decoding. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 12336–12355, Toronto, Canada. Association for Computational Linguistics.

### Weaknesses
1. Some aspects of the work, especially Sections 4 and 5, are poorly defined and demonstrated. For example it is not very clear why the variance of the gradient estimator has the formula in Eq. 9, and also not very clear why extreme masking leads to poor variance. Authors should try to re-formulate these parts in a more sound way.
2. The authors are missing a good number of citations:
    1. First in [1] (https://aclanthology.org/2023.acl-long.689), the parallel GS-Jacobi decoding algorithm is proposed for text autoregressive models and has a similar structure to the approach proposed by the authors: move on blocks from left to right and perform parallel decoding on each block. The difference between the two approaches is that in [1], parallel decoding is done via Jacobi iterations while here instead one uses discrete diffusion. Even more related, a follow-up [5] (https://arxiv.org/abs/2403.00835), trains a consistency-like model [6] (which is a type of diffusion model) to speed-up the Jacobi iterations on each block. I see many parallels between the presented method and these two methods, especially the second. The authors should cite those papers and especially discuss in how they differ with [5].
    2. Additionally, apart from other prominent approaches for discrete autoregressive diffusion like [3] (https://openreview.net/forum?id=Lm8T39vLDTE), there is a rich literature on combining autoregression with continuous diffusion, e.g. [2, 4] (http://proceedings.mlr.press/v139/rasul21a.html, https://openreview.net/forum?id=0EG6qUQ4xE), which the authors barely touch (citing SSD-LM and Diffusion-lm). Please integrate some more references from this literature.
3. Since SAD3-LM is first pre-trained with standard autoregression for 850K steps is it fair to posit it as a semi-autoregressive discrete diffusion model? It can be that it learns representations especially on the pre-training part and the fine-tuning part is more accessory. I think experiments should have been performed also without pre-training as well in order to see how standard autoregressive the pre-training impacts the final model.
4. One advantage of combining sequential autoregression with parallel decoding, as in [1, 5], is to improve inference speed, given that parallel decoding could be done in less steps than $L’$ steps (the number of steps required for autoregressive decoding on such block). I understand that the goal of this work is not much on improving efficiency with respect to autoregressive models since one does 10K steps instead of 1024 steps (Table 7), and I appreciate the reduced inference burden with respect to SSD-LM, but what is the point on doing discrete diffusion if there isn’t any gain on standard autoregression? I agree it is good to have an alternative to standard autoregression, hence all the efforts in the discrete diffusion area, and maybe improved perplexity will be reached in future, but still I think improved efficiency over standard autoregressive should be the main goal to be sought. I do not think authors need to compare with [1, 5] (which do achieve a speed-up, especially in [5]) but at least point and discuss as future work how to target these goals starting from their proposal and maybe improving via the faster models that are researched in diffusion distillation literature (e.g. the already cited consistency models [6]).

### Questions
- Line 212: The authors should define $\alpha’$, in the main body of the paper not only in the appendix.
- Table 5: Any idea why results are so bad on AG News? And why AR is worse than diffusion approaches in 3 settings, different than when evaluating on in-distribution settings? Do the author think that discrete diffusion generalises better on out-of-distribution settings?
- I don’t understand why comparison is SSD-LM is under ablations section. Is SSD-LM the naive implementation?

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
This paper describes a diffusion language model that is autoregressive between blocks.  By being semi-autoregressive, the model achieves lower perplexity than other diffusion models.

### Strengths
The key contribution of this paper is to demonstrate that it is possible to bridge part of the perplexity gap between diffusion-based and autoregressive language models by making a diffusion model partly autoregressive.

The analysis of gradient variance in section 4 is highly appreciated, and will influence the way in which other investigators conduct research.

### Weaknesses
The statistical significance of performance differences is not specified.  The differences are large enough to appear statistically significant, but it would be nice to have confirmation.

p. 3:

Eq. (3) is a negative ELBO.  I think therefore that either Eq. (5) should show -log ptheta(x) <= L_{SAR}, or else it should define L_{SAR} to be the negative of the sum.  If you apply the former solution, I think you need to change the acronym ELBO in the text before and after Eq. (5) to NELBO.

The meaning of Algorithm 1 is obfuscated by the call x_\theta(x), in which the argument, x, has no superscript or subscript.  Is this argument the clean sequence (as in a teacher-forcing mode), or the noisy sequence?  The first paragraph of section 3.2 suggests that x is the clean sequence, in that it specifies two calls to x_\theta: one on the noisy input (which seems to match the line of Algorithm 1 that generates x_{logit}^b), and one on the clean input (which might be the line that generates K^{1:B} and V^{1:B}, but this is the point on which I'm not clear).  On the other hand, Algorithm 2 seems to be defining x, with no superscript or subscript, to be the noisy sequence.

p. 4

based the -> based on the

### Questions
p. 3:

Eq. (3) is a negative ELBO.  I think therefore that either Eq. (5) should show -log ptheta(x) <= L_{SAR}, or else it should define L_{SAR} to be the negative of the sum.  If you apply the former solution, I think you need to change the acronym ELBO in the text before and after Eq. (5) to NELBO.

The meaning of Algorithm 1 is obfuscated by the call x_\theta(x), in which the argument, x, has no superscript or subscript.  Is this argument the clean sequence (as in a teacher-forcing mode), or the noisy sequence?  The first paragraph of section 3.2 suggests that x is the clean sequence, in that it specifies two calls to x_\theta: one on the noisy input (which seems to match the line of Algorithm 1 that generates x_{logit}^b), and one on the clean input (which might be the line that generates K^{1:B} and V^{1:B}, but this is the point on which I'm not clear).  On the other hand, Algorithm 2 seems to be defining x, with no superscript or subscript, to be the noisy sequence.

p. 4

based the -> based on the

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a semi-autoregressive discrete diffusion model to address the problem that diffusion models cannot perform arbitrary length prediction as autoregressive models.  The paper introduces SAD3-LMs, a class of semi-autoregressive diffusion model, that interpolate between discrete denoising diffusion models and autoregressive models. Compared to existing alternative semi-autoregressive diffusion models with Gaussian diffusion process, the proposed discrete method provides tractable likelihood estimates and yields samples with improved generative perplexity using an order magnitude fewer generation steps.

### Strengths
The paper is easy to follow. The paper proposes a semi autoregressive discrete denoising diffusion model and provides an efficient training and sampling algorithm compared to the continuous semi-autoregressive DPM (SSD-LM). The method is incrementally novel. As a semi-autoregressive diffusion model, the paper claimed that the method has advantages in generating full-length sequences that are longer than the length of the output context chosen at training time compared to existing diffusion language models. The paper provides a comprehensive ablation study and well-designed experiments to verify the SAD3-LMs.

### Weaknesses
My main concern is the motivation of integrating a discrete diffusion processing in AR. As when $L'=1$, the method performs the same as AR, however, significant higher NFEs, extra tuning required on noise schedules, and complex training and sampling algorithms are involved. The paper can be further improved by showcasing its advantages in real-world applications compared to AR methods.

Moreover, please see Questions for the details.

### Questions
1. What is the computational complexity and time complexity for the sampling algorithm given an arbitrary $L'$ and B?

2. If I understand correctly, the SAD3-LMs is trying to address the limitation of diffusion models while maintaining the flexibility of autoregressive models. However, as in Table 7, SAD3-LM has significantly increased NEFs compared to AR, but only with limited PPL improvement. And as in Table 1, when $L'=1$, the SAD3-LM performs exactly the same as AR. What are the advantages of SAD3-LM compared to AR?

3. According to Table 2, the method with different $L'$ values have unique noise rate distributions, this may require extra time and effort for tuning in real applications. I'm curious about can the masked-and-replace diffusion strategy by [1] solve the problem?

4. The paper could be improved by involving an experiment on controlled text generation as in SSD-LM to further showcase its advantages of integrating diffusion models in AR. 

Reference

[1] Gu, Shuyang, et al. "Vector quantized diffusion model for text-to-image synthesis." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

### Soundness
2

### Presentation
3

### Contribution
3
