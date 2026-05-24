Now I have all the information I need. Let me construct the consolidated review.

## Summary

This paper proposes Energy-based Concept Bottleneck Models (ECBMs), which extend concept bottleneck models by defining a joint energy over (input, concept, class) tuples through three neural network energy functions (class, concept, and global). This formulation unifies three capabilities under a single probabilistic framework: (1) standard concept-based prediction, (2) test-time concept intervention/correction that propagates corrections to correlated concepts, and (3) conditional interpretations that quantify complex dependencies between concepts and class labels. Empirical results on CUB, CelebA, and AWA2 show that ECBM achieves a large improvement in overall concept accuracy (e.g., 71.3% vs. 39.6% for CEM on CUB) while maintaining competitive per-concept and class accuracy.

## Strengths

1. **Novel unified framework.** The paper is the first to cast prediction, concept correction, and conditional interpretation as conditional probabilities under a joint energy formulation (Eq. 12 and Propositions 3.1–3.5). This goes beyond existing CBMs, which focus primarily on feedforward prediction. The three energy networks (class, concept, global) are well-motivated, and the derivation of different conditional probabilities as compositions of these energy functions is conceptually clean.

2. **Large gains in overall concept accuracy.** Table 1 shows ECBM nearly doubles the best baseline on CUB's overall concept accuracy (71.3% vs. CEM's 39.6%). This directly demonstrates that the global energy network successfully captures high-order concept interactions that independent concept predictors miss. The improvement is consistent across all three datasets.

3. **Effective intervention propagation.** Figure 2 shows ECBM consistently outperforms CEM in concept accuracy and overall concept accuracy across intervention ratios (0.2–1.0) on all three datasets. This provides concrete evidence that the joint energy formulation enables corrected concepts to propagate to correlated concepts, a capability existing CBMs lack.

4. **Conditional probabilities match ground truth well.** Figure 4 reports low L1 errors (0.0033, 0.0096, 0.0017) between ECBM's estimated conditional probabilities and empirical ground truth (Oracle), and Figure 3 shows ECBM's top-3 marginal concept importance matches the Oracle list exactly for four bird classes. These results validate that the probabilistic derivations yield meaningful outputs.

5. **Class accuracy is maintained or slightly improved.** Despite adding capacity for concept interactions and conditional interpretations, ECBM achieves the best class accuracy on CUB (81.2% vs. CEM 79.6%) and CelebA (34.3% vs. CEM 33.0%), showing that the unified formulation does not sacrifice final task performance.

## Weaknesses

### Fatal
None.

### Major
- **Unexplained zero variance on two datasets.** In Table 1, ECBM reports 0.000 standard deviation across all metrics on CelebA and for overall concept accuracy and class accuracy on AWA2 (five random seeds). This is highly unusual compared to all baselines (which show non-zero variance), and the paper provides no explanation. This either indicates a deterministic optimization that is insensitive to seed variation (which itself warrants discussion) or a reporting issue. Either way, the reader cannot assess the stability of the results.

### Minor

1. **No discussion of the inference-time asymmetry with baselines.** ECBM's test-time inference (Section 3.2) requires solving a continuous optimization via backpropagation for each test instance, while all baselines (CBM, CEM, PCBM, ProbCBM) are feedforward. The paper compares accuracy without acknowledging that ECBM uses substantially more inference computation. This does not invalidate the accuracy results, but it would strengthen the paper to report inference cost (time per instance, number of gradient steps, convergence criteria) and ideally ablate a feedforward variant of ECBM to isolate the contribution of the energy formulation from the test-time optimization.

2. **Zero variance on CelebA/AWA2 needs explanation.** (Same as Major point 1, consolidated here — moved to Major.)

3. **Conditional interpretation evaluation lacks baseline comparisons.** Figures 3 and 4 compare ECBM's conditional probabilities only against an Oracle (empirical ground truth). The paper does not show whether existing methods (e.g., CBM or CEM) can or cannot produce comparable conditional interpretations, or how they would fare on the same evaluation. The novelty claim is that ECBM enables these interpretations via its energy framework, but showing a baseline comparison would substantially strengthen the evidence.

4. **The "hard version" for computing probabilities is underspecified in the main paper.** The implementation section (line 207) states "For the propositions, we have implemented a hard version (yielding 0/1 output results) for computing probabilities" without detailing how this is done. While the appendix (stripped by the PDF parser) likely contains these details, the main paper body should give sufficient intuition for a reader to understand what approximation is being made.

### Trivial
- Table 1 would benefit from a note explaining the 0.000 variance entries.

## Nice-to-Haves
- An ablation isolating the contribution of each of the three energy terms (class, concept, global) to the overall concept accuracy improvement. The paper mentions this is in Appendix C.2 (stripped), so this is noted for completeness.
- A per-concept error analysis showing what kinds of concept combinations ECBM gets wrong, to verify the model is learning meaningful interactions rather than just memorizing frequent correlation patterns.
- Runtime and iteration count for the test-time optimization, to help practitioners assess the trade-off.

## Removed Points

These points from the input reviews are removed or weakened per the filtering rules:

1. **"Intractable normalization with missing approximation details"** (Harsh Critic point 1, part about negative sampling not being specified). REMOVED: The paper explicitly states "a negative sampling strategy" is used (line 124), and the appendix (stripped by the PDF parser) would contain the specifics. The instructions forbid penalizing missing appendix content. The main paper body's level of detail is typical for a conference submission.

2. **"Overall concept accuracy is misleading / could be overfitting to concept correlations"** (Harsh Critic point 3). REMOVED: This is a speculative claim unsupported by evidence in the paper. The metric is clearly defined (Eq. 17) and is a natural extension of per-concept accuracy. ECBM also shows improvements in per-concept accuracy (0.965→0.973 on CUB) and class accuracy (0.796→0.812), so the improvement is not isolated to this one metric.

3. **"ECBM underperforms in class accuracy during intervention — conflicts with abstract"** (part of Harsh Critic's Section-by-Section notes). REMOVED: The paper explicitly addresses this (lines 254-255): "Note that the primary focus of our ECBM is not class accuracy enhancement." There is no conflict with the abstract, which claims superiority in overall accuracy (Table 1) — not intervention class accuracy.

4. **"Missing ablation of the three energy terms"** (Harsh Critic). REMOVED: The paper states an ablation study is in Table 4 of Appendix C.2. The appendix is stripped by the parser.

5. **"Proposition typos and argument order errors"** (Harsh Critic). REMOVED per instructions to disregard typos/formatting errors caused by the PDF parser.

6. **"No failure case analysis"** (Harsh Critic). REMOVED: This is a scope-creep request. The paper provides extensive quantitative results across three datasets; a failure case analysis, while nice to have, is not required to validate the core claims.

7. **Generic sycophancy/importance claims** from Strength Finder (e.g., "this paper addressed an important problem"). REMOVED per filtering rules — only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder bring the same observations the paper makes about itself: the energy-based unification is novel, the overall concept accuracy gains are striking, and the conditional interpretation capabilities are a new dimension for CBMs. No cross-paper synthesis revealed a perspective the authors did not already articulate.

## Suggestions

1. Report and discuss the variance of ECBM's results across random seeds, particularly for CelebA and AWA2 where zero variance appears. If the optimization is indeed deterministic given a seed, state this explicitly and explain why. If the results vary, correct the table.

2. Add a paragraph discussing the inference overhead of the test-time optimization versus feedforward baselines. Report approximate inference time per instance, number of gradient steps used, and whether early stopping or a fixed iteration budget is employed.

3. Show that at least one baseline CBM method (e.g., CBM or CEM) cannot produce the conditional interpretations shown in Figures 3–4 by attempting to extract analogous quantities from those models (e.g., through learned weight matrices). This would demonstrate that ECBM provides genuinely *new* interpretability.

4. Provide a brief intuition in the main text for how the "hard version" of the propositions converts the energy-based probabilities into the reported 0/1 results, so a reader can assess the approximation without consulting the appendix.

## Score and Decision

**Calibration Report**

Round 1 bracket: [5, 7] — The paper is clearly stronger than weak papers (3-4 range) but not at the level of top papers (8+).

Retrieved anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/wpL3otU9eY.md` (CBM-zero) | 3.00 | R1 | Much weaker — small incremental contribution vs. ECBM's novel framework |
| `/home/wg25r/review_agent/human_reviews/kTjEPEy96Q.md` (Unsupervised CBM eval) | 3.00 | R1 | Much weaker — evaluation framework paper, no new method |
| `/home/wg25r/review_agent/human_reviews/5Aem9XFZ0t.md` (Zero-shot CBM) | 4.83 | R1/R2 | Weaker — limited novelty, ECBM has more novel framework |
| `/home/wg25r/review_agent/human_reviews/Rv55TnDZ2W.md` (Editable CBM) | 5.60 | R1/R2 | Comparable — both have novel applications to CBMs. ECBM has more conceptual novelty but less mathematical rigor in presentation. |
| `/home/wg25r/review_agent/human_reviews/Q9Z0c1Rb5i.md` (SupCBM) | 5.00 | R1 | Slightly weaker — ECBM's energy-based unification is more novel |
| `/home/wg25r/review_agent/human_reviews/Yt9CFhOOFe.md` (CB-pLM for proteins) | 6.60 | R2 | Stronger — more polished experiments, clear application domain |
| `/home/wg25r/review_agent/human_reviews/n34taxF0TC.md` (InterpGN) | 6.60 | R2 | Stronger — more rigorous evaluation, though different domain |
| `/home/wg25r/review_agent/human_reviews/GjfIZan5jN.md` (Representation interpretability) | 7.33 | R2 | Stronger — more comprehensive experiments and analysis |

Round 2 narrowed the bracket to [5.5, 6.5]. The ECBM paper is slightly above the Editable CBM (5.60) due to greater novelty of its framework, but below the 6.6+ papers that have more polished experimental sections and address computational considerations.

**Final Score: 6.0**

**Justification:** The paper proposes a genuinely novel framework (energy-based unification of prediction, intervention, and conditional interpretation for CBMs) with clear theoretical derivations. The empirical evidence shows a striking improvement in overall concept accuracy and competitive performance across other metrics. The main factors preventing a higher score are (i) unexplained zero variance on two datasets, (ii) lack of discussion of inference-time asymmetry with feedforward baselines, and (iii) incomplete specification of approximation strategies in the main text. These are addressable weaknesses, not fatal flaws. The contribution is solid and the paper is well-positioned to be strengthened through the review process.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>