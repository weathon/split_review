Now I have sufficient calibration data. Let me compile the final review.

---

## Summary

This paper proposes Medix, a two-stage framework that (1) filters outliers from unlabeled wild data using element-wise median (EWM) of gradients, and (2) trains a binary OOD detector on identified outliers plus labeled InD data. The median operation offers robustness to contamination: Theorem 4.1 bounds inlier misclassification provided π < 0.5. Empirically, Medix achieves strong results across 11 InD-OOD pairs, outperforming 20 baselines including WOODS and KNN+ — e.g., reducing average FPR95 on CIFAR-100 from 6.74% (WOODS) to 5.42%.

## Strengths

- **Novel median-based filtering for wild-data OOD detection.** Medix uses the element-wise median (EWM) of gradients as a robust central tendency estimate, which is principled and contrasts with mean-based or threshold-based filtering used in prior work (e.g., Du et al. 2024a). The paper correctly identifies that dataset-level mixing (vs. batch-level) is a more realistic scenario, and Algorithm 1 is designed accordingly.

- **State-of-the-art empirical results across 11 InD-OOD pairs with 20 baselines.** Tables 1 and 2 show consistent and often substantial improvements. On CIFAR-10, Medix achieves average FPR95 of 0.80% vs. WOODS at 3.40%; on CIFAR-100, 5.42% vs. WOODS at 6.74%. The improvements hold across diverse OOD datasets (SVHN, PLACES365, LSUN-C, LSUN-RESIZE, TEXTURES). Results include standard deviations over 5 runs.

- **Two-sided theoretical error bounds (Theorems 4.1 and 4.2).** The analysis provides formal upper bounds on both inlier and outlier misclassification for the EWM-based filtering rule. The contamination term π/(2(1−π)) cleanly captures robustness for π < 0.5; the separation term in Theorem 4.2 quantifies when OOD gradients are far enough from InD to be reliably detected. Remark 4.3 provides empirical evidence for the sub-Gaussian assumption via Q-Q plots and also notes a looser bound without this assumption (Theorem C.3).

- **Dataset-level operation instead of batch-level.** Medix operates on the entire wild set (Algorithm 1), which is more practical than methods requiring structured batch-level mixing (Katz-Samuels et al. 2022a, Du et al. 2024a). The monotonic trend in Figure 1 motivates the iterative removal procedure.

## Weaknesses

### Major

- **Theory–algorithm gap in the claimed guarantees.** Theorems 4.1 and 4.2 bound the misclassification rate of an "EWM filtering rule" — a conceptual procedure whose precise decision rule is not formally defined in the paper. The actual algorithm (Algorithm 1) is a greedy, iterative leave-one-out procedure with parameters ε (stopping threshold) and k (number of points removed per iteration). The theorems contain no dependence on ε, k, or the iterative structure; they involve only sample sizes, π, and sub-Gaussian parameters. The paper states that the theory "provides a two-sided guarantee for the robustness of the Medix filtering method" (Section 4), but the connection between the abstract EWM rule and the implemented greedy algorithm is not established. This does not invalidate the contribution — the theoretical insight about median robustness is valuable independent of the approximation scheme — but the claim of "provably low error" for Medix specifically is overclaimed as written.

### Minor

- **Hyperparameter selection procedure is underspecified.** The paper states that ε and k are selected "from the sets {5e-5, 5e-4, 5e-3, 5e-2} and {4k, 7k, 10k, 20k}, respectively, taking into account dataset sizes and with the objective of maximizing OOD performance." It does not specify whether a held-out validation set was used, how the "objective of maximizing OOD performance" was operationalized, or whether this selection was performed independently per OOD dataset. The paper references Appendix A.2 for hyperparameter sensitivity analysis, suggesting robustness, but the selection methodology itself needs clarification to establish that the reported results are not over-optimistic.

- **CONJ and DRL baselines are mentioned but absent from main results tables.** The baselines section (page 8) states that CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024) were included "to provide a more thorough evaluation," but Tables 1 and 2 do not show their results. The abstract claims Medix "outperforms existing methods across the board." If results for these methods appear only in the appendix (which cannot be verified from the main text), a reader cannot confirm this claim from the main body. The paper should either include these in the main tables or clarify the scope of the claim.

- **Monotonic trend validated for only one InD-OOD pair.** Figure 1 demonstrates monotonic L2 deviation increase only for CIFAR-10 vs. SVHN. The algorithm's convergence criterion (stopping when δ_max ≤ ε) is justified by this monotonicity, but it is unclear whether the same trend holds for other OOD sources (e.g., TEXTURES, LSUN) or for CIFAR-100. If the trend is non-monotonic in some settings, the stopping criterion could behave incorrectly. Showing this trend for at least one additional OOD source would strengthen the motivation.

### Trivial

- The claim that Medix achieves "an outlier extraction error rate as low as 12.5%" (from the 2D synthetic example in Figure 2) is presented in the abstract and conclusions as a headline result. The 2D Gaussian example is intentionally simple (as the paper states, "designed to be simple to facilitate better understanding"), and the 12.5% figure refers to InD samples mistakenly flagged as OOD in this favorable setting. It is not a meaningful bound for real high-dimensional data.

## Nice-to-Haves

- **Vary the contamination ratio π.** All experiments fix π = 0.5. Since π is unknown in practice and the theoretical bounds degrade as π increases toward 0.5, experiments with π ∈ {0.1, 0.2, 0.3, 0.4} would validate the method's practical robustness at lower contamination levels. (The paper notes Appendix A discusses related experiments — if these include varying π, they should be highlighted in the main text.)

- **State the computational complexity of Algorithm 1.** The inner loop (line 5–7) recomputes the EWM after each candidate removal, which could be O(m²·d) in the worst case. A brief complexity statement in the main text would help readers assess scalability.

- **Scope-related clarification about PU learning.** The paper contrasts Medix with positive-unlabeled learning but could more sharply articulate the distinction: PU methods learn a binary classifier from positive + unlabeled data, while Medix additionally uses the filtered outliers to train a separate OOD detector.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"Sub-Gaussian assumption may not hold"** — REMOVED. Remark 4.3 already provides empirical evidence (Q-Q plots) and references a looser bound (Theorem C.3) that relaxes this assumption.
- **"Synthetic 2D example is highly favorable / not meaningful"** — DEMOTED to Trivial above. The paper clearly states the example is for visualization; it is not presented as real-world evidence.
- **"Missing related works"** — REMOVED per policy (no external sources to verify).
- **"Typos/formatting"** — REMOVED per policy (parser artifacts).
- **"Gradient coordinates are assumed independent"** — REMOVED. The paper does not assume independence; it assumes each coordinate is sub-Gaussian, which is a much weaker condition.
- **"Scalability issues not addressed in main text"** — MOVED to Nice-to-Have above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Align the theory with the algorithm.** Either (a) prove that the greedy iterative procedure (Algorithm 1) achieves error bounded by the terms in Theorems 4.1–4.2 (or derive algorithm-specific bounds involving ε and k), or (b) clearly separate the theoretical claim (bounds for the conceptual EWM rule) from the empirical claim (Algorithm 1 approximates this rule well) and demonstrate the approximation quality experimentally (e.g., by comparing the greedy solution to the brute-force optimum on small wild subsets).

2. **Clarify the hyperparameter selection protocol.** State explicitly whether a held-out validation set was used (and if so, how it was constructed from the wild data without test-set leakage). If hyperparameters were chosen based on a general principle (e.g., k ≈ dataset size / class count, ε based on gradient magnitude scale) rather than per-dataset optimization, describe that principle.

3. **Move CONJ/DRL results into the main tables** or at minimum state in the main text whether they are included there, and if their results are deferred to the appendix, add a footnote or table caption explicitly directing readers there.

## Score and Decision

**Calibration protocol:**

*Round 1 bracket (broad):* The paper sits above weak anchors (avg 2.0–3.4, all rejected) and below top-tier anchors (avg 7.6–8.0). The most topically relevant anchor is the SAL paper (Du et al. 2024a, "How Does Unlabeled Data Provably Help OOD Detection?" — avg 6.50, accepted), which also proposes a two-stage filter-and-classify framework for wild-data OOD. Bracketing range: [4.5, 6.5].

*Round 2 narrowing:* Anchors within the bracket include SPADE (avg 5.50, accepted — similar theory-practice gap, weaker experiments), the Gradient Norm paper (avg 5.50, rejected — novelty overlap with prior work), and RobustTSF (avg 5.50, accepted — theory-practice gap). Medix has stronger empirical results than any of these but shares the theory-alignment weakness with SPADE. The SAL paper (avg 6.50) has cleaner theory-alignment but comparable empirical scope; Medix is weaker than SAL on the theory front.

*Final placement:* 5.5 — comparable to SPADE (accepted at 5.50) with similar theory-alignment issues but stronger empirical results.

**Anchors retrieved (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 6Z8rZlKpNT (Normalizing Flows OOD) | 3.40 | R1 | Much weaker, no wild data |
| 3ZdGSTxKuy (Harry Potter atypical video) | 2.00 | R1 | Much weaker, different problem |
| KK29oh8jZs (Synthetic OOD probing) | 3.00 | R1 | Much weaker |
| 10fsmnw6aD (CIL with OOD) | 2.50 | R1 | Much weaker |
| bcWwhF8cTZ (Gradient Norm OOD error) | 5.50 | R1/R2 | Similar score, rejected due to novelty concerns not present here |
| jlEjB8MVGa (SAL / Du et al. 2024a) | 6.50 | R1/R2 | Stronger theory-alignment, accepted |
| 9qpdDiDQ2H (MetaOOD) | 5.25 | R1 | Wider scope, less theory |
| jjjxp9Wgjp (Pseudo-Labels OOD) | 4.25 | R1 | Weaker theory and results |
| cJs4oE4m9Q (Orthogonal Hypersphere AD) | 8.00 | R1 | Much stronger, different topic |
| EUSkm2sVJ6 (Data Usage Inference) | 7.60 | R1 | Much stronger, different topic |
| KbetDM33YG (Online GNN Evaluation) | 8.00 | R1 | Much stronger, different topic |
| TTrzgEZt9s (DRO with Bias/Variance) | 8.00 | R1 | Much stronger, different topic |
| kwCHcaeHrf (SPADE) | 5.50 | R1/R2 | Similar theory-practice gap, accepted |
| sZZ3R0lV9f (MixDiff) | 5.25 | R2 | Weaker contribution |
| nUBLhhVM1l (Tight Rates Outlier Transfer) | 6.33 | R2 | Stronger theory, different setting |
| falBlwUsIH (Ignore Labels OOD) | 6.33 | R2 | Stronger theory |
| 7QDIFrtAsB (Gradients Tabular AD) | 5.75 | R2 | Different domain (tabular) |
| ltZ9ianMth (RobustTSF) | 5.50 | R2 | Similar score, accepted |
| jQ596tXT3k (Likelihood Peaks OOD) | 5.67 | R2 | Different approach |
| kIZ3S3tel6 (Outliers Opposing Signals) | 5.50 | R2 | Different topic |
| w0jk3L3IjV (Detection-Generalization Paradox) | 5.67 | R2 | Different focus |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>