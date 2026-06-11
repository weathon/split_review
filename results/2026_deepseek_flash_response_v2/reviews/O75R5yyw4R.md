## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) MCMC transitions to iteratively refine intermediate states via reward-guided noising-denoising processes. The method is evaluated on MDLM, LLaDA-8B (text), and MaskGIT (image) against several baselines including BoN, SoP, SVDD, and FK Steering. IterRef consistently outperforms baselines across tasks and compute budgets, with a particularly informative analysis showing that more refinement iterations (k) matter more than more particles (N).

## Strengths

- **Principled MCMC-based refinement for discrete diffusion**: IterRef addresses the underexplored problem of test-time scaling for discrete diffusion, where token discretization prevents gradient-based guidance and tokens cannot be corrected once generated. The noising-denoising kernel design within the MTM framework is a well-motivated approach to these challenges, and Proposition 1 establishes convergence to the reward-aligned target distribution (detailed balance guaranteed).

- **Tractable design via balancing function**: The specific choice of transition kernel and balancing function (Eq. 2) reduces importance weights to uniform sampling (w_n = 1/N) and the acceptance rate to a simple reward comparison β = min(1, exp((r(x_t') − r(x_t))/α)). This makes the MTM machinery computationally practical — the expensive rejection step becomes a lightweight reward-gap comparison.

- **Consistent empirical outperformance across modalities**: IterRef outperforms four baselines on MDLM (all four tasks: Toxicity, Sentiment, CoLA, Perplexity), LLaDA-8B (three of four tasks), and MaskGIT (CLIPScore across all compute budgets). The gains are often substantial — e.g., reaching Toxicity scores at 4T NFE that baselines only match at 32T NFE (8× faster).

- **Informative analysis of k vs N (Table 3)**: The experiment varying iteration count and particle count is one of the paper's strongest contributions. It convincingly shows that more iterations (k=8, N=4) outperform more particles (k=1, N=32) at equal compute, directly supporting the iterative refinement thesis.

- **Timestep analysis (Table 2)**: The study of which denoising steps benefit most from refinement provides practical insight — later stages are more effective, contrasting with continuous diffusion where early steps dominate.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation circularity: reward model and metric are the same for language tasks**: For the four language tasks (Toxicity, Sentiment, CoLA, Perplexity), the reward model being optimized is the same function used for evaluation (Section 4.1). This means the results demonstrate IterRef is effective at optimizing its objective, but broader claims about "generation quality" are not supported by held-out metrics. The paper mentions ImageReward scores in the appendix for images (line 254) but provides no analogous held-out evaluation for text. This is a common limitation in the reward-guided generation literature, but it limits what can be concluded from the main results.

### Minor

- **Proposition 1 is a standard MTM guarantee, not a novel theoretical result**: The proposition states that applying MTM with a valid kernel and balancing function yields detailed balance and convergence — this is a known property of the MTM framework (Liu et al., 2000). The paper presents this as a key contribution (line 35: "we provide a theoretical guarantee"), but the real contribution is the specific construction of the kernel and balancing function, not the convergence guarantee itself. The assumption that q and p_θ form a reversible kernel (line 146) is stated without empirical validation.

- **NFE accounting conflates generative and reward model calls**: The paper aggregates generative-model and reward-model calls into a single NFE count (line 186), while acknowledging this "may obscure meaningful differences" (line 174). Appendix C.4 is cited for wall-clock analysis, but the main paper lacks disaggregated reporting, making it hard to assess whether IterRef's advantage comes from algorithmic efficiency or a different allocation of compute.

- **The noising distance (s − t) is underspecified**: The transition kernel in Eq. 2 involves noising from x_t to x_s (s > t) and denoising back, but the paper does not specify how far s is from t. This is a key hyperparameter that affects both exploration range and computational cost, and its absence makes the method description incomplete.

- **Approximation of r(x_t) not validated**: The intermediate reward r(x_t) is approximated by evaluating the reward on the model's single point estimate of x_0 (line 117) rather than the expectation over p_θ(·|x_t). This approximation is a potential source of bias, especially at early timesteps, but is not empirically examined.

- **High minimum compute floor**: With T=1000 denoising steps for MDLM, IterRef's best performance at 2T NFE means a minimum of 2000 function evaluations. The claim of "effectiveness at low NFE" should be qualified relative to this floor.

### Trivial
None.

## Nice-to-Haves

- Held-out evaluation metrics for language tasks (e.g., human evaluation, diversity metrics like self-BLEU, or fluency via a different model) to break the evaluation circularity.
- Wall-clock time or disaggregated NFE reporting in the main paper rather than the appendix.
- Ablation comparing uniform proposal selection (current) against reward-weighted selection to clarify whether the MTM machinery's uniform selection + Metropolis acceptance buys anything over simpler rejection sampling.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Pool reuse lacking proof (Harsh Critic's Critical Issue 5)**: References content in the appendix, which was stripped. The instruction says to remove weaknesses about missing appendix proofs.
- **Uniform proposal selection is "oddly argued" (Harsh Critic's Critical Issue 4)**: The uniform selection is a deliberate consequence of the balancing function choice, motivated by tractability. Reward guidance operates through the acceptance step, not the selection step. This is a design choice explained in the paper, not a weakness.
- **Formatting nitpick about acceptance probability formula**: Parser artifact, not an author error.
- **Wang et al. (2025) "re-masking" undercutting novelty**: The paper cites this in related work and describes how IterRef differs — it is not claiming that no one has addressed irreversibility, only that prior methods lack iterative in-situ refinement.
- **Generic strength ("addresses an important problem")**: Removed per filtering policy.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add held-out evaluation for language**: Include at least one metric per task that differs from the reward function (e.g., diversity, human evaluation, or fluency via a different model). This would significantly strengthen the claim that IterRef improves actual generation quality rather than merely over-optimizing the objective.
2. **Disaggregate compute reporting**: Report generative-model calls and reward-model calls separately in the main paper, or include wall-clock time, to make the efficiency comparison more transparent.
3. **Specify and ablate the noising distance (s − t)**: This hyperparameter controls exploration range and should be documented with an analysis of its effect on acceptance rates and output quality.
4. **Validate the r(x_t) approximation**: Compare point-estimate rewards against Monte Carlo estimates of the expectation at different timesteps to quantify bias.

These suggestions are ordered by impact. Point 1 is the most important for substantiating the paper's quality claims; points 2–4 would improve completeness.

## Score and Decision

**Calibration anchors consulted (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Ombm8S40zN (DDPP) | 6.25 | 1, 2 | Closest topic; requires fine-tuning while IterRef is inference-only; similar evaluation scope |
| XsgHl54yO7 (Unlocking Guidance) | 6.50 | 1, 2 | Stronger theoretical framing but narrower empirical scope (no text domain) |
| 2fgzf8u5fP (SVDD) | 3.80 | 1 | Rejected due to alpha=0 issues and unfair comparisons; IterRef is much stronger |
| 4hFT4rfG40 (Plug-and-Play) | 3.75 | 1 | Only tested on toy + protein; IterRef is much stronger |
| tfemquulED (Sampling Demons) | 6.20 | 2 | Inference-time alignment for continuous diffusion only; images-only evaluation |
| 71mqtQdKB9 (SEDD) | 6.60 | 2 | Different topic (language modeling perplexity, not guidance); incomplete experiments noted |
| 1pTlvxIfuV (Reparameterized DDM) | 5.50 | 2 | Different topic (discrete diffusion training, not guidance) |

**Round 1 bracket**: Between 3.5 and 7.5, with closely related anchors at 6.25 (DDPP) and 6.50 (Unlocking Guidance).

**Round 2 narrowing**: Compared against DDPP (6.25, Accept), Unlocking Guidance (6.50, Accept), Sampling Demons (6.20, Accept), and SVDD (3.80, Reject). IterRef is clearly stronger than SVDD, comparable to DDPP and Unlocking Guidance. Its inference-only nature and broader empirical validation (text + image, multiple backbones) place it slightly above DDPP, and its cross-modality coverage matches or exceeds Unlocking Guidance's narrower molecular scope.

**Final score**: 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>