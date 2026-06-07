Now I have a clear calibration picture. Let me finalize the review.

**Calibration summary:**
- **ljwoQ3cvQh** (7.00, Accept): DNNs extrapolate predictably — stronger, novel phenomenon with clean theory-empirics connection. Medix is below this.
- **jlEjB8MVGa / SAL** (6.50, Accept): The direct predecessor from Du et al. (2024a). Same two-stage framework. Cleaner theory (directly analyzes filtering criterion). Medix comparable but slightly weaker on theory-algorithm connection.
- **eN0RyRVbSm** (6.50, Reject): Double descent + OOD. Similar theory-algorithm gap severity. Medix is comparable in quality but different contribution type.
- **bcWwhF8cTZ** (5.50, Reject): Gradient norm for OOD error. Novelty concerns, missing baselines. Medix is clearly stronger.
- **GQhlM0Mavg** (5.00, Reject): OOD + conformal prediction. Limited novelty, applies existing methods. Medix is clearly stronger.

**Bracket:** 5.0–7.0 → narrowed to 5.5–6.5 based on round 2. Medix lands at **6.0** — below SAL (6.50) due to the more pronounced theory-algorithm gap and deferred key baselines, but above the gradient norm paper (5.50) due to genuine methodological novelty and consistent empirical gains.

---

## Summary
Medix proposes a two-stage OOD detection framework that leverages unlabeled "wild" data. Stage 1 filters candidate outliers from a mixed InD/OOD dataset using a greedy algorithm that iteratively removes samples whose exclusion most reduces the L2 distance between the element-wise median (EWM) of remaining gradients and the mean InD gradient. Stage 2 trains a binary OOD detector on identified outliers and labeled InD data. The paper provides theoretical bounds on misclassification rates and evaluates against ~15 baselines on CIFAR-10 and CIFAR-100, showing consistent improvement over prior methods including WOODS.

## Strengths
- **Consistent empirical outperformance across all test OOD datasets (Tables 1–2).** On CIFAR-10, Medix achieves 0.80% average FPR95 vs WOODS's 3.40% — a 2.60 percentage-point reduction. On CIFAR-100, 5.42% vs 6.74% (1.32 pp). The improvement holds uniformly across all five OOD test sets (SVHN, PLACES365, LSUN-C, LSUN-RESIZE, TEXTURES) on both InD datasets, with low variance across five runs, demonstrating genuine robustness rather than dataset-specific tuning.
- **Well-motivated by a controlled experiment (Figure 1).** The paper directly tests the core hypothesis — that the L2 distance between the InD mean gradient and the EWM of wild-data gradients increases monotonically as OOD samples are added — using CIFAR-10 as InD and SVHN as OOD. The resulting monotonic curve justifies both the optimization objective (Equation 4) and the stopping criterion of Algorithm 1, giving the method a principled foundation.
- **Practical relaxation of the batch-level mixing assumption.** Prior wild-data methods (WOODS, Du et al. 2024a) assume batch-level mixing with fixed InD/OOD ratios per batch. Medix operates under dataset-level random mixing, which is more realistic for outsourced wild data. The theoretical bounds explicitly accommodate arbitrary (but sub-50%) contamination ratios.
- **Synthetic validation (Figure 2) provides intuitive verification.** The 2D Gaussian experiment shows Medix successfully flags 87.5% of actual OOD samples as outliers on a controlled toy problem, corroborating the method's effectiveness independent of deep-network complexity.

## Weaknesses

### Fatal
None.

### Major
- **Theory-algorithm gap.** Theorems 4.1 and 4.2 bound the misclassification rates of "the EWM filtering rule," but this rule is never formally defined in the paper. Algorithm 1 implements a greedy iterative leave-one-out procedure, and the relationship between this algorithm and the rule analyzed in the theorems is neither stated nor argued. The theoretical contribution — highlighted as a main contribution (C2) — is presented as providing guarantees for Medix, but the connection is asserted rather than established. Separately, even accepting the theorems on their own terms, the bounds are uninformative at the experimental setting π = 0.5: the contamination terms alone give π/[2(1−π)] = 0.5 in Theorem 4.1 and (1−π)/(2π) = 0.5 in Theorem 4.2, meaning the bounds only guarantee error rates below ~50%, which is trivial and does not explain the empirical 12.5% error rate shown in Figure 2. The bounds would need to be evaluated at substantially smaller π to provide non-trivial guarantees.

### Minor
- **Key baselines absent from main tables.** DRL (Zhang et al., 2024) and CONJ (Peng et al., 2024) are described as competitive baselines in Section 5.1, and the conclusion claims Medix "outperformed state-of-the-art methods such as WOODS and DRL" (line 262), but neither appears in Tables 1 or 2. The claim of evaluating against "20 competitive baselines" cannot be verified from the main paper.
- **Computational cost not analyzed in the main body.** Algorithm 1 computes the EWM of gradients for |S| different subsets at each iteration, with each gradient of dimension d (penultimate-layer parameters). This yields ~O(d × |S|²) per iteration with |S| starting at 25,000+. The paper acknowledges the cost only by deferring analysis to Appendix A.6 (line 93), but readers cannot assess the practical cost-benefit trade-off from the main paper.
- **Only π = 0.5 tested experimentally.** All experiments use the default mixing proportion π = 0.5. Since the theoretical bounds degrade as π → 0.5, testing at other values (e.g., 0.3, 0.4, 0.45) would strengthen the empirical case and characterize the method's behavior under varying contamination levels.
- **Undefined notation in theorems.** The variables m_in, m_min, and m_out appear in Theorems 4.1 and 4.2 but are never defined in the main body, making the bounds impossible to interpret without consulting the appendix.
- **Baseline grouping conflates different problem settings.** OE and Energy(w/OE) are grouped under "Using P_in and P_out" alongside WOODS and Medix (Tables 1–2), but OE receives clean OOD data while WOODS and Medix use mixed wild data. These are different problem settings — separating them would actually strengthen the narrative, since Medix outperforms OE despite OE's informational advantage.

### Trivial
- **Pseudocode bug in Algorithm 1, line 2.** The loop condition uses "while t ≤ T or |δ_max| > ε" — it should use "and" instead of "or." With δ_max initialized to ∞, the loop could continue past T iterations if the convergence criterion is never met.
- **Notation inconsistency.** Algorithm 1 uses V̄_in while the surrounding text uses ∇̄_in.
- **"Median perspective" framing overstates conceptual novelty.** The method employs the element-wise median, a standard robust estimator. The core idea is sound and well-executed, but presenting it as a "new perspective" is an overstatement.

## Nice-to-Haves
- An ablation comparing EWM against the simple mean (not just geometric median, as in Appendix A.1) would clarify whether the median is necessary or any robust aggregator would suffice.
- The fact that Medix outperforms OE despite OE having access to clean OOD labels is a strong result that deserves more prominent highlighting rather than being obscured by shared table sections.
- Sensitivity analysis for the stopping criterion ε in the main body would help readers assess the method's robustness, since ε controls how many samples are flagged as OOD.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim: 40.98% FPR95 improvement over KNN+ is misleading.** REMOVED. The paper clearly separates methods into groups (using P_in only vs. using P_in and P_out), and comparing wild-data methods against non-wild-data methods is standard practice for establishing the value of wild data. The paper is transparent about the comparison categories.
- **Harsh Critic claim: sub-Gaussian assumption on gradient coordinates is too strong / unrealistic.** REMOVED as a standalone weakness. The paper acknowledges this limitation explicitly in Remark 4.3, provides empirical evidence (Figures 4a, 4b in appendix), and offers a relaxed version under bounded second moments (Theorem C.3). The paper is appropriately cautious about this assumption.
- **Strength Finder: "Two-sided theoretical guarantees" as an unqualified strength.** WEAKENED. The theory-algorithm gap (see Major weakness) means the theoretical contribution does not land cleanly. The bounds exist but their connection to Algorithm 1 is unclear, and they are weak at the experimental π = 0.5 setting.
- **Strength Finder: "Comprehensive baseline coverage (20 methods)."** WEAKENED. While the baseline list is genuinely broad, not all 20 appear in the main tables (DRL, CONJ are deferred to appendix), so the claim cannot be fully verified from the main paper.
- **Harsh Critic claim about missing mean-vs-EWM ablation in main body.** MOVED to Nice-to-Haves. The paper does compare EWM vs geometric median in Appendix A.1, and comparing against the mean would be informative but is not essential.

## Novel Insights
The paper's use of gradient-space median filtering for outlier detection in mixed unlabeled data is a natural application of robust statistics to the OOD detection setting. The key empirical insight — that the L2 distance between the InD mean gradient and the EWM of wild-data gradients increases monotonically with OOD contamination (Figure 1) — provides a clean empirical foundation that prior wild-data methods lacked. The median's breakdown point of 50% maps naturally to the Huber contamination model, and the paper exploits this connection to derive theoretical bounds. No genuinely novel insight beyond the paper's own contributions emerges from the reviews.

## Suggestions
- Define "the EWM filtering rule" formally in Section 4 and explicitly state its relationship to Algorithm 1. If the bounds do not directly apply to the greedy algorithm, reframe the theory as analyzing an idealized one-shot version of the method and discuss the gap honestly. This is essential for the theoretical contribution to land.
- Include DRL and CONJ results in the main tables, or at minimum report their average FPR95 in the text, so the evaluation can stand on its own.
- Move a short computational cost analysis (wall-clock time, GPU memory) from Appendix A.6 into the main body — even a brief paragraph or small table would help readers assess the method's practicality.
- Separate baseline groups into three categories in the tables: InD-only, InD + clean OOD, and InD + wild data. This would clarify the comparison landscape and actually strengthen the narrative.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>