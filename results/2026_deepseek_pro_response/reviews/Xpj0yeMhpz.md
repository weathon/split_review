Now I have a thorough comparison set. Let me synthesize.

**Round 1 bracket**: The paper sits clearly above Deep Unlearning (5.25) and Forget Vectors (4.80), and the same paper in the calibration set got 5.75. It's in the **5.5–7.0** range.

**Round 2 comparison**:
- **LAF / Label-Agnostic Forgetting (6.00, Accept)**: Strong method paper with novel problem angle (no-label unlearning), good empirical validation. Our paper has a richer conceptual contribution (taxonomy of 4 settings vs. one problem) and more comprehensive experiments (ImageNet-1k, CIFAR, multiple architectures, generative models).
- **Utility & Complexity of Unlearning (6.60, Accept)**: Rigorous theoretical paper with formal guarantees and tight trade-off bounds, but limited to synthetic experiments. Our paper has much stronger empirical validation but weaker theory (motivational, not foundational).
- **Same paper (5.75, Reject)**: The human reviewers [6,6,3,8] — the 3-rated reviewer penalized presentation/appendix length heavily and explicitly declined to read the appendix.

Our paper is comparable to LAF (6.00) in overall quality — both are strong method papers with novel problem angles and solid empirical validation. It's below the theoretical paper (6.60) due to weaker theory. I place it at **6.0**.

---

## Summary
This paper expands the scope of class-wise machine unlearning by decoupling the class label from the target concept. It formalizes three new mismatch scenarios (target mismatch, model mismatch, data mismatch) beyond conventional all-matched forgetting, diagnoses why existing methods fail through representation dynamics analysis, and proposes TARF, a three-phase framework using annealed gradient ascent for target identification, joint ascent-descent for target separation, and gradient descent for retraining approximation. The image classification results (CIFAR-10/100, ImageNet-1k) show TARF dramatically outperforming baselines in mismatch settings while remaining competitive in all-matched.

## Strengths
- **Novel and well-formalized problem scope**: The taxonomy of four forgetting scenarios (all-matched, target mismatch, model mismatch, data mismatch) based on label-domain relations (ℒ₁ = ℒ₂, ℒ₁ ≺ ℒ₂) is cleanly defined, and Figure 1 provides concrete instantiations using CIFAR-100's fine/coarse label structure. This formalization reveals genuinely underexplored failure modes of existing unlearning methods.
- **Strong empirical results in mismatch settings**: Table 3 shows TARF achieving dramatically lower Gap↓ than all baselines in target mismatch (CIFAR-100: 0.21 vs. GA's 8.86) and data mismatch (CIFAR-100: 1.17 vs. GA's 2.43), where other methods collapse. Table 4 extends this to ImageNet-1k (data mismatch Gap↓: TARF 4.17 vs. FT 4.24, L1-sparse 5.84). The fine-grained superclass evaluation in Table 2 further validates that TARF can separate the unlearning target within a superclass.
- **Intuitive algorithm grounded in empirical diagnosis**: The three-phase framework (Phase I: target identification via accuracy-drop ranking; Phase II: joint ascent-descent for disentanglement; Phase III: retraining approximation) follows naturally from the representation analysis in Figure 3 and is validated by the dynamics in Figure 5.
- **Thorough ablation study**: Figure 7 systematically probes the effect of k, annealing schedule (constant vs. linear decreasing vs. increasing), robustness across architectures (VGG, ResNet, WideResNet), and the choice of gradient operation on identified false retaining data, all providing useful practical guidance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Known-class-count assumption limits practical applicability in target mismatch**: Section 2 states "we assume that the number of classes in D_un belonging to the target concept is known in target mismatch forgetting." While the algorithm uses a percentile-based threshold (top-10%) rather than hard class count, and the paper acknowledges this assumption, the method's robustness to incorrect class-count estimates is not evaluated. A sensitivity analysis would strengthen the practical claims.
- **Theory-algorithm gap**: Theorem 3.2 provides an upper bound connecting representation distance to loss coupling under gradient ascent, which motivates the "representation gravity" concept. However, the theorem does not inform the algorithm's two key design choices — the annealing schedule k(t) and the hard-threshold selection τ. The algorithm is designed based on empirical observations (Figures 3, 5) rather than derived from the theory. The theoretical framing serves as post-hoc motivation rather than a foundation.
- **TOFU/LLM results are too weak to support cross-domain generality**: Table 5 shows QA probabilities near zero for both forgetting and retaining data across most TARF settings (e.g., target mismatch QA Prob on F=0.0095, on R=0.0094), indicating near-total model collapse. Several TARF (GA) and TARF (NPO) rows are identical to baseline GA, suggesting the framework adds little in this domain. The paper appropriately frames these as case studies, but they do not demonstrate transferability.
- **Phase transition criteria deferred to appendix**: The main text does not specify how t₀, t₁, or β are chosen in practice, referring readers to Appendix E. A brief summary of the selection criteria in the main text would improve self-containedness.

### Trivial
- The "representation gravity" naming is evocative but the theoretical bound (Theorem 3.2) is an inequality, not an equality linking distance to coupling. "Representation coupling" would more accurately reflect what is demonstrated.

## Nice-to-Haves
- A sensitivity analysis showing how TARF performance degrades with incorrect class-count estimates would substantially strengthen the practical applicability claims.
- Providing a retrained reference for the TOFU experiments would help contextualize whether the near-zero QA probabilities represent model collapse or a property of the benchmark.
- Summarizing the t₀/t₁/β selection criteria in the main text (a 2-3 sentence summary of Appendix E) would make the paper more self-contained.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **HC: "False retaining data are identified but not actively forgotten — they receive zero gradient. This is a design issue that the paper does not address. The ablation in Figure 7 only compares gradient ascent vs. gradient cleaning on the selected data but doesn't test the default behavior against active ascent."** → REMOVED. The paper explicitly ablates gradient ascent (−k) vs. cleaning (0) on identified false retaining data in Figure 7 (right panel) and finds cleaning preserves RA better. The critic's claim that this is "never ablated" is factually incorrect.
- **HC: "The introduction overclaims slightly — it frames the mismatch scenarios as arising from practical unlearning requests... but the actual experiments use coarse-to-fine label hierarchies on standard image classification benchmarks."** → REMOVED. CIFAR superclass hierarchies are a legitimate and well-established testbed for studying label-domain mismatch; the connection to practical scenarios is reasonable motivation, not overclaiming.
- **HC: "MIA metric is confusingly signed"** → REMOVED. The paper is internally consistent (MIA=100 means perfect privacy), and this is a presentation nitpick with no weight in evaluation.
- **HC: "Gap metric... obscures which dimension drives the gap"** → REMOVED. The paper reports all individual metrics (UA, RA, TA, MIA) alongside Gap, so readers can fully disaggregate.
- **SF: "Demonstration on generative and language-model domains" as a strong point for TOFU** → Weakened. The Stable Diffusion results (Figure 6) appear reasonable, but the TOFU results are too weak to count as a strength.

## Novel Insights
The most novel insight from this work is the identification that representation-level dynamics during gradient ascent (the "gravity effect") can serve as a practical signal for discovering unlabeled data belonging to a target concept. By observing accuracy drops of different classes during a brief annealed gradient ascent phase, TARF can identify false retaining data without requiring explicit target-concept labels. This transforms an under-entangled representation problem (where D_f ⊂ D_t) from a fundamental obstacle into an exploitable signal.

## Suggestions
- Add a sensitivity analysis evaluating TARF's Gap when the assumed number of target-concept classes is overestimated or underestimated, to quantify robustness to this assumption.
- Either strengthen the TOFU experiments with a retrained reference and analysis of why collapse occurs, or remove them from the main text and keep only the Stable Diffusion case study.
- Summarize the t₀/t₁/β selection criteria in the main text (a 2-3 sentence summary of Appendix E guidance) to make the paper self-contained.
- Consider toning down the "representation gravity" metaphor to "representation coupling" to better match the inequality-based nature of Theorem 3.2.

## Calibration Report

All anchors retrieved across rounds:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| OHOmpkGiYK (Same paper — Decoupling Class Label) | 5.75 | R1/R2 | Same paper; human reviewers gave [6,6,3,8]. The 3-rated reviewer penalized presentation and explicitly declined reading appendix. |
| pUOesbrlw4 (Deep Unlearning) | 5.25 | R1 | Our paper has stronger problem formulation, more comprehensive experiments, and better evaluation. |
| 7tpMhoPXrL (Forget Vectors) | 4.80 | R1 | Our paper has much more comprehensive experiments, clearer problem formulation, and ImageNet-1k validation. |
| HVFMooKrHX (Utility & Complexity of Unlearning) | 6.60 | R2 | Stronger theory (rigorous guarantees), weaker experiments (synthetic only). Our paper is stronger empirically but weaker theoretically. |
| SIZWiya7FE (Label-Agnostic Forgetting) | 6.00 | R2 | Comparable quality — both strong method papers with novel angles and solid empirical validation. Our paper has richer problem formulation. |
| nb3VjILNVs (Low Compute Unlearning) | 5.75 | R2 | Our paper has more comprehensive evaluation and more significant empirical gains. |
| KzSGJy1PIf (Selective Unlearning SURE) | 5.67 | R2 | Our paper has broader scope (4 settings vs. standard unlearning) and stronger empirical results. |

**Round 1 bracket**: 5.5–7.0.  
**Round 2 narrowing**: The paper sits between LAF (6.00) and the theoretical paper (6.60). It matches LAF in overall quality with a richer problem formulation but weaker theory than the 6.60 paper.  
**Final score**: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>