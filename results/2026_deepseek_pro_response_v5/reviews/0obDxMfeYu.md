Now I have a clear picture. Let me finalize the review.

**Bracket and scoring summary:**

Round 1 anchors across all bands:
| Anchor | Avg Score | Decision | Comparison |
|---|---|---|---|
| "What can we learn from Harry Potter?" | 2.00 | Reject | Our paper is substantially stronger |
| "Soft Checksums" | 2.33 | Reject | Our paper is substantially stronger |
| "Pan for gold" | 2.20 | Reject | Our paper is substantially stronger |
| "Semantic or Covariate?" | 4.00 | Reject | Our paper has stronger empirical contribution |
| "SEE-OoD" | 4.25 | Reject | Our paper is stronger in both theory and empirics |
| "SODA" | 3.50 | Reject | Our paper is stronger |
| "MetaOOD" | 5.25 | Accept | Our paper is stronger empirically |
| "Pathologies of OOD Detection" | 4.75 | Reject | Different type (critical analysis) |
| "Gradient norm as proxy" | 5.50 | Reject | Our paper is stronger in novelty and empirics |
| "Double Descent Meets OOD" | 6.50 | Reject | Comparable theory depth; our method more practical |
| "ImageNet-OOD" | 6.50 | Accept | Different type (benchmark/analysis) |
| "Extrapolate Predictably" | 7.00 | Accept | Our paper is weaker — cleaner contribution, tighter theory |
| "Deep Orthogonal Hypersphere" | 8.00 | Accept | Our paper is clearly weaker |
| "DRO with Bias and Variance Reduction" | 8.00 | Accept | Our paper is clearly weaker |

Round 2 narrowed anchors:
| Anchor | Avg Score | Decision | Comparison |
|---|---|---|---|
| "GRIC" | 5.75 | Reject | Our novelty and empirical breadth are stronger |
| "GROD" | 5.00 | Reject | Our paper is clearly stronger |
| "SPADE" | 5.50 | Accept | Our empirical results are stronger; both have theory-practice connections needing work |
| "Can We Ignore Labels in OOD?" | 6.33 | Accept | Different type (theoretical analysis of unlabeled OOD) |

**Bracket:** Round 1 placed the paper between 5.0 and 7.0. Round 2 narrowed this to ~5.5-6.5.

Our paper is: stronger than SPADE (5.50, Accept) and GRIC (5.75, Reject), comparable to or slightly below Double Descent OOD (6.50, Reject), clearly weaker than Extrapolate Predictably (7.00, Accept).

**Final score: 6.0**, reflecting genuine novelty and strong empirical results, tempered by the theory-algorithm gap and hyperparameter ambiguity. Decision: Accept (borderline).

---

## Summary
This paper proposes Medix, a median-centric framework for out-of-distribution (OOD) detection that uses the element-wise median (EWM) of gradient vectors from unlabeled wild data to robustly identify and filter OOD samples. The core idea is well-motivated: the median is robust to contamination, and Figure 1 demonstrates that the L2 distance between the EWM of wild-data gradients and the average InD gradient grows monotonically with OOD contamination. The paper provides theoretical bounds on inlier and outlier misclassification rates (Theorems 4.1, 4.2) and demonstrates strong empirical performance, with Medix achieving 0.80% average FPR95 on CIFAR-10 (vs. 3.40% for WOODS) and 5.42% on CIFAR-100 (vs. 6.74% for WOODS), outperforming all 14 baselines shown in the main tables.

## Strengths
- **Novel median-centric perspective on OOD detection with wild data**: Using the element-wise median of gradients to robustly estimate the central tendency of InD data in a contaminated mixture is a genuinely novel and well-motivated approach. The optimization formulation in Equation 4 provides a clean formalization of the filtering objective, and Figure 1 gives compelling empirical motivation showing monotonic increase in EWM-InD distance as OOD samples are added.
- **Strong empirical results across comprehensive benchmarks**: On CIFAR-10 (Table 1), Medix achieves 0.80% average FPR95, substantially outperforming WOODS (3.40%), OE (6.16%), and KNN+ (10.30%). On CIFAR-100 (Table 2), Medix achieves 5.42% average FPR95 vs. 6.74% for WOODS and 14.26% for OE. The method outperforms all 14 baselines across all five OOD test sets (SVHN, PLACES365, LSUN-C, LSUN-RESIZE, TEXTURES) on both InD datasets.
- **Theoretical analysis with interpretable error decomposition**: Theorems 4.1 and 4.2 provide bounds that decompose misclassification rates into contamination, concentration, and separation effects — giving meaningful insight into when and why median-based filtering works. Remark 4.3 provides empirical support for the sub-Gaussian assumption via histogram and Q-Q plots, and a relaxed version without sub-Gaussianity is claimed in Appendix C.3.

## Weaknesses

### Fatal
None.

### Major
- **Theory-algorithm gap**: Theorems 4.1 and 4.2 analyze an "EWM filtering rule" that is never formally defined in the main text and appears to describe a one-shot thresholding procedure. Algorithm 1, however, implements a greedy iterative removal process: at each iteration, remove the top-k samples whose individual removal produces the largest drop in ‖EWM(G_S) − ∇̄_in‖, recompute the EWM on the reduced set, and repeat. These are fundamentally different procedures, and the paper does not establish any formal connection between the analyzed rule and the implemented algorithm. The claim that the theorems "provide rigorous theoretical assurance that Medix minimizes both types of errors" (line 158) is therefore overstated. The theory provides meaningful intuition for why median-based filtering is robust, but does not directly validate Algorithm 1's iterative greedy procedure.
- **Hyperparameter selection ambiguity regarding test OOD data**: Section 5.2 states that hyperparameters ε and k are selected "with the objective of maximizing OOD performance." This phrasing could imply tuning against OOD test performance, which would invalidate the reported results. If parameters were instead selected via a validation split or data-driven heuristics, this must be explicitly stated. The ambiguity is serious because OOD detection methods must not use test OOD information during any selection step.

### Minor
- **Algorithm specification ambiguity**: The prose description (line 95-96) says the algorithm stops when there is "no significant drop in δ_i or a maximum number of iterations is reached" and that "the convergence criterion is based on the change in the L2 distance between two iterations." The pseudocode (Algorithm 1, line 110) uses `while t ≤ T or |δ_max| > ε do` and computes δ_max as max_i∈S δ_i (per-sample drops), not the change in d_t between consecutive iterations. These inconsistencies — between prose and pseudocode, and within the prose itself — make the algorithm's exact behavior ambiguous and complicate reproducibility.
- **CONJ and DRL baselines absent from main results**: Section 5.1 lists CONJ and DRL as baselines, and the conclusion (line 262) claims Medix "outperformed state-of-the-art methods such as WOODS and DRL." Neither appears in Table 1 or Table 2. The claim of "20 competitive baselines" in contribution C3 is misleading when the main tables show only 14 methods. If these comparisons are in the appendix, the main text should note this explicitly rather than implying they are part of the main evaluation.
- **InD accuracy gap vs. WOODS not discussed**: Medix achieves 93.58% InD accuracy vs. WOODS's 94.74% on CIFAR-10 (a 1.16% drop). The paper attributes accuracy differences to using 25k vs. 50k labeled samples (line 182-183), but this explanation applies only to InD-only baselines, not to WOODS which uses the same protocol. This accuracy trade-off for improved OOD detection deserves explicit discussion.
- **Matched wild/test distribution in main results**: The main experiments (Tables 1-2) construct wild data using the same OOD dataset used for testing (e.g., PLACES365 in both wild and test). The unmatched setting (P_out^test ≠ P_out) is only in Appendix A.4. While all wild-data methods have access to the same wild data, this matched setting is more favorable than the open-world scenario the paper motivates. The unmatched results should be foregrounded to strengthen the real-world applicability claim.

### Trivial
- The abstract and introduction prominently feature the 40.98% improvement over KNN+, but KNN+ uses only InD data (no wild data). The more relevant comparison is to WOODS (1.32-2.60% improvement in average FPR95), which should be foregrounded as the fairer reference point for the wild-data setting.

## Nice-to-Haves
- The synthetic experiment (Figure 2) uses OOD data at [20, 2√3] while InD clusters are within ~3 units of the origin, making distributions trivially separable. A more challenging synthetic setup would better demonstrate the method's filtering capability at the margin.
- A brief discussion of Algorithm 1's computational cost in the main paper (not only the appendix) would help readers assess practicality, given that the algorithm requires recomputing the EWM O(|S|) times per iteration.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Structural disconnect between theory and algorithm" as fatal**: Demoted to Major. While the gap between the analyzed one-shot rule and the iterative algorithm is real, this is a common pattern in ML papers (theory for idealized setting, practical algorithm as approximation). The theory still provides meaningful justification for the median-based approach; it just doesn't directly prove Algorithm 1's convergence or optimality.
- **"Algorithm's stopping criterion contradicts prose" as structural/fatal**: Demoted to Minor. The ambiguity between prose and pseudocode is real, but the core algorithmic idea is clear and the issue is a specification/documentation problem, not a fatal logical error.
- **"Experimental setup gives Medix an informational advantage over baselines"**: Demoted to Minor. All wild-data methods (WOODS, OE, Energy w/OE) have access to the same wild data with the same OOD distribution. The concern is valid as a presentation issue (matched setting should not be the only headline result) but does not indicate an unfair comparison between methods.
- **Demand for batch-level vs. dataset-level mixing experiment**: Removed. This is a claim in the related work section (line 258); demanding a dedicated experiment to validate it is outside the paper's core scope.
- **Question about whether standard deviations are over independent retrainings**: Removed. This is a curiosity about experimental methodology, not a substantive weakness.
- **"The bound contains 1/m_in which is not informative when m_in is small"**: Removed. This is a generic property of finite-sample bounds, not a specific flaw in this paper's analysis.
- **"The separation condition requires OOD mean to be far from InD mean in every coordinate"**: Removed as factually incorrect. The condition ‖μ_out − ∇̄_in‖₂ ≥ Δ√d is an L2-norm condition, not a per-coordinate condition — the reviewer misread this. The condition is standard for this type of analysis.
- **Missing near-OOD evaluation**: Removed. This was imported from a different paper's review (the Harry Potter paper discussed atypical videos) and has no bearing on this paper.
- **Weak adversarial attacks**: Removed. This paper does not evaluate adversarial robustness; the criticism was imported from an unrelated review.

## Novel Insights
None beyond the paper's own contributions. The median-based perspective on gradient statistics for OOD filtering is the paper's novel contribution, and the reviewers did not surface insights that extend beyond what the paper itself presents.

## Suggestions
- Clarify the connection between the theoretical "EWM filtering rule" and Algorithm 1. Either prove that the iterative greedy process approximates the analyzed rule under certain conditions, or explicitly frame the theory as analyzing the underlying principle (median robustness) rather than the specific algorithm.
- Resolve the prose/pseudocode inconsistency in Algorithm 1's stopping criterion. Align the prose with the pseudocode or vice versa, and clarify whether the stopping condition checks per-sample δ_i or the change in d_t between iterations.
- Clarify the hyperparameter selection procedure explicitly. If ε and k are selected via a validation split rather than test OOD data, state this clearly. If they are selected based on dataset size heuristics, describe the heuristic.
- Move CONJ and DRL results into the main tables, or explicitly state they are in the appendix and adjust the "20 baselines" count in contribution C3 to reflect what appears in the main evaluation.
- Consider foregrounding the unmatched-setting results (P_out^test ≠ P_out) in the main paper to strengthen the open-world detection claim, and mention the matched nature of the main experiments as a limitation.
- Explicitly discuss the InD accuracy gap relative to WOODS and whether it reflects a fundamental trade-off or an implementation artifact.

## Score and Decision

**Round 1 bracket:** 5.0–7.0, based on comparison against anchors across all five score bands. The paper is clearly stronger than weak-reject papers (2.0–4.5 range), sits above borderline-accept methods like SPADE (5.50), and is clearly below strong-accept papers like Extrapolate Predictably (7.00) and Deep Orthogonal Hypersphere (8.00).

**Round 2 narrowing:** Within the 5.5–6.5 sub-range. The paper is stronger than GRIC (5.75, Reject) in both novelty and empirical breadth, comparable to Double Descent Meets OOD (6.50, Reject) in having genuine theoretical content with some connection issues, and clearly weaker than Extrapolate Predictably (7.00, Accept) which has a tighter, cleaner contribution. The theory-algorithm gap and hyperparameter ambiguity prevent a score above 6.5; the genuine novelty and strong empirical results prevent a score below 5.5.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>