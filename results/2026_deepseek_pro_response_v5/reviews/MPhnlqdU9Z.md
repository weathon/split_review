## Summary
This paper introduces *monitorability*, a novel concept capturing how well a neural network's internal representations can support runtime error detection, and proposes the MIRA Score as a practical metric that quantifies monitorability using only in-distribution data via FGSM perturbations and Mahalanobis distance-based feature separability. The authors validate MIRA across three modalities (vision, tabular, NLP) by comparing it against the best-achievable OoD detection performance from three detectors.

## Strengths
- **Novel conceptual contribution**: The idea of monitorability as a property separable from accuracy is genuinely novel and well-motivated. The toy example (Figure 1, Section 3.1) effectively illustrates how two models with identical ID accuracy can organize feature space differently, making one more amenable to error detection than the other.
- **Principled metric design that requires no OoD data**: The MIRA Score integrates several well-motivated components — FGSM perturbations (Section 4.2), Mahalanobis distance, and chi-square survival-function calibration (Equation 3) — into a single score computable from ID data alone. This is a practical advantage over methods that require held-out OoD data for tuning.
- **Consistent rank-ordering across three modalities**: Across vision (Table 1), tabular (Table 2), and NLP (Table 3), higher MIRA scores consistently correspond to stronger OoD detection performance. The NLP results show a particularly clean ordering: DeBERTaV3 (MIRA 3793.6, Mahalanobis avg 86.29) > ELECTRA (3636.7, 80.61) > RoBERTa (2632.9, 77.16) > DistilBERT (2015.7, 76.54). The vision results similarly show ViT dominating and CustomNet at the bottom.
- **t-SNE visualizations corroborate quantitative trends**: Figure 2 shows that higher-MIRA models (ViT) exhibit visibly better class separation in penultimate-layer activations compared to lower-MIRA models (CustomNet), providing qualitative support that MIRA tracks a real structural property of the feature space.
- **Detector-agnostic evaluation strategy**: Using three fundamentally different OoD detectors (ODIN, Mahalanobis, Energy) as validation targets is a sensible approach, and the paper explicitly discusses cases where individual detectors disagree (e.g., DenseNet's Mahalanobis detector failing on Places365 while ODIN/Energy succeed, line 271).

## Weaknesses

### Fatal
None.

### Major
- **No quantitative correlation analysis**: The paper's central empirical claim is that MIRA "correlates with the strongest actual detection performance" (abstract, Section 4.4). Yet no correlation coefficient (Spearman ρ, Pearson r), p-value, or any quantitative measure of association is reported. The evidence consists entirely of eyeballing rank-orderings across 3–5 models per domain. While the trends are visually consistent, the paper claims to have *validated* MIRA as a "reliable tool" (abstract) and to demonstrate a "strong correlation" (Section 6, line 287) without any statistical quantification. This weakens the empirical contribution significantly.

- **Mahalanobis circularity unaddressed**: MIRA is built on Mahalanobis distance and chi-square calibration (Definition 2, Equations 3-4). One of the three OoD detectors used as a validation target is the Mahalanobis detector (Lee et al., 2018b), which leverages the same underlying distance and Gaussian Discriminant Analysis assumption (Section 2, line 39). The paper never discusses this shared foundation. This is particularly concerning for the tabular (Table 2) and NLP (Table 3) experiments, where the Mahalanobis detector is consistently the best-performing method by a wide margin, meaning the metric-to-validator alignment may partly reflect shared machinery rather than genuine predictive power.

- **"Best-of" aggregation not operationalized**: Section 4.1 claims the evaluation uses "best achievable detection performance across three representative methods," yet the tables report per-detector averages across OoD datasets and never compute a single "best-of" number per model. The discussion (line 271) compares MIRA qualitatively against whichever detector performs best, but no explicit best-of scores are computed or tabulated. This makes the claimed validation against "best achievable performance" imprecise and difficult to reproduce.

- **Definition-metric gap**: Definition 1 formalizes monitorability as an all-or-nothing iff condition — a model is l-monitorable if there exists a set Z^l such that *for all* (x,y), L(f(x),y) ≤ ε iff f^l(x) ∈ Z^l. The MIRA Score produces a continuous value based on perturbation-integrated feature separability. The paper acknowledges this gap in a single sentence (line 81) but provides no bridging argument, theorem, or even informal justification connecting the binary definition to the continuous metric. The two sit in parallel without a logical link.

### Minor
- **ε_min threshold not stated in main text**: The perturbation range depends critically on ε_min, defined as "the smallest value that reduces accuracy to a certain threshold" (line 133). The specific accuracy threshold used is never stated in the main paper (deferred to Appendix B.6). This is a key hyperparameter that directly controls the MIRA Score.

- **ODIN/Energy failures in Table 2 undiscussed**: In the tabular experiments, ODIN and Energy score near 0.00% AUROC on OoD classes 7 and 11 across all MLP variants. A 0.00% AUROC on a binary detection task indicates catastrophic failure. The paper reports these values without comment, which raises questions about either detector configuration or evaluation protocol.

- **Single-layer evaluation**: MIRA is computed only at the penultimate layer for all experiments. While this is a reasonable default, no ablation or sensitivity analysis across layers is provided. The paper's conclusion claims MIRA can "guide design decisions such as selecting the most suitable layer for feature-based monitoring" (line 287), yet no evidence for this claim is presented.

### Trivial
- **Notation ambiguity in Definition 1**: The quantifier "∀ (x, y) ∼ P_in" (line 69) mixes universal quantification with distribution sampling notation. It is unclear whether this means "for all (x,y) in the support of P_in" or carries a measure-theoretic interpretation.

## Nice-to-Haves
- Discuss whether MIRA scores are intended to be comparable across modalities (currently spanning orders of magnitude: [−0.07, 89] for vision, [4, 64] for tabular, [2016, 3794] for NLP) or only within-domain, and whether any normalization could address the scale gap.
- Clarify whether uniform p(ε) was used in the experiments or another weighting scheme.
- A controlled comparison (e.g., ViT from scratch vs. pretrained) to help disentangle pretraining quality from architectural monitorability would strengthen the vision results.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Toy example 100% accuracy is almost tautological"** (Harsh Critic): The synthetic nature of the toy example is appropriate for its illustrative purpose; the point is to demonstrate that monitorability can differ at fixed accuracy, not to make a statistical claim.
- **"FGSM gradient direction as an unexamined design choice"** (Harsh Critic): The paper explicitly addresses this in Section 4.2, stating that the perturbation just needs to provide a meaningful direction toward the boundary and that FGSM is chosen for efficiency over stronger attacks. This is a deliberate and justified choice, not an oversight.
- **"Pretraining confound between ViT and CNNs"** (Harsh Critic): The paper uses standard publicly available pretrained models and does not claim a controlled architectural comparison. The tabular and NLP results (which lack this pretraining asymmetry) show the same MIRA-performance alignment, mitigating the concern.
- **Generic Strength Finder points**: "Clear formal definition" and "computational practicality" are accurate but superficial as standalone strengths. The paper's formalism is adequate but not exceptional, and efficiency claims are secondary.

## Novel Insights
The paper's core insight is that neural networks can be characterized by an intrinsic property — monitorability — that is conceptually and empirically separable from accuracy. The specific finding that this property can be estimated from ID data alone, without access to any OoD samples, by probing the model with boundary-directed perturbations and measuring representational disruption, is both novel and practically useful. The consistent alignment of this probe-based score with actual OoD detection capability across vision, tabular, and NLP domains suggests that monitorability is a genuine structural property of learned representations rather than an artifact of a particular architecture or data type.

## Suggestions
- Compute and report Spearman's ρ between MIRA and best-of-detector AUROC (explicitly defined as max over ODIN/Mahalanobis/Energy, averaged across OoD datasets) for the full set of 16 model-dataset pairs. Even if N per domain is small, the combined evidence across all domains would be informative. A scatter plot would complement this.
- Discuss the Mahalanobis circularity explicitly. Compute MIRA's correlation separately for the Mahalanobis detector and for the non-Mahalanobis detectors (ODIN, Energy) to quantify how much of MIRA's predictive power is driven by shared machinery.
- Add an explicit "best-of" column to the tables showing max(ODIN avg, Mahalanobis avg, Energy avg) per model.
- Include a brief bridging argument (at minimum an informal paragraph) connecting Definition 1's iff condition to the perturbation-integral design of MIRA, or relax Definition 1 to a probabilistic/continuous form that more directly motivates the metric.

## Score and Decision

**Calibration round 1 (bracketing)**: Anchors spanned from 3.00 (thresholding for NN monitoring, `l5ouuojPGe`) to 8.00 (various accept papers). Initial bracket: 3.5–5.5.

**Calibration round 2 (narrowing)**: Retrieved anchors at 3.67 (`Trg9qb0d5U`, DNN accuracy estimation without test data), 4.33 (`wIFvdh1QKi`, metric space magnitude for representation evaluation), 4.75 (`hlijRgXTDK` and `YMgMGPjUPg`), and 5.50 (`bcWwhF8cTZ`, gradient norm as OOD proxy). The MIRA paper is clearly stronger than the 3.00–3.67 band (those papers had severe presentation issues, limited evaluation scope) but does not match the rigor of the 5.50 anchor (which had theoretical backing plus stronger empirical validation). The paper lands between 4.33 and 5.50, closest to the 4.75 anchors but with a slight discount for its central empirical gap (no quantitative correlation) and unaddressed methodological concerns. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>