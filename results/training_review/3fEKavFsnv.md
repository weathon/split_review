I have thoroughly read the paper and verified all claims. Let me now compose the consolidated review.

---

## Summary

This paper identifies that training deep-kernel MMD on machine-generated texts (MGTs) from multiple LLMs causes high variance in the MMD estimator, degrading detection performance. The authors propose MMD-MP, which removes the intra-class MGT term $k_\omega(y,y')$ from the optimization objective (but not from the test-time estimator). This yields a more stably trained kernel. Experiments across ChatGPT, GPT-2/3, GPT-Neo, and GPT4all-j show consistent improvements over baselines (MMD-D, C2ST, CE-Classifier), with particularly large gains in transfer to unseen LLMs (23–28% test power improvement).

## Strengths

- **Identifies a genuine and underexplored problem.** The paper is the first to study how multi-population MGT training data inflates MMD variance and impairs detection. The variance decomposition and empirical analysis (Figures 1–2) convincingly establish the phenomenon.

- **Clean, principled modification.** The proposed fix — removing $k_\omega(y,y')$ from the training objective — follows directly from the variance decomposition in Section 2.3. The method is simple to implement and well-motivated.

- **Strongest result: transfer to unknown LLMs (Tables 3–4).** MMD-MP outperforms MMD-D by 23.6–27.7% in test power and ~3.25% in AUROC on unseen LLMs (Neo-L, GPT-j-6b, GPT4all-j). This is a large, consistent improvement with clear practical significance.

- **Well-designed synthetic experiment (Section 4.1, Figure 3/5).** The four-center Gaussian mixture experiment directly varies the variance of training data ($\mu$) and shows that MMD-MP's advantage grows with training-data variance (up to ~9% test power). This isolates the variance-reduction mechanism cleanly.

- **Comprehensive evaluation.** Experiments cover full/limited/unbalanced training data, paragraph-level and sentence-level detection, and 7+ LLM families. The method consistently leads in nearly every setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing specification of the feature extractor $\hat{f}$ (Eqn. 3).** The paper states $\hat{f}$ is a "frozen feature extractor" and that the CE-classifier uses "the same model," but never identifies $\hat{f}$'s architecture (e.g., a specific pre-trained BERT variant, word-level embeddings, or a learned neural network). Since the entire deep kernel pipeline depends on this choice, the experiments are not reproducible without this detail. Other training hyperparameters (learning rate $\eta$, batch size, $T_{max}$, architecture of $\phi$, values of $\epsilon$, $\sigma_\phi$, $\sigma_q$) are also omitted.

- **Statistical significance not formally established for small-margin results.** In Tables 1, 5, and 6, several improvements over MMD-D are small (0.2–1.7% AUROC) and fall within one standard deviation of the baseline. With only 5–10 trials, these individual differences are not clearly significant. The consistency of the improvements across all settings partially mitigates this concern, but the paper should acknowledge which results are robust vs. marginal — the current presentation ("superior performance" throughout) overstates the evidence for the smallest-gain settings. (The large transfer gains in Tables 3–4 and multi-population gains in Table 2 are not in question.)

- **The test-time rationale for using full MMD rather than MPP (Algorithm 1) is asserted, not demonstrated.** The paper says "empirically, the performance of these two strategies is almost identical" without citing a supporting experiment or ablation. This should either be shown in an appendix or the language should be softened.

- **Population composition in mixed test columns is unspecified.** For columns like "ChatGPT + Neo-S" (Tables 1, 5), the paper does not state how the test set is composed (balanced? proportionally sampled? how many instances per population?). Since MMD depends on mixture proportions, this matters for interpretation.

### Trivial

- Algorithm 2 (SID) uses the biased MMD estimator without discussion of why the unbiased version is not used.
- The paper uses "n" to denote sample size in multiple contexts without always clarifying whether it refers to the reference set, test set, or training set.

## Nice-to-Haves

- A direct comparison of MPP vs. MMD as the test-time statistic (to validate the "almost identical" claim).
- Hyperparameter sensitivity analysis for $\epsilon$, bandwidths, and learning rate.

## Removed Points

- **"The experimental evaluation does not actually test the paper's core claim (Structural)"** — Removed because this criticism misunderstands the paper's logic. The core claim is that MMD-MP reduces variance *during training* (demonstrated in Figures 1–2 and the synthetic experiment), producing a better kernel that improves detection *at test time*. Using single-population test sets is by design — it evaluates whether the training-phase variance reduction leads to a better detector. This is standard ML methodology (train with one objective, evaluate on held-out data). The synthetic experiment (Section 4.1) directly isolates the variance mechanism. The reviewer's argument that test sets must be multi-population to test the claim is incorrect.

- **"The theoretical analysis (Proposition 1, Corollary 1) is standard/not new"** — Removed because the paper uses these to establish properties of the *new* MPP estimator, not as claimed novel theoretical results. Standard asymptotic theory for a novel estimator is standard practice.

- **"Theorem 1 is a generic bound that applies to many MMD-based estimators"** — The bound applies to the MPP estimator specifically, which is what needs analysis. The bound's form being standard for kernel methods does not make it irrelevant.

- **"Section 2.3 analysis is empirical, not theoretical"** — The paper explicitly frames this as an empirical investigation ("we conduct empirical studies"). This is appropriate for motivating the method.

- **"Figures 1 axes are unlabeled"** — Pure formatting nitpick.

## Novel Insights

The most useful insight from the combined reviews is that the paper would benefit from a cleaner separation of its two claimed benefits (variance reduction vs. enhanced transferability) in the experimental narrative. The synthetic experiment and the variance plots cleanly support the first benefit; the unknown-LLM experiment cleanly supports the second. But in the main tables (1–2, 5–6), it is not always clear whether the improvement comes from variance reduction (more stable kernel learning) or from the kernel focusing more on HWT structure (which the paper invokes to explain the transfer gains). An ablation that explicitly measures test-time variance of the MMD estimator under multi-population test data would close this gap, but this is a nice-to-have rather than a requirement — the paper's existing evidence for both claims is independently sufficient.

## Suggestions

1. **Specify the feature extractor $\hat{f}$ and key hyperparameters** (learning rate, batch size, $T_{max}$, architecture of $\phi$, $\epsilon$, bandwidth values) to make the work reproducible. A supplementary table would suffice.

2. **State the composition of mixed test columns** — are "ChatGPT + Neo-S" test sets balanced? How many sentences/paragraphs from each LLM?

3. **Add a brief caveat** for the smallest-margin results (e.g., sentence-based AUROC on single-population test sets) acknowledging that these improvements are modest and the results are best interpreted as consistent trends rather than individually significant wins.

4. **Provide the ablation** comparing test-time MPP vs. MMD, or else soften the "almost identical" claim.

## Score and Decision

The paper makes a genuine contribution: it identifies a real, underexplored problem (multi-population variance in MMD training), proposes a clean fix, and provides strong evidence — most notably the synthetic validation (isolating the variance mechanism) and the transfer results (23–28% test power improvement). The weaknesses (missing implementation details, modest margins in some sentence-level results, a few unverified assertions) are addressable and do not undermine the core contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>