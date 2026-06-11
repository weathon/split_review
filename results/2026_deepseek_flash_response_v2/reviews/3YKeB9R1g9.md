## Summary

This paper demonstrates that normalized training loss curves (TLCs) collapse across LLM scales (300M–3.9B parameters) when three controls — AdamW timescale τ, tokens-per-parameter ratio (TPP), and LR schedule — are matched. It introduces the Celerity model family trained in this collapse regime, shows that collapse residuals provide early detection of training issues, and proposes an early-stopping method for hyperparameter tuning that uses a small-scale parametric surrogate to predict final loss from partial runs.

## Strengths

1. **Extends loss-curve collapse to practical LLM scales.** Prior work (Qiu et al., 2025) showed collapse only for small autoregressive tasks with vanilla Adam and no weight decay. This paper demonstrates collapse across 300M–3.9B parameter models while co-scaling width, depth, batch size, and weight decay with AdamW (Fig. 6, Sec. 4), directly filling that gap.

2. **Isolates three independent factors governing TLC shape via controlled experiments.** Section 3 systematically varies η, λ, and B independently while keeping τ constant (Fig. 3), showing that TLCs with matching τ converge to the same shape. This causal decomposition goes beyond prior correlational evidence.

3. **Celerity models sit on the compute-efficiency Pareto frontier.** Fig. 2 shows Celerity positioned on the upper-left frontier against a range of open LLMs. Against BTLm, Celerity achieves comparable accuracy with 75% fewer training FLOPs (Sec. 4), demonstrating that collapse-compatible training does not sacrifice practical performance.

4. **Collapse residuals detect training issues substantially earlier than raw loss curves.** For the 1.8B, 234 TPP run, deviation from the collapse reference was detectable at ~60% of training (Fig. 1 right), whereas the raw loss spike only became visible after ~90% (Fig. 6 right). This is a concrete improvement over vague human-judgment criteria used in practice.

5. **Enables early stopping in hyperparameter tuning at 10–30% of training.** Sec. 5 shows (Fig. 9) that the "predicted best" method achieves negligible loss gaps when stopping early, while the "current best" heuristic can fail entirely at 1.7B scale. The alternating fitting procedure reduces grid search cost from O(g⁴) to O(g²).

6. **Provides a theoretical grounding for τ's effect via a noisy quadratic model.** Eq. (3) formalizes the bias-variance trade-off controlled by τ, explaining why normalized TLCs become scale-invariant at matched τ (Appendix B.3).

## Weaknesses

### Fatal
None.

### Major

1. **The Celerity evaluation is limited to seven multiple-choice QA/commonsense tasks.** The "compute-efficiency frontier" claim (Fig. 2) rests on average accuracy on ARC-c, ARC-e, BoolQ, HellaSwag, PIQA, SIQA, and WinoGrande. No generative evaluations (MMLU, GSM8K, HumanEval) are reported. For a paper introducing a new LLM family and making competitive claims, this is a significant gap. The paper's philosophy of avoiding benchmark annealing is principled, but the frontier claim is only meaningful within this restricted task set. Adding generative benchmarks would substantially strengthen the claim.

2. **The warmup proportion differs substantially across model sizes within a TPP band, partially violating the "matched LR schedule" condition.** Table 2 sets warmup to `min(10% of total tokens, 375M tokens)`. At 20 TPP, this gives ~6.25% warmup for the 300M model vs. ~0.48% for the 3.9B model — a 13× difference. The paper acknowledges "small early deviations" at 20 TPP (line 202) but does not verify whether these deviations disappear when warmup proportions are matched. Since LR schedule is presented as one of three essential conditions for collapse, this gap weakens the evidence that those conditions are fully *sufficient*.

### Minor

1. **"Residual bias at end-of-training is negligible" is asserted without direct evidence.** The scale-invariance argument (line 131) depends on this claim, but no analysis (e.g., measuring bias vs. variance empirically at the end of training) is provided to support it.

2. **CompleteP parameterization is mentioned but never explained in the main text.** Line 164 says CompleteP "was more efficient/reliable than µP" and references Fig. 15 in the appendix. Readers relying only on the main text cannot assess what CompleteP is or whether the collapse theory still applies under it.

3. **No uncertainty quantification.** All results are single-run with no error bars, confidence intervals, or variance estimates. The collapse claim is inherently about whether curves differ *less than expected from noise*, but the noise level is never quantified. While single-run evaluation is standard for LLM training at this scale, the paper's distinctive claims (collapse quality, early stopping reliability) would benefit from at least some variance characterization.

4. **The late-stage divergence at 234 TPP for larger models (Fig. 1, middle) complicates the "optimal τ guarantees collapse" narrative.** The paper honestly acknowledges this (attributing it to overfitting on training data), but the fact remains that collapse is imperfect even with matched τ and TPP. This suggests additional factors (e.g., model capacity relative to data diversity) may matter for larger models.

5. **The early-stopping method is demonstrated only on λ sweeps at two model sizes in the main text.** Fig. 9 tests sweeps of λ at 1.7B/20TPP and 3.3B/30TPP. While Appendix D.2 provides additional experiments, the main-text claim would be stronger with demonstrations over η or B sweeps as well.

### Trivial
None.

## Nice-to-Haves
- Quantify collapse quality numerically (e.g., RMS deviation from a reference curve) across all bands instead of relying on visual inspection.
- Validate the warmup effect by running the 20 TPP band with matched warmup proportions to confirm whether early deviations disappear.
- Include generative evaluations for Celerity (MMLU, GSM8K) to strengthen the compute-efficiency frontier claim.
- Provide a more detailed explanation of CompleteP in the main text.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The collapse condition is largely tautological"**: The paper identifies specific, non-trivial conditions (τ, TPP, LR schedule) that govern collapse — this is an empirical finding, not a tautology.
- **Criticism of Bergsma et al. (2025a) robustness**: Per review guidelines, cited references are assumed to exist and be valid.
- **"Comparison set in Fig. 2 mixes eras and methodologies"**: The paper explicitly acknowledges this (line 159) and frames Celerity as a baseline for models trained without benchmark annealing.
- **"Random baseline is a weak comparator"**: The meaningful comparison is "predicted best" vs. "current best"; random is only a floor.
- **"Llama-2 comparison is unfair"**: The paper does not claim Llama-2 is suboptimal for its goals — only that varying TPP/τ prevents collapse.
- **"Does not summarize how robustly Bergsma et al. established optimal τ"**: This is an exposition request, not a substantive weakness.
- Generic strengths from Strength Finder about "addressing an important problem": Removed as they lack specific content tied to the paper's contributions.

## Novel Insights

The reviews highlight one observation worth noting: the tension between the paper's "three essential conditions" framing and the acknowledged warmup mismatch / 234-TPP divergence suggests that collapse is a *robust tendency* under matched controls rather than a strict guarantee. The paper would benefit from sharpening this nuance. Additionally, the diagnostic application (detecting issues at 60% vs. 90%) is arguably the paper's strongest practical contribution, yet it receives less emphasis than the more speculative "signature of compute-efficiency" framing.

## Suggestions

- Add generative evaluations (MMLU, GSM8K at minimum) for the Celerity family. If Celerity performs well, this strengthens the frontier claim; if not, acknowledge the trade-off explicitly.
- Run the 20 TPP band with matched warmup proportions and report whether early deviations disappear.
- Include a numerical measure of collapse quality (e.g., normalized RMS deviation) across all bands.
- Tone down the "collapse as a signature of compute-efficient training" framing to "collapse as a predictable outcome of consistent training recipes" to better match what the evidence supports.
- Clarify what CompleteP is and how it relates to µP in the main text.
- Report at least one experiment with multiple seeds to quantify the noise floor relevant to the collapse claim.

## Calibration Anchors

### Round 1 — Bracketing
| Path | Avg Score | Comparison |
|------|-----------|------------|
| `kkVTeMvC9D.md` (Jacobian geometry) | 3.40 | Much weaker — speculative, thin empirical support |
| `lZRRfupxYn.md` (mesoscience generalizability) | 3.00 | Much weaker — non-standard framing, weak evidence |
| `BUpdp5gETF.md` (decoupled LR schedules) | 2.50 | Much weaker — narrow scope, small-scale |
| `2NwHLAffZZ.md` (weak correlations) | 2.33 | Much weaker — theoretical, no LLM-scale experiments |
| `KnoS9XxIlK.md` (Multi-Power Law) | 6.00 | Weaker — narrower scope (only LR schedules), up to 400M params |
| `o9YC0B6P2m.md` (Scaling Law with LR Annealing) | 6.75 | Comparable — similar empirical methodology, but our paper has more novel findings |
| `xGM5shdGJD.md` (Scaling Law Estimation) | 5.20 | Weaker — methodological meta-study, less novel |
| `iZeQBqJamf.md` (Over-training scaling) | 6.50 | Comparable — similar quality, our paper has more novelty |
| `wg1PCg3CUP.md` (Precision scaling) | 8.00 | Stronger — cleaner execution, tighter claims |
| `Tzh6xAJSll.md` (Associative memories) | 7.60 | Stronger — theoretical + empirical rigor |
| `jOmk0uS1hl.md` (Test task confounds) | 8.00 | Stronger — clean, impactful, tightly argued |
| `d8w0pmvXbZ.md` (Small-scale proxies) | 8.00 | Stronger — cleaner experiments, universal reviewer praise |

**Round 1 Bracket:** 5.5 – 7.0

### Round 2 — Narrowing
| Path | Avg Score | Comparison |
|------|-----------|------------|
| `xGM5shdGJD.md` (already listed) | 5.20 | — |
| `WYL4eFLcxG.md` (Scaling Optimal LR) | 6.00 | Weaker — narrower question, no model release |
| `iEfdvDTcZg.md` (Optimization landscape) | 6.25 | Different topic; comparable empirical quality |
| `KnoS9XxIlK.md` (already listed) | 6.00 | — |
| `P7KRIiLM8T.md` (u-µP) | 7.33 | Stronger — cleaner theoretical contribution |
| `bmrYu2Ekdz.md` (PolyPythias) | 6.50 | Comparable — our paper has larger models, more novel findings |
| `hrOlBgHsMI.md` (Straight to Zero) | 6.33 | Weaker — narrower scope, small models (up to 1.7B), hand-wavy theory |
| `o9YC0B6P2m.md` (already listed) | 6.75 | — |

**Final Score Determination:** The paper is clearly stronger than the 6.00–6.33 anchors (Multi-Power Law, Scaling Optimal LR, Straight to Zero) due to broader scope, larger models, and a more novel central finding. It is comparable to the 6.50–6.75 anchors (Over-training scaling, PolyPythias, Scaling Law with LR Annealing). It is weaker than the 7.33+ anchors (u-µP, Small-scale proxies) which have cleaner execution and tighter claims. Score: **6.5**.

## Score and Decision
MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>