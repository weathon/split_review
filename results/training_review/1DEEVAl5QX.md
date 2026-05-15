Now I have thoroughly analyzed the paper and all reviewer claims. Let me write the consolidated review.

**Summary of verification findings:**

1. **Lemma 4.3 proof flaw** — CONFIRMED. In the original (weighted) Case 2, plugging μ=F(e)/γ into the bound 2exp(-ε²αμ/(3F(e))) yields 2exp(-ε²α/(3γ)) because F(e) cancels. Under Lemma 4.3's new bound 2exp(-ε²αφμ/(6F(e*))), plugging μ=F(e)/γ yields 2exp(-ε²αφF(e)/(6γF(e*))) — F(e) does NOT cancel, leaving an unbounded dependence on F(e)/F(e*). The paper's claim that "the same result still holds with an additional multiplicative 1/φ factor in α" is not supported by the presented algebra.

2. **Narrow experiments** — CONFIRMED. Algorithm comparison only on 2/4 datasets. The justification "ground sets are small" is not persuasive.

3. **"Impossible" claim** — The paper justifies this by giving a worst-case counterexample. This is defensible. The criticism is invalid.

4. **Table 1/algorithms not visible** — Parser artifacts. Remove.

5. **Unequal comparison** — Partially valid. Same β gives mini-batch more total samples. But the paper acknowledges the asymmetry. This is a methodological nuance, not a fatal flaw.

Let me now write the final review.## Summary

This paper introduces the first mini-batch algorithm for maximizing a non-negative monotone decomposable submodular function under constraints. The key idea is to sample a fresh mini-batch (either uniformly or with importance weights) at each greedy iteration rather than constructing a single sparsifier upfront. The authors provide theoretical guarantees for weighted mini-batch sampling (Section 2), empirically observe that uniform sampling outperforms weighted sampling, and propose a smoothed analysis (Section 4) with two noise models (Model 1 and Model 2) to theoretically explain uniform sampling's practical success.

---

## Strengths

- **Novel mini-batch approach for decomposable submodular maximization.** The paper presents the first algorithm that samples a fresh batch per greedy iteration, as opposed to the existing sparsifier approach (Rafiey & Yoshida, 2022). This is a clean and natural algorithmic idea that was previously unexplored in this setting.

- **Clean theoretical analysis for weighted mini-batch sampling (Theorem 1.3, Theorem 1.4).** The analysis of weighted mini-batch under both bounded and unbounded curvature is technically sound and establishes clear query complexity bounds. The introduction of an additive approximate incremental oracle (Theorem 1.2) and its integration into the greedy framework is a useful technical contribution that may be of independent interest.

- **Smoothed analysis Model 1 provides a rigorous justification for uniform sampling under strong assumptions.** Theorem 4.2 convincingly shows that under Model 1 (where every element has expected value ≥ φ), uniform sampling approximates weighted sampling up to an O(1/φ) factor, for both the sparsifier and mini-batch approaches. This part of the analysis is technically solid.

- **Uniform mini-batch eliminates the O(Nn) preprocessing cost.** As noted in the paper and Table 1, uniform sampling requires no preprocessing and has query complexity independent of N, which is a genuine practical advantage for large-scale datasets.

---

## Weaknesses

### Fatal
None. The paper's contributions — the mini-batch algorithm, the weighted analysis, the experimental observations, and the Model 1 analysis — retain value even with the Model 2 issue. However, the flaw described below is severe and undermines the paper's central narrative.

### Major

1. **Lemma 4.3 (Model 2 guarantee for uniform mini-batch) has an invalid proof, leaving the paper's central theoretical claim unsupported.**  
   The proof states that plugging the new Chernoff bound (line 230) into the second case of Theorem 1.3 "yields the same result with an additional multiplicative 1/φ factor in α." This is incorrect.  
   
   In the original (weighted) case, Lemma 2.3 gives ℙ ≤ 2exp(−ε²αμ/(3F(e))). In the second case of Theorem 1.3 (line 159–163), setting μ = F(e)/γ yields ℙ ≤ 2exp(−ε²α/(3γ)) — the F(e) cancels because the denominator is also F(e).  
   
   Under Lemma 4.3's new bound ℙ ≤ 2exp(−ε²αφμ/(6F(e*))), substituting μ = F(e)/γ gives ℙ ≤ 2exp(−ε²αφ·F(e)/(6γF(e*))). The denominator is F(e*), not F(e), so **F(e) does not cancel**. The bound depends on the ratio F(e)/F(e*), which can be arbitrarily small for elements e ≠ e* (Model 2 guarantees nothing about F(e) for e ≠ e*). Setting α proportional to 1/φ alone cannot compensate for this unbounded ratio.  
   
   Since Lemma 4.3 is the only result that provides theoretical support for uniform mini-batch under Model 2 — which is the model that empirically matches *all* datasets — the paper's central claim that "Model 2 is able to explain the empirical success of the uniform mini-batch algorithm on all datasets" (line 235) is not justified by the presented mathematics. This is a genuine mathematical gap, not a presentation issue.

2. **Experimental validation is limited to 2 of 4 datasets.** The paper computes φ values for all four datasets (CIFAR100, FashionMNIST, Uber pickup, Discogs), but the actual algorithm comparison (Figure 1) is only shown for CIFAR100 and FashionMNIST. The paper's justification — "As the ground sets for both Uber pickup and Discogs are rather small, we only run experiments on the image datasets" (line 189) — is not persuasive; small ground sets make experiments *easier*, not harder. This leaves a significant empirical gap: the claim that "uniform mini-batch outperforms weighted sampling" and "Model 2 explains this on all datasets" is only partially supported by direct experimental evidence.

### Minor

1. **The experimental comparison gives the mini-batch an advantage in total samples.** Both methods are compared using the same β (fraction of data sampled), but the sparsifier samples βN elements once, while the mini-batch samples βN *fresh* elements per iteration, totaling k·βN samples over k iterations. This asymmetry in total sampling budget should be explicitly discussed. While the paper is transparent about the setup, a reader could misinterpret the comparison as controlling for total oracle calls.

2. **Section labeling inconsistency.** In line 205, the Model 1 subsection begins with the sentence "Model 1 We show that Model 2 maintains the theoretical guarantees…" — this should read "Model 1" instead of "Model 2." This is a small error but could cause confusion.

### Trivial
- Line 162: The fraction in the exponential has a missing closing parenthesis: `2\left(-\frac{\epsilon^{2}\mu}{3a}\right)` should be `2\exp\left(-\frac{\epsilon^{2}\mu}{3a}\right)`.

---

## Nice-to-Haves
- Showing the algorithm comparison results (Figure 1-style plots) for the Uber pickup and Discogs datasets would substantially strengthen the empirical case, even with small ground sets.
- A discussion of whether the Model 2 proof can be repaired — e.g., by using a two-stage analysis where the first iteration identifies e* and subsequent iterations use it as a reference point, or by requiring a slightly stronger assumption (e.g., F(e)/F(e*) is bounded below by some constant for all e).

---

## Removed Points
These points are flagged to be removed — treat them with caution:

- **"Impossible" claim is too strong**: The paper provides a concrete worst-case counterexample (line 35: "only a single f^j takes non-zero values") that justifies this statement. The criticism is invalid.
- **Algorithms/Table 1 not visible**: Parser artifacts from PDF extraction. The original submission has these.
- **Missing related works constraint**: Excluded per instruction (no external verification possible).
- **Formatting/typo nitpicks beyond the one noted above**: Parser artifacts, not author errors.
- **Reproducibility concerns about undisclosed hyperparameters**: The experimental setup (β, k, 20 runs) is clearly described.
- **Strength Finder's "comprehensive empirical validation across four diverse datasets"**: Overstated — algorithm comparison is only on 2 datasets, though φ values are computed for 4. Downgraded to minor weakness #2 above instead of listing as a strength.

---

## Novel Insights
The key observation from the reviews is that the paper's smoothed analysis contribution is split into two regimes with an important asymmetry: Model 1's proof is clean and complete but only matches some datasets empirically, while Model 2 matches all datasets empirically but has a flawed proof. This tension is not explicitly acknowledged by the paper. The flaw in Lemma 4.3 is subtle but fundamental — the algebraic cancellation that made the original (weighted) analysis work (F(e) appearing in both numerator and denominator) is lost when F(e) in the denominator is replaced by F(e*). Any attempted fix would need to either bound F(e)/F(e*) from below (which Model 2 does not provide) or restructure the proof to avoid the dependence on the specific element e. This suggests that the theoretical explanation for uniform sampling's empirical success is currently incomplete, and the paper's strongest claim — that Model 2 "explains the empirical success on all datasets" — overstates what has been proven.

---

## Suggestions
1. **Fix or qualify Lemma 4.3.** Either provide a corrected proof (which likely requires additional structure or a stronger assumption about F(e)/F(e*)), or explicitly state that the Model 2 guarantee is not currently established and soften the paper's claims accordingly. Without this fix, the paper should not claim that Model 2 explains the empirical results.
2. **Run algorithm comparisons on Uber pickup and Discogs.** The φ values alone do not constitute an empirical test of the algorithm. Even with small ground sets, running mini-batch vs. sparsifier comparisons on these datasets would significantly strengthen the paper.
3. **Acknowledge and discuss the total-sample asymmetry** between the sparsifier and mini-batch comparisons in the experimental setup.
4. **Reorganize the presentation** to clearly separate what is proven (weighted mini-batch, Model 1 results) from what is conjectured or incompletely proven (Model 2 results).

---

## Score and Decision

This paper addresses a relevant problem and introduces a novel algorithmic idea. The weighted mini-batch analysis and Model 1 results are solid contributions. However, the paper's headline narrative — explaining uniform sampling's empirical success via smoothed analysis — hinges on Lemma 4.3 (Model 2), whose proof is mathematically invalid. The experiments are also narrower than claimed. The paper requires a non-trivial revision to either fix the proof or substantially revise its claims. In its current form, it does not meet the acceptance bar for a top venue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>