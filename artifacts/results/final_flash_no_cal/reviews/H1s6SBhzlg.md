Now I have a thorough understanding of the paper and can evaluate each reviewer claim carefully. Let me compose the final consolidated review.

## Summary

This paper studies how to aggregate answers from multiple LLMs by moving beyond majority voting (MV) to leverage higher-order information. It proposes two algorithms: (1) **Optimal Weight (OW)**, a Bayesian-optimal weighted voting scheme using first-order information (per-model accuracies), and (2) **Inverse Surprising Popularity (ISP)**, a second-order method using pairwise answer correlations that provably achieves higher expected advantage than MV and the classic "surprisingly popular" (SP) rule. The paper also introduces practical unsupervised variants (OW-L, OW-I) that estimate the required quantities without ground-truth labels. Experiments on simulated data, UltraFeedback, MMLU, and a real healthcare dataset (ARMMAN) show consistent gains over MV.

## Strengths

1. **Bayesian optimality of OW (Theorem 1).** The OW algorithm with weights given by the inverse of a sigmoid-like function of each LLM's accuracy is proven to be the Bayesian-optimal aggregator among *all* possible rules (linear or not) under conditional independence. This is a clean and non-trivial theoretical result that substantially improves over equal-weight MV. *Evidence: Section 3, Theorem 1.*

2. **Provable advantage ordering for ISP (Theorem 2 & Example 1).** ISP is shown to achieve higher expected advantage than MV, which in turn beats SP, with closed-form expressions for the gaps. Example 1 concretely demonstrates a case where ISP always recovers the truth while MV succeeds only 7/8 of the time and SP only 3/4. *Evidence: Section 4.2, Theorem 2, Table 1.*

3. **Consistent empirical gains across multiple datasets (Tables 3 & 4).** On UltraFeedback (K=2), MMLU (K=4), and ARMMAN (K=2), all proposed methods (OW-L, OW-I, ISP) outperform MV. Across 16 model ensembles, OW-L beats MV in 97.92% of cases, MV never achieves the best accuracy in any case, and improvements reach 2.78–3.36% absolute gain on the non-consensus subset. The t-statistics (12.53, 23.39, 3.22) are substantial. *Evidence: Section 5.4, Tables 3 & 4.*

4. **Practical unsupervised estimation of optimal weights (Section 5.2).** OW-L learns accuracies from pairwise answer correlations via empirical risk minimization, and OW-I uses ISP's own predictions as pseudo-ground-truth to estimate accuracies. Both make the Bayesian-optimal OW usable without any true labels, which is key for real unsupervised settings. *Evidence: Section 5.2, Equations (7) and surrounding text.*

5. **Finite-sample guarantee for ISP (Theorem 3).** The theoretical bound shows that even when second-order information is estimated from the same M questions used for evaluation, ISP's advantage over MV persists with high probability, with a penalty term that decays as Õ(√(log(1/δ)/M)). This directly addresses the realistic setting of finite data. *Evidence: Section 4.3, Theorem 3.*

6. **Characterization of when each method excels (Proposition 2, Corollary 2).** Corollary 2 identifies that MV is optimal only when all agents are homogeneous. Proposition 2 gives precise conditions under which OW strictly beats any individual agent. These results clarify the scope of each method. *Evidence: Section 3, Proposition 2 and Corollary 2.*

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The theoretical claim of "outperforming" is about advantage, not directly about accuracy.** Theorem 2 establishes an ordering of expected *advantage functions*: E[Adv_ISP(s*)] ≥ E[Adv_MV(s*)] ≥ E[Adv_SP(s*)]. The paper then states ISP "outperforms MV" and "consistently outperform[s] majority voting." Since the decision rule selects the label with maximal advantage, higher *expected* advantage for the true label does not *provably* translate to higher *expected accuracy* — the mapping from advantage ordering to accuracy ordering involves the joint distribution over all labels. The paper's wording conflates what is proven (advantage ordering) with what is demonstrated empirically (accuracy gains). The authors should either (a) clarify the theoretical claim is about advantage and that accuracy is evaluated empirically, or (b) provide a formal link between advantage and accuracy. *Evidence: Theorem 2, and the sentence "ISP in Algorithm 2 outperforms MV, which in turn outperforms SP, in expectation" in Section 4.2.*

2. **The evaluation protocol for second-order estimation in real-world experiments is underspecified.** The paper does not clearly state whether the conditional probabilities ℙ̂(A_i | A_j) used by ISP/OW-L/OW-I were estimated on the *same* set of questions used to evaluate accuracy, or whether a holdout set or cross-validation was employed. While Theorem 3 provides a finite-sample bound for ISP that covers the same-data setting (the bound includes a penalty term that vanishes with M), the paper's empirical sections lack any explicit description of the estimation/evaluation split. For OW-I, which uses ISP's predictions on the same data as pseudo-ground-truth to estimate accuracies, the circular dependency is more concerning, yet no special handling is described. The results are almost certainly reliable given the large dataset sizes and consistent gains, but the protocol should be stated explicitly. *Evidence: Sections 5.1–5.4 — no mention of train/test splits or holdout validation.*

3. **Implementation of random shuffling in real experiments is not detailed.** Algorithms 1 and 2 prescribe random label shuffling as a pre-processing step, and the theoretical results rely on the symmetry it induces. While the paper states that shuffling is applied (Section 2), it does not describe how this was actually implemented for each dataset — e.g., whether answer options were physically reordered when querying the LLMs, or whether shuffling was done only as a post-hoc analytical step. This matters because MMLU has fixed answer options (A/B/C/D) and the prompt order could affect LLM behavior. *Evidence: Algorithm 1 (step 2), Algorithm 2 (step 2), Section 2 text.*

4. **Missing error bars or confidence intervals on accuracy estimates.** Table 3 reports point estimates of accuracy without any variance information (standard deviation, standard error, or confidence intervals). While the t-statistics reported for per-question comparisons are large, confidence intervals for the overall accuracy would help gauge the precision of the reported gains, especially on ARMMAN where the improvement over MV is only ~0.54%. *Evidence: Table 3, Section 5.4.*

5. **The derivation of ISP from the binary intuition to the general K>2 formula could be clearer.** Section 4.2 motivates ISP via a binary intuition (Eq. 3→4) but then jumps directly to the full K-option ISP score (Eq. 5) without an explicit bridging step. The connection between the "swap the conditioning" idea and the averaging over counterfactual labels in Eq. 5 is not fully spelled out, making the design choice harder to follow. *Evidence: Section 4.2, transition from Eq. 4 to Eq. 5.*

### Trivial
- Table 3 does not note which differences are statistically significant; the t-test is mentioned but only in text for OW-I vs MV, not for all method pairs.
- The paper defines σ_K(x) = e^x/(K-1+e^x) in Section 3, but in the abstract it says σ_K(x) = x²/(K-1+x²) — there appears to be a notational inconsistency. (The body uses the version in Section 3, which is the correct logistic-like function.)

## Nice-to-Haves
- A comparison to confidence-score-based aggregation methods (e.g., Chen et al., 2023a) would further strengthen the claim that *correlation-based* higher-order information is uniquely beneficial beyond per-model confidence scores.
- The OW-I pipeline (ISP → pseudo-labels → accuracy estimates → OW weights) would benefit from a dedicated analysis of its statistical properties, since it involves a double-use of the same data.
- Error bars or confidence intervals on the accuracy numbers in Table 3 (and Table 2 for simulations) would improve presentation.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The proof sketch is missing; the paper relies on the appendix."* — The appendix is stripped by the parser, not missing from the original submission. Removed per hard rules.
2. *"Data leakage that could make the reported improvements artificially large" presented as a fatal flaw.* — The paper explicitly addresses the same-data estimation setting in Theorem 3, which provides a finite-sample bound with a vanishing penalty term. The critic's assertion that "the theoretical bound in Theorem 3 is not guaranteed to hold when the question used for evaluation is part of the estimation set" misunderstands the theorem, which is designed for exactly this scenario. The underlying concern about underspecified protocol is real but minor (retained as Weakness #2 above); the "fatal" framing is not justified. Demoted.
3. *"The paper does not clarify whether the real-world experiments actually applied random shuffling" presented as a critical gap.* — The paper *does* state that shuffling is applied (Section 2, Algorithms 1 & 2). The critic overlooked this. The remaining concern is that implementation details per dataset are not provided, which is retained as a Minor weakness above. Demoted.
4. *Missing comparison to confidence-based baselines.* — Not a weakness; the paper's scope is higher-order information. Moved to Nice-to-Haves.
5. *Strength Finder's generic/delusional strengths.* — The Strength Finder's outputs were concrete and evidence-backed; none were generic or sycophantic. All retained.

## Novel Insights

None beyond the paper's own contributions. The most interesting observations from the reviews — particularly the explanation for why SP underperforms MV in LLM settings (systematic biases are less pronounced than in human crowds) and the connection between OW weights and the Bradley-Terry model via inverse-logistic weighting (Corollary 1) — are already present in the paper.

## Suggestions

1. **Clarify the experimental protocol.** Explicitly state whether the second-order estimates (ℙ̂(A_i|A_j) etc.) are computed from all data or from a separate estimation set, and whether any holdout or cross-validation is used. If all data are used, note that Theorem 3 provides a theoretical justification and briefly explain why the per-question bias is negligible for large M.
2. **Distinguish theoretical from empirical claims.** Rephrase "ISP outperforms MV" to "ISP achieves a higher expected advantage than MV (Theorem 2)" in the theoretical context, and reserve accuracy claims for the empirical evaluation.
3. **Describe the shuffling implementation per dataset.** For datasets with fixed answer orders (e.g., MMLU's A/B/C/D), explain whether the options were randomized in the prompt or whether shuffling was applied as a post-hoc relabeling step.
4. **Add confidence intervals or error bars to accuracy tables** (e.g., via bootstrap or standard error across ensemble combinations) to quantify the reliability of the reported gains.
5. **Expand the ISP derivation.** Include an explicit intermediate step showing how the binary swap (Eq. 4) generalizes to the K-option average in Eq. 5, perhaps with a small K=3 worked example.
6. **Consistent notation for σ_K.** Align the definition of σ_K between the abstract (x²/(K-1+x²)) and the main body (e^x/(K-1+e^x)).

## Score and Decision

The paper makes a substantial contribution to the important problem of LLM answer aggregation. The theoretical results (Bayesian optimality of OW, advantage ordering for ISP, finite-sample guarantees) are clean and non-trivial. The practical unsupervised variants (OW-L, OW-I) address a genuine deployment challenge. The empirical evaluation covers multiple datasets and shows consistent improvements over MV. The weaknesses are addressable — primarily clarity of presentation and experimental protocol specification — and do not threaten the core claims.

**Overall assessment:** Strong paper with clear contributions. I recommend acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>