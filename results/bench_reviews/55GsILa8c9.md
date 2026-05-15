Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper introduces CausalNovo, a model-agnostic framework for de novo peptide sequencing that learns to focus on causal signal fragment ions while suppressing reliance on spurious noise peaks. The method is grounded in a Structural Causal Model (SCM) from which the authors derive independence and sufficiency principles, implemented via a Causality Extraction Module (CEM) with contrastive and information-theoretic objectives. On three public datasets (Nine-species, Seven-species, HC-PT) and across three SOTA baselines (CasaNovo, AdaNovo, π-HelixNovo), CausalNovo delivers consistent improvements at the amino acid, peptide, and PTM levels (e.g., +12.0% amino acid precision on Seven-species, +14.2% on HC-PT), while also demonstrating improved robustness to noise perturbations and cross-species generalizability.

## Strengths

1. **Consistent, model-agnostic gains across multiple SOTA baselines.** CausalNovo improves CasaNovo, AdaNovo, and π-HelixNovo on all three datasets at all evaluation levels. Improvements are substantial (up to +12.0% amino acid precision, +15.1% PTM precision) and the framework adds negligible inference overhead (<1%). This demonstrates the framework addresses a real limitation in existing models and generalizes across architectures.

2. **Principled SCM-based formulation with clean operationalization.** The paper formalizes de novo sequencing using an SCM (Section 3.2, Figure 2A) and derives two concrete principles—independence and sufficiency—that directly guide the CEM design. The replace-based causal intervention (Section 3.4) is a clever, domain-appropriate way to simulate interventions on non-causal factors.

3. **Thorough ablation studies validating every component.** Tables 4 and 5 isolate the contribution of each proposed component (independence principle: +1.2% AA precision, purification: +0.8%, symmetric training: +0.4%). The ablation on causal intervention strategies confirms the replace-based approach is effective while random dropping is not, ruling out a trivial augmentation explanation.

4. **Empirical evidence of robustness to noise and shifted distributions.** The vulnerability analysis (Figures 1, 3) shows CausalNovo maintains higher precision when noise peaks are perturbed (up to +14.9% relative improvement). The NSR analysis (Figure 4) shows consistent gains across varying noise-signal ratios (+10.2–12.0% average improvement). Cross-species validation (Table 3) confirms generalizability across diverse biological backgrounds.

5. **Attention analysis provides mechanistic insight.** Table 7 shows CausalNovo increases the proportion of predictions attending to three causal peaks from 19.26% to 32.87%, and reduces those attending to zero causal peaks from 12.73% to 10.76%. This directly links the causal objective to model internals.

6. **Honest limitations and practical framing.** The paper explicitly acknowledges its evaluation follows the standard NovoBench protocol (not the more challenging OOD protocol of recent methods) and reports the 2.3× training time overhead. This transparency adds credibility.

## Weaknesses

### Fatal
None.

### Major
None. The paper has no fatal or major flaws that invalidate its core claims.

### Minor

1. **Inference-mode specification is ambiguous.** The paper trains the decoder to predict from z_c (sufficiency principle, line 101) but never explicitly states whether inference uses z_c alone, the full z, or both. The architecture description (Figure 2B) and the <1% inference overhead claim strongly imply z_c is fed to the decoder, but the paper should state this directly and, ideally, ablate z_c vs. full-z at inference to confirm the causal representation is indeed doing the work.

2. **The "causal" framing is somewhat aspirational.** The identification of causal peaks relies on computing a theoretical spectrum from the ground-truth peptide and a tolerance threshold (Eq. 4). This uses domain knowledge to pre-define which peaks are "causal" rather than discovering causal structure from data. While the paper is transparent about this (noting it is "a well-established approach in database search"), the language throughout — "causal representation," "causal intervention," "causal discovery" — implies a stronger form of causal learning. This gap between rhetoric and method risks overinterpretation.

3. **Missing hyperparameter reporting and sensitivity analysis.** The fraction α of noise peaks replaced during the causal intervention (Section 3.4.1) is never reported, and no ablation over α values is provided. Similarly, the temperature τ is reported (0.1) but its sensitivity is not explored. These are relevant hyperparameters for reproducibility and understanding robustness.

4. **No error bars or statistical significance.** All results are reported as point estimates without confidence intervals, standard deviations, or significance tests. While single-run evaluation is common in this field, the lack of error bars makes it impossible to assess whether the smaller improvements (e.g., +0.4% from symmetric training) are meaningful.

### Trivial

1. Table 5 formatting is garbled (likely a parser artifact but should be checked in the original).

## Nice-to-Haves

- An OOD experiment training on the standard corpora and testing on an independent dataset (e.g., from a different instrument or sample preparation protocol) would directly substantiate the paper's claimed robustness motivation. This is acknowledged by the authors as future work.
- A comparison to simple noise augmentation baselines (e.g., random peak dropping/replacement without the causal framing) would clarify whether the causal formulation adds value beyond standard data augmentation.
- Showing example spectra overlaid with learned importance scores M would build intuitive understanding of which peaks CausalNovo prioritizes.

## Removed Points

- *"Missing inference specification is a methodological gap"* — downgraded from major to minor. The paper implicitly clarifies inference (decoder trained on z_c, <1% overhead implies CEM active at inference), making this a clarification issue rather than a gap.
- *"Retrained baselines differ substantially from reported numbers"* — removed. Retraining with different hyperparameters/hardware routinely produces different numbers; the paper transparently marks retrained results with †. This is standard practice.
- *"Table 5 lacks the full combination"* — removed. The text accompanying the table (lines 266-267) discusses the drop-only result explicitly, so no comparison is missing.
- *Strength Finder's overly generic strengths* — filtered. Generic claims like "addressed an important problem" removed; only concrete, evidenced strengths retained.

## Novel Insights

None beyond the paper's own contributions. The combination of SCM-guided disentanglement with domain-specific peak identification (via theoretical spectra) in de novo sequencing is the paper's core novel integration — this is already well-articulated by the authors.

## Suggestions

1. Explicitly state in Section 3.3 or 4.2 that at inference time, z_c is used as input to the decoder (and z_s is discarded). Add a one-sentence ablation in the appendix comparing this to full-z inference.
2. Report the value of α used in experiments and add a sensitivity analysis (α ∈ {0.1, 0.3, 0.5}) to the appendix.
3. Tone down "causal discovery" language where the approach relies on pre-specified domain knowledge. Consider phrasing like "causality-informed feature learning" or "causal representation learning guided by domain priors."
4. Add error bars (at least for key comparisons in Tables 1–3) by reporting results across a small number of seeds.

## Score and Decision

**Calibration anchors used for scoring:**

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/0oqEBQA0UD.md` (PeakNovo) | 3.50 (Reject) | Weaker: inferior method (database dependency), less thorough evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/A5MPzwyq0H.md` (Pep2Prob) | 3.50 (Reject) | Weaker: narrower scope, less impactful |
| `/home/wg25r/review_agent/human_reviews_2026/kvzW81UtyH.md` (CIRRL) | 4.50 (Reject) | Similar framing but weaker experiments, stronger theory; overall comparable quality but this paper has more practical impact |
| `/home/wg25r/review_agent/human_reviews_2026/yQlTgHo1um.md` (PepTri) | 5.50 (Accept Poster) | Comparable empirical thoroughness; this paper has cleaner ablation design and broader baseline coverage |
| `/home/wg25r/review_agent/human_reviews_2026/5d7prMWHNF.md` (Delta Embeddings) | 6.00 (Accept Poster) | Comparable: both have clear motivation, solid experiments, honest limitations; this paper stronger on multi-baseline validation |
| `/home/wg25r/review_agent/human_reviews_2026/bZqCBgm2N0.md` (Beyond DAGs) | 6.50 (Accept Poster) | Stronger on theoretical depth (identifiability proofs); this paper stronger on practical breadth and domain impact |
| `/home/wg25r/review_agent/human_reviews_2026/wwPSfcf5Pj.md` (Extending Sequence Length) | 6.50 (Accept Oral) | Stronger: reveals a non-obvious finding (longer sequences hurt), more surprising insights |

The paper is a solid, well-executed contribution to a specific application domain. It has no fatal flaws, its experiments are thorough and honestly reported, and the improvement over multiple SOTA baselines is consistent and meaningful. The main weaknesses are presentation clarity (inference specification, α reporting) and the gap between causal rhetoric and domain-knowledge-informed implementation. None of these undermine the core contribution. Relative to the calibration anchors, this paper sits between PepTri (5.50) and Delta Embeddings (6.00) — it is more comprehensive than PepTri empirically but slightly thinner theoretically than the stronger causal papers.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>