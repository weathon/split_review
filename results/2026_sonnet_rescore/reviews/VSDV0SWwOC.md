## Summary

LS-Merge proposes a framework that encodes LLM weights into a VAE latent space, performs merging operations there, and decodes back to weights. The three contributions are: (1) an empirical analysis of LLM weight statistics motivating the encoder design (heavy tails, high kurtosis), (2) a transformer-based VAE with two-stage curriculum training, and (3) a heterogeneous merging protocol using dimensionality projection and OT-based latent alignment. The paper demonstrates latent-space interpolation consistently outperforming weight-space baselines for LoRA expert merging, and shows modest cross-architecture capability.

---

## Strengths

- **Heavy-tailed weight distribution analysis (Table 1):** The paper reports excess kurtosis up to 15.05 in self-attention layers of Gemma-3 models, directly motivating an encoder that preserves rare high-magnitude parameters. This is concrete, model-specific evidence informing design choices, not a generic claim.

- **Latent-space expert merging substantially outperforms weight-space baselines (Table 3):** LS-Merge(soup) achieves 56.0 MMLU, 60.1 HellaSwag, and 56.1 NLQGraph, compared to Greedy Soup's 50.8, 54.6, and 52.9. The improvements are large and consistent across all but one metric (K-Crossword), providing strong support for the core claim.

- **Competitive with activation-informed methods without activation access (Table 4):** On Llama-2-13B merged models, LS-Merge achieves 55.07 MMLU and 36.41 IFEval vs. AIM's 54.18 and 32.00, matching a method that requires model activations. This is a meaningful finding for the weight-merging community.

- **Non-linear manifold necessity demonstrated empirically (Table 8):** PCA-reconstructed Gemma-3-1B-it collapses to near-random MMLU accuracy (25.50 at r=1.6) while the VAE retains 39.89 (base: 41.44) and remains stable even at r=4.0. This is a clear, reproducible finding that justifies the non-linear VAE architecture.

- **Zero-shot VAE generalization at low compression (Table 7):** A VAE trained exclusively on Gemma-3-4B-it maintains near-base accuracy on unseen Gemma-3-1B-it (MMLU 39.98 vs. base 40.76) and LLaMA-3.2-1B-it (Winogrande 61.25 vs. 61.56) at r=1.6, showing that weight-structure representations transfer across architectures at moderate compression.

- **MLP/attention complementarity validated (Table 6):** Merging only attention layers degrades performance (WinoGrande 56.67 vs. 56.83 base), merging only MLPs gives modest gains, and combining both achieves the best results. This ablation provides mechanistic insight into functional organization.

---

## Weaknesses

### Fatal
None.

### Major

- **Self-merging mechanism unestablished.** Table 2 shows the headline result: Gemma-3-1B-it MMLU improves from 32.20 (base) to 35.13 with self-merging (sampling multiple posterior codes and averaging them). The paper explains this as "exploring the learned parameter distribution" and attributes stronger gains on the smaller model to "tighter capacity constraints" (Section 4.1). Neither is mechanistically grounded. Averaging posterior samples from a well-trained VAE approaches the posterior mean (MAP estimate), which is a form of regularization or denoising — not a conceptually distinct "merging" operation. The paper does not characterize posterior variance, does not ablate the number of samples drawn, and does not test the prediction that tighter posteriors should yield less benefit from multi-sample averaging. Without this analysis, it is unclear whether the 9% relative MMLU gain is genuine latent-space exploration or the VAE acting as a weight regularizer, which would be a narrower and less generalizable claim. This is the paper's first-listed contribution and the only experiment involving single-model augmentation; it needs mechanistic grounding.

- **Task Arithmetic baseline in Table 4 shows pathological failure.** Task Arithmetic achieves 4.20% on GSM8k — identical to the base model — even though the individual code-only model scores 24.10% and the instruct model scores 43.40%. This is a failure mode inconsistent with normal Task Arithmetic behavior; task vector coefficients that are off by enough to cancel both improvements while leaving MMLU unchanged are unlikely to result from a correct implementation. The paper does not report the specific hyperparameters (task vector scaling coefficients) used for Task Arithmetic, making it impossible to verify the comparison is fair. If Task Arithmetic is misconfigured, the comparison in Table 4 significantly overstates LS-Merge's relative advantage on GSM8k. (Note: AIM achieves 46.20% on GSM8k compared to LS-Merge's 44.12%, so the AIM comparison is unaffected.)

### Minor

- **Cross-family merging gains are small and partially undermined by OT-only degradation.** Table 5 shows OT+interp at λ=0.1 achieves WinoGrande 57.75 vs. base 56.83 (+0.92), ARC-C 43.34 vs. 42.78 (+0.56), HellaSwag 50.10 vs. 49.07 (+1.03). The OT-only row degrades substantially below base on WinoGrande (51.13 vs. 56.83), indicating the OT alignment itself is imperfect and the benefit at λ=0.1 may stem more from mild interpolation than from a principled alignment. No variance or statistical significance is reported for these differences. The paper's claim that this "enables cross-family merging" is technically supported but needs more cautious framing — the gains are modest and the optimal injection weight is very low (only 10% source contribution).

- **VAE training data insufficiently specified.** Section 4 states: "Training data consist of pretrained weight snapshots for Gemma-3-1B-it and Gemma-3-4B-it." The number of distinct snapshots, their provenance (multiple fine-tuning runs, checkpoints from training, etc.), and whether the evaluation models' weights appear in the training set are not stated. This matters for interpreting the reconstruction quality in Table 2 — if the VAE was trained on those exact weights, reconstruction improvements may reflect memorization rather than learned weight-structure generalization.

- **Evaluation code inconsistency between Table 3 and Table 4.** Table 3 (expert merging) uses the authors' custom evaluation code, while Table 4 (comparison to AIM and Task Arithmetic) uses lm-eval, with the paper stating "for fair comparison with the baselines." If lm-eval is appropriate for fair comparison, the expert merging results in Table 3 are reported under a different standard and may not be directly comparable to published baselines on the same tasks.

### Trivial

- **Theoretical framing in Section 3.1** uses the Eckart-Young theorem and manifold embedding results to justify VAE compression, but these results establish only that a compressive map *exists* — not that the specific transformer-VAE will find it or that it will be smooth under interpolation. The motivation is reasonable as inspiration for the empirical approach, but the theoretical claims should be softened from "confirms" to "suggests."

---

## Nice-to-Haves

- A latent trajectory analysis: plot downstream performance as λ varies from 0 to 1 for both latent-space and weight-space interpolation to show that the latent trajectory is smooth (no performance valley at intermediate λ) while weight-space interpolation degrades non-monotonically. This would directly demonstrate *why* latent-space merging is geometrically superior.
- Ablation on posterior sample count for self-merging, showing how performance changes with 1, 2, 4, 8 samples. This would clarify whether multi-sample averaging provides meaningful exploration or trivially converges after a few samples.
- Computational cost analysis: encoding time and GPU memory for Llama-2-13B through the transformer-VAE, to assess practical scalability.
- Wider λ sweep for cross-family merging (Table 5) beyond just λ=0.1, to demonstrate that gains are robust across a range rather than cherry-picked at the optimal.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **OT Gaussian assumption vs. heavy-tailed weights (Harsh Critic, Section 3.3):** The critic argues the Gaussian OT map is internally inconsistent with the paper's own finding that LLM weights are heavy-tailed. However, the OT alignment is applied to the *VAE latent codes*, not to the raw weights. The VAE's KL term (Equation 1) explicitly regularizes the latent distribution toward a standard Gaussian. The Gaussian OT approximation is applied in the correct domain (latent space), not in weight space. This criticism misunderstands what the OT is applied to. REMOVED.

- **Tables 7 and 8 inconsistency (Harsh Critic):** The critic flags that Table 7 shows the cross-generalization VAE (trained on 4B-it, tested on 1B-it) collapsing to 25.02% MMLU at r=4, while Table 8 shows the in-distribution VAE maintaining 39.83% at r=4. This is not an inconsistency — it is a direct demonstration of the generalization gap, which the paper discusses explicitly in Section 5.2: "performance degrades substantially at higher ratios." The two tables serve different purposes (cross-generalization vs. in-distribution), and both are clearly labeled. REMOVED.

- **Strength: "Self-merging improves single model" as generic strength (Strength Finder):** While the numerical result in Table 2 is real, the mechanism is unestablished (see Major weakness above). The strength is retained factually but the mechanistic claim is disputed.

- **Strength: "Zero-shot generalization" as generic strength (Strength Finder):** The strength is valid at r=1.6 but qualified at higher compression ratios. Retained with caveat already noted.

- **Missing related works (Harsh Critic, per standing rules):** Per review rules, no related work criticisms are included. REMOVED.

- **Lack of confidence intervals for Table 5 (Harsh Critic):** The gains are small and uncertainty would be informative, but single-run evaluation without confidence intervals is standard in this field for large model evaluations. Moved to nice-to-have. REMOVED from weaknesses.

- **PCA comparison is not "apples-to-apples" (Harsh Critic, Section 5.3):** PCA is a linear reconstruction baseline, and the VAE was trained specifically to reconstruct these weights. The comparison is not a head-to-head fair competition — it is an ablation between linear and non-linear compression. The paper is transparent about what it is showing (Section 5.3 is titled "Linear Subspace vs. Non-Linear Manifold Learning"). The result validly supports the architectural choice, even if PCA is inherently disadvantaged. The request for a "trained MLP autoencoder" baseline would be a nice-to-have, not a required comparison. REMOVED as weakness; noted in nice-to-haves.

---

## Novel Insights

The most genuinely novel observation in the synthesis is the pairing of two findings: (1) the VAE posterior, when sampled multiple times and averaged, consistently improves over single-sample reconstruction (Table 2), and (2) the VAE maintains stable performance at r=4.0 compression while PCA collapses at r=1.6 (Table 8). Together, these suggest that the learned latent manifold is not merely a compression artifact but captures a smooth, functionally meaningful neighborhood around pretrained weight configurations — one that can be perturbed (via multiple posterior samples or interpolation) and still remain in a high-performance region. This "functional neighborhood" hypothesis, if developed mechanistically with posterior variance analysis, could become a principled account of why weight-space operations in a VAE latent space are qualitatively different from direct weight interpolation.

---

## Suggestions

1. **For the self-merging claim**: Ablate the number of posterior samples (1, 2, 4, 8, 16) and plot the resulting MMLU against sample count. If the gain saturates after 2–3 samples, it is consistent with simple averaging toward the posterior mean; if it grows with samples, it suggests genuine exploration. Report the posterior variance (e.g., mean KL per layer) to help readers understand the regime.

2. **For Task Arithmetic in Table 4**: Report the specific task vector scaling coefficients used. If they were not tuned (e.g., λ=1.0 default), report results across several values (0.2, 0.5, 0.8, 1.0) or state that the default was used. This ensures the comparison reflects the method as it would be used in practice.

3. **For cross-family merging**: Report Table 5 across at least three λ values (0.05, 0.10, 0.20) in the main paper to show the robustness of the gain to the choice of injection weight. Also characterize the per-layer latent distributions empirically (e.g., Q-Q plots against Gaussian) to confirm or qualify the Gaussian OT assumption.

4. **Clarify training data in Section 4**: Specify how many distinct weight snapshots were used to train the VAE, whether the evaluation models' weights appear in the training set, and if so, how the in-distribution/out-of-distribution split is handled. A single sentence resolves this ambiguity.

5. **Add a computational cost section**: Report VAE encoding time and GPU memory for at least one large model (e.g., Llama-2-13B) to allow practitioners to assess practicality.

---

## Score and Decision

**Originality:** The paradigm of encoding LLM weights in a VAE for architecture-agnostic merging is genuinely novel and well-motivated. (4/5)

**Importance:** Model merging is a practically significant and growing field; enabling heterogeneous merging removes a fundamental limitation. (4/5)

**Claims supported:** The expert merging claim (Table 3) is strongly supported. The self-merging mechanism is under-explained. Cross-family gains are modest. Task Arithmetic baseline raises questions. (3/5)

**Soundness:** The transformer-VAE with curriculum training is well-motivated and the OT alignment is theoretically principled (applied correctly to the latent space). Experimental setup has some transparency gaps. (3/5)

**Clarity:** The framework is clearly described and illustrated. Evaluation code inconsistency and training data sparsity reduce clarity. (3/5)

**Community value:** Latent-space model merging is a useful tool; the detailed empirical analysis of weight distributions and the PCA vs. VAE ablation are directly useful to the community. (4/5)

The paper makes a real and novel contribution with strong evidence for its core claim (latent-space expert merging). The self-merging mechanism needs mechanistic grounding, and the cross-family merging results, while promising, are more modest than the paper implies. These are addressable in revision. The paper clears the bar for acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>