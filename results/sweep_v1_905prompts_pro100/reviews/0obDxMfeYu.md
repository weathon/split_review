Now I have sufficient information. Let me write the final consolidated review after carefully filtering the harsh critic's points against the paper.

---

## Summary

Medix introduces a two-stage framework for OOD detection that leverages unlabeled "in-the-wild" data. The first stage filters candidate outliers from a mixed wild dataset using the element-wise median (EWM) of per-sample gradients — a greedy leave-one-out procedure that removes samples whose exclusion most reduces the distance between the EWM and the InD mean gradient. The second stage trains a binary OOD detector on the extracted outliers plus labeled InD data. Theoretical bounds on inlier and outlier misclassification rates are provided, and the method is benchmarked against 20 baselines on CIFAR-10 and CIFAR-100 paired with five OOD datasets, where it achieves state-of-the-art results.

## Strengths

- **Novel median-based filtering mechanism for wild-data OOD detection.** Using the element-wise median of gradients as a robust central-tendency estimate for separating InD from OOD in unlabeled mixtures is a genuine and well-motivated contribution. The monotonic relationship between OOD contamination and EWM deviation (Figure 1) provides clear empirical motivation, and Algorithm 1 gives a concrete, implementable procedure.

- **Strong and comprehensive empirical results.** On CIFAR-10, Medix achieves 0.80% average FPR95 vs. 3.40% for WOODS; on CIFAR-100, 5.42% vs. 6.74%. The evaluation spans 20 baselines across both InD-only and InD+wild-data categories, with error bars over five runs. The 2D synthetic experiment (Figure 2) provides a controlled validation of the filtering stage, showing a 12.5% extraction error rate.

- **Theoretical analysis provides qualitative understanding of why median filtering should work.** The bounds in Theorems 4.1 and 4.2 decompose error into contamination, concentration, and separation effects, establishing that median-based filtering remains robust when OOD contamination is below 50%. Remark 4.3 notes a relaxed version under second-moment assumptions, and Figure 4 provides empirical support for the sub-Gaussian gradient assumption on InD data.

## Weaknesses

### Major

- **Theory-algorithm gap: the theorems analyze a static filtering rule, not the implemented iterative algorithm.** Theorems 4.1 and 4.2 bound misclassification rates for an "EWM filtering rule" — a one-shot threshold-based decision rule that is never explicitly defined in the main text. By contrast, Algorithm 1 is an iterative, greedy, leave-one-out procedure that removes top-\(k\) samples per round based on the drop in EWM distance. The theoretical guarantees do not directly apply to the algorithm that is actually used, and no bridge between the two is established. This undermines the paper's claim that the theory provides guarantees for Medix's filtering stage. The theory still offers useful intuition, but the paper overstates the connection.

- **The "EWM filtering rule" is undefined in the main text.** Theorem 4.1 refers to the "inlier misclassification rate of the EWM filtering rule" without specifying what this rule is. Key quantities such as \(m_{\min}\) in the \(\epsilon\) definition are also not defined in the visible portion of the paper. These definitions likely reside in Appendix C (stripped), but a theorem statement in the main text must be self-contained enough to be interpreted. This makes the theoretical contribution harder to assess on its own terms.

### Minor

- **Pseudo-label dependence is not analyzed in the main text.** The gradients for wild samples are computed using predicted labels \(\hat{y}_{\tilde{x}_i}\) from the InD classifier. For OOD samples, these predictions are arbitrary, and for misclassified InD samples, the gradient signal is noisy. The paper states that Appendix A.5 addresses this, but the main text contains no discussion of how pseudo-label quality affects filtering. The 2D synthetic experiment (Figure 2) uses ground-truth labels, so it does not test this dependency.

- **Figure 1 shows monotonicity for only one InD-OOD pair (CIFAR-10 vs. SVHN).** The stopping criterion in Algorithm 1 is motivated by this monotonic behavior, but its generality across other dataset pairs and contamination ratios is not demonstrated in the main text. A broader validation would strengthen confidence in the algorithm's universality.

- **No complexity analysis or runtime reporting in the main text.** Algorithm 1's leave-one-out step requires recomputing the EWM for each sample in \(\mathcal{S}\) at each iteration. With gradient dimension \(p\) and wild set size \(m\), this is expensive. The paper defers efficiency analysis to Appendix A.6, but a brief complexity statement in the main text would aid assessment of practical scalability.

### Trivial

- The separation condition in Theorem 4.2 (\(\|\mu_{\text{out}} - \bar{\nabla}_{\text{in}}\|_2 \geq \Delta\sqrt{d}\)) is stated as an assumption without empirical verification in the main text, though the overall empirical results suggest it plausibly holds.

- The bound in Theorem 4.2 can exceed 1 for extreme parameter regimes (e.g., \(\pi \to 0\)), rendering it vacuous in those cases — but this is common in theoretical bounds and does not invalidate the contribution.

## Nice-to-Haves

- A direct ablation comparing the iterative Algorithm 1 against the static one-shot filtering rule analyzed in the theory would help bridge the theory-algorithm gap, or at least characterize when the gap matters.
- Extending the Figure 1 analysis to additional InD-OOD pairs and contamination ratios would strengthen the universality claim.
- Comparing against a baseline that operates under identical data access constraints (e.g., the same wild mixture without a clean OOD split) would sharpen the fairness of the OE and Energy (w/OE) comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Theorem 4.1 bound contains \(1/m_{\text{in}}\) which is dimensionally inconsistent with a rate."** REMOVED. This criticism is incorrect. The term \(1/m_{\text{in}}\) is a valid bound on a misclassification rate: it represents the worst case where at most 1 out of \(m_{\text{in}}\) inliers is misclassified from this component of the bound. It is a dimensionless proportion for any \(m_{\text{in}} \geq 1\).

- **"Theorem 4.2 expression can easily exceed 1."** REMOVED as a fatal concern. Probabilistic upper bounds frequently exceed 1 in extreme parameter regimes (e.g., \(\pi \to 0\)), which simply means the bound becomes vacuous — not that it is incorrect. This is standard in theoretical ML.

- **"OE comparison is misleading because OE uses clean OOD data."** WEAKENED and moved to Nice-to-Haves. The paper explicitly acknowledges this difference in the introduction ("Unlike approaches such as Outlier Exposure... which rely on a clean, auxiliary unlabeled dataset... Medix achieves superior results without such assumptions"). The tables clearly separate methods into "Using \(P_{\text{in}}\) only" and "Using \(P_{\text{in}}\) and \(P_{\text{out}}\)," and the paper is transparent about the informational asymmetry.

- **"Appendix experiments are deferred so the empirical case cannot be fully evaluated."** REMOVED. The appendix is stripped by the parser; this is a presentation artifact, not an author error. The main paper contains Tables 1 and 2 with full results.

- **"Theoretical assumptions not verified for OOD gradients."** DEMOTED to Trivial. The sub-Gaussian assumption is checked for InD gradients; checking it for OOD would be nice but is not a core flaw, especially given the strong empirical performance.

- **"The paper does not discuss failure modes for near-OOD."** REMOVED. This is speculative scope creep — the paper addresses the wild-data setting as defined, and near-OOD is a different problem setting.

- **"Missing related works."** REMOVED per hard rule (do not mention missing related works).

- **"Appendix A.1, A.2, A.4, A.5, A.6, A.7 claims cannot be verified."** REMOVED. The appendix is stripped by the parser; this is not an author error.

- **Strength Finder: "The paper addressed an important problem."** REMOVED. This is generic and not a specific, evidence-backed strength.

- **Strength Finder: "Strong ablation on hyperparameter sensitivity (Appendix A.2)."** REMOVED. The appendix is stripped; we cannot verify this claim. If it were in the main text, it would be a strength.

## Novel Insights

The key insight from the median perspective is genuinely interesting: the element-wise median of gradients serves as a naturally robust reference point for filtering in unlabeled mixtures, exploiting the fact that the median is resistant to contamination up to 50%. This contrasts with the top-singular-vector approach of SAL (Du et al., 2024a), which captures a different geometric property of the gradient set. The paper convincingly demonstrates that this robustness translates to strong empirical filtering performance, though the theoretical bridge between the static median analysis and the iterative algorithm remains incomplete.

## Suggestions

- Define the "EWM filtering rule" explicitly in Section 4 before stating Theorem 4.1, even if only in a concise paragraph. Clarify what \(m_{\min}\) refers to and how the decision threshold relates to \(\epsilon\).
- Either (a) extend the theory to analyze the iterative leave-one-out procedure (or a simplified version of it), or (b) explicitly acknowledge the gap and frame the theory as providing intuition rather than direct guarantees for Algorithm 1. The current framing overstates the connection.
- Add a sentence or two in the main text summarizing the key findings from Appendix A.5 (pseudo-label robustness) and A.6 (computational efficiency), so readers can assess these important practical concerns without the appendix.

## Score and Decision

**Originality:** The median-based filtering approach is a novel contribution to the wild-data OOD detection literature, offering a genuinely different mechanism from prior work (SAL's singular vectors, WOODS's constrained optimization). The perspective is well-motivated.

**Importance:** The problem — leveraging unlabeled wild data for OOD detection — is practically significant for real-world deployment. The method's strong empirical results suggest real utility.

**Claim support:** The empirical claims are well-supported by comprehensive benchmarks. The theoretical claims are partially supported — the bounds are structurally sound and provide useful intuition, but the gap between the analyzed static rule and the implemented iterative algorithm means the theory does not directly guarantee the algorithm's performance as claimed.

**Soundness:** The experimental methodology follows established protocols from WOODS and SAL, enabling fair comparison. The greedy approximation to the combinatorial optimization in Equation 4 is reasonable. The main soundness concern is the theory-algorithm gap.

**Clarity:** The paper is generally well-written. The main clarity issue is the undefined "EWM filtering rule" and missing definitions for key theoretical quantities.

**Value to the community:** Medix advances the state of the art on a well-defined benchmark suite and introduces a new filtering mechanism that could inspire further work. The median perspective may generalize beyond the specific OOD detection setting.

**Comparison to anchors:** Medix is most comparable to SAL (avg 6.50, Accept) — same framework, similar strengths, different filtering mechanism. Medix has stronger empirical results but a clearer theory-algorithm gap. It is clearly stronger than SPADE (5.50) and GradNorm (5.50), and clearly weaker than the DNN Extrapolation paper (7.00). I place it at 6.0 — a solid contribution with a significant but addressable weakness in the theory-application connection.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>