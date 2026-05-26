Now I have sufficient information to synthesize the review. Let me compile everything.

## Summary
2-3 sentence summary of the paper's contribution.

**Strengths** — filtered aggressively: I will only keep strengths that cite specific artifacts and make falsifiable positive claims.

**Weaknesses** — I'll tier them as Fatal/Major/Minor/Trivial. The missing comparison with existing synthetic-data methods is Major. The A-MONO assumption, lack of error bars, compute accounting, and the Figure 4 framing issue are Minor.

**Score**: based on calibration, I'll place this around 6.5 — somewhere between "Self-Consuming Generative Models Go MAD" (6.67) and "Real-Fake" (6.00). The paper has a clever core idea with broad experimental support, but the missing comparisons and unverified theoretical assumption for diffusion models prevent it from reaching the top tier.

Let me write the full review now.

---

## Final Review

## Summary

Neon (Negative Extrapolation from self-traiNing) is a post-hoc method that improves pre-trained generative models by briefly fine-tuning them on their own synthetic outputs, then reversing the resulting parameter update via linear extrapolation. The core insight—that mode-seeking inference samplers cause the synthetic-data gradient to be anti-aligned with the real-data gradient—is proved theoretically for autoregressive models and argued for diffusion/flow models. Empirically, Neon delivers consistent FID improvements across diffusion (CIFAR-10 1.78→1.38), flow matching (3.5→2.32), autoregressive (xAR-L ImageNet 1.28→1.02, a new SOTA), and few-step generators (IMM 1.98→1.46), with as little as 1k synthetic samples and <1% extra fine-tuning compute.

## Strengths

- **New SOTA on ImageNet-256.** Neon elevates the xAR-L model from FID 1.28 to 1.02, surpassing the prior best (UCGM's 1.06), using only 0.36% additional fine-tuning compute (Abstract, Figure 5, Section 4.2). This is a specific, verifiable result.

- **Universal across four model families.** The same three-line algorithm (Algorithm 1) improves EDM (diffusion), Flow Matching, xAR/VAR (autoregressive), and IMM (few-step) on CIFAR-10, FFHQ, and ImageNet (Sections 4.1–4.3, Figures 3, 5, 7). No existing synthetic-data method (DDO, SIMS, Discriminator Guidance) spans this range without architecture-specific modifications.

- **Remarkable data and compute efficiency.** Near-optimal results are achieved with as few as 1k synthetic samples (xAR-L: FID 1.05 with 1k vs. 1.02 with 750k), and fine-tuning budgets are <1% of original training (as low as 0.36% for xAR-L) (Section 4.2, Figure 5). The method works with a single forward-backward pass on a modest synthetic dataset.

- **Cross-architecture transfer.** Using synthetic data from a Flow Matching or IMM model to improve an EDM-VP model (FID 1.97→1.59 and 1.80) demonstrates that the degradation signal transfers across architectures (Figure 8, Section 4.4). This is a genuinely novel capability not shown by prior methods.

## Weaknesses

### Fatal
None.

### Major

- **Missing quantitative comparison with existing synthetic-data training methods.** The related work describes DDO, SIMS, Discriminator Guidance, and Self-Play FT and argues that Neon is simpler (no auxiliary models, no inference modifications). Yet the experimental section contains **no direct FID comparison** with any of these methods on a shared benchmark (e.g., diffusion on CIFAR-10). Without such a comparison, a practitioner cannot assess whether Neon's improvements are competitive with, worse than, or orthogonal to prior approaches. This gap weakens the claim that Neon's simplicity advantage translates to comparable or better efficacy. The paper should include at least one head-to-head comparison on a standard setting.

### Minor

- **Theoretical proof for diffusion/flow models relies on an unverified assumption.** Theorem 2's extension to diffusion and flow models requires the "A-MONO" assumption (curvature-density coupling, footnote 2), which is stated without empirical verification or theoretical derivation from the training objective. While the experiments convincingly show the method works for these models, the claimed *universal* mechanism is weaker for this significant portion of the architecture coverage. The gap between theory and practice for diffusion/flow models should be acknowledged, or the assumption should be empirically validated (e.g., by measuring the monotonic trend on CIFAR-10).

- **No error bars or multiple-seed results.** FID is reported as a single number per configuration. Given that the pipeline involves stochastic fine-tuning and grid search over (w, γ, |S|), the variance of the reported improvements is unknown. Reporting confidence intervals or results over 3 seeds for a representative experiment (e.g., EDM-VP on CIFAR-10) would substantially strengthen the quantitative evidence.

- **Computational cost claims exclude synthetic data generation.** The paper quotes "<1% additional training compute" and "0.36% additional compute" for xAR-L, which refer only to the fine-tuning budget. Generating the synthetic dataset S (up to 750k images) has its own non-trivial cost, especially for autoregressive models where sampling is sequential. The paper should explicitly state what is and is not included in the compute percentages.

- **Framing ambiguity around extrapolation vs. interpolation.** Figure 4 shows the optimal w for EDM-VP on CIFAR-10 is negative (≈ -0.5, i.e., interpolation toward θ_s), yet the caption and surrounding text emphasize "w > 0 corresponds to the negative extrapolation regime where Neon demonstrates its improvement capability." The paper does acknowledge the interpolation regime in Section 3, but the dissonance between the framing and the empirical optimum for a primary model type is confusing. The authors should clarify for each experiment whether the optimal w was positive or negative and discuss the implications.

- **Hyperparameter tuning requires real data access despite "no access" claim.** Contribution C1 states Neon requires "no access to the original training data," yet the optimal (w, γ) are selected by minimizing FID computed on 10k real test samples. This is standard practice but should be acknowledged as a mild form of data requirement.

### Trivial

- Figure 4 caption contains a typo: "w = -1 corresponds to the model directly trained on synthetic data, i.e., θ_Neon = θ_r" should read "θ_Neon = θ_s".

## Nice-to-Haves

- **Direct comparison with DDO/SIMS on a shared benchmark** would be the single most impactful addition and would ground Neon's performance relative to prior work.
- **Empirical check of the A-MONO assumption** for a diffusion model on CIFAR-10 (measuring the monotonic trend of expected gradient norm vs. log p(x₀)) would strengthen the theoretical narrative.
- **Limitations discussion:** The paper would benefit from a paragraph on when Neon might fail or be less beneficial (e.g., models with near-perfect recall, non-mode-seeking samplers, or settings where precision is more important than recall).

## Removed Points

- **Figure 9 lines crossing and "nearly matches" being vague:** The paper provides exact FID values in the text (30k→1.87 vs. 50k→1.85), so the visual ambiguity is a presentation issue, not a substantive gap. Removed.
- **Missing limitations discussion:** This is a nice-to-have, not a weakness per se. Moved to Nice-to-Haves.
- **Ablation study quality:** The critic's concern about Figure 9 crossing lines is adequately addressed by the numeric values in the text. Removed.
- **General concerns about reproducibility (hyperparameters, implementation details):** The paper uses standard training recipes with reduced learning rate (Appendix C). These are standard practices; removing.

## Novel Insights

The meta-review reveals a disconnect between the theory's claimed universality and its actual coverage: the anti-alignment proof is rigorous for autoregressive models (temperature, top-k, top-p) but depends on an unverified curvature-density coupling for diffusion/flow. The experiments validate the method empirically across all model types, but this means the theory is partially a post-hoc justification rather than a predictive guarantee for diffusion models. Additionally, the optimal w being negative (interpolation) for the EDM-VP model while the paper is titled "Negative Extrapolation" suggests the key mechanism—reversing self-training degradation—is more general than the specific sign of w: what matters is the existence of *some* merge that improves over the base model, regardless of whether it is extrapolation or interpolation. The paper could be reframed around this broader finding.

## Suggestions

1. Add a direct FID comparison with at least one existing synthetic-data method (DDO on CIFAR-10 diffusion, or SIMS) to ground the claims of simplicity vs. efficacy.
2. Report 3-seed means and standard deviations for a representative experiment (e.g., EDM-VP on CIFAR-10) to establish statistical reliability.
3. Either empirically validate the A-MONO assumption for a diffusion model or explicitly soften the theoretical claim for non-autoregressive models.
4. Clarify that the compute percentages exclude synthetic data generation, and provide a rough estimate of that cost.
5. Add a table or rule-of-thumb for when w is positive (extrapolation) vs. negative (interpolation), linking to sampler properties.

## Score and Decision

I performed a two-round calibration search. In Round 1, I queried papers on "generative model improvement self-training synthetic data negative extrapolation" across three score bands (weak: <3.5, mid: 3.5–7.5, strong: >7.5), plus weakness-anchored queries on "missing comparison with existing synthetic data training methods" and "assumption not empirically verified for diffusion models theory." In Round 2, I queried for anchors in the 5.5–7.5 range on the most topical aspects. I read 7 anchors in full.

**Round‑1 bracket:** The paper clearly exceeds the low-band anchors (avg 2.0–3.4, which are papers with unclear presentation and weak experiments). It sits below the high-band anchors (avg 8.0, which have airtight theory and extremely thorough evaluation). The plausible bracket is 5.5–7.5.

**Round‑2 narrowing:** I compared the paper to mid-band anchors read in full:
- *Self-Consuming Generative Models Go MAD* (6.67, Accept): Similar topic area, comparable mix of theory and experiments. Neon has a more novel core idea (turning degradation into improvement) but lacks the comparison baselines that MAD includes. Comparable or slightly below.
- *On the Stability of Iterative Retraining* (6.75, Accept): Similar topic, accepted despite some unverified assumptions and single-seed experiments. Neon has broader experimental scope. Comparable.
- *Real-Fake: Effective Training Data Synthesis* (6.00, Accept): Strong results but incremental ideas. Neon's core idea is more novel. Above this.
- *Simple ReFlow* (7.00, Accept): Thorough ablations, SOTA results but incremental improvements. Neon has a more novel idea but less thorough evaluation (no error bars, missing comparisons). Slightly below.
- *Collapse or Thrive?* (5.75, Reject): Incremental, some reviewers found it unpolished. Neon is clearly stronger.

The low-band anchors fail at: unclear presentation, weak contributions, insufficient experiments. The Neon paper shares **none** of these failures. The mid-band anchors that were rejected (e.g., Collapse or Thrive? at 5.75) suffered from incremental contributions and unpolished presentation—issues Neon does not have.

The paper's single most significant gap relative to the strongest mid-band anchors is the **missing direct comparison with existing synthetic-data training methods** (DDO, SIMS). This is a Major weakness that prevents the paper from reaching the 7+ tier. The A-MONO assumption for diffusion models is a secondary concern.

**Final score:** 6.5. The paper presents a clever, well-demonstrated idea with broad architectural coverage and a new SOTA result. The missing comparisons and unverified theoretical assumption for diffusion/flow models are real gaps that should be addressed before publication but do not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>