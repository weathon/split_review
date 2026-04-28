# Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data

- Decision: Accept
- Avg Score: 6.20
- Scores: 5, 6, 6, 8, 6

## Abstract
Discrete diffusion models with absorbing processes have shown promise in language modeling. The key quantities to be estimated are the ratios between the marginal probabilities of two transitive states at all timesteps, called the concrete score. In this paper, we reveal that the concrete score in absorbing diffusion can be expressed as conditional probabilities of clean data, multiplied by a time-dependent scalar in an analytic form. Motivated by this finding, we propose reparameterized absorbing discrete diffusion (RADD), a dedicated diffusion model without time-condition that characterizes the time-independent conditional probabilities. Besides its simplicity, RADD can reduce the number of function evaluations (NFEs) by caching the output of the time-independent network when the noisy sample remains unchanged in a sampling interval. Empirically, RADD is up to 3.5 times faster while achieving similar performance with the strongest baseline.
Built upon the new perspective of conditional distributions, we further unify absorbing discrete diffusion and any-order autoregressive models (AO-ARMs), showing that the upper bound on the negative log-likelihood for the diffusion model can be
interpreted as an expected negative log-likelihood for AO-ARMs. Further, our RADD models achieve SOTA performance among diffusion models on 5 zero-shot language modeling benchmarks (measured by perplexity) at the GPT-2 scale.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a reparameterization of the absorbing discrete diffusion, based upon the finding that the concrete score can be decomposed into a time-independent conditional probability of clean data, and a time dependent but data independent term. Therefore, this paper proposes a new network architecture, that removes the time dependency, and add softmax layers to project the output layer to the probability space.

The authors argue that the removed time dependency can accelerate the sampling process by caching the network output before it changes. The total changes would be at most $d$ instead of $n$, and the total number of NFEs reduces to  $n(1 - (1 - \frac{1}{n}))^l)$.

### Strengths
The authors proposed a novel reparameterization of absorbing discrete diffusion, decoupled the time-independent and time-dependent part. This discovery allows for better understanding of discrete diffusions, and the previous reparameterization in SEDD.  The proposed reparameterization allows for a simplified network architecture and efficient sampling.

Moreover, the authors proposed the unification of absorbing diffusion with the any-order autoregressive model.

### Weaknesses
First of all, the proposed algorithm are specified to absorbing discrete diffusion, and does not fit in the other widely used discrete diffusion model, multinomial diffusion. The authors did not discuss if or why not their methodology can not be applied to multinomial diffusion.

There are existing works that have reduced the sampling complexity of discrete diffusions, including absorbing and multinomial diffusion, e.g., Chen et al. 2024 [1]. [1] also made use of the fact that during the reverse sampling process, computation is only required when tokens changes, thus reducing the computation from number of diffusion steps to number of tokens. Also [1] proposed a similar NFE estimation in Theorem D.1, which is the same as (3.4) in this paper. However, the authors did not discuss or mention the relationship with [1].

Also inspired from [1], the sampling complexity essentially does not comes from whether you have $t$ in your score network or not, but comes from times that you change tokens. Even for SEDD based discrete diffusion network, it is also possible to only calculate when change is required, and skip calculation when $x$ does no change. For example, if using [1] for sampling, does RADD still have any advantage over SEDD?

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Previous work in discrete diffusion language modeling have relied on estimating a time-dependent concrete score. The authors derive a simpler parameterization, RADD, expressed as a time-independent conditional probabilities of the clean data, multiplied by a time-dependent scalar. By deriving a simplified objective, they provide a deeper understanding of discrete diffusion and draw a connection with any-order autoregressive models. By training a time-independent denoising network, they simplify the model architecture by removing additional time-conditioning layers used in prior discrete diffusion language models. The authors show theoretically and experimentally that using a time-independent network can significantly reduce the number of function evaluations at inference. On language modeling benchmarks, their architectural simplifications and optimized training loss results in state-of-the-art performance among discrete diffusion models at the GPT-2 scale.

### Strengths
- They provide clear, rigorous analysis showing the equivalence between the concrete score [1], their simplified parameterization, and the any-order autoregressive loss
- The connection between discrete diffusion models and any-order autoregressive models is novel and unexplored in prior work. The authors provide a theoretical and empirical comparison
- They show substantial improvement in sampling speed over SEDD [1] through convincing theoretical and experimental analysis
- They provide thorough comparison to concurrent work [2,3] and explain the added novelty introduced by their paper

[1] Lou, Aaron, et al. "Discrete diffusion language modeling by estimating the ratios of the data distribution."

[2] Shi, Jiaxin. "Simplified and Generalized Masked Diffusion for Discrete Data"

[3] Sahoo, Subham Sekhar. "Simple and Effective Masked Diffusion Language Models."

### Weaknesses
 - The experimental results are limited. Their likelihood evaluation only includes zero-shot likelihoods using models trained on OpenWebText
- The empirical comparison across RADD models is misleading as they have equivalent objectives (Tables 1, 2, 5). In Table 2, one RADD model underperforms SEDD on LAMBADA while another outperforms.
- Experimental ablations on the architectural and theoretical simplifications are not provided, making it difficult to understand its impact on likelihoods (an ablation on the scaling term is instead provided for SEDD). For example, they claim to design a time-independent network that simplifies learning: it would be valuable to compare RADD with and without time conditioning, while controlling for parameter count
- The sampling speed is not compared with AR, making it unclear whether the speedup improvement has practical significance

### Questions
- Does the improvement from including the scaling term in SEDD also hold for RADD?
- If a claim is that the simplification enables a simpler architecture, can the authors provide comparative analysis between RADD with and without time conditioning while controlling for parameter count?
- If the objectives presented are equivalent, why are there differences in the zero-shot likelihoods in Tables 1, 2, 5?
- In Table 4, can the authors compare perplexity from any-order autoregressive generation and parallel generation using the $\tau$-leaping sampler?
- What is the number of tokens used for training, instead of the number of iterations, in order to compare with baselines? In Table 5, the authors report zero-shot likelihood on models trained for 1000K iterations, why do the models in the main paper use 400K iterations?

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
5

### Summary
This paper studies simplifications of discrete diffusion models with absorbing/masking processes. First, the concrete score in Lou et al. 2024 can be reparameterized as conditional probability of clean data, i.e. p(x_0^i | x_t). Second, when noise samples are not changed during a time-step, cached NN output from previous step can be reused (since the input values are unchanged). Lastly, equivalence between absorbing discrete diffusion and any-order autoregressive models is identified. The simplified training objectives enable better test data perplexity on zero-shot language modeling tasks. The caching trick helps reduce number of function evaluations.

### Strengths
The first result on reparameterizing score as conditional denoising probability is the most original contribution. It helps clarify that training concrete score entropy and clean data reconstruction cross-entropy are essentially equivalent up to scalar difference. And this results in better training efficiency compared to SEDD as shown in language modeling experiments. On a side node, the use of clean data reconstruction cross-entropy loss for mask/absorbing discrete diffusion is previously proposed in Austin et al. 2021 for discrete timesteps and Campbell et al. 2024 for continuous time. The connection of this reconstruction distribution and concrete score is newly identified in this paper.

### Weaknesses
The second result on caching when samples are not changed during a previous timestep is somewhat well-known. For example, Chen et al. 2023 proposes to only incur NFE at times when actual transition from mask token to infilled token happens, which also corresponds to how AO-ARM sample one dimension at a step. The caching strategy proposed in this paper becomes less efficient when sampling a batch of samples: in a small timestep when some samples might remain unchanged while some are not, caching cannot be used. Hence I think it should be more efficient to use different $\Delta t$ time steps for different samples in [1], and the $\Delta t$ should be sampled to be the amount of time until next transition from mask to data token for each sample. 

The third result on equivalence of absorbing discrete diffusion and AO-ARMs is not new. This has been shown in previous works (Austin et al. 2021, Hoogeboom et al. 2021, Campbell et al. 2024)

### Questions
- Experiments: For evaluation on language modeling, in G.4 evaluation of generative perplexity, which model is used for evaluating the generation quality? The numbers in Table 3 seem to be much higher than SEDD’s generative perplexity evaluated using GPT-2-Large. 
Another ablation might be training both SEDD and RADD to 1000k iterations and compare the performance gap v.s. SEDD and RADD with 400k iterations. Just to see if the gap closes down with more training, or is there a fundamental gap in learning under different parameterization of the model.

- Theory: Clarify which contribution is original and which are already existing in previous literature. Point connection to existing literature when there is. For example, connection to cross-entropy loss proposed in (Austin et al. 2021, Hoogeboom et al. 2021, Campbell et al. 2024); and the connection of caching to derandomized sampling in Chen et al. 2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors express the concrete score for an absorbing (only masked to unmasked) diffusion in terms of a time conditional scalar and prediction of the t=0 data distribution. This significantly simplifies the training of discrete diffusion models as given the state transitions only from masked to unmasked the rate matrix is 0 at all most all positions.

The authors then explain how such a parameterisation can lead to efficient sampling as one may cache the unmasked components rather than recompute.

### Strengths
The paper is well explained, the authors make a thorough comparison to concurrent works [1,2] which propose the very much the same methods.

Restricting the generative process from unmasked to masked sounds limiting but greatly simplifies the parameterisation of the concrete score (RADD) as simply learning the masked to unmasked transition. 

This RADD reparameterisation also provides insights into heuristic "scaling" in prior works.

The authors provide detailed numerical evidence of how the caching procedure reduces the E-NFE in Fig 1a.

The empirical performance is compelling.

[1]  Shi eta.  Simplified and generalized masked diffusion for discrete data, 2024.
[2] Sahoo et al. Simple and effective masked diffusion language models,  2024

### Weaknesses
Although the caching reduces the *effective* NFE, I assume the actual number of function evaluations remains the same given the number of steps, just with fewer outputs per evaluation? This may not reduce workload for jitted - shape static compiled programs like those implemented in jax.

As discussed, many of the ideas are the same as those in concurrent but published works [1,2] from June 2024. Whilst I give the authors the benefit of the doubt given concurrency and explaining similarities, it does temper my score slightly, given it is not clear how the author have attempted to differentiate the paper for this submission.

I will refer to the AC as to whether I should consider these papers, my current score does not reflect these papers.

### Questions
See weaknesses.

It is mentioned that the network is time-independent, however, if it is the same as Prop 1 in [1] as discussed in section 5, then it would need to condition on time it seems. Is it really the same as in Prop1 of [1] or can the term in Prop1 of [1] be simplified to be time independent?

[1]  Shi eta.  Simplified and generalized masked diffusion for discrete data, 2024.

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
5

### Summary
The paper introduces a reparameterized absorbing discrete diffusion (RADD) framework, which reinterprets the concrete score of a masked diffusion process as a conditional distribution on the clean data. This approach allows for modeling the backward process independently of the timestep t, significantly reducing the number of function evaluations required during sampling. Additionally, the paper establishes a connection between discrete diffusion and any-order autoregressive models, offering greater flexibility in choosing the training loss, sampling procedure, and likelihood evaluation.

### Strengths
The paper presents a theoretically sound method for reframing score entropy discrete diffusion as a denoising prediction. The insight drawn from its connection to any-order autoregressive models is particularly valuable. Furthermore, the experimental results provide strong support for the claims made in the paper.

### Weaknesses
Most of the theoretical results in this paper align with concurrent and prior research. For instance, time-independent parameterization is also discussed in [1]; t-DCE and tau-CDE are introduced in [1] and [2], with [2] additionally proposing a caching trick to enhance sampling efficiency.

Moreover, the connection between masked diffusion and any-order autoregressive models is established in [3, Appendix C]. It would be appropriate to give proper credit to that work.

Nevertheless, I believe this paper offers valuable contributions and insights, with experimental results that strongly support its claims.

### Questions
The parametrisation of the any-order auto-regressive model (AO-ARM) is unclear to me. Given a denoising model p_\theta(x_0 | x_t) trained with the t-DCE loss for instance, could it be reparametrised as an AO-ARM? It would be helpful to include a seesion in the appendix discussing the parametrisation of AO-ARM and to provide both the training and sampling algorithm of AO-ARM in appendix F.

### Soundness
3

### Presentation
3

### Contribution
3
