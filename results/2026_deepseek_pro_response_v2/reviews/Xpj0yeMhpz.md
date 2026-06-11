Now I have a clear calibration picture. Let me finalize.

**Round 1 bracket**: 5.5–7.0 (anchored by same paper at 5.75, LAF at 6.00, Utility/Complexity at 6.60)

**Round 2 narrowing**: The closest comparators are:
- Same paper (5.75, Reject) — scores [6, 6, 3, 8]; the 3-reviewer didn't read appendix and was biased by submission length
- Label-Agnostic Forgetting (6.00, Accept) — comparable in quality; novel problem + solid experiments + some weaknesses
- SLUG (5.75, Reject) — clever idea but limited evaluation
- Utility/Complexity (6.60, Accept) — theoretical paper with formal guarantees; stronger

This paper is comparable to LAF (6.00): both introduce novel problem formulations with solid core experiments and have fixable weaknesses. The LLM results are the main drag, but they're presented as case studies. The image classification results are comprehensive and the margins are dramatic. **Final score: 6.0, Accept.**

---

## Summary
This paper introduces a novel problem formulation for machine unlearning that decouples the class label from the target concept. The authors define four unlearning scenarios (all-matched, target mismatch, model mismatch, data mismatch) based on relationships among the label domains of forgetting data, model output, and target concept. They analyze the challenges arising from label-domain mismatch through representation-level forgetting dynamics ("representation gravity") and propose TARF, a three-phase framework using annealed gradient ascent and target-aware gradient descent. Experiments on CIFAR-10/100 and ImageNet-1k show TARF consistently achieves the lowest Gap metric across all four scenarios, with dramatic improvements in mismatched settings where existing methods fail.

## Strengths
- **Novel and rigorous problem formulation**: The paper provides the first systematic taxonomy of label-domain mismatch in class-wise unlearning, defining four scenarios via the subclass relation. Each setting is instantiated with concrete CIFAR-100 examples (Figure 1). This is a genuine conceptual advance over prior work that uniformly assumed label alignment.
- **Strong empirical results on image classification**: Table 3 shows TARF achieves the lowest Gap in all four scenarios on both CIFAR-10 and CIFAR-100. In CIFAR-100 target mismatch, TARF achieves Gap=0.21 vs. next-best GA at Gap=8.86 — a ~40× reduction. Table 4 extends this to ImageNet-1k where TARF again achieves the lowest Gap across all four settings.
- **Well-motivated algorithm design grounded in analysis**: The three-phase framework (target identification → target separation → retraining approximation) emerges organically from the representation-gravity analysis (Theorem 3.2, Figure 3), implemented as a single unified objective (Eq. 3) rather than an ad-hoc pipeline. The t-SNE visualizations in Figure 3 compellingly demonstrate how forgetting dynamics propagate through representation space.
- **Informative ablation studies**: Figure 7 demonstrates that annealed (linearly decreasing) gradient ascent outperforms constant/increasing schedules, that TARF generalizes across architectures (VGG-16bn, ResNet-18, WideResNet-50), and that gradient cleaning on identified false-retaining data preserves RA better than gradient ascent.

## Weaknesses

### Fatal
None.

### Major
- **LLM results are unconvincing and insufficiently analyzed**: Table 5 presents results on TOFU/LLaMA where TARF(GA) and TARF(NPO) produce identical values across multiple rows (e.g., both report QA Prob on F. = 0.0762 and QA Prob on R. = 0.0824 for all-matched). Identical values across different optimization variants are implausible and suggest either a reporting error or a collapsed retaining mechanism. Moreover, TARF substantially underperforms the CL(NPO) baseline on retaining (QA Prob on R. of 0.0824 vs. 0.4218 in all-matched). These results do not support TARF's effectiveness beyond image classification. Either deeper analysis is needed or the results should be removed.

### Minor
- **The "known number of target classes" assumption is acknowledged but not characterized**: For target mismatch, the paper states (line 61) that "the number of classes in D_un belonging to the target concept is known." This assumption is critical to Phase I target identification, yet sensitivity to misspecification is not examined. An ablation varying the assumed number would transform this from an unexamined limitation into a characterized one.
- **Theorem 3.2 is mathematically thin**: The theorem derives a first-order Taylor bound essentially showing that gradient ascent on one data subset affects another proportionally to their representation distance. While the "representation gravity" concept that follows is useful for motivating the algorithm, the theorem itself does not provide deeper mechanistic insight beyond this basic proportionality. The framing should be more modest.
- **Unexplained Gap value for Retrained reference in Table 2**: The CIFAR-100 Retrained row shows Gap=3.42, which is impossible if Gap means deviation from Retrained (as in Table 3). The Gap metric in Table 2 is not defined, and FT for CIFAR-100 has no Gap value. These presentation issues weaken confidence in the fine-grained evaluation.
- **Gap metric equally weights UA, RA, TA, and MIA** without discussing whether uniform weighting is appropriate when these metrics have very different dynamic ranges across scenarios (e.g., in model mismatch, Retrained UA is ~88% while RA is ~99%).

### Trivial
- Section 3.1 describes empirical observations qualitatively without reporting precise values in the text, forcing readers to estimate from bar charts.

## Nice-to-Haves
- An ablation running TARF without Phase I target identification (τ=1 for all remaining data from the start) would isolate whether the target identification step matters or whether the annealed GA+GD recipe alone explains the gains.
- The connection between the practical unlearning motivations invoked in the introduction (privacy, fairness, copyright) and the specific label-hierarchy scenarios studied merits more explicit bridging.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **REMOVED: Data inconsistency between Tables 2 and 3**: The Harsh Critic claimed Table 3's UA (86.67) and Table 2's UA-F (74.70/81.28) should agree. This is incorrect — Table 3 UA is superclass-level accuracy (the model output label domain in model mismatch), while Table 2 UA-F is a fine-grained class-level evaluation within the superclass. They measure different quantities by design, as the paper explicitly labels Table 2 as "fine-grained evaluation on superclass."
- **REMOVED: "FT shows no Gap value at all" across Table 2**: The CIFAR-10 FT row has Gap=5.53. Only the CIFAR-100 FT row has "-" for Gap. This is a single-cell issue, not a systematic problem.
- **REMOVED: Overstated real-world motivation**: The critic asserted the introduction overstates motivation. The introduction explicitly discusses how practical unlearning requests may not align with pre-training taxonomy, with Figure 1 grounding this in concrete examples. The connection is adequately argued.
- **REMOVED: Missing "no identification" ablation as a major weakness**: This is a useful ablation to request but does not rise to the level of a major weakness. Moved to nice-to-haves.
- **REMOVED: Generic concern about hyperparameter settings deferred to appendix**: The paper provides guidance through ablation studies (Figure 7) and references Appendix E for detailed recipes. Deferring hyperparameter details to appendix is standard practice.

## Novel Insights
None beyond the paper's own contributions. The core insight — that label-domain mismatch creates fundamentally different unlearning challenges requiring both target identification (via representation gravity) and representation disentanglement — is the paper's own contribution.

## Suggestions
- Either remove the LLM results (Table 5) or provide a detailed analysis explaining the identical TARF(GA)/TARF(NPO) values and the contexts where TARF helps vs. hurts relative to CL baselines.
- Add a sensitivity study for the known-class-count assumption in target mismatch, showing how Gap degrades as the assumed number of target classes is varied.
- Define the Gap metric used in Table 2 explicitly, fix the Retrained Gap value, and provide Gap values for all rows.
- Consider reporting standard deviations in main-table summaries rather than only in the appendix.

## Calibration Anchors
| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| UGradSL | hwXUmwJAq5.md | 3.00 | R1 | Weaker — simple label-smoothing method, limited novelty |
| Pseudo-Probability Unlearning | Xagys9QD3T.md | 3.00 | R1 | Weaker — narrow contribution |
| MASIMU | BJfIDS5LsS.md | 2.50 | R1 | Weaker — multi-agent approach, low scores |
| Deep Unlearning | pUOesbrlw4.md | 5.25 | R1/R2 | Weaker — SVD-based method, less comprehensive evaluation |
| Unlearning via Sparse Reps | TLBPjECC5D.md | 5.25 | R2 | Weaker — narrower contribution |
| **Same paper (TARF)** | OHOmpkGiYK.md | 5.75 | R1/R2 | Direct match — scores [6,6,3,8], the 3 biased by appendix length |
| SLUG | 3p4raemLAH.md | 5.75 | R2 | Similar quality — clever idea but limited evaluation |
| Oblivious Unlearning | wAemQcyWqq.md | 5.67 | R2 | Similar quality — novel privacy angle |
| **Label-Agnostic Forgetting** | SIZWiya7FE.md | 6.00 | R1/R2 | **Closest comparator** — novel problem, solid experiments, fixable weaknesses |
| Utility & Complexity | HVFMooKrHX.md | 6.60 | R2 | Stronger — theoretical paper with formal guarantees |

**Round 1 bracket**: 5.5–7.0. **Round 2 narrowing**: This paper is most comparable to Label-Agnostic Forgetting (6.00, Accept) — both introduce novel problem formulations with solid core experiments and have fixable weaknesses. The LLM results are the main drag but presented as case studies. The image classification results are comprehensive with dramatic margins. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>