## Summary
WithAnyone addresses the "copy-paste artifact" in identity-consistent (ID-consistent) image generation—where models excessively replicate reference faces rather than preserving identity flexibly. The paper makes three contributions: (1) **MultiID-2M**, a 2M-image dataset with ~500k paired group photos of celebrities, each identity having ~400 diverse reference images; (2) **MultiID-Bench**, a benchmark with a novel copy-paste metric that uses ground-truth-aligned face similarity (Sim(GT)) rather than reference similarity (Sim(Ref)); and (3) **WithAnyone**, a FLUX-based model trained in four phases with GT-aligned ID loss and InfoNCE-based contrastive loss with a large negative pool, achieving competitive Sim(GT) while markedly reducing copy-paste.

---

## Strengths

- **Crisp problem formalization**: The paper clearly identifies and quantifies the copy-paste failure mode with a principled angular-distance metric (Eq. 2). The observation that Sim(Ref) incentivizes trivial copying while Sim(GT) penalizes it is genuinely insightful and directly actionable for the broader community designing future benchmarks.

- **GT-aligned ID loss**: Using GT face landmarks to align generated images before ArcFace extraction—instead of predicting noisy landmarks from partially denoised images—is an elegant and practically impactful design choice. Figure 7 clearly shows that GT-alignment produces lower and more stable ID loss across all noise levels, validating the idea empirically.

- **Dataset and benchmark scale**: MultiID-2M is a large-scale, carefully curated paired dataset that addresses a known gap (multi-ID with diverse per-identity references). The benchmark (435 test cases, 1–4 people per case) uses long-tail identities with no training overlap and standardizes evaluation—a real community service, since prior works sample from CelebA ad hoc.

- **Empirical breadth**: Comparison against 14 diverse baselines (general customization + face-specific) across two benchmarks (MultiID-Bench and OmniContext), with ablations and a user study, presents a thorough experimental picture. Figure 5 compellingly visualizes the trade-off curve that other methods follow while WithAnyone breaks from it.

- **Large contrastive negative pool**: Scaling InfoNCE negatives from 63 (in-batch) to 4096 (from the identity bank) is well-motivated and the ablation shows a meaningful effect on both Sim(G) and CP metrics.

---

## Weaknesses

### Fatal
None.

### Major

1. **Contrastive loss formulation anomaly (Eq. 5)**: The InfoNCE loss as written does *not* include the positive (target `t`) in the denominator—the sum runs only over negatives `n_j`. This departs from standard InfoNCE (Oord et al., 2018), where the positive competes with negatives in the partition function. The paper neither acknowledges this deviation nor justifies it. This needs explicit discussion: if intentional, the theoretical motivation should be given; if a typographical error, the actual formula used in training should be stated.

2. **Ablation of extended negatives is confounded**: "w/o Ext. Neg." yields CP=0.074 vs. the full model's CP=0.161, which appears *better* not worse. However, Sim(G) also drops (0.368 vs. 0.405). Since CP = (θ_gt − θ_gr)/max(θ_tr, ε), a generated face that is dissimilar to *everything* (reference and GT alike) can trivially score low copy-paste. The paper does not disentangle this confound, so the claim that extended negatives improve copy-paste resistance is not clearly supported by Table 3.

3. **Aesthetics degradation**: WithAnyone achieves the **lowest aesthetics score (4.783)** among all methods in Table 1, including competitors. Given that the goal is practical usability, a model that significantly reduces copy-paste but degrades visual quality may offer a less favorable trade-off than claimed. The quality-tuning phase (Phase 4) evidently does not fully recover aesthetics. The paper downplays this; it warrants more thorough analysis.

### Minor

1. **User study size**: Ten participants is too small for statistically robust conclusions about perceptual quality. Confidence intervals or significance tests are not reported, limiting the strength of the user study claim.

2. **Celebrity-only data and generalization**: The entire paired dataset is built from public celebrities sourced via search engines. Celebrities' faces are better-lit, better-photographed, and more distinctive than average. The paper does not discuss whether the model and benchmark generalize to non-celebrity identities—a practical limitation for real-world use.

3. **Copy-paste metric edge case**: When θ_tr is very small (near-identical reference and GT), the metric is numerically unstable despite the ε floor, and the interpretation becomes ill-defined. No analysis is provided on how frequently this occurs in the test set or how it affects reported scores.

### Trivial

- Some figure captions are duplicated due to parser artifacts, but this does not affect content comprehension.

---

## Nice-to-Haves

- A disentangled analysis of the CP metric across different levels of reference–GT pose/expression difference would clarify when copy-paste is detectable vs. acceptable.
- Reporting compute (GPU-hours, number of parameters) for the four-phase training pipeline would improve reproducibility.
- Ablation of the temperature τ in the contrastive loss and the λ weights (both fixed at 0.1) would strengthen confidence in the hyperparameter choices.

---

## Novel Insights

The most genuinely novel observation in this paper is that face-similarity to the reference image (Sim(Ref)) is a *flawed* proxy for identity preservation: models that maximize Sim(Ref) do so by replicating reference appearance rather than preserving identity flexibly across variation. By introducing Sim(GT)—measuring similarity to a *different* image of the same identity described by the prompt—and the angular-distance copy-paste metric, the paper reframes what "good identity preservation" actually means. This framing could reshape how the broader community designs evaluation protocols and training objectives for ID-conditioned generation.

---

## Suggestions

- Clarify whether Eq. 5 omits the positive from the denominator intentionally and, if so, provide theoretical justification or compare empirically to standard InfoNCE.
- Reanalyze the "w/o Ext. Neg." ablation by normalizing for Sim(G) level, e.g., reporting CP only among generated images with Sim(G) > 0.40 as done elsewhere.
- Expand the user study to ≥30 participants and report statistical significance (e.g., Wilcoxon signed-rank test).
- Add an analysis of aesthetics degradation: does Phase 4 quality tuning help aesthetics but not enough, or does the paired tuning itself cause the drop?

---

## Score and Decision

The paper's core contributions—a large-scale paired dataset, a principled benchmark and metric, and a technically sound model—are genuine and valuable to the community. The problem formalization is crisp and the empirical results convincingly show that WithAnyone breaks the copy-paste trade-off curve. The concerns around the contrastive loss formulation and the confounded ablation are real but resolvable, and the aesthetics degradation requires better explanation. Overall this sits at a solid borderline accept.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>