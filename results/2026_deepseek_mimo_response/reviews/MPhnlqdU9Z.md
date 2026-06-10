Now I have enough anchors to calibrate. Let me write the final review.

**Round 1 bracket:** 4.5–7.0. The paper is clearly above the rejected OoD detection papers in the 3.0–4.75 range (more novel concept, broader experiments), but below the accepted "LiDAR" (6.67) which reported formal Spearman/Kendall correlations.

**Round 2 narrowing:** 5.5–6.5. The paper is comparable to MetaOOD (5.25, accepted, similar domain but weaker methodology) but stronger conceptually, and comparable to LiDAR (6.67, accepted) in ambition but weaker in empirical rigor.

**Final positioning:** The paper's genuine conceptual novelty and multi-modal experimental breadth place it above weak accepts, but the missing correlation analysis and small model sets prevent it from reaching the level of well-validated metric papers like LiDAR. Score: **6.0**.

---

## Summary
This paper introduces "monitorability" as a formal intrinsic property of neural networks—capturing the degree to which a model's internal representations enable runtime error detection—and proposes the MIRA Score, a practical metric computed using only ID data and FGSM perturbations. Experiments across vision (CIFAR-10/100 with 4 models), tabular (5 models), and NLP (4 transformer models) domains show that higher MIRA scores consistently align with better best-of-3 OoD detection AUROC across 3 detection methods.

## Strengths
- **Genuinely novel conceptual contribution.** The distinction between "detecting anomalies" and "characterizing whether anomalies are detectable" is well-motivated, practically relevant for safety-critical model selection, and—to the authors' knowledge—the first formalization of this property. Figure 1's toy example effectively demonstrates two models with identical ID accuracy but vastly different feature separability.
- **Consistent rank-ordering trends across three modalities.** In every experiment (Tables 1–3), higher MIRA scores align with better best-of-3 AUROC: ViT MIRA=89.25 → ~99% AUROC vs. CustomNet MIRA=−0.07 → weakest detection on CIFAR-10; DeBERTaV3 MIRA=3793.6 → 86.29% vs. DistilBERT MIRA=2015.7 → 76.54% on SST-2; WideMLP MIRA=63.5 → 92.88% vs. DeepTransformer MIRA=4.37 → 77.86% on tabular data.
- **Practical, OoD-data-free metric.** MIRA requires only ID data and FGSM perturbations—no external OoD datasets, no generative models, no detector-specific tuning—making it usable as a pre-deployment evaluation tool addressing a genuine practical gap.
- **Well-motivated technical construction.** The pipeline (Eq. 2–4: perturbation → Mahalanobis distance → chi-square normalization to dimensionless surprisal → integration over perturbation magnitudes) is justified step-by-step, with the chi-square normalization (Eq. 3) specifically addressing cross-layer and cross-architecture comparability.
- **Comprehensive experimental breadth.** 13+ model architectures across vision (CNNs, ViTs), tabular (MLPs, Transformers), and NLP (RoBERTa, DeBERTa, ELECTRA, DistilBERT), with 7/6/4 OoD datasets respectively, supporting the generalizability claim.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative correlation analysis despite headline claim.** The paper's central empirical claim (Abstract: "the MIRA Score correlates with the strongest actual detection performance"; RQ1; Discussion) is that MIRA correlates with best achievable OoD detection. Yet no correlation coefficient (Spearman ρ, Pearson r, Kendall τ) is ever reported, no scatter plot is shown, and no p-value is computed. The "correlation" is assessed purely by eyeballing rank-orderings in tables of 4–5 data points. With only 3–5 models per modality, consistent rank-ordering could arise by chance. Computing Spearman ρ with p-values is trivial and would either validate or undermine the paper's primary contribution.

- **Shared inductive bias between MIRA computation and one validation detector.** MIRA uses Mahalanobis distance (Eqs. 1–4) to measure feature separability. One of the three OoD detectors comprising the "best achievable detection performance" target is also the Mahalanobis distance method (Lee et al., 2018b). This creates a confound: MIRA's alignment with best-of-3 is partly expected because it shares the same inductive bias as one component. The paper should report MIRA's correlation with each detector independently, or remove Mahalanobis from the validation set.

- **Very small model sets with no sensitivity analysis.** Each setting tests only 3–5 models (4 on CIFAR-10, 3 on CIFAR-100, 5 tabular, 4 NLP). No sensitivity analysis is provided for key design choices: the perturbation range [ε_min, ε_max], the accuracy threshold for ε_min, or the ε_max = 2·ε_min heuristic (Section 4.2). The paper acknowledges the perturbation range limitation but provides no experiments quantifying its impact.

### Minor

- **Formal definition (Definition 1) is trivially satisfiable.** As the paper acknowledges ("Z^l may be arbitrarily complex"), for any ε one can set Z^l = f^l({x : L(f(x),y) ≤ ε}), making every model with learned features monitorable. This is a necessary-but-not-sufficient condition that does not capture monitoring difficulty. The paper should either add a complexity constraint or explicitly acknowledge this as a characterization gap that MIRA addresses quantitatively.

- **Ambiguous rank-orderings at close model quality.** For CIFAR-100 (Table 1), ResNet-18 (MIRA=0.66) and DenseNet (MIRA=2.81) show similar best-of-3 AUROC averages despite different MIRA scores. For NLP (Table 3), RoBERTa (MIRA=2632.9) and DistilBERT (MIRA=2015.7) show minimal AUROC difference (77.16 vs. 76.54). These boundary cases weaken the "clear correlation" narrative and suggest MIRA's discriminative power may be limited for similarly-performing models.

### Trivial
None.

## Nice-to-Haves
- Comparison to alternative monitorability proxies (e.g., Fisher's linear discriminant ratio, between/within-class variance ratio) to establish that MIRA captures something beyond generic feature quality.
- Discussion of why "best-of-3" is a reasonable proxy: all three detectors operate on the penultimate layer—monitoring on logits or early layers could yield different rankings.
- Sensitivity ablation for perturbation range parameters.

## Removed Points
These points are flagged to be removed; treat them with caution.
- The harsh critic's framing of Definition 1 as "fatal" or "structural" is demoted. The definition is indeed trivially satisfiable, but the paper acknowledges Z^l can be "arbitrarily complex" and MIRA's purpose is precisely to quantify the quantitative aspect Definition 1 omits. This is a real but minor conceptual gap, not a fatal flaw.
- Strength from Strength Finder claiming "strong empirical correlation" is removed because no formal correlation metric is computed—consistent rank-ordering across 4–5 models is suggestive but does not constitute "strong" correlation.

## Novel Insights
The paper's genuinely novel contribution is the conceptual reframing: shifting from "detect OoD inputs" to "measure whether OoD detection is feasible for this model." This distinction has clear practical value for model selection in safety-critical deployment. The MIRA score—probing decision boundaries with perturbations to assess feature separability without OoD data—is a technically sound instantiation that could spawn a line of work on intrinsic model evaluation metrics.

## Suggestions
- Compute Spearman ρ (with p-values and confidence intervals) for each modality. This single addition would transform the empirical evidence from suggestive to rigorous.
- Report MIRA's correlation with each individual OoD detector to disentangle the shared-Mahalanobis confound.
- Add a brief sensitivity analysis for perturbation range parameters.

## Calibration Report

### Anchors Retrieved

**Round 1 (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| l5ouuojPGe.md (Thresholding Strategies for NN Monitoring) | 3.00 | 1 | Less novel concept; narrower scope; worse presentation |
| KK29oh8jZs.md (Probing OOD with Synthetic Datasets) | 3.00 | 1 | Incremental contribution; narrower scope than MIRA |
| rcKzU0Vns0.md (Active Learning + OOD) | 2.50 | 1 | Less focused; weaker empirical validation |
| 6Z8rZlKpNT.md (Normalizing Flows for OOD) | 3.40 | 1 | Method-only contribution; no model-evaluation angle |
| VAmVEghgoC.md (NC-OOD) | 4.50 | 1 | Similar domain but limited novelty (weight vector distance) |
| Gr8nHvOivO.md (OOD via Neural Collapse) | 4.50 | 1 | Similar domain; incremental over existing detectors |
| YMgMGPjUPg.md (NAP for OOD) | 4.75 | 1 | Incremental; overlaps with existing methods like ASH |
| Oo5spZRpH6.md (HAct for OOD) | 3.67 | 1 | Method-only; no model-evaluation concept |
| KbetDM33YG.md (Online GNN Evaluation) | 8.00 | 1 | Stronger: novel problem, formal validation (Spearman ρ), comprehensive ablations |
| cJs4oE4m9Q.md (Hypersphere Compression) | 8.00 | 1 | Different domain; strong theoretical + empirical contribution |
| kbjJ9ZOakb.md (Neuron Invariance Manifolds) | 8.00 | 1 | Different domain; strong theoretical grounding |
| SctfBCLmWo.md (Dataset Bias) | 8.00 | 1 | Different domain; major finding with broad implications |

**Round 2 (narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| oKglS1cFdb.md (Feature Accompaniment) | 5.67 | 2 | Rejected; addresses a related question about OOD generalization from ID data; MIRA's concept is more novel |
| 9qpdDiDQ2H.md (MetaOOD) | 5.25 | 2 | Accepted; weaker methodology (one reviewer gave 3, concerns about baselines); MIRA is conceptually stronger |
| todLTYB1I7.md (Neuron Explanation Evaluation) | 5.00 | 2 | Rejected; different domain but similar "evaluation metric" structure; MIRA has broader experiments |
| AhMEkBSdIV.md (LCA-on-the-Line) | 5.33 | 2 | Rejected; predicts OOD from ID using class taxonomies; MIRA's monitorability concept is more distinct |
| ugXGFCS6HK.md (Principal Distortions) | 6.20 | 2 | Accepted; novel metric for comparing representations; comparable novelty but different domain |
| f3g5XpL9Kb.md (LiDAR) | 6.67 | 2 | Accepted; closely analogous paper—metric for representation quality; LiDAR reports Spearman/Kendall correlations (reviewer strength #3); MIRA lacks this |
| Qj1KwBZaEI.md (Intrinsic Dimension Correlation) | 7.00 | 2 | Accepted; novel metric with theoretical grounding; stronger theory than MIRA |
| eN0RyRVbSm.md (Double Descent + OOD) | 6.50 | 2 | Rejected; theoretical + empirical on OOD and model complexity; comparable empirical rigor |

### Bracket and Score Justification

**Round 1 bracket: 4.5–7.0.** MIRA is clearly above rejected OoD papers in the 3.0–4.75 range (more novel concept, broader multi-modal experiments, practical model-evaluation angle). It is clearly below the 8.0 anchors (which have formal statistical validation, theoretical grounding, or broader ablations).

**Round 2 narrowing: 5.5–6.5.** MIRA is stronger than MetaOOD (5.25, accepted) conceptually and in breadth of experiments, but weaker than LiDAR (6.67, accepted) in empirical rigor—LiDAR reports Spearman and Kendall coefficients while MIRA relies on eyeball rank-orderings. The closest comparator is ugXGFCS6HK (6.20, accepted), which proposes a representation metric with comparable novelty.

**Final score: 6.0.** The paper's genuine conceptual novelty (monitorability as a first-class model property) and broad multi-modal experiments place it above weak accepts. However, the absence of formal correlation analysis, the shared-Mahalanobis confound, and small model sets prevent it from reaching the level of well-validated metric papers like LiDAR (6.67). A version with Spearman ρ + p-values and expanded model sets would comfortably score 7+.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>