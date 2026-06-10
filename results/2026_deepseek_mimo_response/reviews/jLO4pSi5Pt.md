Now I have enough calibration data. Let me finalize the review.

Based on my calibration:
- Round 1 bracket: 6.0–8.0
- Round 2 anchors: PROGRAM (6.20), TTVD (6.00), TTE (6.50), Active TTA (6.75) in the 5.5–7.0 range; READ (8.00) in the 7.0–8.5 range
- Concept drift paper (7.00) from Round 1 is the closest comparator

**Positioning**: L-TTA has a cleaner problem formulation, more comprehensive evaluation (15 datasets, 3 imbalance ratios, 4 benchmarks), and theoretical grounding (BEM propositions) compared to PROGRAM (6.20) and TTVD (6.00). It's closer to the concept drift paper (7.00) — both address LT issues in VLMs, but L-TTA has cleaner evaluation while the concept drift paper has confounding experimental factors. However, L-TTA has the EP description-math inconsistency and missing error bars, while READ (8.00) has a cleaner presentation and a more fundamental paradigm innovation. I place L-TTA at 6.5 — clearly above the TTA papers at 6.0–6.2, slightly below the concept drift paper at 7.0 due to the EP exposition issue and missing error bars.

## Summary
This paper proposes L-TTA, the first method for test-time adaptation of vision-language models under long-tailed test distributions. It introduces three co-designed mechanisms — Synergistic Prototypes (SyPs), Rebalancing Shortcuts (RSs), and Balanced Entropy Minimization (BEM) — and evaluates on 15 datasets across OOD, cross-domain, and corruption benchmarks under three imbalance ratios (10, 20, 50).

## Strengths
- **First systematic treatment of LT-TTA for VLMs with concrete failure mode identification**: The paper identifies text-induced tail erosion and modality-bias amplification as unique challenges, supported by Figure 1(b) showing per-class accuracy patterns and VLM backbone instability under long-tailed settings. This establishes a well-motivated problem that prior TTA work on balanced distributions does not address.
- **Theoretically grounded BEM with formal propositions**: Propositions 1 and 2 (§3.2) prove that standard EM creates a gradient gap favoring head classes, and that BEM shortens this gap (Eq. 10). The penalty term (1−P̃)^β in Eq. 9 provides an elegant mechanism that reduces the contribution of confident (typically head) classes while favoring rare and uncertain classes.
- **Consistent and substantial macro-F1 improvements demonstrating class-balancing**: On the OOD benchmark (Table 1, imb=10), L-TTA achieves +3.61% macro-F1 over the next-best DPE (61.18 vs 57.57). The macro-F1 improvements consistently exceed accuracy improvements across all three benchmarks (Tables 1–3), directly confirming the method addresses class balance specifically.
- **Robustness to increasing imbalance severity**: L-TTA shows only 1.29% macro-F1 variation across imb=10→50 on OOD Average, compared to 4.86% for TDA and 4.72% for DPE (Table 1).
- **Comprehensive evaluation**: 15 datasets, 3 benchmark types, 3 imbalance ratios, 12 recent baselines (including CVPR'25 and NeurIPS'24 methods), multi-backbone evaluation on 4 additional VLMs (Table 5), and efficiency analysis (Table 4: 1.45h, 1.89G).
- **Clean ablation studies**: Table 6 shows each component's contribution (~3–4% macro-F1 drop when removing DP or EP). Figure 4 provides sensitivity analyses for all major hyperparameters.

## Weaknesses

### Fatal
None

### Major
- **Conceptual description of Exclusionary Prototypes (EPs) contradicts the mathematical formulation** — The paper describes EPs as storing "the most improbable features of each class" (§3.2, line 98) and claims they "indirectly exclude the features least likely to occur in every class" (line 106). However, in Eq. 5, φ_c = (max P − P_c) / max P. When class c is the predicted class (P_c is maximal), φ_c = 0, yielding the strongest update weight (N^{EP}). When P_c ≈ 0, φ_c ≈ 1, yielding a weaker update. This means EPs are updated *most strongly* by samples predicted *as* that class — they accumulate class-typical features, not "improbable" ones. The mechanism works by including class-typical features that are then subtracted in Eq. 8 to suppress overconfident matching. This is effective (ablation confirms ~3% macro-F1 contribution), but the verbal description mischaracterizes what EPs encode. Since EP is one of three core contributions, this narrative-math mismatch needs resolution: either the description should accurately characterize the mechanism, or Eq. 5 should be reformulated to match the stated intent.
- **No variance or confidence intervals despite claiming 5 runs** — The paper states "We conduct 5 runs for each experiment" but Tables 1–3 report only means. For improvements of 1–3% (e.g., ImageNet-V2 at imb=50: L-TTA 67.10 vs DPE 65.80), TTA's inherent stochasticity (random augmentation crops, data ordering) means these gaps could plausibly fall within one standard deviation. Error bars are needed to validate whether the reported SOTA is genuine.

### Minor
- **K = 0.3 in implementation vs K = 0.2 in ablation** — The implementation details (§4, line 208) state K = 0.3, but the ablation (§4.2, line 334) explicitly reports "setting K = 0.2 yields the best performance." If K = 0.3 was chosen for cross-dataset robustness, this should be stated; otherwise the main results should use the empirically best value.

### Trivial
None

## Nice-to-Haves
- Quantitative analysis correlating text-prior strength with per-class accuracy degradation would strengthen the "text-induced tail erosion" failure mode analysis beyond the qualitative Figure 1.
- Temporal analysis showing how accuracy evolves during the datastream (early vs. late) would clarify whether L-TTA primarily prevents late-stage tail collapse.
- Brief sensitivity analysis of the affinity function A(x) = λ₁ exp(−λ₂(1−x)), given that λ₁ = λ₂ = 6 makes it very steep near x = 1.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Table 7 formatting (Harsh Critic)**: The Flowers column layout is slightly inconsistent but the data is present; this is a minor presentation artifact, not a substantive issue.
- **Synthetic LT distribution limitation (Harsh Critic)**: Random sampling with exponential decay is standard practice in LT learning literature and not a unique weakness.
- **Temporal adaptation analysis scope creep (Harsh Critic)**: Suggesting analysis of when L-TTA helps most during the datastream is a nice-to-have, not a core flaw within the paper's stated scope.
- **Affinity function A(x) sensitivity (Harsh Critic)**: Adopted from prior work; sensitivity analysis would strengthen but is not required.

## Novel Insights
The EP mechanism, despite its naming issues, represents a genuinely novel design choice: using all views to update all class prototypes with prediction-probability-weighted incorporation rates ensures tail classes accumulate prototype representations even when rarely predicted. The BEM penalty term (1−P̃)^β is an elegant, principled solution to the unsupervised rebalancing problem where standard logit adjustment would exacerbate head-class bias under EM.

## Suggestions
1. Rewrite the EP conceptual description to accurately reflect the mechanism — EPs store class-typical features that, when subtracted, suppress overconfident matching — or reformulate Eq. 5 to match the "improbable features" intent.
2. Add ±std notation to Tables 1–3, at minimum for OOD Average and Average columns.
3. Reconcile K = 0.3 implementation with K = 0.2 ablation finding: either use K = 0.2 or explain the discrepancy (e.g., cross-dataset robustness selection).

## Calibration Report

**Retrieved anchors across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| pdzHpQbGrn (Active TPT) | 2.50 | 1 | Clearly weaker — flawed setting, limited contribution |
| JIlIYIHMuv (LVLM-CL) | 2.50 | 1 | Clearly weaker — lacks clear contribution |
| ZaudLwn0Hm (Prototypical evaluation) | 2.50 | 1 | Clearly weaker |
| gNoqEdT2wO (MCIL benchmark) | 2.33 | 1 | Clearly weaker |
| b20VK2GnSs (Concept drift MLLM) | 7.00 | 1 | Most similar topic; L-TTA has cleaner evaluation but EP naming issue; comparable overall |
| BUDxvMRkc4 (BLG) | 4.67 | 1 | Weaker — limited scope, less evaluation |
| lF9QXpfNHm (ROSITA) | 4.67 | 1 | Weaker — overclaimed setting, limited baselines |
| 9RnTw9YiXV (Long-tail LVLMs) | 4.40 | 1 | Weaker — analysis-focused, less methodological contribution |
| TPZRq4FALB (READ) | 8.00 | 1 | Stronger — novel paradigm, cleaner presentation, perfect reviewer consensus |
| WyEdX2R4er (Visual Data-Type) | 8.00 | 1 | Different focus (analysis paper), stronger consensus |
| uAFHCZRmXk (Two Effects) | 8.00 | 1 | Different focus (analysis), stronger consensus |
| 9Cu8MRmhq2 (Multi-granularity) | 8.00 | 1 | Different area, stronger consensus |
| YHUGlwTzFB (Active TTA) | 6.75 | 2 | Similar TTA area; L-TTA has more extensive evaluation and clearer novel problem |
| 5sU32OCxgZ (TTVD) | 6.00 | 2 | L-TTA has broader evaluation and clearer novelty |
| 4wk2eOKGvh (TTE) | 6.50 | 2 | L-TTA has more comprehensive evaluation and a novel problem setting |
| x5LvBK43wg (PROGRAM) | 6.20 | 2 | Similar prototype-based TTA; L-TTA has better theoretical grounding and more extensive evaluation |
| TPZRq4FALB (READ) | 8.00 | 2 | Stronger; novel paradigm with perfect consensus |
| X1OfiRYCLn (VLB) | 7.50 | 2 | Different focus; strong but unrelated |

**Round 1 bracket: 6.0–8.0**
**Round 2 narrowing: 6.2–7.0**

L-TTA is clearly above PROGRAM (6.20) due to more extensive evaluation, clearer novelty (first LT-TTA), and theoretical grounding for BEM. It is comparable to the concept drift paper (7.00) — L-TTA has cleaner evaluation (15 datasets vs. limited experiments, no confounding factors) but has the EP exposition issue and missing error bars. It is below READ (8.00) which has a more fundamental paradigm innovation and perfect reviewer consensus. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>