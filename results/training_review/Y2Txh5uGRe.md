Now I have a thorough understanding of the paper. Let me construct the final review, carefully cross-checking every claim.

## Summary
Text2Data proposes a two-stage diffusion framework for text-to-data generation under low-resource settings: (1) pretrain an unconditional diffusion model on all data (mostly unlabeled), then (2) finetune on labeled data using a constraint-optimization objective designed to prevent catastrophic forgetting. It is evaluated on molecules (QM9), human motion (HumanML3D), and time series data across 2%–40% label proportions.

## Strengths

- **Relevant problem and sensible high-level approach.** Low-resource controllable generation is practically important, and the two-stage design — leveraging unlabeled data for unconditional pretraining followed by finetuning — is a reasonable starting point. The method avoids the semantic ambiguity of pseudo-labeling and the cost/fidelity issues of data augmentation.

- **Evaluation across three diverse modalities and multiple label proportions.** The paper tests on molecules, motions, and time series at 8 different label proportions (2%–40%), going beyond single-modality studies. This breadth gives some sense of generalizability.

- **Ablation against unconstrained finetuning.** The paper includes a "finetune" baseline (same pretraining + finetuning without the constraint) across all modalities, which isolates the effect of the proposed constraint mechanism.

## Weaknesses

### Fatal
None.

### Major

1. **Marginal empirical improvement on motion and time series, and underperformance at low label rates.** In Table 1 (motion), Text2Data is *worse* than unconstrained finetuning at the lowest label proportions (2%: 0.34 vs 0.37 R-Precision; 4%: 0.39 vs 0.42). At most proportions where Text2Data leads, differences are within one standard deviation (e.g., 8%: 0.44±0.01 vs 0.43±0.01). Table 2 (time series) shows similarly tiny margins (e.g., Frequency: 2.59 vs 2.62 on a ×10⁻¹ scale). Only on molecules (Figure 1) are the gains more substantial. The claim of "consistently superior performance" is not supported by the motion and time-series results.

2. **Missing critical baseline: weight decay or EWC as a regularizer.** The paper's constraint optimization is a specific form of regularization that keeps parameters near the pretrained values. The simplest alternative — L₂ weight decay on the parameter change, or Elastic Weight Consolidation — is never compared. Since the "finetune" baseline uses no regularization at all, it is unclear whether the proposed dynamic λ mechanism provides any benefit over trivial alternatives. Without this baseline, the core claim that the constraint-optimization objective is a novel and effective contribution lacks empirical support.

3. **Generation quality results reported in prose without tables or error bars.** Section 5.5 states quantitative claims like "surpasses EDM-finetune and EDM by average margins of 19.07% and 58.03%" for negative log-likelihood, with similar prose-only claims for validity, stability, FID, and diversity. None are presented in a table with standard deviations or per-label-proportion breakdowns. This is a severe reporting failure — the reader cannot verify these numbers or assess their statistical reliability.

4. **Overclaimed framing: "textual control" conflates natural language with property conditioning.** For molecules and time series, the "text descriptions" are formatted numeric property values (e.g., polarizability thresholds), not free-form natural language. The abstract's framing ("Natural language serves as a common and straightforward control signal") and the title's "Textual Control" imply semantic text understanding that is not evaluated. Only the motion modality uses genuine text descriptions. The paper's contribution — conditional generation on structured attributes — is still valid, but the framing overstates what is demonstrated.

5. **Theoretical contribution is a standard bound with a problematic assumption and no algorithmic impact.** Theorem 1 assumes a *finite* parameter space Θ, which does not hold for neural networks. The bound depends on log|Θ|, which is undefined for continuous parameters. The results are a straightforward application of Bernstein's inequality + union bound — standard concentration results with no novel insight connecting to the proposed algorithm. The theory does not guide hyperparameter choices, nor does the algorithm actually use the bound beyond justifying a relaxation parameter ρ that could be chosen without any theory.

### Minor

- **Algorithm underspecified for the core mechanism.** The dynamic λ computation involves hyperparameters α, β, γ, and ρ with no guidance on values, ranges, or sensitivity. Since the gains over unconstrained finetuning are small, it is unclear whether the complex λ update is necessary or whether a fixed λ or simpler schedule would suffice.

- **Molecule evaluation uses a classifier to predict properties, introducing a confound.** The MAE on molecular properties includes classifier prediction error. The paper does not report classifier accuracy or analyze whether the improvements reflect better molecule generation or classifier bias. (This is a common practice in the field but should still be noted as a caveat.)

- **t-SNE visualization for time series is purely qualitative.** No quantitative distribution overlap metric (e.g., Wasserstein distance, MMD) is reported for the time series modality, making the claimed "largest overlap" unverifiable.

### Trivial
None.

## Nice-to-Haves
- Ablate the dynamic λ computation against a fixed λ (e.g., 0.1) to test whether the adaptive mechanism is responsible for the gains.
- Diagnose parameter drift (‖θ_finetuned − θ_pretrained‖) for Text2Data vs. unconstrained finetune vs. weight decay to directly test whether the constraint is working.

## Removed Points
These points are from the reviewers but were removed for the reasons noted:

- **Harsh Critic: "evaluation by MAE on same properties is circular"** — Removed because this is factually wrong. Measuring whether a conditionally generated sample matches the specified condition is precisely how controllability should be evaluated; it is not circular.

- **Harsh Critic: "indistinguishable from transfer learning with weight decay or EWC"** — Weakened. The approach IS a form of regularized transfer learning, but the specific lexicographic optimization formulation is a specific technical choice. The missing baseline concern is kept in Major Weakness #2, but the claim of "indistinguishability" is removed as overstatement.

- **Harsh Critic: "the theoretical argument (Eq. 4) that p_θ(x) ≈ E[p_θ(x|c)] is circular"** — Removed. Eq. 4 is simply the law of total probability applied to the conditional model. It is mathematically sound.

- **Harsh Critic: "the method is a standard two-stage pipeline"** — Weakened. The method IS a two-stage pipeline (pretrain + finetune), but the specific constraint-optimization learning objective is a distinct algorithmic choice. The criticism is kept in spirit (missing baselines, marginal gains).

- **Strength Finder: "Novel constraint-optimization finetuning objective that mitigates catastrophic forgetting... ablation results consistently show improvement"** — Removed because the "consistently" claim conflicts with verified weaknesses: Table 1 shows Text2Data is worse than MDM-finetune at 2% and 4%.

- **Strength Finder: "Theoretical generalization bound that guides constraint relaxation... concrete advance over heuristic regularization"** — Removed. The theory is a standard Bernstein + union bound application with a finite-Θ assumption that doesn't hold for neural networks, and it does not guide algorithm design.

- **Strength Finder: "Ablation studies that isolate the benefit... consistently beaten by Text2Data"** — Removed. Conflicts with Table 1 where MDM-finetune beats Text2Data at 2% and 4% label proportions.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a consistent picture: the paper's method is a sensible but incremental combination of existing ideas (pretraining on unlabeled data + constraint-based finetuning), and the empirical evidence for its advantage over simpler alternatives is inconclusive for 2 of 3 modalities. The absence of a weight-decay/EWC baseline and the prose-only reporting of generation quality metrics prevent the paper from making a convincing case.

## Suggestions
1. Add an EWC or L₂-weight-decay-on-parameter-change baseline to all modalities. If the proposed constraint mechanism does not meaningfully outperform such simple regularizers, the paper's core contribution is undermined.
2. Move all generation quality results (currently in prose in Section 5.5) into a proper table with standard deviations across label proportions.
3. Address the low-label setting (2%–4%) where the constraint actually hurts motion generation — either explain why or modify the algorithm.
4. Clarify the framing: the paper is about conditioning on structured attributes (formatted as text strings), not about semantic natural language understanding for molecules and time series.
5. Provide hyperparameter sensitivity analysis for α, β, γ, and ρ, or at minimum state the values used.

## Score and Decision

**Originality:** 3/10 — The two-stage design (pretrain unconditional + finetune with regularization) is well-established. The specific lexicographic optimization formulation is incremental.

**Importance of research question:** 7/10 — Low-resource controllable generation is relevant and under-explored for non-image modalities.

**Claims supported:** 3/10 — Core claims of consistent improvement are not supported by motion/time-series results; generation quality metrics are unreported in tables; missing simple baselines.

**Soundness of experiments:** 4/10 — Three-modality evaluation is broad, but missing baselines, prose-only quality reporting, and marginal gains weaken the evidence.

**Clarity of writing:** 6/10 — The paper is generally well-structured, though the prose-only quality results and overclaimed framing detract.

**Value to community:** 4/10 — The problem framing and two-stage approach may be useful, but the evidence is insufficient to recommend the specific algorithm over simpler alternatives.

The paper addresses a relevant problem with a sensible framework, but the empirical evidence is weak in 2 of 3 modalities, a critical simple baseline (weight decay/EWC) is missing, generation quality metrics are not reported in tabular form, and the theoretical analysis does not provide substantive guarantees. These issues collectively prevent the paper from establishing its contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>