- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces the Data-Prediction Denoising Model (DPDM), a multi-step generative model designed to address the performance degradation of diffusion models when sampling steps are limited (≤10 NFEs). The key insight is that diffusion models trained with L₂ denoising objectives produce denoisers that output conditional expectations, which become blurry under high noise. DPDM improves these denoisers by minimizing a smoothed KL divergence between the denoised data distribution and the clean data distribution. The paper evaluates DPDM on data distribution recovery (denoising FID) and few-step image generation on CIFAR-10 and ImageNet 64×64, reporting significant improvements over baselines including EDM, consistency models, progressive distillation, and solver-based methods.

## Strengths

- **Empirical identification of the root cause of poor few-step DM performance**: Section 3.1 demonstrates (via Figure A.4 and analytical reasoning) that DM denoisers trained with the L₂ objective produce blurred outputs under high noise, directly motivating the DPDM approach. This is supported by quantitative evidence in Table 1, showing order-of-magnitude improvements in denoising FID (e.g., at noise std=0.1, DPDM achieves FID 3.9 vs DM's 33.7).

- **Strong data distribution recovery results**: Table 1 systematically evaluates denoiser quality across 11 noise levels (σ from 0.02 to 10.0), showing DPDM consistently and substantially outperforms baseline DM denoisers at every level. This directly supports the paper's core claim about denoiser strength.

- **Practical training efficiency**: The paper reports concrete training metrics — FID 2.72 within 100k iterations (~13 hours on 4×2080ti GPUs for CIFAR-10) — and compares GPU memory costs with consistency distillation (Table 6), demonstrating the method is computationally feasible.

- **Informative cross-use ablation**: The exploration of four model-sampler combinations (DPDM/DM models × DPDM/DM samplers) in Section 5.2 shows that only the DPDM model paired with its own sampler achieves good FID, while cross-use degrades. This supports the paper's claim that DPDM is a distinct generative model, not merely a variant of the DM sampling procedure.

- **Forthright about limitations**: Section 6 explicitly acknowledges that DPDM is sub-optimal with sufficient sampling steps and that training relies on an auxiliary diffusion model — a level of honesty that strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **Factual inaccuracy about consistency models and LPIPS**: Section 4 states "the CM requires both a learned data metric (i.e. the LPIPS)." This conflates consistency distillation (CD, which does use LPIPS as a metric function) with consistency training (CT, which uses standard L₂ loss, as described in Song et al., 2023). The paper's claimed advantage — that DPDM "does not require any learned neural metric" — is weakened because this advantage applies only against CD, not against CT. This is a verifiable factual error about a directly compared method.

### Minor

- **Training objective is not shown to be tractable in the main text**: Section 3.2 defines the smoothed KL divergence $\mathcal{D}_{\text{smooth-KL}}(q_0,p_0) = \mathcal{D}_{\text{KL}}(q_t,p_t)$ but does not derive a tractable loss function, gradient estimator, or variational bound that can be directly minimized. The KL divergence between $q_t$ and $p_t$ — both distributions over high-dimensional data convolved with Gaussian noise — is not obviously computable. The paper references "Algorithm 1" (in the appendix, stripped by the parser) and mentions alternating updates with an auxiliary DM, but the main text alone does not explain how a reader could implement the core training procedure. While the algorithms exist in the original submission, the paper would benefit from a brief sketch of the tractable objective in the main text.

- **"State-of-the-art" claim is overbroad**: The paper claims "DPDMs achieve the state-of-the-art few-step generation ability among diffusion-based multi-step generative models." The reported comparisons use a controlled setup (same architecture and teacher model for compared methods), which is methodologically sound. However, consistency models in their original publications report competitive FID at substantially fewer steps (e.g., ~2.31 FID at 1 step on ImageNet 64×64 vs. DPDM's 3.66 at 8 steps). The absolute SOTA claim should be scoped to the specific controlled experimental configuration, or the paper should directly explain any discrepancies with the original CD/CT numbers.

- **Proposition 3.1 is near-trivial**: The non-negativity and identifiability properties of the smoothed KL divergence follow directly from standard KL divergence properties. While not harmful, this proposition does not meaningfully advance the theoretical foundation.

### Trivial

None.

## Nice-to-Haves

- The cross-use experiment result (DPDM sampler + DM denoiser performs poorly, DM sampler + DPDM denoiser performs poorly) is presented as supporting the "essentially different" claim, which is reasonable. However, this result could also be interpreted as the denoisers being specialized to a particular noise schedule; a brief discussion of this alternate interpretation would strengthen the analysis.

- Clarify how the smoothed KL objective is extended across the continuous range of noise levels — whether a time-conditioned network is trained jointly on the integrated objective or separate denoisers are trained per noise level.

## Removed Points

These points from the inputs were removed or demoted with justification:

- **"Training objective not specified" as a fatal flaw**: The algorithms (1 and 2) exist in the original submission's appendix, which was stripped by the PDF parser. The paper does reference these algorithms and describes alternating updates with an auxiliary DM. The issue is reduced to a Minor weakness about main-text clarity.
- **"Method not described for multiple noise levels"**: The paper explicitly notes it fixes σ(t)=1 "to make the discussion clear" (Section 3.2), and the sampling algorithm naturally extends across noise levels through iterative denoising-and-noising steps. This is standard expository practice.
- **"Data recovery experiment does not validate central claim"**: This experiment is presented as a separate evaluation task (data distribution recovery), not as a proxy for generation. The paper also separately evaluates generation performance. The use of FID for denoised outputs, while non-standard, is a reasonable distributional distance metric for this purpose.
- **"Cross-use experiment undermines paper's claim"**: The result that DPDM model + DPDM sampler works best while cross-use fails actually supports the paper's argument that DPDM is a fundamentally different model from DM, not a mere sampling variant of it.
- **Missing related works / comparison to BOOT, TRACT**: Instruction prohibits mentioning missing references without external confirmation.
- **Missing code/hyperparameters/experimental details**: These are standard appendix content; the parser stripped the appendix.
- **Statistical significance / confidence intervals**: Single-run FID reporting is standard practice for this evaluation setup; not a meaningful weakness.
- **Formatting nits and typos**: Parser artifacts from PDF extraction, not author errors.
- **Strength Finder's removed strengths**: Generic praise ("addressed an important problem") and claims that conflict with verified weaknesses have been removed or downgraded.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the LPIPS factual inaccuracy and the main-text tractability gap, which are important to address but do not constitute novel observations about the method itself.

## Suggestions

1. **Correct the factual error about CMs and LPIPS** — either specify that CD (not CT) uses LPIPS, or clarify the statement to accurately represent the distinction between CD and CT.
2. **Provide a tractable form of the training objective in the main text** — even a brief derivation showing how D_KL(q_t, p_t) can be estimated (e.g., via a variational bound, density ratio estimation, or score matching equivalence) would significantly improve clarity.
3. **Scope the SOTA claim precisely** — replace "state-of-the-art ... among diffusion-based multi-step generative models" with a more measured statement like "competitive with or better than existing methods under a controlled comparison with identical architecture and teacher."
4. **Add a schematic or pseudocode sketch** in the main text for the training algorithm, so the reader can understand the alternating update procedure without consulting the appendix.
5. **Report FID at matching step budgets** (1, 2, 4 steps) to enable direct comparison with consistency models at identical compute.
