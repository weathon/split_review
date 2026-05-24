Now I have all the information needed. Let me compose the final review.

## Summary

This paper presents CausalNovo, a model-agnostic causal representation learning framework for de novo peptide sequencing. The key idea is to formalize peptide sequencing via a Structural Causal Model and enforce two principles — independence (causal factors should be invariant to noise) and sufficiency (causal factors should retain predictive information) — through contrastive and information-theoretic objectives. CausalNovo introduces a lightweight Causality Extraction Module (CEM) that can be plugged into any existing sequencing model. Experiments across three standard benchmarks and three baseline architectures (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements at the amino acid, peptide, and PTM levels (up to ~15% relative gains), with additional analyses demonstrating improved robustness to noise and better attention to signal peaks.

## Strengths

1. **Consistent and substantial performance gains across diverse settings.** Table 1 shows CausalNovo improves amino acid precision by +12.0% (CasaNovo, Seven-species), +14.2% (AdaNovo, HC-PT), and +12.4% (π-HelixNovo, HC-PT). Improvements hold at the peptide and PTM levels across all three datasets, demonstrating robustness beyond a single configuration. (Tables 1–2)

2. **Model-agnostic design with demonstrated generality.** The framework is integrated with three distinct baseline models and improves all of them, validating that the causal learning mechanism transfers across architectures rather than being tailored to a specific model. (Tables 1–2)

3. **Behavioral evidence of reduced reliance on spurious noise.** Vulnerability analysis (Figures 1, 3) shows baseline models degrade substantially when noise peaks are perturbed, while CausalNovo maintains higher precision (average Relative Improvement of +14.9%, +15.7%, +13.5% on HC-PT). This directly demonstrates the framework's intended effect. (Figures 1, 3)

4. **Generalization across varying noise-signal ratios (NSR).** Figure 4 shows CausalNovo maintains amino acid precision as NSR increases, with average improvements of +10.2%, +12.2%, and +12.0% across baselines. This is a clean, independent evaluation (not using the training intervention) that supports the core claim. (Figure 4)

5. **Mechanistic interpretability via attention analysis.** Table 7 shows CausalNovo increases the proportion of predictions attending to three causal peaks from 19.26% to 32.87%, providing interpretable evidence that the model redirects attention toward signal ions as intended. (Table 7)

6. **Systematic ablation studies.** Tables 4 and 5 isolate the contributions of independence, purification, symmetric training, and the replace/enhance intervention, showing additive benefits of each component. (Tables 4–5)

7. **Robustness to different peak-distinction strategies.** Table 6 shows that even with 18 ion types (vs. the default 3), CausalNovo achieves a 28.5% relative improvement under strict thresholds, demonstrating that the benefits are not tied to a specific noise identification rule. (Table 6)

## Weaknesses

### Fatal

None.

### Major

1. **The contribution of the causal objectives is confounded with added model capacity.** The Causal Extraction Module (CEM) — 3 Transformer layers + MLP — introduces parameters absent in the baseline. The ablation (Table 4) compares the full CEM+causal-losses configuration against the raw baseline (no CEM), but never against a control where the CEM is added *without* the causal objectives (e.g., with L2 regularization or a random-masking objective on the importance scores). The baseline→+Independence jump (0.741→0.753, +1.2% AA precision) could partially reflect the extra representational capacity rather than the causal framework itself. This is the most significant methodological gap, as the paper's central claim is that the gains stem from causal disentanglement. A simple control experiment would resolve it.

### Minor

2. **The vulnerability evaluation tests the same intervention used during training.** The analysis in Figures 1 and 3 replaces noise peaks with other noise peaks from the training batch — the *identical* procedure used to train the independence objective. This measures how well CausalNovo learned its training objective, not necessarily whether it generalizes to different or more realistic noise patterns. The concern is partially mitigated by (a) the NSR analysis (Figure 4), which evaluates on naturally varying noise levels without any intervention, and (b) the 18-ion analysis (Table 6), which uses a different peak-distinction rule. A stronger test would be to perturb noise peaks using strategies unseen during training (e.g., random m/z injection, intensity jittering, structured noise from different instruments).

3. **Adding the full theoretical spectrum to the intervened data could create an information shortcut.** The "enhance" step augments the intervened spectrum with all theoretical peaks of the ground-truth peptide (Section 3.4.1). This means the contrastive pair shares a strong common signal — the complete theoretical spectrum — which could make the independence objective easier to satisfy without truly learning noise invariance. The ablation (Table 5) shows replace-only achieves 0.747 vs. replace+enhance 0.753, so the effect is partial, but an ablation removing the enhance step entirely from the evaluation pipeline would clarify whether the gains rely on this oracle-like signal.

4. **No statistical significance or variance reporting.** The paper does not report multiple seeds, confidence intervals, or significance tests for any experiment. Given some improvements are modest (e.g., +2.2% on Nine-species AA precision for π-HelixNovo), variance estimates would help the reader assess stability. Standard practice in this field is to run 3–5 seeds.

5. **Cross-species validation limited to one baseline.** Table 3 shows leave-one-out cross-species results only for CasaNovo, confirming generalization but leaving open whether the benefit transfers similarly through AdaNovo and π-HelixNovo.

### Trivial

- The checkmarks in Tables 4 and 5 are rendered identically across all rows in the PDF extraction, making the ablation configurations ambiguous at a glance (the text description clarifies the intended progression).

## Nice-to-Haves

- Provide details on whether hyperparameters were tuned separately per baseline or kept fixed, and whether CausalNovo introduced any hyperparameter search beyond the baseline settings.
- Report training and inference time in absolute terms (seconds per spectrum) rather than only the multiplicative factor (~2.3×).
- Test generalization on a dataset from a different lab, instrument type, or sample preparation protocol to strengthen claims of practical robustness.

## Removed Points

*These points were flagged by reviewers but removed after cross-checking. Treat them with caution — they may contain useful context but do not represent valid criticisms of the paper.*

1. **"Causal framework rests on strong structural assumptions that are not validated"** — The SCM assumptions (C⟂S, Y=g(C)) are standard modeling choices grounded in Reichenbach's Common Cause Principle and domain knowledge about fragmentation chemistry. The paper provides extensive empirical validation (NSR robustness, cross-species transfer, attention analysis) that the learned representations behave as intended. The request for formal causal discovery or ground-truth interventions asks for a different kind of validation outside the paper's scope.

2. **"PTM-level results not broken down by PTM type"** — The paper reports standard PTM-level metrics used in the field. Requesting per-PTM-type analysis is a granularity beyond what is expected and would not alter the conclusions.

3. **"The method essentially equates 'causal' with 'robust to the replace intervention'"** — This is a reductive reading. The framework derives independence from the SCM's structural equations and operationalizes it via the do-operator. The replace intervention is one implementation choice; the sufficiency and purification objectives provide independent learning signals.

4. **"Baseline reimplementation differences from original papers not discussed"** — The paper states baselines are retrained "with the same configurations" (Section 4.1), which is standard practice. The differences between original and retrained numbers are modest and do not affect the comparative conclusions.

## Novel Insights

The most interesting observation from the reviews is that the vulnerability evaluation's circularity concern (strength #2 in the paper) and the capacity confound concern (weakness #1 above) intersect nontrivially: the NSR analysis (Figure 4) is the cleanest independent evidence for the causal claim, but even that could partially reflect extra model capacity. This suggests that a single ablation — adding CEM without causal losses and testing on NSR robustness — would simultaneously address both concerns. None of the reviewers drew this connection explicitly.

## Suggestions

Add a capacity-matched control: retain the CEM architecture but replace the contrastive and purification losses with a simple regularizer (e.g., L2 penalty on importance scores or a random-masking prediction objective). If gains shrink or vanish, the causal objectives are the key driver; if they persist, the contribution is architectural rather than causal, and the paper should reframe accordingly. This single experiment would substantially strengthen the paper.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/EKjt05WxMI.md` (PLMNovo) | 2.50 | R1 | Much weaker — marginal improvements, questionable methodology, missing baselines |
| `/home/wg25r/review_agent/human_reviews_2026/0oqEBQA0UD.md` (PeakNovo) | 3.50 | R1 | Weaker — contradictory design (database dependency for "de novo"), unclear contributions |
| `/home/wg25r/review_agent/human_reviews_2026/A5MPzwyq0H.md` (Pep2Prob) | 3.50 | R1 | Different task, comparable evaluation scope but less ambitious contribution |
| `/home/wg25r/review_agent/human_reviews_2026/7wjqoJj62s.md` | 2.67 | R1 | Unrelated topic, not comparable |
| `/home/wg25r/review_agent/human_reviews_2026/wXan3GYeHL.md` | 1.60 | R1 | Unrelated topic, not comparable |
| `/home/wg25r/review_agent/human_reviews_2026/6renfxmnAZ.md` | 5.00 | R1 | Causal representation learning but different domain; narrower evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/yQlTgHo1um.md` (PepTri) | 5.50 | R1 | Similar quality — well-executed but has unclear implementation details and insufficient ablation; CausalNovo comparable |
| `/home/wg25r/review_agent/human_reviews_2026/QI2xC19p7U.md` | 4.50 | R1 | Different topic (protein language model pretraining), less directly comparable |
| `/home/wg25r/review_agent/human_reviews_2026/ZAvI3lxYTh.md` (CaSBRE) | 4.50 | R1 | Similar topic (causal + biomedical) but different task; comparable experimental rigor |
| `/home/wg25r/review_agent/human_reviews_2026/RDerF20JYT.md` (La-Proteina) | 8.00 | R1 | Much stronger — more impressive results, more mature methodology; CausalNovo not at this level |
| `/home/wg25r/review_agent/human_reviews_2026/hiD1bo11Mm.md` | 4.80 | R2 | Different task (small molecule retrieval), well-executed study but narrower scope |
| `/home/wg25r/review_agent/human_reviews_2026/dGE8GNOLKs.md` (OmegAMP) | 4.67 | R2 | Peptide-related but different task (AMP discovery); less comprehensive evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/uKn9PdREBA.md` | 5.00 | R2 | Protein dynamics, different topic; not directly comparable |
| `/home/wg25r/review_agent/human_reviews_2026/bZqCBgm2N0.md` | 6.50 | R2 | Stronger — has theoretical identifiability results CausalNovo lacks |
| `/home/wg25r/review_agent/human_reviews_2026/f12Lo7ZUX5.md` | 6.50 | R2 | Stronger — principled framework with elegant theoretical grounding |
| `/home/wg25r/review_agent/human_reviews_2026/5d7prMWHNF.md` (Delta Embeddings) | 6.00 | R1/R2 | Well-executed but limited to one benchmark; CausalNovo has more comprehensive evaluation |

**Round 1 bracket:** 4.5–6.5. CausalNovo is clearly stronger than the weak de novo sequencing papers (PeakNovo at 3.5, PLMNovo at 2.5) and clearly below the high-band papers (8.0) on different topics.

**Round 2 narrowing:** Comparing to PepTri (5.50, accepted poster) — similar quality, both have methodological gaps but clear empirical contributions. Comparing to Delta Embeddings (6.00, accepted poster) — CausalNovo has more comprehensive evaluation but a more significant methodological gap (capacity confound). Comparing to Beyond DAGs (6.50, accepted poster) — that paper has theoretical identifiability results that CausalNovo lacks. CausalNovo sits between 5.0 and 6.0, closest to 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>