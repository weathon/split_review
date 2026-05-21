---
job_id: 3f224dee-7345-4ac5-9930-cc3356c2f50b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: SA8xDYrUYB.pdf
paper: Purrception: Variational Flow Matching for Vector-Quantized Image Generation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically generative modeling, variational inference, flow matching, and representation learning for vision in vector-quantized latent spaces.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific structure, including abstract, introduction, background/method, experiments, quantitative and qualitative results, related work, and conclusion/limitations, and it presents a technically coherent method with nontrivial empirical evaluation.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions targeting automated reviewers, or suspicious embedded text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper introduces Purrception, a variational flow matching method for image generation in vector-quantized latent spaces. The key idea is to learn a categorical posterior over codebook indices while computing the induced flow velocity in the continuous embedding space, with training reducing to a cross-entropy objective over latent code indices. The paper evaluates the approach on class-conditional ImageNet-1k \(256\times256\), comparing against continuous and discrete flow matching baselines, and studies convergence speed, temperature scaling, and final FID performance.

## Strengths
1. The paper addresses a real modeling mismatch in VQ latent generation. The framing in Section 3 is sensible: continuous latent FM preserves geometry but ignores discrete code identity, while purely discrete methods use token supervision but discard codebook geometry. This is a clean motivation, and the proposed hybrid treatment is conceptually natural.

2. The method itself is simple and easy to implement. Equations (12) to (15) make the core construction fairly transparent: predict a categorical distribution over codebook entries, form the posterior mean
\[
\mu_t(z_t)=\sum_{k=1}^K \pi_t^{\theta,k}(z_t)e_k,
\]
then use the induced velocity
\[
v_t^\theta(z_t)=\frac{\mu_t(z_t)-z_t}{1-t}.
\]
That connection between categorical supervision and continuous transport is the main technical contribution, and it is at least internally consistent with the VFM view summarized earlier in the paper.

3. The empirical convergence comparison in **Figure 3** is one of the stronger parts of the submission. The curves for both DiT-L/2 and DiT-XL/2 show a fairly consistent advantage for Purrception over CFM, CFM-endpoint, and DFM in terms of FID versus training iterations. Even if one debates the exact causal explanation, the figure does support the practical claim that the method reaches a given FID level earlier.

4. The temperature-control analysis is a useful addition rather than empty garnish. **Figure 4** shows a nontrivial U-shaped dependence of FID on softmax temperature, and **Figure 5** qualitatively illustrates the tradeoff the paper discusses: low \(\tau\) produces cleaner but simpler images, while high \(\tau\) yields more texture and also more artifacts. This is one of the few places where the hybrid discrete-continuous design produces an inference behavior that is clearly distinct from plain continuous FM.

5. **Table 1** provides useful positioning against a broad range of model families, including autoregressive, continuous diffusion, and discrete latent approaches. The paper is appropriately honest that Purrception does not beat top continuous diffusion baselines such as DiT-XL/2 or SiT-XL/2, while still showing competitive performance relative to several VQ-based approaches. That makes the contribution easier to assess.

6. The paper is generally readable. **Figure 2** helps communicate the train/sample pipeline clearly, especially the distinction between latent interpolation, categorical prediction over codebook entries, and decoding through the frozen tokenizer-decoder pair. The appendix discussion of training instability and the use of the \(z\)-loss is also practically relevant.

## Weaknesses
1. **The novelty is narrower than the paper sometimes suggests.**  
   At a high level, the proposal is a fairly direct specialization of Variational Flow Matching with a categorical variational posterior to the VQ-latent setting. The paper itself already points to CatFlow-style categorical VFM in Section 2.2 and to continuous diffusion for categorical data in Section 5. Because of that, the conceptual jump from prior VFM to Equations (12) to (15) is not very large. What is new here is mainly the adaptation to VQ image latents and the empirical demonstration that the hybrid formulation is useful in this domain. That is a valid contribution, but the paper occasionally overstates this as if it established a substantially new modeling principle rather than a fairly natural domain transfer of existing VFM machinery. This matters for the contribution rating, because ICLR main track standards are not only about whether an idea works, but also how much intellectual distance it travels beyond prior frameworks.

2. **Some of the mathematical presentation is too compressed, and a few key assumptions are left implicit.**  
   The transition from the general VFM formulation in Equations (6) and (7) to the VQ-specific cross-entropy loss in Equation (14) is intuitive, but not fully spelled out. In particular, Equation (14)
   \[
   \mathcal{L}_{\text{Purr}}(\theta)=-\mathbb{E}_{t,x,z_t}[\log q_\theta(c\mid z_t)]
   \]
   implicitly treats each latent position as conditionally factorized and supervised with a categorical label, but the paper does not explicitly define whether \(c\) denotes the full latent grid or one code per site, nor how the factorization over spatial positions is handled in the notation. This is hinted at in Figure 2, where the DiT predicts distributions “for each patch,” but the formal objective in the main text is written as if there were a single categorical variable.  
   Similarly, Equation (13) uses a posterior mean over codebook embeddings to define the velocity, but if the model predicts site-wise independent categoricals, the induced velocity on the full latent tensor is also site-wise factorized. That modeling assumption may be perfectly reasonable, but it should be stated explicitly because it defines what dependencies the variational posterior can and cannot represent. Right now, the notation papers over this. For a paper whose central contribution is an inference reformulation, the math section should be sharper.

3. **The sampling dynamics near \(t=1\) are under-discussed, despite the singular-looking factor \((1-t)^{-1}\).**  
   Equation (13) and the sampling algorithm in **Figure 6** both use
   \[
   v_t(z_t)=\frac{\mu_t(z_t)-z_t}{1-t}.
   \]
   This is standard for linear interpolation, but in practice such parameterizations can be numerically delicate near the endpoint. The paper states that Euler integration with 100 or 250 steps is used, but it does not discuss whether any clipping, terminal-time offset, or solver-specific stabilization is needed. This omission matters because the method’s claimed efficiency advantage depends not just on optimization speed, but also on stable and reliable ODE sampling. Since the paper emphasizes training convergence, I would still want a sentence in the main paper clarifying how the endpoint singularity is handled in implementation and whether the same treatment was used across Purrception and the flow-matching baselines.

4. **The empirical scope is still fairly narrow relative to the breadth of the claims.**  
   The paper makes broad claims about “bridging continuous transport and discrete supervision” for vector-quantized generation, but the evaluation is concentrated on a single benchmark, ImageNet-1k at \(256\times256\). Yes, two tokenizers are used across different experiments, and Table 2 in the appendix is informative, but the main paper’s central evidence comes from one dataset and one resolution regime. There is no evidence on unconditional generation, other image domains, higher resolutions, or tasks where VQ geometry might matter even more. This matters because the paper is selling a modeling principle, not merely a one-benchmark trick. Without broader validation, it is hard to know whether the observed gains are robust or particularly favorable to the chosen ImageNet + DiT + tokenizer setup.

5. **Several experimental comparisons are weaker than they could be, especially around fairness and attribution of gains.**  
   The convergence plots in **Figure 3** are compelling visually, but the attribution “categorical supervision + geometry-aware transport causes faster optimization” is more asserted than isolated. The CFM-endpoint baseline is a useful addition, but the paper still changes more than one ingredient across methods: target parameterization, output space, and loss type. An ablation that keeps the exact same network head and varies only the supervision target, or one that compares different decoding/projection choices from continuous outputs back to indices, would have helped disentangle whether the gains come from the VFM principle itself, from easier classification-style supervision, or from better alignment with the tokenizer.  
   Also, the paper states in Section 4.1 that all images are sampled with Euler and 100 steps “for a fair comparison,” but there is no discussion of whether each baseline is near its own best inference setting. That matters because some methods can be disproportionately sensitive to sampler choice and step count.

6. **The final benchmark results are respectable but not strong enough to fully support some of the stronger positioning claims.**  
   **Table 1** shows Purrception at FID 3.88 with 750M parameters, which is competitive against several VQ-based and discrete methods, but it remains clearly behind strong continuous baselines such as DiT-XL/2 at 2.27 and SiT-XL/2 at 2.06. The paper acknowledges this, which I appreciate, but then still uses language like “state-of-the-art approach, among VQ-based latent generative models” and “bridge the fidelity of continuous diffusion with the categorical training objective.” I think the first part is arguable only within a narrow subset of methods and tokenizers, and the second is more aspirational than demonstrated. The main result is better framed as a practically appealing hybrid baseline with faster convergence than FM baselines, not yet as a clearly leading generative model.  
   A related issue is that **Table 1** mixes methods with different tokenizers, reconstruction bottlenecks, training durations, and likely evaluation conventions. The comparison is still useful, but the table should be interpreted cautiously, and the discussion should be less triumphalist.

## Questions
1. In Equation (14), can the authors clarify the exact factorization of \(q_\theta(c\mid z_t)\)? Is \(c\) the entire \(32\times32\) grid and the likelihood factorizes over positions, i.e.
   \[
   q_\theta(c\mid z_t)=\prod_{d=1}^{D} q_\theta(c_d\mid z_t),
   \]
   or is some structured dependence modeled across sites? A precise statement here would improve both the mathematical clarity and the interpretation of the variational approximation.

2. For Equation (13) and the Euler sampling algorithm in Figure 6, how is the \(1/(1-t)\) term handled numerically near \(t=1\)? Do you stop at \(t=1-\varepsilon\), clip the denominator, or rely on the discretization to avoid instability? A short explanation would increase confidence in the robustness of the method and the fairness of the baseline comparisons.

3. Can the authors provide more evidence that the convergence gains in **Figure 3** come from the hybrid VFM formulation rather than mostly from switching to a classification-style target? For example, is there an ablation using the same model head and the same continuous latent representation but alternative losses or projection schemes?

4. The tokenizer dependence appears important, and the appendix **Table 2** suggests the method is quite sensitive to VQ quality. Could the authors summarize this dependence more directly in the main paper? In its current form, a reader could overestimate how tokenizer-agnostic the method is.

5. On the temperature analysis, **Figure 4** is interesting, but can the authors say more about whether the optimal \(\tau\) depends strongly on solver step count, guidance strength, or tokenizer choice? If \(\tau\) is to be promoted as a practical control knob, this sensitivity matters.

6. It would help to report at least one compute-oriented metric beyond iterations, for example wall-clock time to a target FID, or effective training FLOPs to reach the same FID threshold as CFM/DFM. Since the paper’s main practical claim is faster convergence, a compute-normalized comparison would make that claim materially stronger.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The concerns are limited and fairly standard for image generation work, not unique to this paper. The Ethics Statement on **Page 10** already acknowledges misuse risk. Since the method is trained on ImageNet and generates realistic images, there are familiar concerns around misuse for deceptive or unauthorized content generation, and around compliance with dataset licensing and downstream deployment practices. I do not see an immediate red flag requiring special intervention, but these concerns are relevant enough to flag given the application domain.

## Soundness Rating
3: good. The core method is technically plausible and the main empirical claims are mostly supported, but the mathematical exposition is somewhat underspecified and the experimental scope is narrower than the general framing suggests.

## Presentation Rating
3: good. The paper is readable and the figures are helpful, especially Figures 2 to 5, but the notation around the variational posterior and latent-grid factorization should be tightened, and some claims are stronger than the evidence warrants.

## Contribution Rating
3: good. This is a useful and practically relevant adaptation of VFM to VQ image generation, with convincing convergence results, but the conceptual novelty is moderate and the final generative performance does not yet redefine the frontier.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper presents a clean and useful hybridization of categorical supervision and continuous transport for VQ image generation, and the convergence results are compelling enough to make it worth sharing with the community. At the same time, the novelty is more incremental than the presentation implies, and the empirical/theoretical support is not broad enough for a stronger accept.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with flow/diffusion-style generative modeling and VQ latent modeling, though some implementation details and the exact variational factorization would benefit from author clarification.