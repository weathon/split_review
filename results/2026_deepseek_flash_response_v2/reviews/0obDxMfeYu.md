Now I have all the calibration data I need. Let me synthesize the final review.

## Summary

This paper introduces Medix, a two-stage framework for OOD detection that (1) extracts candidate OOD samples from unlabeled "in-the-wild" data using element-wise median (EWM) filtering on gradients, and (2) trains a binary OOD detector on the extracted outliers plus labeled InD data. The key novelty is using the median's robustness to contamination as a filtering mechanism, supported by theoretical bounds on misclassification rates and extensive evaluation against 20 baselines.

## Strengths

1. **State-of-the-art empirical results across a wide range of settings.** On CIFAR-100, Medix achieves avg FPR95 of 5.42% and AUROC of 98.96%, outperforming WOODS (6.74%, 97.73%) and all other baselines (Tables 1–2). On CIFAR-10, Medix averages 0.80% FPR95 vs. WOODS at 3.40%. Results are averaged over 5 runs with standard deviations, demonstrating consistent and meaningful superiority. The comparison covers 20 baselines including the strongest prior method (WOODS) and the direct predecessor SAL (Du et al. 2024a).

2. **Novel and well-motivated use of median-based gradient filtering.** The core idea — using the element-wise median of gradients as a robust estimate of central tendency that is naturally resistant to OOD contamination — is genuinely novel in the wild-data OOD setting. The motivating experiment (Figure 1) showing monotonic increase in EWM deviation as OOD samples accumulate provides intuitive grounding for the approach.

3. **Theoretical framework that provides formal scaffolding.** Theorems 4.1 and 4.2 offer upper bounds on inlier and outlier misclassification rates, decomposed into interpretable contamination, concentration, and separation effects. The fallback bound (Theorem C.3) that removes the sub-Gaussian assumption shows the core guarantee extends beyond ideal conditions.

4. **Dataset-level mixing without batch-level assumptions.** As noted in Section 6, prior methods (Katz-Samuels et al., 2022a; Du et al., 2024a) assume batch-level mixing where each batch has a fixed InD/OOD ratio. Medix operates under the more realistic dataset-level mixing scenario where data is mixed randomly across the entire dataset.

## Weaknesses

### Major

1. **Theory-practice gap between the theorems and the implemented algorithm.** Theorems 4.1 and 4.2 analyze the statistical properties of a *one-shot* EWM filtering rule applied to the wild dataset. However, Algorithm 1 is an *iterative, greedy* procedure that repeatedly computes leave-one-out EWM distances, selects top-k samples by drop in distance, and removes them. The paper states that the theorems "provide provable upper bounds on the misclassification rates for both InD and OOD points" for "Medix's filtering stage" (line 132), but never explicitly states whether the bounds apply to the one-shot rule, the greedy algorithm, or both. This disconnect means a reader cannot determine whether the formal guarantees hold for the procedure that was actually evaluated. The gap is acknowledged only implicitly via the optimization-to-greedy approximation (line 93) but the theorems are presented as if they directly justify Algorithm 1's performance.

2. **Theoretical bounds are very loose at the experimental contamination ratio (π = 0.5).** The inlier misclassification bound (Theorem 4.1) contains a contamination term π / [2(1-π)] = 0.5 / 1.0 = **0.5** at π = 0.5. This means the bound guarantees at most ~50% of InD samples could be misclassified as outliers — plus decaying concentration terms. While the bound is technically correct and demonstrates the method does not catastrophically fail, it does not explain or guarantee the strong empirical performance (which achieves ~87.5% correct OOD extraction in the synthetic experiment). The paper's framing that "Medix achieves a low error rate" (abstract) and that the bounds demonstrate "robustness even under significant OOD contamination" is partially misleading, as the bound is vacuous at the tested contamination level. The actual low error rates are an empirical finding, not one explained by the theory.

3. **The 40.98% improvement claim is ambiguous.** The abstract and introduction state that Medix outperforms KNN+ "by an average of 40.98% in terms of FPR95." From Table 2: KNN+ FPR95 = 46.40%, Medix = 5.42%, an absolute difference of 40.98 percentage points. The relative improvement is ~88%. Readers will naturally interpret "40.98%" as a relative improvement, which would be misleading. This should be disambiguated (e.g., "40.98 percentage points" or state the relative improvement).

### Minor

4. **Missing main-text discussion of computational cost.** Algorithm 1 computes leave-one-out EWM distances at every iteration — costing O(d·|S|²) per iteration for |S| samples and d-dimensional gradients. The paper acknowledges the original optimization (Equation 4) is "computationally prohibitive" (line 93) and proposes the greedy approximation for tractability, but never provides even a high-level complexity analysis or wall-clock time in the main text. Reference to Appendix A.6 is made but no summary is given. For a method whose practical deployability is important, this is a notable omission.

5. **No verification of the OOD gradient assumption under pseudo-labels.** The algorithm computes gradients for wild samples using *predicted* labels (ŷ in Equation 4). For OOD samples, this means computing gradients w.r.t. an incorrect (InD) label. Theorem 4.2 assumes OOD gradients are i.i.d. sub-Gaussian with a well-separated mean ||μ_out − ∇̄_in|| ≥ Δ√d. This assumption is nontrivial and unverified: gradients of OOD data under *predicted incorrect* pseudo-labels may not have a consistent directional mean or clean separation from InD gradients. Remark 4.3 validates the sub-Gaussian assumption only for InD gradients. While Appendix A.5 evaluates pseudo-label quality, the specific statistical assumption underlying Theorem 4.2 receives no empirical scrutiny in the main paper.

6. **π is fixed at 0.5 with no ablation.** The contamination proportion π is always 0.5 in experiments. Given that the theoretical contamination term grows with π and becomes large at π = 0.5, an ablation varying π (e.g., {0.1, 0.2, 0.3, 0.4, 0.5}) would directly test whether empirical degradation matches the theoretical prediction and would strengthen both the empirical and theoretical claims.

7. **CONJ and DRL baselines are mentioned but absent from main tables.** Section 5.1 lists CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024) as baselines but they do not appear in Tables 1–2. If they are in the appendix, the main text should note this explicitly.

### Trivial

8. The synthetic experiment (Figure 2) places OOD data at a Euclidean distance of ~20 from the nearest InD cluster — an extremely easy separation. The paper describes this correctly as "simple to facilitate better understanding," so it is not a weakness of the method, but the "12.5% error rate" from this setting should not be presented as strong evidence of robustness without additional, harder synthetic tests.

## Removed Points

- **"Figure 1 doesn't validate the leave-one-out scoring"**: The paper presents Figure 1 as motivation for why EWM distance changes with OOD contamination, not as validation of the specific scoring mechanism. Removed — criticism misreads the paper's intent.
- **"Computational cost is prohibitive / unreported"**: The paper defers this to Appendix A.6 (line 238). Kept a weakened version as Minor (#4 above) since the main text should summarize efficiency. The harsh critic's cost calculation is rough but directionally correct.
- **"The 12.5% error claim is not meaningful"**: Kept as Trivial (#8) since the paper acknowledges the experiment's simplicity. Not a significant weakness.
- **"No random-filtering baseline"**: This is a nice-to-have suggestion, not a weakness. Moved to Nice-to-Haves.
- **"The bounds involve unknown m_in, m_out"**: The bounds are stated in terms of population parameters (π, m_in, m_out). This is standard for statistical learning bounds; not a weakness per se.

## Nice-to-Haves

- **Ablation on contamination proportion π** (0.1 to 0.5) to test whether empirical performance degrades as theory predicts.
- **Random-filtering baseline** (replace Algorithm 1 with random subsampling to quantify the value of median-based selection).
- **Additional empirical characterization of OOD gradient distributions** under pseudo-labels (e.g., t-SNE visualization or separation statistics).
- **Wall-clock time** and iteration count for Algorithm 1 in the main text, not just the appendix.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from synthesizing the reviews is that the median-based approach to outlier filtering in unlabeled mixtures presents a clean conceptual alternative to prior SVD-based methods (Du et al. 2024a) — trading the linear-algebraic signal (top singular vector) for a robust-statistics signal (element-wise median). This substitution is theoretically appealing because the median's breakdown point is well-understood, but the reviews collectively reveal that the gap between this theoretical appeal and the actual iterative greedy implementation is wider than the paper acknowledges. The pseudo-label issue is a cross-cutting concern that neither the theory nor the current experiments fully resolve, and it represents a productive direction for future work.

## Suggestions

1. **Align the theory with the algorithm.** Either analyze the iterative greedy procedure, or simplify Algorithm 1 to a one-shot EWM rule that the theorems actually study, and clearly delineate which guarantees apply to which procedure.
2. **Be transparent about bound looseness at π = 0.5.** State explicitly that the bound guarantees the method does not lose more than ~50% of InD data (i.e., does not catastrophically fail), and that the strong observed performance is an empirical finding beyond what the theory currently explains.
3. **Add π ablation** to directly connect the theory's contamination term with empirical behavior.
4. **Disambiguate the 40.98% claim** — use "40.98 percentage points" or give the relative improvement.
5. **Report computational cost in the main text**, even briefly — e.g., wall-clock time per iteration, total runtime for the full pipeline.
6. **Add CONJ and DRL results to the main tables** or explicitly note their placement in the appendix.

## Score and Decision

**Anchoring summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SAL (Du et al. 2024a) | jlEjB8MVGa.md | 6.50 | 1,2 | Direct predecessor; similar two-stage framework with stronger theory-alignment but weaker empirical results than Medix. |
| SPADE (EVT) | kwCHcaeHrf.md | 5.50 | 2 | Theory-grounded OOD detection; weaker empirical results (often outperformed by baselines); accepted despite impractical assumptions. |
| Gradient Norm Proxy | bcWwhF8cTZ.md | 5.50 | 1 | Gradient-based OOD method; rejected despite similar score. |
| ProMix | voVjW1PT2c.md | 6.00 | 2 | Mixup-based OOD detection with theory; rejected (mixed reviews). |
| Can We Ignore Labels | falBlwUsIH.md | 6.33 | 1 | Unlabeled OOD theory paper; accepted. |
| ImageNet-OOD | VTYg5ykEGS.md | 6.50 | 2 | OOD benchmark paper; less directly relevant. |
| Semantic or Covariate | uWUovmBRUq.md | 4.00 | 1 | OOD detection analysis paper; rejected. |

**Round 1 bracket:** 4.5–6.5 (based on weak anchors ~2–3, SAL at 6.5, and strong anchors at 8).

**Round 2 narrowing:** compared against SAL (6.50, accepted), SPADE (5.50, accepted), ProMix (6.00, rejected), and Gradient Norm (5.50, rejected). Medix has stronger empirical results than SPADE and comparable empirical strength to SAL, but a more significant theory-practice gap than SAL. The paper's core methodological contribution (median-based filtering) is novel and empirically validated, placing it above SPADE (which had weak empiricals) and Gradient Norm (rejected). However, the theory-practice disconnect and overclaimed guarantees prevent it from reaching SAL's score.

**Final score: 5.5** — The paper makes a real empirical contribution (novel median-based filtering outperforming 20 baselines) with a clean motivating idea, but the theoretical analysis has a significant gap relative to the implemented algorithm, and several claims are over-stated relative to what is proven.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>