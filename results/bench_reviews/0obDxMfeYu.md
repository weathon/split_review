Now I have sufficient calibration information. Let me write the final consolidated review.

## Summary

This paper introduces Medix, a framework that uses a median-based, iterative greedy algorithm to filter OOD samples from unlabeled wild data (a mixture of InD and OOD), then trains an OOD detector on the identified outliers. Theoretically, it provides two-sided error bounds on inlier and outlier misclassification rates. Empirically, it evaluates against 20 baselines across 11 InD-OOD pairs on CIFAR-10 and CIFAR-100, reporting state-of-the-art FPR95 (0.80% on CIFAR-10, 5.42% on CIFAR-100).

## Strengths

- **Novel median-based filtering approach.** Using the element-wise median of gradients for OOD extraction from unlabeled wild data is a genuinely new idea in this setting. The motivation (Figure 1 shows monotonic deviation as OOD increases) is intuitive and well-supported. The paper also relaxes the batch-level mixing assumption of WOODS/Du et al. (2024a), operating at dataset-level mixing which is more realistic for outsourced wild datasets.

- **Strong empirical performance across diverse benchmarks.** Medix is evaluated on 11 InD-OOD pairs against 20 baselines. On CIFAR-100 (Table 2), it achieves average FPR95 of 5.42% vs. WOODS 6.74% and OE 14.26%. On CIFAR-10 (Table 1), 0.80% vs. WOODS 3.40%. The performance is consistent with low variance across runs (error bars reported).

- **Two-sided theoretical bounds.** Theorems 4.1 and 4.2 provide upper bounds on both inlier misclassification (InD flagged as OOD) and outlier misclassification (OOD retained as InD). This symmetric treatment is a conceptual advancement over prior wild-data methods that address only one type of error.

- **Thoughtful ablation and analysis deferred to appendix.** The paper signals ablation studies (EWM vs. geometric median, hyperparameter sensitivity, unseen OOD evaluation, pseudo-label quality) that preempt common concerns, even though these are in the appendix.

## Weaknesses

### Major

- **Theoretical guarantees are disconnected from the actual algorithm.** Theorems 4.1 and 4.2 analyze a *generic* element-wise median (EWM) filtering rule under i.i.d. gradient assumptions, but Algorithm 1 is an *iterative greedy procedure* that removes top-k samples each iteration and recomputes the median. The paper does not bridge this gap — it is unclear that the bounds apply to the iterative procedure. The i.i.d. assumption on gradients is also technically questionable, as all gradients are computed from the same trained model and are coupled through the loss. The bounds are loose (π/[2(1-π)] = 0.5 when π=0.5, and m_min is never defined in the main text). While the paper mentions a looser version without sub-Gaussian assumptions (Theorem C.3, Appendix C.3), the core gap between theory and algorithm remains unaddressed.

- **The filtering stage is not independently validated on real data.** The paper's central claim is that median-based gradient deviation can identify OOD samples in an unlabeled mixture. Yet no precision, recall, or F1 for the outlier extraction stage (Algorithm 1) is reported on real wild mixtures. The only direct evidence is Figure 2 (a 2D Gaussian toy example where OOD is placed at [20, 2√3] vs. InD near the origin — a trivially separable case). Without standalone filtering metrics, it is impossible to attribute the final OOD detection gains to the median mechanism vs. the downstream detector training protocol.

### Minor

- **Wild data construction limits the strength of generalization claims.** The main evaluation (Section 5.1) constructs wild data from the *same* OOD distribution used for testing (e.g., wild mixture uses PLACES365, test OOD is PLACES365). This follows the standard WOODS protocol, so comparisons to baselines are fair. However, the paper's headline claim of "outperforming across the board in open-world settings" is stronger than what this protocol supports. The unseen-OOD evaluation (Appendix A.4) partially addresses this, but it should be a primary result rather than deferred.

- **No runtime or scalability analysis in the main text.** Algorithm 1 requires O(m²d) operations per iteration for the leave-one-out EWM computation. With m up to 50,000, this is computationally intensive. The main text contains no wall-clock comparisons or scalability discussion, only a pointer to Appendix A.6. Given that WOODS is a baseline, a runtime comparison would help assess practical deployability.

- **Several minor notational issues in the theory.** In Theorem 4.1, ε is defined but does not appear in the stated bound; m_min appears in the bound and in ε's definition but is not defined in the main text. These are likely clarified in the (removed) appendix, but the main text should be self-contained.

### Trivial

- The algorithm's loop condition (line 2) uses δ_max initialized to ∞ with `|δ_max| > ε`, but δ_max is only updated after the first removal iteration — the first iteration always proceeds regardless of ε, which is fine but could be clearer.
- The top-k selection uses indices I_k from the previous iteration before updating S, making the first iteration add an empty set to O — this is correct but the presentation could be tighter.

## Nice-to-Haves

- An ablation comparing the iterative greedy removal to a single-pass threshold (e.g., remove all samples whose individual gradient deviation exceeds a threshold) would clarify whether the iteration is necessary.
- A comparison to a simple baseline that thresholds gradient-norm distance from mean InD gradient (without the median) would isolate the benefit of the median operation.
- Systematic sensitivity analysis on the mixing parameter π (varying from 0.1 to 0.9) would strengthen the paper.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Evaluation protocol uses wild data that contains test OOD samples, invalidating the claim of general OOD detection."** — This is the standard protocol established by WOODS (Katz-Samuels et al., 2022a). All baselines are evaluated under the same protocol, so comparisons are fair. The paper also evaluates unseen OOD (Appendix A.4). This is a limitation of the sub-field's standard benchmark, not a unique flaw, and does not invalidate the core contribution.

- **"The enormous gap between KNN+ (46.40%) and Medix (5.42%) is suspicious."** — KNN+ is an *InD-only* method (Table 2, "Using P_in only"). Methods using wild data (OE, WOODS, Medix) are expected to perform far better. The comparison against WOODS (6.74%) is the appropriate wild-data baseline, and the 1.32% gap is reasonable and not suspicious.

- **"Figure 1 does not demonstrate that the distance decreases when actual OOD is removed."** — The logic is monotonic: Figure 1 shows that adding OOD increases the deviation monotonically. The algorithm removes samples to minimize this deviation. If the relationship is monotonic, removing OOD samples (which caused the increase) would decrease the deviation. The reasoning is sound.

- **"The core filtering mechanism is not validated on real data"** regarding Figure 1 being "synthetic." — CIFAR-10 and SVHN are real image datasets, not synthetic. This part of the critique incorrectly characterizes the experiment.

- **Weaknesses about formatting/typos, missing appendix content, or missing related works.** — These are parser artifacts or out-of-scope from the reviewer's knowledge limitations.

## Novel Insights

None beyond the paper's own contributions. The median-as-filter for wild-data OOD detection is the paper's own insight, and the reviews do not synthesize a deeper observation beyond what the authors already present.

## Suggestions

1. **Bridge theory and algorithm.** Either adapt the theoretical analysis to the actual iterative greedy procedure, or clearly state what the existing bounds imply (e.g., that a single-pass EWM filtering step has certain guarantees, and the iterative extension is a heuristic).

2. **Report filtering-stage metrics.** On at least one real wild mixture, report precision, recall, and F1 for Algorithm 1's OOD identifications. This directly validates the core claim that the median mechanism identifies OOD samples.

3. **Move unseen-OOD results to the main paper.** The evaluation where P_out^test ≠ P_out (Appendix A.4) should be a primary table, as it directly addresses the most significant concern about the evaluation protocol.

4. **Provide runtime analysis.** Include wall-clock training time vs. WOODS and other wild-data baselines, even if in an appendix with a summary in the main text.

5. **Define all theorem variables in the main text.** Ensure m_min and other quantities used in the bounds are defined where the theorem appears.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Human Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/c4r7iLhGcQ.md` | 2.00 | Much weaker — limited experiments, flawed theory assumptions, no strong empirical results. Medix is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/rWrr6EUKpm.md` | 3.60 | Weaker — core premise (redefining OOD as low-density training data) was a conceptual stretch. Medix has a clearer, more standard problem framing. |
| `/home/wg25r/review_agent/human_reviews_2026/WOh2D1V0Ru.md` | 3.50 | Weaker — insufficient baselines and novelty concerns. Medix is more comprehensive in evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/9gvUS0ewHm.md` | 3.50 | Weaker — tackled a niche sub-problem (fairness in OOD detection). Medix tackles a more central problem. |
| `/home/wg25r/review_agent/human_reviews_2026/g7zjJZMbV5.md` | 3.00 | Weaker — theoretical analysis showed task degradation rather than proposing a solution. Medix proposes a concrete algorithm. |
| `/home/wg25r/review_agent/human_reviews_2026/GEtOzC4MIi.md` | 6.00 | Comparable — both have an interesting theoretical framing that doesn't fully connect to the final method. Both have strong experiments. The Fisher-Rao paper's theory is more cohesive, but Medix's empirical scope is broader (20 baselines vs. 9). |
| `/home/wg25r/review_agent/human_reviews_2026/Eu25AOvORb.md` | 6.00 | Slightly stronger — cleaner contribution (universal OD), well-received by all reviewers. Medix has more methodological concerns (theory-algorithm gap). |

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>