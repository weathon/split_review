Now I have enough information to write the meta-review. Let me evaluate each rebuttal claim against the paper.

---

## Summary

PI-CCA (Prompt-Invariant CCA Certificates) recasts catastrophic forgetting in vision-language continual learning as alignment-geometry drift, preserving the top-*k* canonical correlations and subspaces of the whitened image-text cross-covariance via a compact, replay-free certificate. Prompt robustness is induced by averaging projectors over perturbations. Across four benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), PI-CCA achieves replay-free SOTA and even surpasses GIFT (synthetic-replay) on retrieval/structured-concept tasks.

---

## Rebuttal Assessment

---

**Weakness:** Geometry→performance correlation (Fig. 3) is self-referential

**Author's response:** Partially address

**Assessment:** Partially convincing — The author makes two arguments. First, the sweep is "multi-dimensional and structurally diverse" across sketch type, pairing scheme, whitening variant, LoRA capacity, and EMA rates, producing a point cloud rather than a 1D regularization curve. This is verifiable from §4.3: "We sweep realistic perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type)." The diversity argument has genuine merit — a method that merely weakened a single regularization knob would trace a 1D curve, while heterogeneous implementation variants that all happen to exhibit drift-performance coupling is somewhat more informative. Second, the author cites independent theoretical grounding in §A.4. The appendix content was not available for direct verification, but the paper does explicitly state "§A.4 provides a theoretical explanation" in §4.3. However, the fundamental critique stands: **all 35+ scatter points share the same training objectives (ℒ_spec, ℒ_sub) that directly minimize D_ang and D_ρ**, so configurations with weaker regularization will simultaneously show higher drift AND lower performance by construction, regardless of structural diversity. The author's own proposed reframing — "ablation consistency evidence supporting a theoretically grounded geometry–performance relationship" — is appropriate and represents an honest concession. The cross-method validation (adding ZSCL, C-CLIP, Mod-X to Fig. 3) remains absent from the paper.

**Score impact:** Weakness downgraded (from major to minor-major boundary) — the structural diversity argument and §A.4 theoretical backing provide partial mitigation; the reframing concession is honest, but no new experimental evidence appears in the paper.

---

**Weakness:** Missing statistical uncertainty for MTIL and X-TAIL (Table 1)

**Author's response:** Partially address

**Assessment:** Partially convincing — The author correctly points to Figure 5, which shows boxplots across 20 randomly shuffled MTIL task orders with 3 seeds each; this is confirmed in the paper (§4.3, Figure 5 caption: "Dots show per-order means (3 seeds). Narrow IQRs indicate low order sensitivity"). This implicitly bounds variance for the MTIL Avg number in Table 1 (IQR ≈ 76.0–77.4%, confirming the 1.6 pp margin over C-CLIP is stable). However, the author explicitly concedes: "For the X-TAIL margin over RAIL (68.1 vs. 67.4, a 0.7 pp gap), we agree that multi-seed variance would be needed for a statistically rigorous comparison." Figure 5 covers MTIL only, not X-TAIL. The X-TAIL comparison remains statistically unsubstantiated, and the narrowest competitive margin is precisely on X-TAIL.

**Score impact:** Weakness unchanged for X-TAIL; partially mitigated for MTIL via the existing Figure 5 analysis.

---

**Weakness:** Memory cost of streaming covariance EMAs not surfaced in efficiency analysis

**Author's response:** Partially address

**Assessment:** Partially convincing, with a meaningful factual correction — The author correctly identifies an **arithmetic error in the original review**: the reviewer stated "≈ 14M float32 values (≈56 MB)" but the correct calculation is 768×768 ≈ 589K per matrix × 3 matrices ≈ 1.77M values ≈ 7 MB, not 56 MB. This is a factor-of-8 error that materially reduces the severity of the concern. At 7 MB, the covariance EMAs are a modest fixed overhead rather than a dominant contributor, which changes the framing of the weakness. The author still acknowledges that Fig. 2 does not separately itemize (a) covariance EMA buffers, (b) certificate memory, and (c) LoRA weights, and commits to adding a breakdown table in the final version. The "constant-memory" claim is confirmed accurate.

**Score impact:** Weakness downgraded — the reviewer's arithmetic was wrong; the actual covariance EMA footprint is ~7 MB, not ~56 MB, reducing the practical significance of this gap in the efficiency analysis.

---

**Weakness:** Prompt invariance stress test covers template variation, not genuine style shifts

**Author's response:** Partially address (acknowledge)

**Assessment:** Unconvincing as a rebuttal — The author acknowledges the limitation directly: "We accept that the abstract language should be narrowed: 'resilience to prompt phrasing and template variation' is a more accurate characterization." The paper's abstract currently reads "resilience to prompt/style shifts," which the author concedes overstates the evidence. The only new data offered is that the OOD condition yields R@1 gap (+2.51 pp OOD vs. +2.44 pp ID at s=1.0), but the OOD templates are "held-out template families not seen during training," still within the retrieval-caption linguistic register. The weakness is acknowledged and flagged for revision, but the abstract remains uncorrected in the submitted paper.

**Score impact:** Weakness unchanged — overstated claim in abstract, fix promised but not implemented.

---

**Weakness:** Code not released during review

**Author's response:** Acknowledge

**Assessment:** Straightforward acknowledgment with reproducibility documentation (Algorithm 1 in §A.1, hyperparameters in §A.2) and commitment to open-sourcing at camera ready. The paper's Reproducibility Statement is thorough. No further defense is offered or warranted.

**Score impact:** Weakness unchanged but trivial.

---

## Strengths
- **Consistent SOTA across all four benchmarks**: Verified from Tables 1–2. PI-CCA achieves best replay-free results: MTIL Avg 76.8 vs. 75.2 (C-CLIP, +1.6 pp), X-TAIL Avg 68.1 vs. 67.4 (RAIL, +0.7 pp), VLCL I2T R@1 48.6±1.0 vs. 47.3±1.2 (GIFT†, +1.3 pp), ConStruct-VL FA 75.2±1.3 vs. 73.9±1.5 (GIFT†), AF 2.7±0.2 vs. 3.3±0.3. Surpassing GIFT (synthetic-replay) while being fully replay-free is a meaningful resource-asymmetric result.
- **Both geometric components shown necessary**: Table 3 (verified) shows removing ℒ_spec (λ₁=0) drops MTIL Avg −2.5 pp and removing ℒ_sub (λ₂=0) drops −2.2 pp, larger than any other single ablation.
- **Prompt-invariance robustness confirmed**: Figure 4 (verified description in §4.3): ℒ_pi improves R@1 by +2.44 pp (ID) / +2.51 pp (OOD) at s=1.0, and reduces AF by ~1.10 (ID) / 0.96 (OOD).
- **Task-order robustness analysis**: Figure 5 (verified) covers 20 shuffled MTIL orderings × 3 seeds; IQR on Avg spans ≈76.0–77.4%, demonstrating stability.
- **Efficient Pareto frontier**: Figure 2 shows the (k=64, h=256) configuration sits near the knee of the performance-vs-memory curve (verified in §4.3).

---

## Weaknesses

### Fatal
None.

### Major
- **Geometry→performance correlation (Fig. 3) remains primarily internal consistency evidence.** The rebuttal's structural-diversity argument and §A.4 theoretical backing partially mitigate this, but all scatter points are still PI-CCA hyperparameter variants whose training objectives *directly minimize* the quantities plotted on the x-axis. The near-perfect Pearson/Spearman values (r=1.00 annotated in the figure) will draw scrutiny from readers who recognize the circularity. Adding baseline methods (ZSCL, C-CLIP, Mod-X) to Figure 3 remains the necessary fix for the causal framing, and it is absent from the paper. The reframing ("ablation consistency evidence") is appropriate but not yet implemented.

### Minor
- **X-TAIL classification statistics unresolved.** The 0.7 pp margin over RAIL on X-TAIL (the closest competitive gap in Table 1) has no multi-seed uncertainty bounds in the paper. The author acknowledges this explicitly. Figure 5's MTIL coverage does not extend to X-TAIL.
- **Memory accounting in efficiency analysis incomplete.** The reviewer's original arithmetic was incorrect (56 MB → 7 MB for the EMA buffers), but the lack of a breakdown table distinguishing covariance EMA, certificate, and LoRA memory costs in Fig. 2 is a real gap. Practitioners benefit from this decomposition.
- **Abstract overstates prompt robustness.** "Resilience to prompt/style shifts" is not substantiated by the synonym-swap/template-jitter stress test, which operates within the retrieval-caption register. Author acknowledges this but the paper is uncorrected.

### Trivial
- Code unavailable during review (documented in Reproducibility Statement; camera-ready commitment provided).

---

## Nice-to-Haves
- Add baseline methods (ZSCL, C-CLIP, Mod-X) geometry-drift measurements to Figure 3 to transform internal consistency evidence into cross-method validation.
- Add multi-seed results or confidence intervals for X-TAIL classification table.
- Include memory breakdown table for Fig. 2 (covariance EMAs ≈ 7 MB, certificate, LoRA adapters).
- Narrow abstract language from "style shifts" to "phrasing/template variation."

---

## Novel Insights
The projector-averaging mechanism for prompt invariance is the paper's most distinctive methodological insight: by averaging sketched projectors $$\bar{Q}_t^* = \frac{1}{M}\sum_m Q_t^*(\delta_m)$$ across perturbations and extracting the top eigenvectors of the averaged projector (Eqs. 5–6), PI-CCA constructs a canonical text basis that is simultaneously sign/rotation-ambiguity-free and prompt-stable, without Procrustes alignment. The observation that averaging *projectors* (which commute under sum and are invariant to sign flips of individual basis vectors) rather than *directions* achieves subspace averaging cleanly is non-obvious and applicable beyond the VL-CL setting. The streaming EMA architecture (three covariance buffers updated per mini-batch, certificate refreshed via slow EMA) is a practical and elegant solution to the challenge of estimating CCA statistics without replay.

---

## Suggestions
1. **Add baseline drift measurements to Fig. 3**: Run D_ang, D_ρ on ZSCL, C-CLIP, and Mod-X checkpoints under the same protocol and add them to Figure 3's scatter plots. This single inference-only addition converts the figure from internal consistency to cross-method evidence.
2. **Multi-seed uncertainty for X-TAIL**: Report 3-seed range or ±s.d. for X-TAIL columns in Table 1 to match Table 2's rigor.
3. **Memory decomposition table**: Add a 3-row breakdown in §4.3: EMA buffers (~7 MB fixed), certificate (varies with k, h), LoRA adapters.
4. **Correct abstract language**: Replace "resilience to prompt/style shifts" with "resilience to prompt phrasing and template variation."
5. **Reframe Fig. 3 caption**: Replace the current causal framing with "ablation consistency evidence supporting a theoretically motivated geometry–performance relationship."

---

## Score and Decision

**Rebuttal impact summary:**

| Weakness | Original severity | Post-rebuttal |
|---|---|---|
| Self-referential Fig. 3 | Major | Downgraded (partially mitigated by diversity argument + §A.4 theory) |
| Missing Table 1 stats | Minor | Unchanged (MTIL partially addressed via Fig. 5; X-TAIL unaddressed) |
| Memory accounting | Minor | Downgraded (reviewer arithmetic was wrong; 7 MB not 56 MB) |
| Overstated style-shift claim | Minor | Unchanged (acknowledged but not fixed in paper) |
| Code release | Trivial | Unchanged |

The rebuttal is honest, acknowledges most concerns squarely, and makes two genuine points: (1) the ablation sweep's structural diversity is greater than a single-knob regularization sweep, and (2) the original review overstated the memory burden by a factor of 8. The proposed reframings are appropriate but constitute revision promises rather than paper-present evidence. The major weakness (Fig. 3 circularity) is partially mitigated but not eliminated. No new experimental results are introduced. The overall contribution—consistent SOTA across four benchmarks, well-ablated components, task-order robustness analysis—remains strong and unchanged by the rebuttal.

The score remains at **7.0**. The rebuttal partially addresses the major weakness and corrects a reviewer arithmetic error, but all proposed fixes are future revisions, and the cross-method validation of the geometry hypothesis remains absent. The paper's empirical contribution is solid and the acceptance decision stands.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>