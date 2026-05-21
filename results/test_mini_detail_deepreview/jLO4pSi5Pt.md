Now I have all the information needed. Let me write the final consolidated review.

## Summary
This paper introduces L-TTA, the first method for test-time adaptation of vision-language models under long-tailed test distributions. The approach identifies two VLM-specific failure modes (text-induced tail erosion and modality-bias amplification) and addresses them with three co-designed components: Synergistic Prototypes (DPs+EPs) for enriching tail-class representations, Rebalancing Shortcuts for adaptive class re-balancing, and Balanced Entropy Minimization as a tailored objective that reduces the gradient gap between head and tail classes. Experiments across 15 datasets, three benchmarks (OOD, cross-domain, corruption), three imbalance ratios, and multiple backbones show consistent gains over 12 existing VLM TTA methods, particularly on the class-balanced macro-F1 metric.

## Strengths
- **First principled analysis of VLM-specific failure modes in long-tailed TTA.** Section 1 and Figure 1(b) explicitly characterize *Text-induced Tail Erosion* and *Modality-bias Amplification* — problems that arise from the cross-modal nature of VLMs and are absent from unimodal long-tailed learning. This analysis directly motivates the bi-modal design of the proposed method.
- **Exclusionary Prototypes (EPs) provide a novel mechanism for tail-class enrichment.** Unlike prior prototype caching methods (e.g., TDA) that update only the predicted class, Eq. (5) defines EPs that are updated for *all* classes using prediction-guided weights φ_c. The ablation in Table 6 confirms that removing EPs degrades macro-F1 by ~3.2% on ViT-B/16, demonstrating their distinct contribution.
- **Balanced Entropy Minimization (BEM) with a verified theoretical rationale.** Eq. (9) introduces a penalty term (1−P̃)^β that down-weights confident classes while steering uncertain/tail classes toward better optimization. Proposition 2 (stated in the main text) proves that BEM reduces the optimization gap between head and tail class gradients — the first entropy-minimization variant tailored for long-tailed TTA with a theoretical claim.
- **Comprehensive and well-structured benchmarking.** Tables 1–3 report results across OOD, cross-domain, and corruption benchmarks at imbalance ratios 10/20/50. On the OOD benchmark (Table 1, imb=10), L-TTA achieves 65.97% / 61.18% (Acc/Mac) vs. the best prior DPE at 64.50% / 57.57%. On the cross-domain benchmark (Table 2), the macro-F1 gap over DPE is 2.20 percentage points. The robustness study on head/tail shift (Table 7) and efficiency analysis (Table 4) are thoughtful additions.
- **Diagnostic ablation isolating each component.** Table 6 systematically ablates DPs, EPs, RSs, and BEM across two backbones. Figure 4 provides sensitivity analyses for λ₁, λ₂, η, K, and β, showing that the method's performance is well-behaved across a reasonable range of hyperparameter values.

## Weaknesses

### Fatal
None.

### Major
- **Missing adapted baselines.** The paper compares L-TTA against 12 existing VLM TTA methods using their default hyperparameters (designed for balanced test sets). This is appropriate for showing that off-the-shelf TTA methods degrade under long-tailed distributions. However, the paper does not include simple baselines that adapt existing methods to the long-tailed setting — e.g., combining TPT or TDA with logit adjustment using estimated class priors, or applying class-balanced reweighting to the entropy minimization objective. The claim that L-TTA is the *first* long-tailed TTA method for VLMs makes this gap significant: the paper should demonstrate that the problem cannot be trivially solved by plugging a standard long-tailed technique (e.g., logit adjustment) into an existing TTA method. The current experiment design does not rule out this simpler alternative, which weakens the evidentiary support for the claim that L-TTA's co-designed components are necessary.

### Minor
- **No variance estimates reported.** All main results (Tables 1–3, 5) report only mean values over 5 runs without standard deviations or confidence intervals. Some gains are modest (e.g., Table 1, imb=50 OOD Average: L-TTA 64.68 Acc. vs. DPE 63.71 — a 0.97% gain). Without variance estimates, the reader cannot assess whether these improvements are statistically meaningful. This is a common issue across many TTA papers, but given the modest gains in some settings, it would substantially strengthen the paper to include them.
- **Empirical analysis of Exclusionary Prototypes is thin.** The paper claims that EPs "capture more refined inter-class associations and enrich tail class representations" but provides no visualization or quantitative analysis of what EPs actually store, how they differ from DPs, or the similarity structure between EP and DP features. An analysis of prototype similarity matrices or a t-SNE visualization would strengthen this claim beyond the aggregate ablation in Table 6.
- **Noisy class prior estimates in early BEM optimization.** The class priors π in BEM (Eq. 9) are "continually updated based on the current predicted pseudo-labels." Early in the datastream, these pseudo-labels will be unreliable — particularly for tail classes that may not yet have been observed. The paper does not discuss how this affects BEM's behavior in the initial adaptation phase or whether it causes instability.

### Trivial
- Figure 4 captions inconsistently refer to the hyper-class vector count as both "K" (in the text) and "b" (in the caption of subfigure (c)).
- The "next part will summarize" sentence at the end of Section 3.2 (page 4, before the BEM subsection) is a dangling forward reference that briefly breaks the flow.

## Nice-to-Haves
- A comparison against long-tailed TTA methods for unimodal models (e.g., SAR, DELTA) adapted to VLMs would strengthen the claim that cross-modal issues are unique and require bi-modal solutions. The paper hints at this via Figure 1(b.2) but does not provide quantitative comparison.
- Ablating the threshold θ for DP updates (Eq. 4) and the number of augmented views Q (set to 15) would be informative, particularly for practitioners concerned with computational cost.
- Including per-class accuracy breakdowns for head vs. tail in the main text (currently deferred to appendix) would help readers diagnose exactly where the improvements come from.

## Removed Points
These points are flagged to be removed; treat them with caution:
1. *Theoretical propositions are central but unverifiable in the main text.* → The proofs of Propositions 1 and 2 are in Appendix A, which was removed by the parser. Per policy, criticisms about missing appendix content are not valid — the proofs exist in the original submission. The main text clearly states both propositions, which is sufficient for a conference paper.
2. *Criticisms about missing related works.* → Per policy, I cannot verify claims about missing references.
3. *Pure formatting/style nitpicks and typos.* → These are parser artifacts, not author errors.
4. *Strength Finder strengths that are generic or conflict with verified weaknesses.* → Several overly generic strengths were removed (e.g., "this paper addresses an important problem," generic praise without specific evidence).

## Novel Insights
None beyond the paper's own contributions. The two reviewers' perspectives largely converge: the harsh critic accurately identifies the comparison fairness gap and the missing variance estimates as the paper's main weaknesses, while the strength finder correctly highlights the principled failure-mode analysis and the synergistic prototype design. The main insight from synthesizing both reviews is that the paper's core claims are credible and well-supported by the breadth of evaluation, but the "first long-tailed TTA method" framing would be better defended with a few additional comparison points that rule out simpler alternatives.

## Suggestions
1. **Add 2–3 adapted baselines:** Combine TPT or TDA with (a) logit adjustment using estimated class priors, (b) class-balanced entropy reweighting, and (c) a version of BEM's penalty without the logit adjustment term. If L-TTA still outperforms these, the contribution is clearly due to the synergistic co-design. If not, reframe the claims accordingly.
2. **Report standard deviations** for all main tables. Five runs is sufficient; this is a quick addition that substantially improves the paper's evidentiary quality.
3. **Add a prototype similarity analysis** (e.g., cosine similarity matrices between DP and EP features, or t-SNE visualizations) to empirically substantiate the claim that EPs capture complementary inter-class associations benefiting tail classes.
4. **Discuss early-stage prior noise** in BEM and consider a warm-up phase or prior smoothing to address it. Even a brief comment acknowledging the limitation would improve the paper's thoroughness.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| DOTA (Distributional TTA) | 6.00 (R) | Bracketing, Narrowing | Weaker than L-TTA — DOTA had conceptual issues about estimation with batch size 1 and a weak human-in-the-loop component. L-TTA has a cleaner method and more thorough evaluation. |
| ROSITA (Open-world TTA) | 4.67 (R) | Bracketing | Weaker than L-TTA — criticized as incremental with missing baselines. L-TTA has stronger novelty and broader evaluation. |
| BLG (Long-tailed CLIP) | 4.67 (R) | Bracketing | Weaker than L-TTA — limited innovation concerns, less thorough evaluation. L-TTA tackles a genuinely new problem. |
| RLCF (CLIP Reward TTA) | 6.67 (A) | Narrowing | Comparable to L-TTA — RLCF was accepted but its novelty was questioned as incremental by some reviewers, and it only evaluated on ImageNet. L-TTA has broader empirical support (15 datasets) and a more specific problem framing. |
| Multi-Label TTA with BEM | 6.25 (A) | Narrowing | Comparable — similar structure (new TTA variant with theoretical motivation), but L-TTA has more extensive evaluation. |
| Concept Drift for MLLMs | 7.00 (A) | Narrowing | Stronger scorer but had significant experimental design issues (new dataset confounds comparison) — L-TTA's experiments are cleaner and more controlled. |

**Round-1 bracket:** The paper clearly sits above the weak anchors (2.33–3.00) and below the very strong anchors (8.00), placing it in the 4–7 range. The comparison against DOTA (6.00) shows L-TTA is stronger, while the comparison against RLCF (6.67) shows similar quality. The concept drift paper at 7.00 had broader scope but significant clarity issues that L-TTA avoids.

**Round-2 narrowing:** Reading Multi-Label TTA (6.25), RLCF (6.67), and Concept Drift (7.00) in full confirms L-TTA sits between 6.25 and 7.00. L-TTA has better experimental control than the Concept Drift paper (which introduced a confounded dataset), broader evaluation than RLCF, and a cleaner method than both. However, the missing adapted baselines and variance estimates prevent it from reaching the 7.0 level. The most plausible score is **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>