Now I have enough calibration to write the review.

## Summary
The paper introduces "monitorability" as an intrinsic property of neural networks that captures how well internal activations can reveal prediction errors, and proposes the MIRA Score — an integral of Mahalanobis-based surprisal shifts under FGSM-perturbed inputs — to quantify it without external OoD data. The authors validate MIRA by showing its ordering aligns with the best-of-three (ODIN, Mahalanobis, Energy) OoD AUROC across CV, tabular, and NLP models.

## Strengths
- **Clearly framed, novel question.** The paper articulates a property — monitorability as distinct from accuracy — that, even if its formalization is imperfect, is a useful framing. Figure 1's toy example (Net1 vs. Net2 at identical 100% ID accuracy with different penultimate-layer separability) is a sharp illustration of the intuition the score is trying to capture (§3.1).
- **A practical, OoD-free computation.** MIRA is computable with only ID data and a cheap FGSM perturbation, integrated over a perturbation range (Eq. 4). This is a genuine practical advantage over OoD-detection-based evaluations that require curated external OoD sets.
- **Cross-modality evaluation.** Empirical evaluation spans three modalities (CIFAR-10/100, Sensorless Drive Diagnosis, SST-2) with multiple architectures, and the qualitative ordering of MIRA matches the best-of-three AUROC in most blocks of Tables 1–3 (e.g., ViT at MIRA 89.25 vs. CustomNet at -0.07 on CIFAR-10).

## Weaknesses

### Fatal
None. The structural concerns below are serious but the paper still contains a coherent contribution.

### Major
- **Definition 1 and the MIRA Score are not connected.** Definition 1 (§3.2) is a *binary biconditional* property over ID samples: L(f(x), y) ≤ ε ⇔ f^l(x) ∈ Z^l. The MIRA Score (Eq. 4) is a *continuous integral of expected surprisal shifts on FGSM-perturbed features*. The paper bridges them only by the phrase "an abstract formalization … we propose a metric that estimates this property" (§3.3), but no derivation shows MIRA estimates the existence of Z^l or operates on ID misclassifications. The formalization therefore sits beside the metric rather than grounding it, and the headline claim of providing "the first formalization and quantitative measure" overstates the coherence of the contribution.
- **Validation is partly circular with Mahalanobis OoD detection.** MIRA is built on Mahalanobis distance in the penultimate layer, and the "best-of-three" envelope used as ground truth is dominated by the Mahalanobis detector — bolded as best (or tied-best) in essentially every cell of Table 2 and Table 3, and the large majority of Table 1. Showing that a Mahalanobis-perturbation summary correlates with Mahalanobis-detection AUROC is a substantially weaker claim than "MIRA tracks intrinsic monitorability." A genuinely diverse validator pool, or a Mahalanobis-free variant of MIRA, would be needed to support the stronger claim.
- **ID accuracy is not reported, so monitorability is not disentangled from capability.** The paper's motivating example (Fig. 1) hinges on Net1/Net2 achieving *identical* accuracy yet differing in monitorability. None of Tables 1–3 reports ID accuracy, so the headline contrasts (e.g., CustomNet vs. ViT) cannot be read as monitorability differences rather than simply ViT being a better classifier with sharper features. The Figure 1 promise is never instantiated on real data.
- **The "intrinsic" claim is weakened by the perturbation protocol.** Two model-dependent choices break the framing: (a) FGSM uses each model's own gradient, so MIRA conflates feature geometry with adversarial gradient fragility; (b) ε_min is chosen per model to hit a fixed accuracy drop, with ε_max = 2·ε_min (§4.2). The paper acknowledges this in §6 as a limitation, but it is doing real work in the headline comparisons — cross-model differences in MIRA can reflect fragility differences rather than feature-space differences.
- **The central correlation claim is not quantified.** The paper repeatedly asserts that MIRA "correlates with" the best AUROC, yet reports no Pearson/Spearman/Kendall coefficient and no statistical test. With 4 CV models on CIFAR-10, 3 on CIFAR-100, 5 tabular, and 4 NLP, the ordering is read by eye on small blocks. Even the orderings are imperfect: in Table 3, MIRA ranks RoBERTa (2632.94) above DistilBERT (2015.66), but RoBERTa's average AUROC (77.16) is below ELECTRA's (80.61) which MIRA ranks higher correctly — so the ordering isn't strictly preserved across the 4 NLP points. For the headline result of a measurement paper, the absence of any quantitative effect size is a notable gap.

### Minor
- **RQ3 ("detector-agnostic") rests on one cell.** §4.4 supports the detector-agnostic claim by citing exactly one case (DenseNet/Places365, where Mahalanobis underperforms). A single supporting cell is a thin basis for the claim that "MIRA captures intrinsic monitoring potential even when individual detectors disagree."
- **t-SNE visualization (Fig. 2) does no causal work.** Saying "higher MIRA ↔ cleaner t-SNE" largely restates that better classifiers have more separable penultimate features. It is illustrative, not evidence for a property distinct from classification quality.
- **Numerical behavior of the surprisal score across modalities.** S uses the χ² survival function (Eq. 3) which for high-dimensional D_M can be very small, leading to surprisal values in the thousands for NLP versus tens for CV. The paper claims a "dimension-calibrated and unbounded scale" but does not discuss this regime or whether MIRA values are comparable across modalities/architectures with very different feature dimensionalities.
- **Symbol reuse for ε.** In Definition 1, ε is the *loss threshold*. In Eq. 2 and Definition 2 (and the FGSM setup), ε is the *perturbation radius*. These are different quantities and reusing the symbol obscures the disconnect between the definition and the metric.

### Trivial
None.

## Nice-to-Haves
- Validate MIRA against the property Def. 1 actually states: AUROC of feature-based detectors on ID errors (right vs. wrong on ID), rather than OoD AUROC. This would also distance MIRA from the Mahalanobis detector.
- Hold the perturbation budget fixed across compared models, or replace FGSM with a model-independent perturbation (e.g., a fixed Gaussian noise level), so cross-model MIRA differences can be attributed to feature geometry.
- Include detectors that don't share the penultimate-feature Gaussian assumption (e.g., MSP, KNN, ViM, ReAct) in the validator pool, or compute a non-Mahalanobis MIRA variant and show the correlation survives.
- Report quantitative correlation coefficients (Pearson/Spearman) with bootstrap intervals on the within-modality model rankings, along with ID accuracy for each model.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"Missing baselines like MSP/KNN/ViM/ReAct broaden best-of-three"* (Harsh critic, Section 4.1 note) — moved to Nice-to-Haves because it is constructive advice, not a verifiable flaw in the paper as written. Three detectors with different principles is a defensible (if narrow) choice.
- *Strength: "MIRA Score is a practical, OoD-free metric"* — kept (rephrased) under Strengths; it is concrete and well-supported.
- *Strength: "t-SNE visualizations link MIRA to feature-space structure"* — demoted to Minor weakness about the visualization, since it does no causal work beyond restating that better classifiers have more separable features.

## Novel Insights
None beyond the paper's own contributions. The reviewers' most useful insight — that MIRA and the Mahalanobis OoD detector share the same penultimate-feature Mahalanobis machinery and so the validation is partly circular — is a finding *about* the paper, not a new claim of its own.

## Suggestions
- Either reformulate Definition 1 as a graded quantity that MIRA actually estimates (e.g., AUROC of an optimal feature-space detector for ID errors), or drop the formal definition and present MIRA as a useful empirical diagnostic. The current binary-definition + continuous-estimator pairing is the single biggest structural problem.
- Report ID accuracy in every table and produce at least one within-accuracy controlled comparison (the Fig. 1 promise on real data).
- Replace per-model ε with a common ε or a model-independent noise perturbation in the headline comparisons.
- Report Spearman/Pearson rank correlation with confidence intervals across all (model, AUROC, MIRA) triples.
- Demonstrate MIRA's value via a non-Mahalanobis validator (e.g., MSP/KNN/ViM) to defuse the circularity concern.

## Evaluation Axes
- **Originality.** The framing of "monitorability" as a property distinct from accuracy is a fresh angle; the formalization itself is straightforward but novel as far as the paper claims.
- **Importance.** Pre-deployment, OoD-free diagnostics for monitorability are genuinely useful to practitioners. The question matters.
- **Soundness of claims.** Weakest axis. Def. 1 ≠ MIRA, Mahalanobis-Mahalanobis circularity, per-model ε, missing ID accuracy, and unquantified correlations together undermine the headline.
- **Soundness of experiments.** Cross-modality evaluation is a strength, but sample sizes within each block are small and no statistical test backs the central claim.
- **Clarity.** Generally readable; the chief clarity issue is the symbol reuse of ε and the lack of a derivation linking Def. 1 to Def. 2.
- **Value to the community.** The concept is worth pursuing; the current execution leaves the central claim under-supported.

## Calibration

Round-1 anchors retrieved (all rounds; ★ = read in full):

- ★ l5ouuojPGe — "Red Pill or Blue Pill? Thresholding Strategies for NN Monitoring" — avg **3.00** — R1 low band — *Closest topical match (runtime NN monitoring); rejected for unclear contribution and weak experimental design — MIRA is structurally similar but has a more articulated metric and concept.*
- 6Z8rZlKpNT — "Normalizing Flows for OOD" — avg 3.40 — R1 low band — Topically OOD; rejected for limited novelty/scope. MIRA scope of contribution slightly larger (a new property concept).
- KK29oh8jZs — "IN the known, OUT of the ordinary" — avg 3.00 — R1 low band — Synthetic OOD benchmarks; different focus.
- rcKzU0Vns0 — "Unified AL + OOD" — avg 2.50 — R1 low band — Different framing.
- ★ VAmVEghgoC — "NC-OOD" — avg **4.50** — R1 mid band — Comparable methodology paper, rejected for unconvincing justification and missing comparisons. MIRA has worse structural alignment between motivation and method than NC-OOD, but a more original framing.
- ljwoQ3cvQh — "Deep Neural Networks Tend To Extrapolate Predictably" — avg 7.00 — R1 mid band — Stronger experimental program; not directly comparable.
- 9ROuKblmi7 — "NECO" — avg 5.75 — R1 mid band — Accepted; new OOD method with theoretical grounding.
- Gr8nHvOivO — "Neural Collapse OOD" — avg 4.50 — R1 mid band — Similar tier to NC-OOD.
- cJs4oE4m9Q — "Deep Orthogonal Hypersphere" — avg 8.00 — R1 high band — Strong methodology paper; not comparable.
- kbjJ9ZOakb, cNmu0hZ4CL, KbetDM33YG — avg 8.00 — R1 high band — Topically distant.
- ★ 5HGPR6fg2S — "Normalized Space Alignment" — avg **3.75** — R2 — New representation-space metric, rejected for unconvincing motivation and limited validation. Similar tier to MIRA: a new metric where the metric's connection to claimed property is the weakness reviewers focused on.
- dA4EWchlbn — "Adversarial Robustness from Data Perspective" — avg 3.50 — R2 — Similar tier.
- kz78RIVL7G — "Statistical Attack-Agnostic Detection" — avg 2.60 — R2 — Detection metric; less coherent.
- RxhOEngX8s — "Expecting The Unexpected" — avg 4.25 — R2 — Benchmark/evaluation paper.
- ★ 9qpdDiDQ2H — "MetaOOD" — avg **5.25** — R2 — Accepted: OOD model selection with statistical tests and broader experimental scope. Clearly above MIRA on validation rigor.
- GQhlM0Mavg — "OOD and Conformal Prediction" — avg 5.00 — R2 — Conceptual bridging paper, comparable level of novelty but stronger formalism.

**Round-1 bracket.** Topical anchors cluster between 3.0 and 4.5. MIRA has more articulated novelty than the 3.0 Red Pill paper but has structural soundness issues (Def 1 ≠ MIRA, Mahalanobis circularity) at least as severe as NC-OOD (4.5). Initial bracket: **3.0–4.5**.

**Round-2 narrowing.** Within 2.5–4.5: NSA (3.75) is the sharpest comparison — a new metric whose connection to the claimed property is the central weakness, with limited validation. MIRA has similar structural problems plus the Mahalanobis circularity, but a more compelling motivating concept (monitorability as distinct from accuracy). On the upper side, MetaOOD (5.25, accepted) is clearly above MIRA because it has Wilcoxon-tested statistical validation across 24 dataset pairs. NC-OOD (4.5) is comparable but better experimentally supported than MIRA.

Placing MIRA between NSA (3.75) and NC-OOD (4.5), closer to NSA because of the Mahalanobis-circular validation and missing quantitative correlations: **3.5**.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>